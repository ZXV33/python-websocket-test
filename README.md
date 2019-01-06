# これはなに？
pythonでWEBソケットを扱った自分用サンプル。  
  
websocketを扱うのも初めてだったので、
勉強として作ってみた。

# 実行方法
サーバー側  
```
git clone https://github.com/ZXV33/python-websocket-test.git
cd python-websocket-test
pipenv install
pipenv shell
python test.py
```

クライアント側
```
以下をブラウザで開く
python-websocket-test/test.html
```

# 確認方法
適当な値を入力して送信する。

# ファイルの解説
```
├── Pipfile ・・・pipenvでインストールしたパッケージの情報が入っている
├── Pipfile.lock ・・・pipenvでインストールしたパッケージの情報が入っている
├── README.md ・・・このファイル
├── test.html ・・・クライアント側のHTML
├── test.js ・・・クライアント側のjavascript。このファイルにwebsocketのクライアント側の処理が書いてある。
└── test.py ・・・サーバー側のpythonスクリプト。websocketのサーバー側の処理が書いてある。
```


