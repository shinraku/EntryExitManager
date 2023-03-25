# EntryExitManager

flaskとHTMLの勉強のために入退室管理アプリを作成

https://qiita.com/kii95/items/65aa7b9e010b609c6cb2
を参考にボタンのデザインなどのUIを若干いじったもの

## 使い方
venv環境をアクティベート化したのち
```
python3 app.py
```
を実行することでサーバが起動できる

起動後は
```
https://"IPアドレス":8080
```
で入室者一覧のページを見ることができる

一覧から"入室する"、"退出する"のボタンを押すか
```
https://"IPアドレス":8080/entry
```
```
https://"IPアドレス":8080/exit
```
にアクセスすることで、それぞれ入退室用のフォームに飛べる

log.txtには
```
user , YYYY-MM-DD 22:23:38.873097 , entry 
user , YYYY-MM-DD 22:23:44.150553 , exit 
```
のように"入退室者名、日付、入退室"が各行に記録されている
