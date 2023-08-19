import Navbar from "~/components/navbar";
import { selectionItems } from "~/constants/navbar";
import React, { useEffect } from "react";
import { formItems } from "~/constants/navbar";

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
      
      {/* Paste the Typeform embed code snippet here */}
      <div
        data-tf-widget="xEGXCFMK"
        data-tf-opacity="100"
        data-tf-iframe-props="title=Add Company"
        data-tf-transitive-search-params
        data-tf-medium="snippet"
        className="w-11/12 md:w-10/12 lg:w-9/12 xl:w-8/12 mx-auto mt-8 pb-8"
        style={{
          height: "500px",
        }}
      ></div>
    </div>
  );
}
