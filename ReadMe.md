# このソフトウェアについて

Pythonで別の親ディレクトリに存在するmoduleをimportする。

```
src/
    tests/
        test.py
    mypackage/
        mymodule.py        def mymethod(): ...
```

上記のディレクトリ構成のとき、`test.py`から`mypackage.mymodule.mymethod()`を参照する。

# 実行

```sh
$ python test.py 
```

```sh
$ python test.py
.../src/tests
.../src/mypackage
.../src/mypackage/__pycache__
mymodule
mymethod
```

# 要点

* 実行するとき.pyのファイルパスは絶対パスにすること
    * `$ python /tmp/Python.import.201709091150/src/tests/test.py`等
* `sys.path`(list型)に参照したいディレクトリの絶対パスを追加する

```python
import sys, os
rootdir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
for root, dirs, files in os.walk(rootdir):
    for d in dirs:
        print(os.path.join(root, d))
        sys.path.append(os.path.join(root, d))
```

あとはモジュール名を指定してimportするだけ。

```python
import mymodule
mymodule.mymethod()
```

わざわざ自前で実装せねばimportもできない。さらにファイルパスまで関係あるらしい。よくわからない。

# 開発環境

* Linux Mint 17.3 MATE 32bit
* [pyenv](https://github.com/pylangstudy/201705/blob/master/27/Python%E5%AD%A6%E7%BF%92%E7%92%B0%E5%A2%83%E3%82%92%E7%94%A8%E6%84%8F%E3%81%99%E3%82%8B.md) 1.0.10
    * Python 3.6.1

# ライセンス

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

