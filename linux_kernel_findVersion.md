# linux kernel source code 初探
## 一 、/proc/version中的信息是如何写入的
在Linux中有额外的机制可以为内核和内核模块将信息发送给进程-- /proc 文件系统。最初设计的目的是允许更方便的对进程信息进行访问（因此得名）。
- proc 文件系统是一种内核和内核模块用来向进程(process) 发送信息的机制(所以叫做/proc)。
- 这个伪文件系统让你可以和内核内部数据结构进行交互，获取 有关进程的有用信息，在运行中(on the fly) 改变设置(通过改变内核参数)。
- 与其他文件系统不同，/proc 存在于内存之中而不是硬盘上。

这里讲述了一些相关的信息：
<br>http://blog.csdn.net/kevinx_xu/article/details/8178746

通过一个简单的例子来分析这一过程：
打印操作系统的版本信息

    cat /proc/version
来查看内核的信息，结果如下：

    Linux version 4.4.0-24-generic (buildd@lgw01-12) (gcc version 5.3.1 20160413 (Ubuntu 5.3.1-14ubuntu2.1) )#43-Ubuntu SMP Wed Jun 8 19:27:37 UTC 2016


### 1.1kernel源码文件目录结构
根据我自己的操作系统的版本，在kernel.org上下载了对应的源码,文件的目录结构如下：

```
arch     CREDITS        firmware  ipc      lib          net             scripts   usr
block    crypto         fs        Kbuild   MAINTAINERS  README          security  virt
certs    Documentation  include   Kconfig  Makefile     REPORTING-BUGS  sound
COPYING  drivers        init      kernel   mm           samples         tools
```
this is a website that I refered to:<br>
http://gaylord.iteye.com/blog/2176841

- COPYING 版权声明，linux是一个GNU项目，是在GPL下的项目，在此之上的程序，要公开源码
- CREDITS： 工作人员
- MAINTAINERS： 维护人员
- Makefile： 第一个Makefile文件
- README： 说明书
- Arch/： 包含了与结构体系相关的代码，每个子目录表示一种体系结构。
- Inculde/： 就是各种头文件，与平台没关系的头文件就在linux中，其他的就在相应的体系目录下
- Init/： 包含了初始化的代码，，包含了main.c和Version.c
- Mn/: 这个目录包括了独立于cpu体系结构的内存管理代码。与体系结构有关的代码在arch/*/mm中
- Kernel/: 主要的核心代码，实现了大多数linux系统的内核函数
- Drivers/： 各种驱动
- Documentation/：各种文档，告诉你各种技巧，你懂得
- Fs/: 所有和文件系统代码和各个类型的文件系统操作相关 的代码
- Ipc/：就是ipc
- Lib/:核心库
- Net：/网络
- Modules/：模块文件，用于存放编译时产生的模块目标文件
- Scripts/： 描述文件，脚本，配置文件

###　1.2 Init/version.c
```c
/*
 *  linux/init/version.c
 *
 *  Copyright (C) 1992  Theodore Ts'o
 *
 *  May be freely distributed as part of Linux.
 */

#include <generated/compile.h>
#include <linux/module.h>
#include <linux/uts.h>
#include <linux/utsname.h>
#include <generated/utsrelease.h>
#include <linux/version.h>
#include <linux/proc_ns.h>

#ifndef CONFIG_KALLSYMS
#define version(a) Version_ ## a
#define version_string(a) version(a)

extern int version_string(LINUX_VERSION_CODE);
int version_string(LINUX_VERSION_CODE);
#endif

struct uts_namespace init_uts_ns = {
        .kref = {
                .refcount       = ATOMIC_INIT(2),
        },
        .name = {
                .sysname        = UTS_SYSNAME,
                .nodename       = UTS_NODENAME,
                .release        = UTS_RELEASE,
                .version        = UTS_VERSION,
                .machine        = UTS_MACHINE,
                .domainname     = UTS_DOMAINNAME,
        },
        .user_ns = &init_user_ns,
        .ns.inum = PROC_UTS_INIT_INO,
#ifdef CONFIG_UTS_NS
        .ns.ops = &utsns_operations,
#endif
};
EXPORT_SYMBOL_GPL(init_uts_ns);

