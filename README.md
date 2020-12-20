# Logfet

## このアプリケーションについて
- ライフログのアプリケーションです。
- URLは
https://logfet-298314.et.r.appspot.com/login
- ID:sample password:sample
- Logfet がこのアプリケーションの名前で、"Log Feeling Every Thing/Time" を意味しています。
- 出来事や感情に対してタグ付けして日記をつけることができます。

## 参考と相違
- 基本的にはFlaskのチュートリアルを参考にしています。
- その上で、Flaskチュートリアルでは利用していないSQL Alchemy(Flask-SQLAlchemy)を利用して、MySQLに接続しています。
- また、投稿への複数タグ付けとそれに伴うOUTER JOIN などは自分のアプリならではです

## 開発の目的
- Webアプリケーションの作り方を学びたかった。具体的には以下
    - データベースの作り方や操作の仕方、接続について知りたかった
    - バックエンドの経験に乏しかったので、実装したかった
    - デプロイの方法が知りたかった、今回はGAEでおこなう
    
    
## Requirement

### How to dev
- Use python 3.8
- Use venv `python -m venv venv` & `. venv/bin/activate`
- Use pip and Do `pip install -r requirements.txt`

### How to Run
1. `python main.py`


## やった結果

### 学んだこと
- 同一のリンクでもGETとPOSTで挙動を変えられること
- Proxyとは何か
- 通信の種類やIPアドレスと、ポート番号の確認やkillについて
- GAEスタンダード Python3.8 のおおよその仕様
- SQLの基本的な構文、リレーショナルなテーブルの引っ張り方としてのINNERJOIN/OUTERJOIN


### 学習の上での課題
- チュートリアルに頼っている部分はあるので、調べながらなんとか実装することはできると思うが、仕様を聞いて自由にコードが設計できるレベルではない。書くまでに絶対調べる、見本を見るを挟まないと書けないレベルの熟達度なので、もっと書く量は増やしていかないといけない
- SQLで出来ることについてはもっと深く知ることが出来れば、バックエンド処理でできることの幅が広がったり、検索が楽になると思う
- フロントについてはデザイン力がないのでアイデアやイメージがなくて実装するのが難しい。


### 今後開発するとしたら
- 感情や出来事について集計してグラフとして示したり、感情や出来事ごとに記事の検索をかけたいです
- 許可された日記については他のユーザーのものも見れるようにしたいです
- 感情や出来事から分析して、ユーザーにあった行動をおすすめできるようにしたいです
