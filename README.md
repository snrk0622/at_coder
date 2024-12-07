# at_corder

## references
- [AtCorder.jp](https://atcoder.jp/home)
- [AtCorder Problems](https://kenkoooo.com/atcoder/#/table/)
- [atcorder-cli](https://github.com/Tatamo/atcoder-cli)
- [online-judge-tools](https://github.com/Tatamo/atcoder-cli)

## create contest
```
acc new ${contest_id}
```

## add tasks
```
add add
```

## test
```
oj t -c "python3 ./main.py" -d ./tests/
```

## submit
提出言語が `pypy3` の場合
```
acc s main.py -- --guess-python-interpreter pypy
```