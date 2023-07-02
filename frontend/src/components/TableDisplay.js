import React, { useState, useEffect } from 'react';
import './TableDisplay.css'

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

  const handlePlay = (index) => {
    const song = tableData[index].Song;
    const response = fetch("http://localhost:5000/play", {
        method: 'POST', mode: 'cors', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({"song": song})
    })
    console.log(response);
  };

  const handleLike = (index) => {
    const song = tableData[index].Song;
    const response = fetch("http://localhost:5000/likesong", {
        method: 'POST', mode: 'cors', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({"song": song})
    })
    console.log(response);
    const updatedTableData = [...tableData];
    if (updatedTableData[index].Liked === 1) {
      updatedTableData[index].Liked = 0;
      setTableData(updatedTableData);
    } else {
      updatedTableData[index].Liked = 1;
      setTableData(updatedTableData);
    }
  };

  const renderLikedColumn = (value) => {
    if (value === 1) {
      return '❤️'; // Replace 1 with a heart emoji
    } else {
      return '-';
    }
  };

  const likedSongsCount = tableData.filter((row) => row.Liked === 1).length;

  return (
    <div className="table-container">
      <div className="scrollable-table">
        <table className="table">
          <thead>
            <tr>
              <th>Song ({tableData.length})</th>
              <th>Liked ({likedSongsCount})</th>
            </tr>
          </thead>
          <tbody>
            {tableData.map((row, index) => (
              <tr key={index}>
                <td className={`song-cell ${row.Song.length > 60 ? 'scrollable' : ''}`} onClick={() => handlePlay(index)}>
                  <div className="song-text-container">
                    <div className="song-text">{row.Song}</div>
                  </div>
                </td>
                <td onClick={() => handleLike(index)} >{renderLikedColumn(row.Liked)}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default TableDisplay;