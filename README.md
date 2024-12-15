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

## check list
- [ ] 全探索  
  - オーダー10^8程度であれば2分以内にAC可能
- [ ] 二分探索  
  - リストが昇順・降順である必要があるが、条件を満たせば線形探索よりも高速
  - また、bisectで降順のリストを扱う場合は、リストの各要素と検索値をマイナスに反転する必要がある
  - [bisect](https://docs.python.org/ja/3/library/bisect.html)
    - bisect.bisect_left()
      - 挿入点は既存のどのエントリーより前（左）
    - bisect.bisect_right()
      - 挿入点は既存のどのエントリーより後（右）
    - bisect.bisect()
      - bisect.bisect_right()と同じ挙動