# FIND(1) in Linux 详细解读

find 其实也算是很常用的命令，但是平时自己用的功能都比较菜，所以全面的整理一下。
这里应该囊括了几乎所有的find的用法

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

- -d,-depth 深度优先进行操作，例如使用-delte的时候，会先删除文件夹中的内容再删除文件夹。
- -help,--help 这个不用解释了
- -ignore_readdir_race　通常如果在find的过程中，find的内容发生了变化。这个参数的作用是忽略它
-  -noignore_readdir_race。不忽略上面这种情况
- -maxdept　搜索深度上限
- -mindepth 搜索深度下限，例如-mindepth ２ 会忽略两层以内的所有文件，即使他们可能满足你的测试。
- -mount 只会在当前的文件系统中搜索，不会搜索其他挂载的文件系统
- -noleaf 如果在非Unix规范的文件系统中搜索，需要加上这个选项。

## ６、find表达式中的"TEST"
**TEST是搜索的条件**
#### 常识
    在TEST中的数值可以有三种表达
    +n    表达大于n
    -n    表示小于ｎ
     n    就是ｎ

### TEST中的**时间**相关的表达

**这里的ｎ都是数值，所以可以套用上面的规范，例如：**<br>

    -amin -4表示４分钟内访问的文件
    -amin +4表示４分钟之前访问的文件
    -amin 4表示正好４分钟前访问的文件

- -amin n "access minite"就是在n分钟之前访问的文件（这里的ｎ属于上面的数值表达）,例如　-amin -4表示４分钟内访问的文件
- -atime n 在n*24小时内访问的文件,不满２４小时的部分会被忽略。这里的ｎ通常结合+, -使用。例如　-atime -1 表示一天内访问的文件
- -cmin n　在ｎ分钟前，被改变状态的文件(例如　读写权限，所属等)
- -ctime n　在ｎ天内，被改变状态的文件
- -mmin n　在ｎ分钟前，被修改的文件
- -mtime n　在ｎ天内，被修改的文件

- -anewer file 在访问“file”前访问的文件
- -cnewer file 在修改文件状态“file”前修改文件状态的文件
- -newer file 在修改“file”前修改的文件

- -userd n 这个文件最后的访问时间在它最后修改时间的n天后

- -newerXY reference　这里的XY也是参数，如果Ｘ比Ｙ新的话就返回真。ＸＹ可以的取值如下
  - a 文件"reference"的访问时间
  - B 文件"reference"的创建（birth）时间
  - c 文件"reference"的inode状态改变的时间
      inode包含文件的元信息，具体来说有以下内容：
      - 文件的字节数
      - 文件拥有者的User ID
      - 文件的Group ID
      - 文件的读、写、执行权限
      - 文件的时间戳，共有三个：ctime指inode上一次变动的时间，mtime指文件内容上一次变动的时间，atime指文件上一次打开的时间。
      - 链接数，即有多少文件名指向这个inode
      - *///////文件数据block的位置
  - m 文件"reference"的修改时间
  - t "reference"会被直接作为一个时间处理
  例如： -newermt “2012-12-4 12:10:04” 表示在这个时间后修改的文件


### TEST中的**用户**相关的表达

- -nogroup 没有组的文件
- -gid n 文件的组id是ｎ
- -group gname 以gname为组名的组拥有的文件

- -nouser 没有用户的文件
- - -uid n 以n为uid的用户拥有的文件
- -user name "name"用户拥有的文件

### TEST中的**文件**相关的表达

- -empty 文件是个空文件
- -fsytpe type 文件在type类型的文件系统上。
- -name pattern 匹配文件名
- -ilname pattern 大小写敏感的匹配
- -iname pattern 大小写不敏感的匹配
- -lname pattern 文件是一个符号链接，并且内容匹配pattern
- -inum n 这个文件的i节点编号为n，一般而言，用--samefile更方便
- -ipath pattern 大小写敏感的路劲匹配
- -path pattern 匹配完整的文件名（包括路劲的文件名）
- -iwholename pattern和path是一样的意思
- -iregex pattern 大小写敏感的正则匹配
- -regex pattern 正则匹配，匹配的时候匹配整个路劲，而不是文件名。默认使用的是Emacs的正则匹配。
- -links n 文件有n个链接

- -samefile 同一个文件
- -size n\[cwbkMG\] 文件大小为n（会经过四舍五入）的文件，可以用+n表示大于n，-n表示小于n的形式。
- -type c 类型为c的文件，c可以的选择如下
    - b  块设备
    - c  字符设备
    - d  文件夹
    - p  命名管道
    - f  常规问价
    - l  符号链接
    - s  套接字
    - d  d门（solaris中的）

- -xtype c 与type类似，但是在处理符号链接的时候有区别
- -context （在SELinux中）匹配的安全上下文的文件

### TEST中的**权限**相关的表达

- -perm mode  匹配文件权限刚好为mode的文件，mode可以是 ‘g=w’或者‘0020’
- -perm -mode 匹配拥有mode所有权限的文件
- -perm /mode 匹配拥有mode任何权限的文件
- -readable  可读的文件
- -writable  可以写的文件
- -executable 有x的文件或者目录，对于文件x表示可执行，对于目录x表示可搜索。

## 7、find表达式中的"ACTION"

**ACTION可以执行一些操作，结合TEST和ACTION可是灵活的实现一些功能**

- -delete 删除找到的文件，如果成功放回真，如果失败返回非零值。
- -exec command 执行command。之后所有的命令都会作为exec的参数，直到遇到一个；，在实际的使用中需要对；转义。find找到的参数，可以用{}来替换。
    - 例如find * -exec rm {} -rf \\;就是删除该目录下的所有文件
- -exec command {} + 这个和之前相同，但是不是把每个文件都作为一次参数，而是把所有文件并列作为参数
    - 使用“find * -exec echo {} \\;” 和 “find * -exec echo {} \\+”可以很清楚的显示他们的区别
