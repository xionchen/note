# scalpels项目分析
## 0、简述


    一句话：分布式的追踪和debuging工具

目的：
  - 首先了解各个文件是是什么，干什么，从而了解openstack项目的结构，测试和持续集成
  - 然后再了解项目中涉及的相关的概念
  - 最后了解项目本身

## 1、文件目录结构和关系
这里逐个说明目录下的文件和作用


###    tox.ini

tox的的配置文文件

  <font color=red>这里有个问题，为什么在项目目录下直接执行flake8和执行tox -e pep8返回的结果是不同的？</font>



```
[tox]                                      #主要是一些全局变量
minversion = 1.6                            #最低的需求的tox版本
skipsdist = True                            #跳过sdisk
envlist = py27,py34,pep8                    #环境的列表

[testenv]                                  #配置默认的测试环境
setenv = VIRTUAL_ENV={envdir}              #包含一个多列的 NAME=VALUE的环境变量（次行不清楚，可能是默认的行）
        LANG=en_US.UTF-8  【1】            #（虽然知道是配置的是语言，但是不知道有什么用）
        LANGUAGE=en_US:en
        LC_ALL=C                          #去除所有本地化设置
        PYTHONHASHSEED=0                    #hash随机种子，保证随机的结果是一样的（python环境变量）
deps = -r{toxinidir}/requirements.txt        #依赖 可以直接写在这里，也可以写到一个txt文件中
      -r{toxinidir}/test-requirements.txt
install_command = pip install -U {opts} {packages} #packages会自动被替换为要安装的包 opts的作用是可以接受诸如indexserver这样的参数
usedevelop = True                              #使用setup.py develop而不是setup.py install
commands =                                    #测试命令 可以在命令前加 - 来忽略命令的exit编号
  /usr/bin/find . -type f -name "*.pyc" -delete #删除编译的文件
  python setup.py testr --slowest --testr-args='{posargs}'#【2】【3】testr全称test repository是一个追踪测试工具，
因为它整合到了setuptools中，所有可以用这种方式并行的调用。这里的posargs是可能的潜在的参数 ， slowest表示显示最慢的测试
任何测试可以作为一个自单元测试流插入到仓库中
distribute = false                        #不使用默认的虚拟环境中的 distribute（也是一个打包，安装工具），这里使用的是setuptools所以是false
basepython = python2.7                    #用来创造虚拟环境的的python的编译器的名字

[testenv:pep8]              #this ia a name for virtual environment
commands = flake8            #flake8是一个 pep8 PyFlakes 和Ned Batchelder’s McCabe script的一个包裹，它会执行flake8 它会读取一些配置【4】
#commands = {toxinidir}/tools/fake_pep8.sh
distribute = false          #这里是多余的

[testenv:py34]
basepython = python3.4    #和之前是一样的

[testenv:venv]
commands = {posargs}

[testenv:cover]
commands = {toxinidir}/tests/ci/cover.sh {posargs}    #覆盖率测试

[testenv:docs]
changedir = doc/                                    #转换工作目录
commands = make html

[flake8]
ignore = H703,H102,E265,E262,H233
show-source = true
exclude=.venv,.git,.tox,dist,doc,*lib/python*,*egg,tools,build,setup.py,tests/ci/*,scripts/*
```


###    test-requirements.txt
    它服务与tox.ini文件，其中定义了test所需的依赖：
