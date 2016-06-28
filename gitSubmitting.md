# 如何写提交信息
## 0 决定你工作的基础
一般而言有几种情况：
- 修复bug，应该基于'maint'分支。如果bug不在maint分支，就基于master分支，如果不在master分支，基于其他的topic
- 新特性， 应该基于master。但是如果新特性在pu中，应该基于这个topic
- 对于一个话题的增强和改进，应该基于这个话题
- 对于实验的情况，在next或者是pu中。同时你需要把pathes拿来讨论，在最后合入之前，你可能必须要等到一些tpoic能保证master，然后重新构建你的工作
- 有的系统有指定的维护者，维护他们的子系统，那么就应该基于子系统提交

## 1 commits应该是逻辑分离的
    除非你的patch比较琐碎，不然多进行几次commit，然后解释清楚每次commit是干啥的

    确保你有对于修复的bug的测试

    如果添加了一个新的特性，确包你添加了新的测试来展示你的新特性是什么

    如果你在github上有账号，你可以用 Travis CI 集成来测试linux上的变化

    更新你的文档，尽量使用美式英语（如果你使用英文的话）

    不要有空白错误，你可以在commit之前，通过git diff --check来检测

## 2 好好描述你的commit
描述信息的第一行，最好不好超过50个字母。
使用下面这种方式加上区域的描述也是不错的：
    . archive: ustar header checksum is computed unsigned
    . git-cherry-pick.txt: clarify the use of revision range notation

然后下面是一个空白行，下面加上你的描述信息。描述信息一定是要imperative（命令的）不要说“我给这里加上了一个功能”，而是说“加上了一个功能”
不要在你的commit信息里面带链接

## 3 从你的提交上利用git tools 生成path
尽量减少你的path的干净，不要提交任何无关的文件

## 4 发送你的path
有可能的话，学会使用 format-path和 send-email

## 5 署名

## 理想的工作流

0 你发现问题，code it up
1 发送邮件给你邮件列表中的刃
2 你获得改进的建议
3 打磨 修复 完善，然后再发邮件
4 邮件列表认为你的patch好。发送给维护者，抄送其他人
5 一个topic分支建立，然后合入到next中，最终有可能合入到master中
