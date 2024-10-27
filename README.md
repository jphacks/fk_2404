# サンプル（プロダクト名）

[![IMAGE ALT TEXT HERE](https://jphacks.com/wp-content/uploads/2024/07/JPHACKS2024_ogp.jpg)](https://www.youtube.com/watch?v=DZXUkEj-CSI)

### 製品概要

　NFTとセンサを用いた『ウン遅延証明書』の発行


### 背景(製品開発のきっかけ、課題等）


通勤通学時にどうしてもトイレに行きたくて、電車を降りたことがありませんか？
その結果、授業や出勤に遅れてしまい、不利益を被ることも。。。
しかし、なぜ誰しもが抱えている生理現象を我慢しなくてはならないのでしょうか。
それは、排泄に対して具体的な救済策がなかったからです。
それをデバイスとブロックチェーンなどを用いたデジタル証明書によって、トイレに行きた
いけど我慢することをなくします。


### 製品説明（具体的な製品の説明）

　

　この製品は、緊急のトイレ使用による遅刻を客観的に証明するNFTベースの証明書発行システムです。ガスセンサーによる実際の排便検知と、ブロックチェーン技術を組み合わせることで、改ざん不可能な遅延証明を実現します。


### 特長
* 特長1：緊急のトイレ使用における遅刻に対して「遅延証明（NFT）を発行」する。

  緊急のトイレ使用による遅刻に対して、ブロックチェーン上で検証可能な遅延証明NFTを発行します。トイレ使用という極めてプライベートな事象に対して、個人のプライバシーを最大限に保護しながら、信頼性の高い証明を提供します。


* 特長2：「ガスセンサーによる排便判定」

  空気中に含まれる特定の気体の成分を、ガスセンサー電圧の変化により検出します。
　一定時間内に排せつ物由来のガスを検知した場合、排せつが行われたと判定します。
　これにより、遅刻や欠席の理由として多く挙げられる「お腹の調子が悪かった」という申告を、客観的に証明することができます。


### 今後の展望
#### 「遅延証明（NFT）を発行」

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
- 現在：証明トークン生成
- 将来目標：フロント画面作成、DAOによる資金調達の実装


#### 「ガスセンサーによる排便判定」

- 現在：回路作成、センサ電圧取得
- 将来目標：3Dプリント、成分取得


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

#### フレームワーク・ライブラリ・モジュール
React、Node.js
(raspi)spidev, RPi.GPIO,requests

#### デバイス
　Raspberry
　piガスセンサ
<img width="1002" alt="スクリーンショット 2024-10-27 15 24 20" src="https://github.com/user-attachments/assets/9594113d-2de7-49c5-a3c8-c3e26d8d5542">
<img width="1002" alt="スクリーンショット 2024-10-27 15 24 15" src="https://github.com/user-attachments/assets/751353d8-7065-4594-80de-ed357f248a1b">


##### ハードウェア面
![IMG_3400 2](https://github.com/user-attachments/assets/db74fd2a-d557-4519-8748-d56d2feb18b6)


