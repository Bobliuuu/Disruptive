import Head from "next/head";
import Link from "next/link";
import Navbar from "../components/navbar";
import Home from "../components/home";

export default function Index() {
  return (
    <>
      <Navbar />
      <Home />
    </>
  );
}
