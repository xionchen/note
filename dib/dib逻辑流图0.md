```{puml}
@startuml
skinparam monochrome true
title 创建一个合适的块设备
start
:删除lost-found;
:sync;
:unmount所有当前镜像文件夹下的所有挂载目录;
:将mnt目录重名名为built;
if (已经设置了大小) then (yes)
    :使用设置的大小;
else (no)
    :计算现在所占的空间,然后扩展1.6倍作为大小;
endif 
if (文件系统类型是ext4) then (yes)
    :空间需要加上6m来存放日志文件系统;
endif
:向下取整,让大小是64k的整数倍;
:创建一个大小为之前结果的文件;
:在这个文件上创建一个块设备;
:run_d block-device;
:mkfs创建文件系统;
stop
@enduml
```

```{puml}
@startuml
skinparam monochrome true
title dib功能测试流程图
start
:找到所有的test_elements想的各个element;
:每个element还有测试的类型(但这只是个名字,具体逻辑还是认为控制);
:逐个测试每组test_elements,主要的测试依据是是否有镜像完成;
stop
@enduml
```

```{puml}
@startuml
skinparam monochrome true
title dib功能测试流程图
start
:处理参数;
:展开元素;
:检查环境;
:create_base(有了一个chroot的环境);
:在镜像中安装一些需要用到的工具;
:extra-data;
:pre_install;
:do_extra_package_install;
:install;
:post_install;
:创造大小合适的文件;
:在这个文件上建立块设备;
:建立分区和文件系统;
:把之前镜像中的内容拷贝到这个块设备上;
:finalise_base(防止遗留);
:通过qemu-img工具转换格式;
stop
@enduml
```