```
#The order of packages is significant, because pip processes them in the order
#of appearance. Changing the order has an impact on the overall integration
#process, which may cause wedges in the gate later.
hacking<0.10,>=0.9.2      #【4】是一系列flake8插件

coverage>=3.6              #【5】 python代码的覆盖率测试
ddt>=0.7.0                #多测试用例的库
mock>=1.2                  #python中用于测试的库，可以用mock对象来代替系统中的组件。用于测试
testrepository>=0.0.18    #这个项目提测试结果的数据库可以用来检测这些情况：
                            没有测试失败没有提交，测试固定周期
                            没有新的测试添加没有提交
                            自从上一次提交开始最晚失败的测试
                            现在什么测试失败了，需要工作
testtools>=1.4.0        #python单元测试的框架扩展

oslosphinx>=2.5.0 # Apache-2.0 #OpenStack项目中Sphinx文件的主题和扩展的支持
oslotest>=1.10.0 # Apache-2.0  #Oslo测试框架提供通用的组件，支持debugging和mocking结果的更好的支持

    setup.py
这个文件包含了setuptools(他是Distutils的增强)，可以用于安装，测试，发布等
pbr【6】

    setup.cfg
setup.cfg提供一种方式，可以让包的开发者提供命令的默认选项，同时为用户提供修改的机会。对setup.cfg的解析，是在setup.py之后，在命令行执行前。

[metadata]                      #metadata包含了这个组件的一些元数据信息
name = scalpels
summary = OpenStack digging system
description-file = README.rst
author = Kun Huang
author-email = academicgareth@gmail.com
maintainer = Kun Huang
maintainer-email = academicgareth@gmail.com
home-page = https://github.com/pyKun/scalpels
license = apache v2.0
classifier =
    Topic :: Utilities
    Intended Audience :: Developers
    Intended Audience :: Information Technology
    Intended Audience :: System Administrators
    Environment :: Console
    License :: OSI Approved :: Apache Software License
    Operating System :: POSIX :: Linux
    Programming Language :: Python
    Programming Language :: Python :: 2
    Programming Language :: Python :: 2.7
    Programming Language :: Python :: 3
    Programming Language :: Python :: 3.4

[files]
packages = scalpels

[entry_points]              #定义了命令行脚本和python库的入口点
console_scripts =
    sca = scalpels.client.shell:main
    sca-manage = scalpels.cmd.manage:main
    sca-agent = scalpels.cmd.agent:main
    sca-tracer = scalpels.cmd.tracer:main
```
###    .testr.conf【7】
    他是testr的配置文件，里面配置了单元测试的脚本
```
[DEFAULT]
test_command=OS_STDOUT_CAPTURE=1 OS_STDERR_CAPTURE=1 ${PYTHON:-python} -m subunit.run discover -t ./ ./tests/unit $LISTOPT $IDOPTION
#运行test/unit目录下的所有文件进行测试，显示最慢的（OS_STDOUT_CAPTURE和OS_STDERR_CAPTURE表示是否捕获测试的输出和错误输出）

test_id_option=--load-list $IDFILE    #
test_list_option=--list #列出所有的测试的选项？
```
###    .gitreview
    gitreview所用的一些配置

###    .gitignore
    git在add的时候需要忽略的文件

###    tools文件夹
    基本每个项目都会放如此一个文件夹，里面会包含一些测试的脚本和安装的脚本等（这个某种配置所需还是俗成约定？）
    例如 pretty_tox.sh    flake8wrap.sh   install_venv.py等

### test文件夹
    --ci     #在集成测试中的测试代码
  <br/>

    --unit    #会在测试中被调用，由tox中的commond中调用到testr，在testr的配置文件中可以看到调用了这个文件夹的内容做单元测试

###    scalpels文件夹
项目主要的py代码所在，在之后进行分析

### 项目主要的脚本，在之后进行分析

###    doc
    这个文件夹包含了一些source和一个makefile，source主要是README markdown文件有关
    makefile是一个标准的sphinx 文件的makefile，类似于javadoc来为python代码生成一个文档【8】
    keystone中使用的似乎是markdown格式

###   devstack
    这个文件夹和devstack项目有关
    在devstack中支持一个标准化的机制来从其他仓库引入插件。【9】这个插件的接口有一下的假设：
    在顶层目录中有一个devstack/文件夹，里面包含三个文件

- override-defaults 包含了全局变了的文件，会在lib/\*file文件之前被sourced，可以覆盖默认的一些参数
举例言之：
    可以覆盖CINDER_ENABLED_BACKENDS来引入一个插定特定的存储后端，这样能够负载默认的Cinder的仅有的后端存储的默认lvm

