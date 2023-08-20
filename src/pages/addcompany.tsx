import Navbar from "~/components/navbar";
import { selectionItems } from "~/constants/navbar";
import React, { useEffect } from "react";
import { formItems } from "~/constants/navbar";
import Link from "next/link";

// Typeform (add company page)
export default function AddCompany() {
  useEffect(() => {
    // Load the Typeform script dynamically
    const script = document.createElement("script");
    script.src = "//embed.typeform.com/next/embed.js";
    script.async = true;
    document.body.appendChild(script);

    return () => {
      // Clean up by removing the script when the component unmounts
      document.body.removeChild(script);
    };
  }, []);

  return (
    <div className="dark-bg-gradient min-h-screeen">
      <Navbar navbarData={formItems} />
      <div className="mt-3 w-11/12 md:w-10/12 lg:w-9/12 xl:w-8/12 mx-auto">
        <Link href="/upload" className="mt-8 gradient-text text-sm font-bold"><span className="font-bold text-base">+</span> Upload Pitch</Link>
      </div>
      <div
        data-tf-widget="xEGXCFMK"
        data-tf-opacity="100"
        data-tf-iframe-props="title=Add Company"
        data-tf-transitive-search-params
        data-tf-medium="snippet"
        className="w-11/12 md:w-10/12 lg:w-9/12 xl:w-8/12 mx-auto pb-8"
        style={{
          height: "500px",
        }}
      ></div>
    </div>
  );
}
