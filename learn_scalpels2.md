## 一 找到运行的文件
### 1 产看命令在哪
    whereis sca
    /usr/local/bin

### 2 找到调用文件
    cd /usr/local/bin
    vim sca

```shell
#!/usr/bin/python
# PBR Generated from u'console_scripts'

import sys

from scalpels.client.shell import main


if __name__ == "__main__":
        sys.exit(main())

```

### 3 找到命令调用的python

    在pythonzhong
    import sys
    print sys.path

```python
['', '/home/stack/openstack/keystone', '/home/stack/openstack/glance', '/home/stack/openstack/cinder', '/home/stack/openstack/nova', '/home/stack/openstack/horizon', '/home/stack/openstack/tempest', '/home/stack/openstack/scalpels', '/usr/lib/python2.7', '/usr/lib/python2.7/plat-x86_64-linux-gnu', '/usr/lib/python2.7/lib-tk', '/usr/lib/python2.7/lib-old', '/usr/lib/python2.7/lib-dynload', '/usr/local/lib/python2.7/dist-packages', '/usr/lib/python2.7/dist-packages']

```

通过上面可以找到在/home/stack/openstack/scalpels中的python文件
    这里有py文件和pyc文件，pyc文件是编译好的文件，在加载模块的时候，优先加载pyc，但是会检测更新的时间
    如果py文件比较新的划就会重新对模块进编译

## 二 研究一条命令入手
    sca tracer -l

### 具体执行改命令的函数是scaples.client.shell:main函数
    shell.py是壳，用来包裹里面的各种功能
### 1 argparse模块
here  is a useful website:
http://python.usyiyi.cn/python_278/library/argparse.html
    这是一个用来解析参数的模块
例子(这个例子接受一个整数序列并且打印出他们的和或者是最大值)：
```shell
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                   help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                   const=sum, default=max,
                   help='sum the integers (default: find the max)')

args = parser.parse_args()
print args.accumulate(args.integers)
```

#### a 创建一个解析器

    parser = argparse.ArgumentParser(descritption='一些描述')
#### b 添加参数

    arser.add_argument('--sum',dest='accumulate',action='store_const',const=sum,default=max,help='sum the integers')

参数：
##### name或flags参数
    创建一个可选参数：
    parser.add_argument('-f', '--foo')
    <br>
    创建一个位置参数：
     parser.add_argument('bar')

##### action 参数
如何处理命令行参数
- store默认动作 只保存参数的值
- store_const 保存const关键字指出的值
- store_ture store_false 它们是store_const的特殊情况，用来保存False和True
- append 保存一个列表，将每个参数值附加在后面
- append_const 保存一个列表，将const关键字指出的参数附加在之后
- count 计算关键字出现的次数
- help 打印帮助
- version 将version=xxx添加在这里，打印版本

我们可以自己定义处理参数的动作，例子如下:
```python
>>> class FooAction(argparse.Action):
...     def __call__(self, parser, namespace, values, option_string=None):
...         print '%r %r %r' % (namespace, values, option_string)
...         setattr(namespace, self.dest, values)
...
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', action=FooAction)
>>> parser.add_argument('bar', action=FooAction)
>>> args = parser.parse_args('1 --foo 2'.split())
Namespace(bar=None, foo=None) '1' None
Namespace(bar='1', foo=None) '2' '--foo'
>>> args
Namespace(bar='1', foo='2')

```

##### nargs 参数
与参数的数量与欧冠
    N(一个整数)。命令行中的N个参数被一起收集在一个列表中
    <br>
    ?   如果有的话就从命令行读取一个参数。没有参数就产生一个来自于default的值
    <br>
    * 出现的所有的命令行参数都收集
    <br>
    +  与*一样，如果没有至少出现一个命令行就会报错
    <br>
    argparse.REMAINDER 所有剩余的命令行参数都收集到一个列表中
##### const 参数

##### default 参数
##### type 参数
可以规定参数的类型，常见的内建类型都可以作为type的类型
##### choices 参数
一个列表，列出了所有的可用的选项
##### required 参数
可以表示必须的参数
##### help 参数
包含了简短的描述，说明
##### metavar 参数
改变显示出去的名字，用在帮助文档里面
##### dest 参数
目标，包获取的值放在说明里面（由于使用的时候可能存在 -f --foo这种情况，需要指定）
#### c 解析参数
    parser.parse_args(['--sum','7','-1','42'])
    Namespace(accumulate=<built-in fuction sum>,integers=[7,-1,42])

实际上这条命令实现的效果是，通过远程调，获取了数据库中Tracer表中的所有tracer
sca start -a rpc -a rabbit -a traffic

其实要学一堆python模块：
数据库的
远程调用的
