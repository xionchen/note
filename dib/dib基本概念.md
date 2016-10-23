# dib代码逻辑和细节


主要是shell的一些边边角角，不弄清楚，感觉寸步难行

先通过逻辑顺一遍，主要是浏览shell的一些用法和代码的逻辑组织

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
\*\*\* an erroe occured \*\*\*

##### export 导入函数的运行空间
export -f 可以导入函数，如果你source这个文件再引用这个函数的话，是在你自己的进程空间中调用的函数，而不会新建一个定义这个函数的脚本的进程

## 3 寻找所有element

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
上述讲的是diskimage_builder中的情况,实际上python xxx也是一样的

##### shell中的数组
example：</br>
读入一个数组：</br>
read -a xxx <<< “a b c d e f”
遍历数组：</br>
for x in ${xxx} do;

## 4 检查工具 生成快设备uuid 生成root的label

### 学到的用法

##### ()的用法
```
()
command group.
(a=hello; echo $a)

Important
A listing of commands within parentheses starts a subshell.

Variables inside parentheses, within the subshell, are not visible to the rest of the script. The parent process, the script, cannot read variables created in the child process, the subshell.
a=123
( a=321; )

echo "a = $a"   # a = 123
\# "a" within parentheses acts like a local variable.

array initialization.
Array=(element1 element2 element3)
```


