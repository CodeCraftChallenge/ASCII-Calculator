# orion

## Overview

提供两个方案, 一个是 Pyth, 一个是 C++. Pyth 的 ASCII 和是 291, 但是需要特定的 Python 解释器. C++ 的 ASCII 和是 37657, 可以编译运行.

优先选择 Pyth, 如果 Pyth 被判定作弊, 则使用 C++.

使用 Pyth 时, 在表格中添加如下内容:

| 排名 | 作者 | 项目 | 分数 | 语言 | 你的留言 |
| :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | orion | pyth | 291 | Python | 嘻嘻, 我一定要赢 |

使用 C++ 时, 在表格中添加如下内容:

| 排名 | 作者 | 项目 | 分数 | 语言 | 你的留言 |
| :--: | :--: | :--: | :--: | :--: | :--: |
| 10 | orion | cpp | 37657 | C++ | 咕, 杀了我 |

## Python with pyth

位于 `orion/pyth` 目录下. 运行方法:

```shell
# 首先安装 pyth
git clone https://github.com/isaacg1/pyth <some-path>

# 然后创建 pyth 别名
alias pyth='python3 <some-path>/pyth/pyth.py'

# 使用 pyth 运行代码
pyth -c $(cat orion/pyth/ascii-sum.py)
```

接下来输入目标字符串, 注意需要用 `"` 包裹. 例如:

```shell
"ab"
```

## C++

简单地编译运行就行了:

```shell
g++ -o ascii-sum ascii-sum.cpp
./ascii-sum "test"
```
