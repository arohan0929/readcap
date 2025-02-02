import Image from 'next/image'

export default function Home() {
  return (

    <div className="main-container">

      <div className="center">

        <Image className='img-logo' src="/logo.svg" alt="Vercel Logo" width={400} height={300} />


        <div className="row-1">
          {/* <h1>Readcap</h1> */}
          <p>
            AI with just a text message away.
          </p>
          <p className="normal-size">Simply tag @readcap for responses</p>
        </div>



        <div className="row">

          <p className="phone-number">
            <a href='tel:9084490604'>+1 (908) 449 0604</a>
            </p>

        </div>

      </div>

    </div>

  );
}
