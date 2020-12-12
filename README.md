# Logfet

## Discription of this app
- ライフログのアプリケーションです。URLは
https://logfet-298314.et.r.appspot.com/login
ID:sample password:sample

- Logfet がこのアプリケーションの名前で、"Log Feeling Every Thing/Time" を意味しています。
- 出来事や感情に対してタグ付けして日記をつけることができます。


## References
- 基本的にはFlaskのチュートリアルを参考にしています。その上で、SQL Alchemyを利用して、MySQLに接続しています。

## Purpose of develop
- Webアプリケーションの作り方を学びたかった。具体的には以下
    - データベースの作り方や操作の仕方、接続について知りたかった
    - バックエンドの経験に乏しかったので、実装したかった
    - デプロイの方法が知りたかった、今回はGAEでおこなう
## Requirement
- Use python 3.8
- Use venv
- Use pip and Do `pip install -r requirements.txt`
### How to Run
1. `export FLASK_APP=logfet`
2. (if you want to hot reload `export FLASK_ENV=development` )
3. ` flask run `

## 今後開発するとしたら
- 感情や出来事について集計してグラフとして示したり、感情や出来事ごとに記事の検索をかけたいです
- フロントエンドはまるまるFlask Tutorialのまんまなので変更していきたいです
- 許可された日記については他のユーザーのものも見れるようにしたいです
- 感情や出来事から分析して、ユーザーにあった行動をおすすめできるようにしたいです
