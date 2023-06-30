import React, { useState, useEffect } from 'react';


function TableDisplay() {
  const [tableData, setTableData] = useState([]);

  useEffect(() => {
    const fetchTableData = async () => {
      try {
        const response = await fetch('http://localhost:5000/table');
        if (response.ok) {
          const data = await response.json();
          // Extract the table data from the nested structure
          const extractedData = Object.values(data.Song).map((value, index) => ({
            Song: value,
            Liked: data.Liked[index],
            Played: data.Played[index]
          }));
          setTableData(extractedData);
        } else {
          throw new Error('Request failed with status ' + response.status);
        }
      } catch (error) {
        console.error('Error:', error);
      }
    };

    fetchTableData();
  }, []);

  return (
    <div>
      <table>
        <thead>
          <tr>
            <th>Song</th>
            <th>Liked</th>
          </tr>
        </thead>
        <tbody>
          {tableData.map((row, index) => (
            <tr key={index}>
              <td>{row.Song}</td>
              <td>{row.Liked}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default TableDisplay;