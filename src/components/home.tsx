import React from "react";
import Link from "next/link";

export default function Home() {
  return (
    <div className="flex flex-col min-h-screeen p-5 items-center justify-center dark-bg-gradient">
      <h1 className="text-5xl m-5 text-beige font-bold mb-8">Welcome to <span className="gradient-text">Disruptive</span>!</h1>
      <p className="text-beige text-lg flex items-center justify-center h-full w-4/5 text-center">An insight and funding DAO platform for new and veteran investors to seek out data, insights, and connections related to everything from micro acquisitions to series A portfolios.</p>
      <Link href = "signin" className="text-white m-8 inline-block pb-2 pt-2 pr-3 pl-3 rounded border border-white duration-300 hover:scale-105 hover:highlight">
        Get Started
      </Link>
    </div>
  );
}