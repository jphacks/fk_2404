import React, { useEffect, useState } from 'react';

function App() {
    const [data, setData] = useState(null);
    const [error, setError] = useState(null);

    useEffect(() => {
        // Node.jsサーバーからデータを取得
        fetch('http://localhost:3000/api')
            .then((response) => {
                console.log(response); // レスポンスをログに出力
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then((data) => setData(data))
            .catch((error) => {
                console.error('Error fetching data:', error); // エラーをコンソールに出力
                setError(error.message);
            });
    }, []);

    return (
        <div>
            <h1>Sensor Data</h1>
            {error ? (
                <p>Error: {error}</p>
            ) : data ? (
                <div>
                    <p>開始時間: {data.start_time}</p>
                    <p>終了時間: {data.end_time}</p>
                    <p>場所: {data.label}</p>
                    <p>深刻さ: {data.grade}</p>
                </div>
            ) : (
                <p>Loading...</p>
            )}
        </div>
    );
}

export default App;
