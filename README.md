# サンプル（プロダクト名）

[![IMAGE ALT TEXT HERE](https://jphacks.com/wp-content/uploads/2024/07/JPHACKS2024_ogp.jpg)](https://www.youtube.com/watch?v=DZXUkEj-CSI)

## 製品概要

　NFTとセンサを用いた『ウン遅延証明書』の発行

### 背景(製品開発のきっかけ、課題等）

====
通勤通学時にどうしてもトイレに行きたくて、電車を降りたことがありませんか？
その結果、授業や出勤に遅れてしまい、不利益を被ることも。。。
しかし、なぜ誰しもが抱えている生理現象を我慢しなくてはならないのでしょうか。
それは、排泄に対して具体的な救済策がなかったからです。
それをデバイスとブロックチェーンなどを用いたデジタル証明書によって、トイレに行きた
いけど我慢することをなくします。
====

### 製品説明（具体的な製品の説明）

　
製品概要*

概要: 
駅のトイレ内に設置するデバイスです。
ユーザーがトイレに入ったことを検知し、においセンサーによる排便・排尿判定を行いま
す。トイレされていることが検知できた場合に、デジタル証明書へのアクセス用のQRコード
をデバイスの画面に表示し、ウン遅延証明書をダウンロードすることが可能です。
また、PDFのメタデータに記載されているアカウントIDを元に照合を行うこともできます。


### 特長

#### 1. 特長1：緊急のトイレ使用における遅刻に対して「遅延証明（NFT）を発行」する。

- 現状
    - 証明トークン生成。
- 明日
    - フロント画面作成

#### 2. 特長2：「ガスセンサーによる排便判定」

- 現在
    - 回路作成
    - センサ電圧取得
- 明日
    - 3Dプリント
    


### 今後の展望

実社会に役立つコンセプト：
今回のシステムでは健常者だけでなく、腸過敏などの症状がある人たちにも、精神的なハー
ドルを下げたいという気持ちで企画しました。

ブロックチェーン&NFTを用いたことによる改ざん耐性＆真正性を保証：
今回、メンバーが実装したことのなかったブロックチェーン&NFTを使った開発を行いまし
た！資料や構成が難しい開発でしたが、できる範囲での実装を頑張りました！


### 注力したこと（こだわり等）

手作りデバイス！
RaspberryPiとLCDモニター、においセンサーなどの各種センサーを搭載したデバイスを開発
しました。
今回は時間が足りなかったですが、もし次の機会があれば3Dプリンターでハードケースを作
成します！


## 開発技術

### 活用した技術


使用技術:
* React
* Truffle Box
* Node.js
* Python
* Solidity
* Javascript


#### API・データ


#### フレームワーク・ライブラリ・モジュー


#### デバイス
使用デバイス:
* RaspberryPi 4
* においセンサー(TGS2450)
* OSOYOO Touch Screen 3.5inch

### 独自技術

#### ハッカソンで開発した独自機能・技術

* 独自で開発したものの内容をこちらに記載してください
* 特に力を入れた部分をファイルリンク、またはcommit_idを記載してください。

##### ハードウェア面
* 
