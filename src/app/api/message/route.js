const { AzureOpenAI } = require("openai");
const { MongoClient, ServerApiVersion } = require("mongodb");

require('dotenv').config();

const endpoint = process.env.AZURE_ENDPOINT;
const apiKey = process.env.AZURE_KEY;
const apiVersion = process.env.AZURE_VERSION;
const deployment = process.env.AZURE_DEPLOYMENT;

const client = new AzureOpenAI({ endpoint, apiKey, apiVersion, deployment });


const mongoDBUri = process.env.MONGODB_URI;


const mongoDBClient = new MongoClient(mongoDBUri, {

    serverApi: {
        version: ServerApiVersion.v1,
        strict: true,
        deprecationErrors: true
    }

});

async function aiResponse(old_messages, message) {


    // remove the @readcap from the message
    message = message.replace('@readcap', '');


    const result = await client.chat.completions.create({
        messages: [
            {
                role: "system",
                content: `You are an AI assistant that can be accessed. You can answer questions, provide information, help with tasks, and may have access to some sms messages for context`
            },
            {
                role: "user",
                content: `Here is a prompt for you to answer: ${message}. 
                If the prompt asks to summarize the old texts use the old texts to summarize the texts. 
                If the prompt asks for any events use the previous messages to find any events people have planned and get its exact date using the messages time field in the json. If the promopt asked what did I miss or what is the plan, then you should look for any events that are planned in the messages.
                The messages are stored in the the format {name: "name", message_content: "message", message_type: "text", time: "time"}. So once you find any relevant event, look inside the messages for the time field and use that to answer the prompt. For example if the message_content says "I am planning to meet you tomorrow at 5pm" and the time field says "2022-03-01T17:00:00Z" then you should answer the prompt with "{name of event}: MM/DD/YY, time" by calculating what is tomorrow's date and the time for the event. Do not say anything but the name, date and time of the event.
                Show the time in the format Day, MM/DD/YY, time for the event.
                Here are all the old texts. Use these messages only if needed; your primary goal is to answer the prompt. The old messages are in a json format.
                ${old_messages}`
            },
        ],
        max_tokens: 800,
        temperature: 0.7,
        top_p: 0.95,
        frequency_penalty: 0,
        presence_penalty: 0,
        stop: null
    });



    return result.choices[0].message.content;

}


async function get_messages() {
    
    await mongoDBClient.connect();

    const database = mongoDBClient.db("readcap");
    const collection = database.collection("messages");

    const messages = await collection.find({}).toArray();

    await mongoDBClient.close();

    return JSON.stringify(messages);
    
}

async function send_message_DB(message, user) {

    await mongoDBClient.connect();

    const database = mongoDBClient.db("readcap");
    const collection = database.collection("messages");

    const doc = { name: user, message_content: message, message_type: "text", timestamp: new Date().toLocaleString() };

    await collection.insertOne(doc);

    await mongoDBClient.close();

}


export async function GET(request) {


    const url = new URL(request.url);
    const message = url.searchParams.get('message');
    const user = url.searchParams.get('user');


    if (!message || !user) {
        return new Response("No message or user provided");
    }

    await send_message_DB(message, user);


    if (message.includes('@readcap')) {
        const ai_response = await aiResponse(await get_messages(), message);
        return new Response(ai_response);
    } else {
        return new Response(`${user} said: ${message}`);
    }

}