- setting 包含了在过程之中很早就会被sourced的全局变量。这样如果其他的插件也需要它就也可以
最好这么声明比较安全：
FOO=${FOO:-default}.

- plugin.sh 就是插件，在stack.sh中某个特定的点会被执行
<br/>
<br/>

在local.conf中是这么定义一个插件的

    [[local|localrc]]
    enable_plugin <NAME> <GITURL> [GITREF]
    名字就是一个随便的名字，你想取啥都随你
    giturl很显然是git的url
    gitref是git clone的分支 默认的分支是master

## 2、OpenStack CI
OpenStack 如何安装和维护它的基础设施的，通过对openstack ci工程的角度切入到项目中，同时也是从项目的角度切入ci

### 基础设施工程
#### 范围
    包括了 部署，测试和协作工具（其实主页也算是一个基础设施工程）
    这里有一个幻灯片讲了openstack的ci：
        http://docs.openstack.org/infra/publications/zuul/#(1)

#### 优先级努力
    指定一些优先级高的。集中资源

#### 测试基础设施需求
总体需求
     能阻止代码合入的测试必须是高可用的 ，有不同的故障域，因为测试失败的后果是比较坑爹的

测试运行风格
- 实验，实验job有较低的可靠性需求，是开发者手动启动的，
- silent，没有准备好投票的job。其他方面和checkjob一样
- 第三方，只能给代码vote（+-1）.第三方job不能阻止代码落地，不能作为gates，不能+2
- check，检测每个提交到gerrit上的path，checkjob的失败会组织代码落地，所以要高可用
- gates，gates job用于检测批准后的path的失误，用于检测予以冲突多个path合并的错误。gate出错会到是path无法落地和在复检之后的所有pathes挂起。他必须要HA

### 主要的系统（只是简单说说每个系统是干嘛的）

#### Cacti
    一个前段的RRD工具，存储信息来创造图像，用mysql数据库的信息填充他们。

#### Gerrit
    一个review系统，

#### Grafana
    一个开源的dashboard，openstack运行Graphite，其中存储所有与Nodepool,Zuul和jenkins相关的矩阵
    Grafyaml是一个利用Git中存储的YAML文件来配置Grafana dashboard的系统

#### Jenkins
    Jenkins是一个持续集成工具，上面会运行测试和自动项目运作的某些部分。
    它大部分通过Zuul来控制，Zuul决定了再上面要运行的job

#### Zuul
Zuul是个面向管道的gating系统。作为Gerrit时间的回应，它促成运行测试和自动化任务
Zuul的管道：
    - check
    新的上传的pathset进入这个管道来获得jenkins的+/-1
    - gate
    被core同一个的改变会按照顺序进入这个管道，如果它们通过了Jenkins的测试，会被合入
    - post
    这个管道运行在change被合入之后的操作的jobs
    - pre-release
    这个管道在项目中运行job来回应pre-lease标签
    - release
    如果commit被标记作为一个release，这个管道运行job来出版archives和文档
    - silent
    这个管道用于运行新job的silently测试
    - experimental
     这个管道用于 新jobs 的on-demand测试
    - periodic
    这个管道有jobs，这些jobs用定时器出发（例如测试每天环境的变化）
Zuul观测Gerrit中的事件（使用Gerrit“流事件”指令），然后把这些事件和相应的管道相结合，如果发现了匹配，它会将变化添加到管道中，同事开始运行相关的工作
    Gate管道采用推测执行，假设前面的工作会被合入，一定前面的没有被成功合入，就会重新进行没有前面的测试

#### Jenkins Job Builder
    它是一个用简单的YAML文件来配置Jenkinsjobs的系统

#### Logstack
    它是一个高性能的log 索引和搜索引擎

#### Devstack Gate
    一些列测试脚本，OpenStack CI 用于测试每个变化对于核心openstack项目的变化，通过用davsatck把openstack部署再一个云服务器上