/* FIXED STRINGS! Don't touch! */
const char linux_banner[] =
        "Linux version " UTS_RELEASE " (" LINUX_COMPILE_BY "@"
        LINUX_COMPILE_HOST ") (" LINUX_COMPILER ") " UTS_VERSION "\n";

const char linux_proc_banner[] =
        "%s version %s"
        " (" LINUX_COMPILE_BY "@" LINUX_COMPILE_HOST ")"
        " (" LINUX_COMPILER ") %s\n";

```
这里会根据不同的架构等等配指出最后的一个version的字符，内核可以通过这个文件来获取version信息

### 1.3　fs/proc/version.c

```c
#include <linux/fs.h>
#include <linux/init.h>
#include <linux/kernel.h>
#include <linux/proc_fs.h>
#include <linux/seq_file.h>
#include <linux/utsname.h>

static int version_proc_show(struct seq_file *m, void *v)
{
        seq_printf(m, linux_proc_banner,
                utsname()->sysname,
                utsname()->release,
                utsname()->version);
        return 0;
}

static int version_proc_open(struct inode *inode, struct file *file)
{
        return single_open(file, version_proc_show, NULL);
}

static const struct file_operations version_proc_fops = {
        .open           = version_proc_open,
        .read           = seq_read,
        .llseek         = seq_lseek,
        .release        = single_release,
};

static int __init proc_version_init(void)
{
        proc_create("version", 0, NULL, &version_proc_fops);
        return 0;
}
fs_initcall(proc_version_init);