##### 双引号的用法
之前虽然看过，但是后来忘了，为了防止再忘了记在这里
使用双引号除了变量名前缀($)、后引符(`)和转义符(\)外，会使shell不再解释引号中其它所有的特殊字符

##### 反引号`和$()的区别
1. 反引号齐本身就对\\进行了转义，保留了齐本身意思，如果我们想在反引号中起到\\的特殊意义，我们必须使用2个\\来进行表示。
所以我们可以简单的想象成反引号中： \\ = \
2. $()中则不需要考虑\\的问题，与我们平常使用的一样： \\ = \\

题外话： 反引号是老的用法，$()是新的用法，不管是在学习测试中，还是在实际工作中， $()的用法都是被推荐的。

##### 查看快设备属性
blkid
```
/dev/sda1: UUID="220E1B870E1B5361" TYPE="ntfs" PARTUUID="0c1d5622-01"
/dev/sda2: UUID="36134715-a23e-4189-9ec8-d669a1fa8d69" TYPE="ext4" PTTYPE="dos" PARTUUID="0c1d5622-02"
/dev/sda3: UUID="0007D87B00058E22" TYPE="ntfs" PARTUUID="0c1d5622-03"
/dev/sda5: LABEL="software" UUID="0006FE2D000A3C10" TYPE="ntfs" PARTUUID="0c1d5622-05"
/dev/sda6: UUID="0000C0C5000C67D1" TYPE="ntfs" PARTUUID="0c1d5622-06"
/dev/sda7: UUID="000C10F90003C17B" TYPE="ntfs" PARTUUID="0c1d5622-07"
/dev/sda8: UUID="65341e30-0bb0-47bf-abf4-b792e7d1c8c6" TYPE="swap" PARTUUID="0c1d5622-08"

```

##### 一个明显改动过的bug和它的考虑

```shell
# FS_TYPE isn't available until after we source img-defaults
if [ -z "$DIB_ROOT_LABEL" ]; then
    # NOTE(bnemec): XFS has a limit of 12 characters for filesystem labels
    # Not changing the default for other filesystems to maintain backwards compatibility
    if [ "$FS_TYPE" = "xfs" ]; then
        DIB_ROOT_LABEL="img-rootfs"
    else
        DIB_ROOT_LABEL="cloudimg-rootfs"
    fi
fi
```
## 创建目录 注册信号

##### mktemp
1. mktemp 里面的最后的参数名是一个目标，其中的XXXX会被随机字符替代
2. -t 选项保证参数中不带斜杠，以确保把参数作为一个文件名或目录名而不是路劲处理

##### 注册信号
trap 函数名 信号名

##### bash 中的test
man test 可以看判断条件，很实用

##### zsh 和bash有区别的
他们不是完全相同的，被这个问题坑了一下

##### find命令

##### egerp 和 grep

## 5 create_base
![](pic/create_base.png)

整体流程，其中一些处理写的挺有意思

##### run_d

这是一个通用的函数，它的作用就是用于调度钩子。这个函数主要对dib_run_parts进行了包裹，包裹的目的在于在之前和之后增加调试的能力。

#### dib_run_parts（）

从功能上来说还是比较清晰的，先处理了异常数据，然后找到所有运行的脚本，统计运行的时间，最后输出结果。这个脚本的功能还是很实用的。
![](pic/dib_run_part.png)
#### 其中学到的一些用法：

##### find
find的内容比较多，就记在了[linux中find的用法](/linux_shell/linux中find的用法.md)中

##### pushd popd
把目录压栈和出栈，可以用来改变目录

## 6 将install type写入环境变量 run_d extra-data
这里基本上都和上面类似

## 7 run_d_in_target
这个函数的作用是把一个文件夹中的脚本在chroot下运行
这个函数比较重要，基本上理解了这个部分，就大概对dib的工作原理理解了。
首先，run_d_in_target 的流程图如下：
![](pic/run_d_in_target.png)

## 8 do_extra_package_install
这是一个类似与装饰起之类的东西，真正运行的东西其实如下：
<!-- ``` -->
./elements/dpkg/bin/install-packages
./elements/gentoo/bin/install-packages
./elements/opensuse/bin/install-packages
./elements/yum/bin/install-packages
```
这个利用了element中的packages-install，只要是在WORKDIR中以package-installs-开头的文件，都会被解析
这个element通过一个json或者是yaml文件定义要暗转或者卸载的包，然后会自动安装这些包，下面是一些配置的信息：
```
phase: install.d
uninstall: False                                                        installtype: * (Install package for all installtypes)                      arch: * (Install package for all architectures)
```

## 9 unmount_image
留下一个问题 这个地方什么时候加载上去的？

## 剩下的步骤

- 计算镜像大小(可以人工定义或者自动计算)
    - du_size镜像大小
- 如果设置了，显示所用空间大小
- 如果类型是ext4
    - 设置快的大小为64
    - 如果设置了DIB_IMAGE_SIZE
      - 增加65536空间来存储日志
- 将du_size按照64的倍数取整（- line403的用法可以研究下）
-  truncate TMP_IMAGE_PATH的空间到理想的空间
- 如果设置了最大支持的文件系统的块数
    -把他加到mkfs的选项中
- 使用losetup命令把镜像目录虚拟为块设备
- eval_run_d block-device
- 创建mnt目录
- 把快设备挂载到mnt目录上
- 把built的内容拷贝到mnt目录中
- mount_proc_dev_sys，在mnt下挂载proc、sysfs文件系统，和dev目录
- run_d_in_target finalise
- finalise_base

## IMAGE_TYPES
    ACI:application container image 一般用于容器
#### shell 里字符匹配的一种写法
[[ "表达式" =~ "匹配字符" ]]

#### tar的一些语法

这里有一些解释:
http://www.gnu.org/software/tar/manual/html_section/tar_52.html#transform

sudo tar -C ${TMP_BUILD_DIR}/mnt -cf $IMAGE_NAME.aci --exclude ./sys \
                --exclude ./proc --xattrs --xattrs-include=\* \                               --transform 's,^.,rootfs,S' .
在${TMP_BUILD_DIR}/mnt目录下,-cf 创建一个压缩文件 不要sys/ 不要proc
然后修改名字	在前面加上rootfs

## 之后的流程

- 遍历所有的IMAGE_TYPES
  - 如果是tar或者是aci
    - 如果是aci类型的
    - 基于mnt目录,创建压缩文件$IMAGE_NAME.aci,排除sys和proc文件夹,然后在文件名之前加上rootfs(相当于把所有文件放入到了rootfs文件夹下)
      - 如果有ACI_MANIFEST,把他追加到压缩文件中
    - 如果是tar类型的
      - 直接把除了sys proc的文件打包到IMAGE_NAME.tar中
    - 改变文件所属用户
  - 如果是docker
    - 压缩然后通过管道给 docker import命令
- 如果是 ironic-agent
  - fstrim_image (剪裁不需要的空间)
- unmount_image(unmount 之前先执行sync)
- cleanup_build_dir
- 对于所有的的image_types
  - compress_and_save_image image_name.image_type
  - 最后才执行raw的compress,因为raw的compress是破坏性的
- cleanup_image_dir(unmount+rm)
