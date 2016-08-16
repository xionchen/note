find 其实也算是很常用的命令，但是一直都没掌握，先初步的总体看看
```
    -P 表示不追随符号链接
    -L 表示追随符号链接
    -H 表示只追随命令行中的符号链接
find 的表达是分为几个部分
    Test
    Action
    Clobal options 影响全部的 test 和 action
    Positional options 影响之后的test 或者 action
    Operators 用于逻辑表达，-a and -o or 默认的是-a
```
