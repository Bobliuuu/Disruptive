import Link from "next/link";
import Navbar from "~/components/navbar";
import { insightItems } from "~/constants/navbar";


export default function Insights() {
    const insights = "";
    return (
        <div className="text-beige">
            <Navbar navbarData={insightItems} />
            <div className="flex flex-col min-h-screeen p-5 items-center justify-center dark-bg-gradient">
                <h1 className="gradient-text text-3xl font-bold mb-6">Company Name</h1>
                <iframe src="http://localhost:3003" title="insights"></iframe>
                <iframe src="http://localhost:3004" title="graphs"></iframe>
                <Link href="http://localhost:3005" className="submit-button w-full m-6">Fund This Company</Link>
            </div>
        </div>
    );
}