```
version_proc_show函数的作用是seq文件的标准写，而seq_file这种机制就这里的关键所在

### 1.4然后我就找到了两篇详细讲述这个过程的博客

博客１<br>
http://blog.chinaunix.net/uid-20543672-id-3220151.html

博客２<br>
https://www.ibm.com/developerworks/cn/linux/l-kerns-usrs/

对于proc下的文件，有两种方式可以进行设置，对于它的设置的实质上是用户空间与内核空间信息的交换的方式

#### 1.4.1 procfs
这个方式是以前的linux内核使用的方式，自从3.10的内核版本开始，里面的一些api就被废弃了。

这种方式下，提供了下面一些api

create_proc_entry   创建一个条目

remove_proc_entry   删除一个条目

proc_mkdir          创建一个目录

proc_syslink        创建软连接

。。。

这些函数与文件系统的操作有一定程度的相似，用户可以通过cat和echo来查看这些proc文件，但是procfs对于超过一个页的大文件处理起来比较复杂，所以针对这一缺陷，剔除了seq_file的概念

#### 1.4.2  seq_file
如果要使用seq_file 功能，用户要包含linux/seq_file文件，并且定义一个seq_operations的结构：
```c
struct seq_operations {
        void * (*start) (struct seq_file *m, loff_t *pos);
        void (*stop) (struct seq_file *m, void *v);
        void * (*next) (struct seq_file *m, void *v, loff_t *pos);
        int (*show) (struct seq_file *m, void *v);
};
```
start函数用于指定seq_file文件的读开始位置，返回实际读开始位置，如果指定的位置超过文件末尾，应当返回NULL，start函数可以有一个特殊的返回SEQ_START_TOKEN，它用于让show函数输出文件头，但这只能在pos为0时使用<br>
next函数用于把seq_file文件的当前读位置移动到下一个读位置，返回实际的下一个读位置，如果已经到达文件末尾，返回NULL<br>
stop函数用于在读完seq_file文件后调用，它类似于文件操作close，用于做一些必要的清理，如释放内存等<br>
show函数用于格式化输出，如果成功返回0，否则返回出错码。

##### Seq_file也定义了一些辅助函数用于格式化输出：
    int seq_putc(struct seq_file *m, char c);
函数seq_putc用于把一个字符输出到seq_file文件。

    int seq_puts(struct seq_file *m, const char *s);
函数seq_puts则用于把一个字符串输出到seq_file文件。

    int seq_escape(struct seq_file *, const char *, const char *);
函数seq_escape类似于seq_puts，只是，它将把第一个字符串参数中出现的包含在第二个字符串参数中的字符按照八进制形式输出，也即对这些字符进行转义处理。

    int seq_printf(struct seq_file *, const char *, ...)
            __attribute__ ((format (printf,2,3)));
函数seq_printf是最常用的输出函数，它用于把给定参数按照给定的格式输出到seq_file文件。

    int seq_path(struct seq_file *, struct vfsmount *, struct dentry *, char *);
函数seq_path则用于输出文件名，字符串参数提供需要转义的文件名字符，它主要供文件系统使用。

在定义了结构struct seq_operations之后，用户还需要把打开seq_file文件的open函数，以便该结构与对应于seq_file文件的struct file结构关联起来，例如，struct seq_operations定义为：
```c
struct seq_operations exam_seq_ops = {
	.start = exam_seq_start,
   .stop = exam_seq_stop,
   .next = exam_seq_next,
   .show = exam_seq_show
};
```

那么，open函数应该如下定义：
```c
static int exam_seq_open(struct inode *inode, struct file *file)
{
        return seq_open(file, &exam_seq_ops);
};
```
注意，函数seq_open是seq_file提供的函数，它用于把struct seq_operations结构与seq_file文件关联起来。 最后，用户需要如下设置struct file_operations结构：
```c
struct file_operations exam_seq_file_ops = {
        .owner   = THIS_MODULE,
        .open    = exm_seq_open,
        .read    = seq_read,
        .llseek  = seq_lseek,
        .release = seq_release
};
```

注意，用户仅需要设置open函数，其它的都是seq_file提供的函数。
然后，用户创建一个/proc文件并把它的文件操作设置为exam_seq_file_ops即可：
```c
struct proc_dir_entry *entry;
entry = create_proc_entry("exam_seq_file", 0, NULL);
if (entry)
entry->proc_fops = &exam_seq_file_ops;
```
对于简单的输出，seq_file用户并不需要定义和设置这么多函数与结构，它仅需定义一个show函数，然后使用single_open来定义open函数就可以，以下是使用这种简单形式的一般步骤：

1. 定义一个show函数
```c
int exam_show(struct seq_file *p, void *v)
{
…
}```

2. 定义open函数
```c
int exam_single_open(struct inode *inode, struct file *file)
{
        return(single_open(file, exam_show, NULL));
}```

  注意要使用single_open而不是seq_open。

3. 定义struct file_operations结构
```c
struct file_operations exam_single_seq_file_operations = {
        .open           = exam_single_open,
        .read           = seq_read,
        .llseek         = seq_lseek,
        .release        = single_release,
};
```

注意，如果open函数使用了single_open，release函数必须为single_release，而不是seq_release。 在源代码包中给出了一个使用seq_file的具体例子seqfile_exam.c，它使用seq_file提供了一个查看当前系统运行的所有进程的/proc接口，在编译并插入该模块后，用户通过命令"cat /proc/ exam_esq_file"可以查看系统的所有进程。

    到了这里我们再回看version.c文件就十分的清晰明了了，
show函数负责打印信息，
```c
static int version_proc_show(struct seq_file *m, void *v)
{
        seq_printf(m, linux_proc_banner,
                utsname()->sysname,
                utsname()->release,
                utsname()->version);
        return 0;
}

```

open函数负责打开文件
```c
static int version_proc_open(struct inode *inode, struct file *file)
{
        return single_open(file, version_proc_show, NULL);
}

```

operations函数负责定义一些操作
```c
static const struct file_operations version_proc_fops = {
        .open           = version_proc_open,
        .read           = seq_read,
        .llseek         = seq_lseek,
        .release        = single_release,
};

```


初次之外，这里有一个proc_version_init函数，它在这里定义了入口，这个__init表示内核启动的时候使用的初始化代码，内核启动完成之后就不在使用了。
```c
static int __init proc_version_init(void)
{
        proc_create("version", 0, NULL, &version_proc_fops);
        return 0;
}

```
