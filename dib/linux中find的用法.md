# FIND(1) in Linux

find 其实也算是很常用的命令，但是一直都没掌握，所以就专门看看有些什么功能，以后查阅也方便。

## 1、find 命令后的参数

**之前一直对find后加的参数有误解，直到看了资料之后才明白是怎么回事，一般而言，find 的语法规则是这样的：**

    $ find [-H] [-L] [-P] [-D debug选项] [-Olevel] [搜索的目录] [表达式]

## 2、find的参数
其实find的参数很少，就5个：
- -P 表示不追随符号链接
- -L 表示追随符号链接
- -H 表示只追随命令行中的符号链接
- -D debug的选项，一般的使用者不关心这个。
- -O 开启查询的优化有1,2,3级。

## 3、find的表达式
所谓的表达是，值得就是find用于限定要搜索的文件的范围的表达式。

例如“find -name abc”中 “-name abc”这个部分就是一个表达式


### find的表达式元素的类型

- Test 用于判断的表达式，返回true或者是false。例如　--empty　用于检测一个文件是否为空，为空就返回１。
- Action　是对符合test标准的文件的行为，例如　-print 在标准输出打印文件的名字。
- Clobal options 影响全部的 test 和 action。例如　-depth　让搜索以深度优先。
- Positional options 影响之后的test 或者 action。例如　-regextype选项　之后可以选择regex的类型
- Operators 用于逻辑表达，-a and -o or 默认的是-a

通过上面这些表达是元素的组合，我们就能进行find操作了

## 4、find表达式中的"POSITIONAL OPTIONS"的表达
**positional options 影响之后的test或者action**

- -daystart 今天发生变化内的文件（包括今天内的改动、访问等等）
- -regextype type 改变之后在-regex 和　-iregex后的正则语句的语法（find支持的正则语法有：emacs、posix-awk、posix-basic、posix-egrep、posix-extended）
- -warn 是否输出警告信息

## 5、find表达式中的"GLOBAL OPTIONS"
**Clobal options 影响全部的 test 和 action**

- -d,-depth 深度优先进行操作
- -help,--help 这个不用解释了
- -ignore_readdir_race　通常如果在find的过程中，find的内容发生了变化。这个参数的作用是忽略它
-  -noignore_readdir_race。不忽略上面这种情况
- -maxdept　搜索深度上限
- -mindepth 搜索深度下限，例如-mindepth ２ 会忽略两层以内的所有文件，即使他们可能满足你的测试。
- -mount 只会在当前的文件系统中搜索，不会搜索其他挂载的文件系统
- 
