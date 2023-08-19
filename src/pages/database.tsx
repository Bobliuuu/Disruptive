import React, { useState, useEffect } from "react";
import Papa from "papaparse";

const Database: React.FC = () => {
  const [data, setData] = useState<string[]>([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch("/output.csv"); // Adjust the path as needed
        const text = await response.text();

        const csv = Papa.parse(text, {
            worker: true,
            step: function(results) {
                console.log("Row:", results.data);
            }
        });
        const parsedData = csv?.data;
        
        if (parsedData && parsedData.length > 0) {
          setData(parsedData);
        }
      } catch (error) {
        console.error("Error fetching and parsing CSV:", error);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <h1>Database Viewer</h1>
      <div>
        {data.length > 0 ? (
          <table>
            <thead>
              <tr>
                {data.map((col, idx) => (
                  <th key={idx}>{col}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {data.map((row, rowIndex) => (
                <tr key={rowIndex}>
                  {Object.values(row).map((cell, cellIndex) => (
                    <td key={cellIndex}>{cell}</td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        ) : (
          <p>Loading data...</p>
        )}
      </div>
    </div>
  );
};

export default Database;
