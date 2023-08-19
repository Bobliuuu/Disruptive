import React from "react";
import navigationItems from "../constants/navbar";

export default function Navbar() {
  return (
    <nav className="bg-gray-800 py-4">
      <ul className="flex gap-6 justify-center">
        {navigationItems.map((item, index) => (
          <li key={index}>
            <a
              href={item.link}
              className="text-white hover:text-gray-300 font-semibold"
            >
              {item.label}
            </a>
          </li>
        ))}
      </ul>
    </nav>
  );
}