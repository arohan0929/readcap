import React from "react";
import { auth } from "./firebase/firebase";
import { GoogleAuthProvider, signInWithPopup } from "firebase/auth";


const App = () => {

  const provider = new GoogleAuthProvider();

  function signInWithGoogle(){
    signInWithPopup(auth, provider).then((result)=>{
      console.log(result.user);
      
    }).catch((error)=>{

    });
  }

  return (
    <>
      <button onClick={signInWithGoogle}>sign in</button>
    </>
  );
};

export default App;
