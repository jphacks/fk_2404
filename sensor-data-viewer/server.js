const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const PORT = 3000;

app.use(bodyParser.json());
app.use(cors());
app.use(express.json());

// データを保存するための変数（実際にはデータベースを使うことを推奨）
let sensorData = {};

// POSTエンドポイント
app.post('/api/data', (req, res) => {
    sensorData = req.body;
    console.log('Data received:', sensorData);
    res.status(200).send('Data received successfully');
});

// GETエンドポイント（Reactからデータを取得する際に使用）
app.get('/api/data', (req, res) => {
    res.json(sensorData); // 正しいJSON形式でデータを返す
});
console.log(sensorData)

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
