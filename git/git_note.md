

## 2 git基础
### 2.1 查看更新状态
在git中的文件转换：
![](pic/lifecycle.png)

    git status    覆盖Unmodified至Staged
查看不同

    git diff     从Unmodified至Modified
或

    git diff --staged 从Modified到Staged

简单的输出状态

    git status -s

使用工具查看不同

    git difftool

跳过使用暂存区域

    git commit -a 直接将追踪过得文件暂存并且提交

移除文件操作

    git rm xxx
    --cache 至从缓冲层移除
    -f      （如果这个文件是新建的划，需要）强制删除，这与就无法找回这个文件了

### 2.2 查看提交历史
比较

    git log -p -2

打印详细信息
    git log --stat

格式化打印,查找记录<br>
   https://git-scm.com/book/zh/v2/Git-%E5%9F%BA%E7%A1%80-%E6%9F%A5%E7%9C%8B%E6%8F%90%E4%BA%A4%E5%8E%86%E5%8F%B2

打印图

    git log --graph

### 2.3 撤销操作
commit的撤销

    git commit --amend      重新提交心信息
取消暂存的文件

    git reset HEAD 文件
撤销对文件的修改

    git checkout -- 文件（你的记录回消失）

### 2.4标签
打标签

    git tag -a 标签 -m 注释
通过标签显示信息

    git show 标签
后期打标签

    git tag -a 标签 一个hash码
共享标签

    git push origin 标签
检出标签

    git checkout -b 分支名字 标签名

## 3 GIt分支
分支简介：

    https://git-scm.com/book/zh/v2/Git-%E5%88%86%E6%94%AF-%E5%88%86%E6%94%AF%E7%AE%80%E4%BB%8B

树对象、blob对象（保存文件快照），commiter对象

### 3.1 教你拉分支
创建一个分支

    git branch xxx

切换一个分支
    git checkout xxx

删除一个分支

    git branch -d xxx


合入一个分支
1 切换到要合入的分支下
2 git merge
3 可能会有冲突，可以通过git status来查看
4 可以利用git mergetool 来修复（或者自己随便修复）

git的哲学是，拉分支就是爽！

### 3.2 教你管理分支
列出分支

    git branch
查看每个分支最后一次提交

    git branch -v

查看所有包含未合并工作的分支

    git branch -no-merge

查看已经合并到当前分支的分支

    git branch --merged

如果一个分支包含了为合并的工作，那么删除它的时候就会失败。当然如果你比较猛，你也可以使用-D强制删除

    git branch -d testing
      error: The branch 'testing' is not fully merged.
        If you are sure you want to delete it, run 'git branch -D testing'.
### 3.3 分支用来干什么
- 长期分支：
  - 稳定
  - 开发
  - next

- 特效分支
  - 特性实现1
  - 特性实现2
  - 特性实现3


然后你同事发现你的特性实现1 碉堡了，于是你就不要2 3 分支了，如图
开发
![](pic/topic-branches-1.png)
合入
![](pic/topic-branches-2.png)
### 3.4 远程分支
获取远程仓库
    git fetch

获取远程仓库master并且
    git pull=git fetch + git merge

删除远程分支
    git push origin --delete xxx

### 3.5 变基

**变基的风险**

**不要对在你的仓库外有副本的分支执行变基。如果你遵循这条金科玉律，就不会出差错。 否则，人民群众会仇恨你，你的朋友和家人也会嘲笑你，唾弃你。**

**总的原则是，只对尚未推送或分享给别人的本地修改执行变基操作清理历史，从不对已推送至别处的提交执行变基操作，这样，你才能享受到两种方式带来的便利。**

合并不同分支有两种方法：merge和rebase
merge：
![](pic/basic-rebase-2.png)

rebase:
![](pic/basic-rebase-3.png)
![](pic/basic-rebase-4.png)

例子：
    $ git checkout experiment
    $ git rebase master
    First, rewinding head to replay your work on top of it...
    Applying: added staged command

以master为基础，分析c4与c2的差异，然后在c3之上在运用一次

两种整合方法的最终结果没有任何区别，但是变基使得提交历史更加整洁。 你在查看一个经过变基的分支的历史记录时会发现，尽管实际的开发工作是并行的，但它们看上去就像是先后串行的一样，提交历史是一条直线没有分叉。
## 4 服务器上的git
### 4.1协议
**本地协议**
*优点*
简单，可以直接使用网络权限
*缺点*
恭喜文件系统比较难配置

**HTTP协议**
*优点*
智能HTTP，不用秘钥。广泛采用，一般企业的防火墙不允许ssh协议
*缺点*
假设HTTP/S服务端比较棘手

