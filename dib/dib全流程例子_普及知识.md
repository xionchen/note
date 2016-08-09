# 通过一个例子，完整的看一看disk-image-builder是怎么工作的


主要是shell的一些边边角角，不弄清楚，感觉寸步难行


例子：

    disk-image-builder vm centos


## 1 获取参数，目录，die
### 学到的用法

##### die函数
这个函数也算一个比较常用的函数，一般用于输出错误信息并且退出
```shell
function die {
    local exitcode=$?
    set +o xtrace
    echo $@
    exit $exitcode
}

```
##### 取出文件名：
basename 绝对路径

##### 读取路劲：
readlink 文件名</br>
-f 读取完整路劲

##### 获取目录
dirname 路劲

##### export和直接赋值
1. 它们都无法改变爸爸的环境变量
2. exprot可以改变儿子的环境变量

##### getopt解析参数
这里有个问题，坑了一下，“，‘的区别忘了

参考网址
https://blog.linuxeye.com/389.html

用法：</br>
getopts -o xxx -l xxx</br>，隔开参数，：表示需要参数

例子：</br>
```
TEMP=`getopt -o ab:c:: --long a-long,b-long:,c-long:: \
     -n 'example.bash' -- "$@"`
```

## 2 创建cache，修改提示符，导入lib

### 学到的用法

##### 提示符

你可以定制提示符的信息

**PS1** 默认提示符</br>
**PS2** 继续提示符</br>
**PS3** 选择提示符</br>
**PS4** -x提示符</br>

##### 内建函数caller

```shell
#!/bin/bash
die() {
  local frame=0
  while caller $frame;do
      ((frame++));
  done
  echo "$*"
  exit 1
}

f1(){ die "*** an erroe occured ***"}
f2(){ f1;
}
f3(){ f2; }
```
output
12 f1 ./callertest.sh
13 f2 ./callertest.sh
14 f3 ./callertest.sh
16 main ./callertest.sh
*** an erroe occured ***

##### export 导入函数的运行空间
export -f 可以导入函数，如果你source这个文件再引用这个函数的话，是在你自己的进程空间中调用的函数，而不会新建一个定义这个函数的脚本的进程

3 ## 寻找所有element

主要涉及文件“element_depencies.py”,"logging_config.py"
### 学到的用法

##### collections模块

https://docs.python.org/2/library/collections.html


**namedtuple()**	factory function for creating tuple subclasses with named fields
New in version 2.6.

**deque	**list-like container with fast appends and pops on either end
New in version 2.4.

**Counter	dict** subclass for counting hashable objects


**OrderedDict	dict** subclass that remembers the order entries were added


**defaultdict	dict** subclass that calls a factory function to supply missing values

##### logging模块

https://docs.python.org/2/library/logging.html?highlight=logging#module-logging

##### shell中调用python

1. shell中调用shell函数
2. shell函数调用一条命令，这个命令封装了python模块的main函数
3. shell可以获取到python的标准输出和退出错误码

例子
```
a.sh
source b
...
do a shell fun
...

b
export -f fun
fun{
  pythonshell xxxx
}

pythonshell
#!/bin/python
import sys
from xxx import mian
sys.exit(main(sys.argv))
```

##### shell中的数组
example：</br>
读入一个数组：</br>
read -a xxx <<< “a b c d e f”
遍历数组：</br>
for x in ${xxx} do;
