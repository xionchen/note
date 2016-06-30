# rpm快速查询手册

rpm---Red Hat Package Manger
这个手册基本罗列了rpm命令的选项和各个选项的解释，可以用于rpm命令的快速查询
## 一 查询
查询命令

    rpm -q


  选项：

    .
      -R  -- list dependencies
      -a  -- query all packages
      -c  -- configuration files only
      -d  -- documentation files only
      -f  -- query packages that own specified files
      -g  -- query packages in one of specified groups
      -i  -- display package information
      -l  -- display package file list
      -p  -- query uninstalled packages
      -s  -- show file states
      -v  -- verbose output
例子：

## 二 安装
安装命令

    rpm -i xxx     这里的xxx可是一个是一个包的文件名，或者是一个url


  选项：

    .
      -v              输出详细过程

      --test          测试安装（只检查依赖和环境）

      --replacepkgs   替换包的安装

      --replacefiles  计算替换其他的包文件也安装
          如果替换的文件是配置文件rpm会自动备份（看看人家多么机智！）

      --nodeps        在装包之前不检查依赖
          能不能装的起来是一回事，能不能运行就是另外一回事了

      --force         ”我不管，你给我装好"命令
          实际上相当于 replacepkgs+replacefiles，但是依赖冲突还是会中断它

      --excludedocs   不要给这个包装文档
          rpm把文件分成了三类，配置文件，文档，其他文件

      --includedocs   装文档

      --prefix <path>把包装在指定的位置

      --noscripts     不要执行安装前和安装后脚本
          如果不知道你这么做会发生什么就不要加这个选项，因为可能造成危险的后果

      --percent       显示安装进度

      --rffile <rcfile> 指定rpm的设置

      --root <path>   把这个目录作为根目录

      --dppath <path> 通过这个path找RPM数据库

      --ftpath <port> 在基于ftp的安装中用这个端口

      --ftpproxy<host>用这个host作为代理

      --ignorearch    不要验证包的架构
            rpm包中会指定架构，有事可能有错误（没有覆盖使用机器的架构），所以你可以选择忽略

      --ignoreos      不要验证操作系统

  ## 三 擦除

  移除命令

      rpm -e xxx

  选项

    .
      -v             啰嗦的输出

      --test        实验一下
            什么都不删，结合-vv有奇效

      --nodeps      不检查依赖

      --noscripts   不执行 pre 和 post 安装脚本

      --fcfile，--root，--dppath都和安装中的意义相同

注意：
- 用rpm移除是很方便的，所以不要删除你不知道是什么的东西，例如
  - 用rpm删除rpm自己，那么你将用于失去rpm，因为rpm要用rpm来装
  - 用rpm删除bash，这条命令基本会让你的系统没法正常运行

## 四 升级

升级命令

    rpm -u xxx

选项

    .
      -
