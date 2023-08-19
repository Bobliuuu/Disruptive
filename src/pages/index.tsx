import Head from "next/head";
import Link from "next/link";
import Navbar from "../components/navbar";
import Home from "./home";
import { selectionItems } from "~/constants/navbar";

export default function Index() {
  return (
    <>
      <Navbar navbarData={selectionItems}/>
      <Home />
    </>
  );
}
