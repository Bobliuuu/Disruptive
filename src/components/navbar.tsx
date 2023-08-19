import React from "react";
import Link from "next/link";
import Image from "next/image"; // Import the Image component

export default function Navbar() {
  return (
    <nav className="flex flex-row items-center justify-between p-2 dark-navbar-gradient border-b-2 border-gradient-midblue-beige">
      <div className="flex items-center">
        {/* Display the image */}
        <Image src="/disruptive.png" alt="Disruptive Logo" width={30} height={40} className="ml-2"/>
        <a className="font-semibold text-xl ml-3 text-slate-100" href="/">
          Disruptive
        </a>
      </div>
      <div className="ml-auto">
        <Link href="/" className="text-white inline-block m-3 pb-1 pt-1. pr-2 pl-2 rounded border border-white duration-300 hover:scale-105">
          Sign In
        </Link>
      </div>
    </nav>
  );
}