**SSH协议**
*优点*
假设简单，传输高效
*缺点*
实现匿名访问比较困难

**Git协议**
*优点*
快
*缺点*
缺乏授权机制，难假设，没有推送的权限


## 5 分布式Git
### 5.1 工作模式
集中式工作流
简单粗暴
![](pic/centralized_workflow.png)

集成管理者工作流
你可以持续的工作，不用等待
![](pic/integration-manager.png)

司令官与副官工作流
十分大型的项目特别适合
![](pic/benevolent-dictator.png)

## 5.2 向一个项目贡献
**提交准则**
我们要写好提交的信息，这样开发才高效。所以来看看git源码中Documentation/SubmittingPatches的文件，这里说了怎么写提交信息

在gitSubmitting.md中大致描述了里面的内容

## 5.3 维护项目

### 来自邮件的path
**apply**
对于git diff创建的补丁，可以使用git apply来使用
**am**
对于使用 format-path创建的补丁，合入就比较轻松
## 6 内部原理
### 6.1 .git目录
    HEAD
    config*
    description
    hooks/
    info/
    objects/
    refs/

- config 文件包含项目特有的配置选项。
- info 目录包含一个全局性排除（global exclude）文件，用以放置那些不希望被记录在 .gitignore 文件中的忽略模式（ignored patterns）。
- hooks 目录包含客户端或服务端的钩子脚本（hook scripts）。

剩下的四个条目很重要：HEAD 文件、（尚待创建的）index 文件，和 objects 目录、refs 目录。 这些条目是 Git 的核心组成部分。
- objects 目录存储所有数据内容；
- refs 目录存储指向数据（分支）的提交对象的指针；
- HEAD 文件指示目前被检出的分支；
- index 文件保存暂存区信息。

### 6.2 git对象
#### 数据对象
    echo ‘version 1’>test.txt
    git hash-object -w test.txt
    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

这个对象保存了文件的内容，但是没有文件名

#### 树对象

    $ git cat-file -p master^{tree}
    100644 blob a906cb2a4a904a152e80877d4088654daad0c859      README
    100644 blob 8f94139338f9404f26296befa88755fc2598c289      Rakefile
    040000 tree 99f1a6d12cb4b6f19c8655fca46c3ecf317074e0      lib

树对象保存了文件结构的信息

#### 提交对象
可以通过调用 commit-tree 命令创建一个提交对象，为此需要指定一个树对象的 SHA-1 值，以及该提交的父提交对象（如果有的话）。 我们从之前创建的第一个树对象开始：
    $ echo 'first commit' | git commit-tree d8329f
    fdf4fc3344e67ab068f836878b6c4951e3b15f3d

现在可以通过 cat-file 命令查看这个新提交对象：

    $ git cat-file -p fdf4fc3
    tree d8329fc1cc938780ffdd9f94e0d364e0ea74f579
    author Scott Chacon <schacon@gmail.com> 1243040974 -0700
    committer Scott Chacon <schacon@gmail.com> 1243040974 -0700

    first commit

#### 关于对象生成的细节
can refer：<br>
https://git-scm.com/book/zh/v2/Git-%E5%86%85%E9%83%A8%E5%8E%9F%E7%90%86-Git-%E5%AF%B9%E8%B1%A1

### 6.3 Git引用
git的分支的本质是引用，在文件.git/heads/ref中有各种名字，这些名字里面存有一个commit的引用

#### HEAD引用
通过HEAD文件指向现有的引用，HEAD是一个链接：
    xion@xion-Aspire-7750G:~/mygit/test$ cat .git/HEAD
    ref: refs/heads/master

#### 标签引用
标签对象指向一个提交对象，它包含了标签创建者的信息，一个日期，一段注释和一个指针。
git中有两种标签

- 轻量标签 他只是一个固定的引用
- 附注标签 会创建一个标签对象，记录一个引用指向这个对象，一个具体的例子如下：
创建附注标签：<br>
```git tag -a v1.1 1a410efbd13591db07496601ebc7a059dd55cfe9 -m 'test ```<br>
创建标签的SHA-1值：<br>
``` $ cat .git/refs/tags/v1.19585191f37f7b0fb9444f35a9bf50de191beadc2```<br>
对这个SHA-1值进行cat-file命令：<br>
```$ git cat-file -p 9585191f37f7b0fb9444f35a9bf50de191beadc2
object 1a410efbd13591db07496601ebc7a059dd55cfe9
type commit
tag v1.1
tagger Scott Chacon <schacon@gmail.com> Sat May 23 16:48:58 2009 -0700
test tag```