Any proposed change to the configured set of projects must pass the devstack gate test【10】
    how it work
    devstack从一个本质上是裸的虚拟机开始准备测试环境（这个虚拟机由Nodepool提供）。这是由devstack-gate仓库驱动的，它持有几个由jenkins来运行的脚本。

- 如果core通过了变化，jenkins就触发davestack测试。

- 首先job在一个事先配置好的机器上运行devstack-vm-gate-wrap.sh它会把代码从仓库中check out同时merges变动。

- 然后脚本调用devstack-vm-gate.sh安装一个devstak配置文件

- 然后调用devstack。

- 在devstak完成之后，运行exercies.sh 和 Tempest，作为集成测试

- 一切完成后，devstak-gate复制所有的log，jenkin job吧这些log复制到日志归档

#### Nodepool
    在云服务器上部署和管理devstack镜像池的服务，这个镜像池用于openstack 工程测试

#### Jeepyb
    一些管理Gerrit的工具。管理gerrit项目和相关的上游集成（与例如Github和Launchpad）

#### IRC服务
    聊天服务

#### Etherpad
    文档实时协作

#### Paste
     一个分享粘贴工具，还有这种工具你敢信？

#### Planet
    一个博客聚合器

#### Puppet Master

#### stackalytics
    是一个分析工具，可视化项目，公司，共享者，和其他因素

#### Static Web Hosting
    一些虚拟主机从static.openstack.org Apache服务器提供静态数据

#### Bandersnatch
    一个pypi镜像工具

#### mailing list
    展示mail list

#### wiki
    就是一个wiki

#### git
    就是一个git

#### openstackid Server
    为所有的openstack web提供唯一的在线身份

#### StoryBoard
    任务和项目的追踪，

#### Kerberos
    计算机网络授权协议，

#### OpenAFS
    文件系统，全球分布式文件系统

#### Askbot
    问答的东西

#### Apps site
    app目录

#### Translate
     翻译平台

#### Refstack

#### CodeSearch
    代码搜索工具



## 3、运行例子
    通过devstack plugin的方式进行运行

## 4、代码
### 4.1 devstack/plugin.sh

