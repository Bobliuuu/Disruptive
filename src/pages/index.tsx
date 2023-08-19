import Head from "next/head";
import Link from "next/link";
import Navbar from "../components/navbar";
import Home from "../components/home";
import { navigationItems } from "~/constants/navbar";

export default function Index() {
  return (
    <>
      <Navbar navbarData={navigationItems}/>
      <Home />
    </>
  );
}
