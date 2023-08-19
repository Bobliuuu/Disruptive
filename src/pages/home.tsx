import React from "react";
import Link from "next/link";
import { auth } from "./firebase";
import { signInWithPopup, GoogleAuthProvider } from "firebase/auth";
import { useAuthState } from "react-firebase-hooks/auth";


// Home component added to pages for the sake of imports/Firebase error
export default function Home() {
  const [user, setUser] = useAuthState(auth);
  const googleAuth = new GoogleAuthProvider();
  const login = async () => {
    try {
      const result = await signInWithPopup(auth, googleAuth);
      if (result.user) {
        window.location.href = "/selection";
      }
    } catch (error) {
      console.error("Error logging in", error);
    }
  };

  return (
    <div className="flex flex-col min-h-screeen p-5 items-center justify-center dark-bg-gradient">
      <h1 className="text-5xl m-5 text-beige font-bold mb-8">Welcome to <span className="gradient-text">Disruptive</span>!</h1>
      <p className="text-beige text-lg flex items-center justify-center h-full w-4/5 text-center">An insight and funding DAO platform for new and veteran investors to seek out data, insights, and connections related to everything from micro acquisitions to series A portfolios.</p>
      <button type="submit" className="submit-button mt-8" onClick={ login }> Get Started </button>
    </div>
  );
}