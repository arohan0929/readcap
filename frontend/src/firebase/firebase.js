// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getAuth } from "firebase/auth";

// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDDA_0ejizTOaM_P2Aap6MhtpvEOtdd9vo",
  authDomain: "readcap-63926.firebaseapp.com",
  projectId: "readcap-63926",
  storageBucket: "readcap-63926.firebasestorage.app",
  messagingSenderId: "813357105617",
  appId: "1:813357105617:web:037a02f69af157833060f0",
  measurementId: "G-HL1XLDGJC5"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
export const auth = getAuth(app);