#### 远程引用
查看远程引用：<br>
``` $ cat .git/refs/remotes/origin/master
ca82a6dff817ec66f44342007202690a93763949```

*一个远程引用是只读的，所以无法通过commit命令来更新远程引用*

### 6.4 包文件
git最初向磁盘中存储的对象所使用的格式是“松散（loose）”的对象格式。<br>
但是git会时不时的把这些对象打包成一个二进制包文件。<br>
你可以使用git gc命令来打包，向远端推送的时候也会自动执行这个过程

### 6.5 引用规格
添加一个远程曾库：<br>
```$ git remote add origin https://github.com/schacon/simplegit-progit ```

添加之后，在```.git/config```中间中会有如下更新：<br>
``` remote "origin"]
	url = https://github.com/schacon/simplegit-progit
	fetch = +refs/heads/\*:refs/remotes/origin/\*```
下面三种方式都可以访问到这个提交：<br>
```$ git log origin/master
$ git log remotes/origin/master
$ git log refs/remotes/origin/master ```

#### 提交到远程仓库的命名空间的master分支上
    git push origin master:refs/heads/qa/master

#### 删除引用
    git push origin :Topic
因为push了一个空的分支到，意味着吧topic分支留空

### 6.6 内部原理-传输协议
略

### 6.7 维护和数据回复
#### 维护
回收垃圾：<br>```git gc --auto```

#### 数据恢复
找到最近的提交的引用：<br>
```$ git reflog
1a410ef HEAD@{0}: reset: moving to 1a410ef
ab1afef HEAD@{1}: commit: modified repo.rb a bit
484a592 HEAD@{2}: commit: added repo.rb```

创建分支指向一个提交：<br>
```$ git branch recover-branch ab1afef
$ git log --pretty=oneline recover-branch
ab1afef80fac8e34258ff41fc1b867c702daa24b modified repo a bit
484a59275031909e19aadb7c92262719cfcdf19a added repo.rb
1a410efbd13591db07496601ebc7a059dd55cfe9 third commit
cac0cab538b970a37ea1e769cbbde608743bc96d second commit
fdf4fc3344e67ab068f836878b6c4951e3b15f3d first commit```

显示所有没有被指向的对象：<br>
```
$ git fsck --full
Checking object directories: 100% (256/256), done.
Checking objects: 100% (18/18), done.
dangling blob d670460b4b4aece5915caf5c68d12f560a9fe3e4
dangling commit ab1afef80fac8e34258ff41fc1b867c702daa24b
dangling tree aea790b9a58f6cf6f2804eeac9f0abbe9631e4c9
dangling blob 7108f7ecb345ee9d0084193f147cdad4d2998293
```

##### 移除对象（破坏性的移除，无法恢复的移除,主要是为了传输的时候不再传输它）：<br>

为了演示，我们将添加一个大文件到测试仓库中，并在下一次提交中删除它，现在我们需要找到它，并将它从仓库中永久删除。 首先，添加一个大文件到仓库中：
```
$ curl https://www.kernel.org/pub/software/scm/git/git-2.1.0.tar.gz > git.tgz
$ git add git.tgz
$ git commit -m 'add git tarball'
[master 7b30847] add git tarball
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 git.tgz```
哎呀 - 其实这个项目并不需要这个巨大的压缩文件。 现在我们将它移除：
```
$ git rm git.tgz
rm 'git.tgz'
$ git commit -m 'oops - removed large tarball'
[master dadf725] oops - removed large tarball
 1 file changed, 0 insertions(+), 0 deletions(-)
 delete mode 100644 git.tgz```
现在，我们执行 gc 来查看数据库占用了多少空间：
```
$ git gc
Counting objects: 17, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (13/13), done.
Writing objects: 100% (17/17), done.
Total 17 (delta 1), reused 10 (delta 0)```
你也可以执行 count-objects 命令来快速的查看占用空间大小：
```
$ git count-objects -v
count: 7
size: 32
in-pack: 17
packs: 1
size-pack: 4868
prune-packable: 0
garbage: 0
size-garbage: 0```
size-pack 的数值指的是你的包文件以 KB 为单位计算的大小，所以你大约占用了 5MB 的空间。 在最后一次提交前，使用了不到 2KB - 显然，从之前的提交中移除文件并不能从历史中移除它。 每一次有人克隆这个仓库时，他们将必须克隆所有的 5MB 来获得这个微型项目，只因为你意外地添加了一个大文件。 现在来让我们彻底的移除这个文件。

