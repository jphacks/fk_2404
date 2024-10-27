import React, { useEffect, useState } from 'react';

function App() {
    const [data, setData] = useState(null);

    useEffect(() => {
        // Node.jsサーバーからデータを取得
        fetch('http://localhost:3000/api/data')
            .then((response) => response.json())
            .then((data) => setData(data))
            .catch((error) => console.error('Error fetching data:', error));
    }, []);

    return (
        <div>
            <h1>Sensor Data</h1>
            {data ? (
                <div>
                  <p>開始時間: {data.start_time}</p>
                  <p>開始時間: {data.end_time}</p>
                  <p>場所: {data.label}</p>
                  <p>深刻さ: {data.grade}%</p>
                </div>
            ) : (
                <p>Loading...</p>
            )}
        </div>
    );
}

export default App;
