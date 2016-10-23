#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Xion Chen  <xionchen@foxmail.com>

import os


def get_valid_option(promt, valiad_list):
    valiad = False
    while (not valiad):
        result = raw_input(promt)
        if result in valiad_list:
            valiad = True
    return result


def print_mode_help():
    print
    print("=" * 50)
    print("- 手动模式: 在镜像中手动定制你想要的任何配置,安装软件等")
    print("- 自动模式: 先进行配置,然后根据配置来自动安装")
    print("该程序调用了dib,仅仅是增加了一层易用,\n需要全自动化可以直接使用dib,dib能够满足要求")
    print("=" * 50)
    print


def print_element_help():
    print
    print("更多详细用法请见,http://docs.openstack.org/developer/diskimage-builder/elements.html")
    print

def get_dib_options_string():
    opt_str_list = []
    trace = get_valid_option("是否打开调试模式:[y\\n]:\n", ['y', 'n'])

    if trace == 'y':
        opt_str_list.append('-x')
    image_type = get_valid_option("选择镜像的格式(qcow2,tar,vhd,docker,aci,raw),默认为qcow2\n", \
                                  ['qcow2', 'tar', 'vhd', 'docker', 'aci', 'raw', ''])
    if image_type != "":
        opt_str_list.append('-t %s' % image_type)
    tmpfs = get_valid_option("是否使用tmpfs[y\\n]", ['y', 'n'])

    if tmpfs == 'n':
        opt_str_list.append("--no-tmpfs")

    elements = raw_input("如果还需要其他元素,请输入,并且用空格分割\n   [h] for help")
    while elements == 'h':
        print_element_help()
        elements = raw_input("如果还需要其他元素,请输入,并且用空格分割\n   [h] for help")

    opt_str_list.append(elements)



    opt_str = ' '.join(opt_str_list)
    return opt_str


def config_install_software():
    os.system('vim ../package-install.yaml')


def do_manual_operation():
    opt_str = get_dib_options_string()
    cmd = 'break=after-install disk-image-create vm euleros %s' % opt_str
    print "run %s" % cmd
    os.system(cmd)


def do_auto_operation():
    opt_str = get_dib_options_string()
    config_install_software()
    cmd = 'disk-image-create vm euleros %s' % opt_str
    print 'run %s' % cmd
    os.system(cmd)


def main():
    mode = get_valid_option("选择模式:[1]手动 [2]自动:\
            [h]for help\n", ['1', '2', 'h'])
    while mode == 'h':
        print_mode_help()
        mode = get_valid_option("选择模式:[1]手动 [2]自动:\
                [h]for help\n", ['1', '2', 'h'])

    if mode == '1':
        do_manual_operation()
    elif mode == '2':
        do_auto_operation()


if __name__ == "__main__":
    main()
