import React from "react";

export default function Home() {
  return (
    <div className="flex flex-col min-h-screeen p-5 items-center justify-center dark-bg-gradient">
      <h1 className="text-5xl m-5 text-beige font-bold mb-8">Welcome to <span className="gradient-text">Disruptive</span>!</h1>
      <p className="text-beige text-lg flex items-center justify-center h-full w-4/5 text-center">An insight and funding DAO platform for new and veteran investors to seek out data, insights, and connections related to everything from micro acquisitions to series A portfolios.</p>
      <button className="text-white m-5 inline-block pb-1 pt-1 pr-2 pl-2 rounded border border-white duration-300 hover:scale-105 hover:highlight">
        Get Started
      </button>
    </div>
  );
}