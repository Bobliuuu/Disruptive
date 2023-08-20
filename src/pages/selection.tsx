import Navbar from "~/components/navbar"
import { selectionItems } from "~/constants/navbar";
import Link from "next/link";

export default function Selection() {
    return (
      <div>
        <Navbar navbarData={selectionItems} />
        <div className="flex flex-col min-h-screeen pb-5 pr-5 pl-5 items-center justify-center dark-bg-gradient">
          <h1 className="text-3xl m-5 text-beige font-bold mb-8">
            Do you want to <span className="gradient-text">invest in...</span>
          </h1>
          <div>
            <div className="mb-4">
              <Link href="http://10.17.2.107:8500" className="button-selection"> Pre Seed Companies </Link>
            </div>
            <div className="mb-4">
              <Link href="http://10.17.2.107:8501" className="button-selection"> Seed+ Companies </Link>
            </div>
          </div>
        </div>
      </div>
    );
  }