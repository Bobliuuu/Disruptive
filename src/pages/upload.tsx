'use client'
import Navbar from "~/components/navbar";
import { uploadData } from "~/constants/navbar";
import { useState } from "react";

export default function Upload() {
    const [file, setFile] = useState<File>()
    const onSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault()
        if (!file) return
        try {
          const data = new FormData()
          data.set('file', file)
          const res = await fetch('../constants/apiupload.ts', {
            method: 'POST',
            body: data
          })
          // handle the error
          if (!res.ok) throw new Error(await res.text())
        } catch (e: any) {
          // Handle errors here
          console.error(e)
        }
    }

    return (
      <div>
        <Navbar navbarData={uploadData} />
        <div className="flex flex-col min-h-screeen p-5 items-center justify-center dark-bg-gradient">
            <h1 className="text-4xl text-beige font-bold mb-3">Upload <span className="gradient-text">Company Pitches</span>!</h1>
            <p className="text-beige text-lg flex items-center justify-center h-full w-4/5 text-center">Choose pitches to upload.</p>
            <form onSubmit={onSubmit} className="text-beige flex flex-col">
                <input type="file" className="text-beige w-full block mx-auto py-2 mt-4" name="video" onChange={(e) => setFile(e.target.files?.[0])} />
                <input type="submit" value="Upload" className="text-beige block mx-auto w-40 py-1.5 rounded border mt-2 border-beige duration-300 hover:scale-105 hover:highlight"/>
            </form>
        </div>
      </div>  
    );
}