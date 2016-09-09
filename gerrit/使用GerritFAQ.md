# 使用Gerrit FAQ

因为工作中遇到了一些比较常见的问题,列在这里给大家参考.
无论是在windows平台下使用,还是在linux平台下使用,都请先参考Gerrit提交代码的三条军规

## 1 git review 时 rebase失败
在执行git review 时,可能会遇到下面的错误:

Errors running git rebase -i remotes/gerrit/master
error: could not apply xxxxx... Add logging when policies forbid an action
When you have resolved this problem run "git rebase --continue".
If you would prefer to skip this patch, instead run "git rebase --skip".
To check out the original branch and stop rebasing run "git rebase --abort".

这个错误,通常是rebase中的冲突造成的,解决方法
- 查看冲突文件,git status
- 处理冲突文件
- 添加冲突的文件,git add xxxxxxx
- 以修改的方式提交,git commit --amend
- 继续rebase,git rebase --continue

还遇到的情况,是暂存区的内容没有保存,这种情况下就提交代码就行了
## 2 git review 提示无法找到gerrit地址
如果你配置了ssh

git remote add gerrit ssh://账号@域名/仓库名.git


## 3 提交依赖的patch时,应该如何修改
例如A是master,changeB在A的基础上修改的,changeC在changeB的基础上修改的
最后的逻辑为A<--changeA<--changeB

假设目前已经提交了changeA和changeB,想要修改changeA
首先在changeB上,进行rebase -i master
然后根据提示选择需要修改的changeA
然后对当前文件进行修改
git commit --amend对changeA 的修改进行提交
然后使用 rebase --continue继续进行rebase
然后在changeB上输入git review.
然后就会自动把changeA的修改进行提交

## 4 git push 和 git review 的区别
git reivew 会进行很多检查,git push 不会,所以不要用git push
## 5 git review时提示ASCII错误
这个可以忽略,不影响提交
## 6 checkout cherry Pick Pull的区别
checkout 适用于同一个change下提交新的patch
例如:
- checkout 一个change的某个patchset
- 修改文件
- git add 修改的文件
- git commit --amend
- git review

cherryPick 是把一个change中一个patchset中的内容拿到本地
例如:
- cherryPick某个change的patchset

pull 是把chenge中的一个patchset合入到当前的分支下

## 7 如何对比每个patch之间的不同

## 8 git review 安装之后无法使用
这个问题可能是包的原因导致的,一般只在windows下出现
如果是包的问题导致的,在cmd中重装git-review
- 配置pip内源地址
- pip uninstall git-review
- pip  install git-review

或者:
按照提供的进行一次安装