```shell
# plugin.sh - DevStack plugin.sh dispatch script Scalpels
#这里配置了一些目录 scalpel本地的地址 git仓库地址 分支 DATA_DIR放了一些脚本
SCALPELS_DIR=$DEST/scalpels
SCALPELS_REPO=${SCALPELS_REPO:-${GIT_BASE}/openstack/scalpels.git}
SCALPELS_BRANCH=${SCALPELS_BRANCH:-master}
SCALPELS_DATA_DIR=$DATA_DIR/scalpels/scripts
#初始化函数
function install_scalpels {
#把仓库clone下来
  git_clone $SCALPELS_REPO $SCALPELS_DIR $SCALPELS_BRANCH

  setup_develop $SCALPELS_DIR

  local tempfile=`mktemp`

  echo "$STACK_USER ALL=(ALL) NOPASSWD:ALL" >$tempfile #权限设置
  chmod 0440 $tempfile #权限
  sudo chown root:root $tempfile #文件权限
  sudo mv $tempfile /etc/sudoers.d/scalpels-tracer #移动文件
}

function init_scalpels {                                                                           #初始化
  echo "run sca setup later"
  install -d $SCALPELS_DATA_DIR                                                #这一步发生了扫描 和一条有重叠吗
  install -t $SCALPELS_DATA_DIR $SCALPELS_DIR/scripts/*
}

function start_scalpels {
  run_process scalpels "sca-agent"
  $SCALPELS_DIR/tools/init_scalpels.sh                     #启动
}

function stop_scalpels {
  stop_process scalpels
}

function configure_scalpels {
  echo "nothing need config now."
}

function install_systemtap { #下载 解压 安装
  old_dir=`pwd`
  cd $DATA_DIR
  wget https://sourceware.org/systemtap/ftp/releases/systemtap-2.5.tar.gz
  tar zxf systemtap-2.5.tar.gz
  wget https://fedorahosted.org/releases/e/l/elfutils/0.158/elfutils-0.158.tar.bz2
  tar jxf elfutils-0.158.tar.bz2
  cd systemtap-2.5
  ./configure "--with-elfutils=$DATA_DIR/elfutils-0.158" --prefix=/usr/
  make
  sudo make install
  sudo stap -e 'probe begin { printf("Hello, World!\n"); exit() }'
  cd $old_dir
}

function install_dtrace_python {         #安装dtrace
  old_dir=`pwd`
  cd $DATA_DIR

  wget https://github.com/python/cpython/archive/ad609d460a207bc12ca83b43ab764ea58bd013ab.zip -O cpython.zip
  wget https://raw.githubusercontent.com/pyKun/openstack-systemtap-toolkit/master/cpython-patch/python_dtrace-2_7_9-enhanced.patch -O python_dtrace-2_7_9-enhanced.patch
  unzip cpython.zip
  mv ./cpython-ad609d460a207bc12ca83b43ab764ea58bd013ab ./cpython
  cd cpython

  git init
  git apply ../python_dtrace-2_7_9-enhanced.patch

  #sudo rm -rf /usr/local/lib/python2.7
  autoconf
  ./configure "--prefix=$DATA_DIR/cpython_build/" '--with-dtrace' '--enable-ipv6' '--enable-unicode=ucs2' '--with-dbmliborder=bdb:gdbm' '--with-system-expat' '--with-system-ffi' '--with-fpectl'
  make -j && make install

  cd $DATA_DIR
  ./cpython_build/bin/python -c "import sys"
  sudo stap -l 'process("./cpython_build/bin/python").mark("*")'
  cd $old_dir
}

# check for service enabled 配置了一些方式 让在调用stack unstack 预安装有相应的操作
下面的内容源自于devstack/stack.sh

===============start=============
549 run_phase override_defaults
578 run_phase source
756 run_phase stack pre-install
1165 run_phase stack post-config
1334 run_phase stack extra
================end================

if is_service_enabled scalpels; then

  if [[ "$1" == "stack" && "$2" == "pre-install" ]]; then
  # Set up system services
  echo_summary "Configuring system services scalpels"
  if is_ubuntu; then                                                                     #安装环境
  install_package autoconf automake gcc m4                        #安装一些配置 ubuntu的判断？  systemtap dtrace_python
  install_systemtap
  install_dtrace_python
  fi

  elif [[ "$1" == "stack" && "$2" == "install" ]]; then                #安装
  # Perform installation of service source
  echo_summary "Installing scalpels"
  install_scalpels

  elif [[ "$1" == "stack" && "$2" == "post-config" ]]; then           #配置
  # Configure after the other layer 1 and 2 services have been configured
  echo_summary "Configuring scalpels"
  configure_scalpels

  elif [[ "$1" == "stack" && "$2" == "extra" ]]; then                 #初始化，启动
  # Initialize and start the scalpels service
  echo_summary "Initializing scalpels"
  init_scalpels
  start_scalpels
  fi

  if [[ "$1" == "unstack" ]]; then                                         #停止
  # Shut down scalpels services
  # no-op
  stop_scalpels
  fi

  if [[ "$1" == "clean" ]]; then
  # Remove state and transient data
  # Remember clean.sh first calls unstack.sh
  # no-op
  :
  fi
fi
```
[4] https://pypi.python.org/pypi/hacking<br>
[5] https://pypi.python.org/pypi/coverage<br>
[6] http://docs.openstack.org/developer/pbr/<br>
[7] http://testrepository.readthedocs.io/en/latest/MANUAL.html<br>
[8] http://www.sphinx-doc.org/en/stable/invocation.html<br>
[9] http://docs.openstack.org/developer/devstack/plugins.html<br>
[10]http://docs.openstack.org/infra/system-config/devstack-gate.html<br>
