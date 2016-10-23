# shell中的特殊字符--其他
> 初学shell的时候,shell的一些特殊字符很容易让人混淆.例如**单引号**,**双引号**和**括号**的区别.这里进行全面的整理

## 1  #(井号)
> shell中井号用于注释,这里并没有什么问题.

但是关于"#"有一下需要注意的地方:

###  作为注释的时候要在前面留空格
注意下面两者的区别;

```shell
echo "This is a comment" # Comment
输出结果是This is a comment
echo "This is a comment"#Comment
输出结果是This is a comment#Comment
```

### #的其他情况
看下面这个例子,第四行中包含注释:
```shell
echo "The # here does not begin a comment."
echo 'The # here does not begin a comment.'
echo The \# here does not begin a comment.
echo The # here begins a comment.

echo ${PATH#*:}       # 参数替换, 不是一个注释.
echo $(( 2#101011 ))  # 进制转换,也不是注释

```

## 2 ;(分号)
> 分号是命令分割符,可以把同一行中两个命令分割开

### 分号最为命令分割符时,后面要加空格
虽然不会影响功能,但是这是规范的写法,例如:
```shell
echo hello; echo there
```

## 3 ;;(双分号)
> 双分号是case的结束表示

例如:
```shell
case "$variable" in
  abc)  echo "\$variable = abc" ;;
  xyz)  echo "\$variable = xyz" ;;
esac
```

## 4 ;;&, ;&
>这是bash中的新特性,他们同样是作为case结束的表示,但是与;;有所不同

例子:
```shell
case "$1" in
  abc)  echo "\$variable = abc" ;;
  abc)  echo "\$variable = abc2" ;;
esac
```
```shell
case "$1" in
  abc)  echo "\$variable = abc" ;&
  abc)  echo "\$variable = abc2" ;;
esac
```
---
```
第一个例子的输出结果是
$variable = abc

第二个例子的输出结果是
$variable = abc
$variable = abc2
```