首先你必须找到它。 在本例中，你已经知道是哪个文件了。 但是假设你不知道；该如何找出哪个文件或哪些文件占用了如此多的空间？ 如果你执行 git gc 命令，所有的对象将被放入一个包文件中，你可以通过运行 git verify-pack 命令，然后对输出内容的第三列（即文件大小）进行排序，从而找出这个大文件。 你也可以将这个命令的执行结果通过管道传送给 tail 命令，因为你只需要找到列在最后的几个大对象。
```
$ git verify-pack -v .git/objects/pack/pack-29…69.idx \
  | sort -k 3 -n \
  | tail -3
dadf7258d699da2c8d89b09ef6670edb7d5f91b4 commit 229 159 12
033b4468fa6b2a9547a70d88d1bbe8bf3f9ed0d5 blob   22044 5792 4977696
82c99a3e86bb1267b236a4b6eff7868d97489af1 blob   4975916 4976258 1438```
你可以看到这个大对象出现在返回结果的最底部：占用 5MB 空间。 为了找出具体是哪个文件，可以使用 rev-list 命令，我们在 指定特殊的提交信息格式 中曾提到过。 如果你传递 --objects 参数给 rev-list 命令，它就会列出所有提交的 SHA-1、数据对象的 SHA-1 和与它们相关联的文件路径。 可以使用以下命令来找出你的数据对象的名字：
```
$ git rev-list --objects --all | grep 82c99a3
82c99a3e86bb1267b236a4b6eff7868d97489af1 git.tgz```
现在，你只需要从过去所有的树中移除这个文件。 使用以下命令可以轻松地查看哪些提交对这个文件产生改动：
```
$ git log --oneline --branches -- git.tgz
dadf725 oops - removed large tarball
7b30847 add git tarball```
现在，你必须重写 7b30847 提交之后的所有提交来从 Git 历史中完全移除这个文件。 为了执行这个操作，我们要使用 filter-branch 命令，这个命令在 重写历史 中也使用过：
```
$ git filter-branch --index-filter \
  'git rm --ignore-unmatch --cached git.tgz' -- 7b30847^..
Rewrite 7b30847d080183a1ab7d18fb202473b3096e9f34 (1/2)rm 'git.tgz'
Rewrite dadf7258d699da2c8d89b09ef6670edb7d5f91b4 (2/2)
Ref 'refs/heads/master' was rewritten```
--index-filter 选项类似于在 重写历史 中提到的的 --tree-filter 选项，不过这个选项并不会让命令将修改在硬盘上检出的文件，而只是修改在暂存区或索引中的文件。

你必须使用 git rm --cached 命令来移除文件，而不是通过类似 rm file 的命令 - 因为你需要从索引中移除它，而不是磁盘中。 还有一个原因是速度 - Git 在运行过滤器时，并不会检出每个修订版本到磁盘中，所以这个过程会非常快。 如果愿意的话，你也可以通过 --tree-filter 选项来完成同样的任务。 git rm 命令的 --ignore-unmatch 选项告诉命令：如果尝试删除的模式不存在时，不提示错误。 最后，使用 filter-branch 选项来重写自 7b30847 提交以来的历史，也就是这个问题产生的地方。 否则，这个命令会从最旧的提交开始，这将会花费许多不必要的时间。

你的历史中将不再包含对那个文件的引用。 不过，你的引用日志和你在 .git/refs/original 通过 filter-branch 选项添加的新引用中还存有对这个文件的引用，所以你必须移除它们然后重新打包数据库。 在重新打包前需要移除任何包含指向那些旧提交的指针的文件：
```
$ rm -Rf .git/refs/original
$ rm -Rf .git/logs/
$ git gc
Counting objects: 15, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (11/11), done.
Writing objects: 100% (15/15), done.
Total 15 (delta 1), reused 12 (delta 0)```
让我们看看你省了多少空间。
```
$ git count-objects -v
count: 11
size: 4904
in-pack: 15
packs: 1
size-pack: 8
prune-packable: 0
garbage: 0
size-garbage: 0```
打包的仓库大小下降到了 8K，比 5MB 好很多。 可以从 size 的值看出，这个大文件还在你的松散对象中，并没有消失；但是它不会在推送或接下来的克隆中出现，这才是最重要的。 如果真的想要删除它，可以通过有 --expire 选项的 git prune 命令来完全地移除那个对象：
```
$ git prune --expire now
$ git count-objects -v
count: 0
size: 0
in-pack: 15
packs: 1
size-pack: 8
prune-packable: 0
garbage: 0
size-garbage: 0```
