```
1: + true
2: + case "$1" in
3: + shift
4: + break
5: + export DIB_IMAGE_CACHE=/home/xion/.cache/image-create
6: + DIB_IMAGE_CACHE=/home/xion/.cache/image-create
7: + mkdir -p /home/xion/.cache/image-create
8: + '[' '' = 1 -a /home/xion '!=' '' ']'
9: + export -f _ps4
10: + export 'PS4=+ $(_ps4):   '
11: + PS4='+ $(_ps4):   '
12: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:230                  :   source /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/lib/img-defaults
13: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-defaults:source:17 :   source /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/lib/common-defaults
14: +++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-defaults:source:18 :   '[' -f /etc/debian_version ']'
15: ++++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-defaults:source:19 :   dpkg --print-architecture
16: +++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-defaults:source:19 :   _ARCH=amd64
17: +++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-defaults:source:34 :   ARCH=amd64
18: +++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-defaults:source:35 :   export ARCH
19: +++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-defaults:source:37 :   export DIB_NO_TMPFS=0
20: +++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-defaults:source:37 :   DIB_NO_TMPFS=0
21: +++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-defaults:source:38 :   export DIB_MIN_TMPFS=2
22: +++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-defaults:source:38 :   DIB_MIN_TMPFS=2
23: +++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-defaults:source:41 :   _BASE_ELEMENT_DIR=/home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements
24: +++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-defaults:source:42 :   ELEMENTS_PATH=
25: +++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-defaults:source:43 :   export ELEMENTS_PATH=/home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements
26: +++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-defaults:source:43 :   ELEMENTS_PATH=/home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements
27: +++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-defaults:source:44 :   export DIB_OFFLINE=
28: +++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-defaults:source:44 :   DIB_OFFLINE=
29: +++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-defaults:source:49 :   [[ :/home/xion/gitRepo/openstack/env/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin =~ :/sbin ]]
30: +++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-defaults:source:52 :   [[ :/home/xion/gitRepo/openstack/env/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin =~ :/usr/sbin ]]
31: +++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-defaults:source:55 :   [[ :/home/xion/gitRepo/openstack/env/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin =~ :/usr/local/sbin ]]
32: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-defaults:source:20 :   export FS_TYPE=ext4
33: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-defaults:source:20 :   FS_TYPE=ext4
34: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-defaults:source:22 :   export IMAGE_TYPE=qcow2
35: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-defaults:source:22 :   IMAGE_TYPE=qcow2
36: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-defaults:source:23 :   export IMAGE_NAME=image
37: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-defaults:source:23 :   IMAGE_NAME=image
38: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:231                  :   source /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/lib/common-functions
39: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:232                  :   source /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/lib/img-functions
40: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:234                  :   '[' 0 == 1 ']'
41: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:240                  :   '[' -z 'vm ubuntu' ']'
42: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:244                  :   arg_to_elements vm ubuntu
43: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:arg_to_elements:189 :   for arg in '"$@"'
44: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:arg_to_elements:189 :   IMAGE_ELEMENT=' vm'
45: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:arg_to_elements:189 :   for arg in '"$@"'
46: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:arg_to_elements:189 :   IMAGE_ELEMENT=' vm ubuntu'
47: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:arg_to_elements:191 :   '[' '' '!=' 1 ']'
48: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:arg_to_elements:192 :   IMAGE_ELEMENT='base  vm ubuntu'
49: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:arg_to_elements:194 :   '[' 0 == 1 ']'
50: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:arg_to_elements:197 :   echo 'Building elements: base  vm ubuntu'
51: Building elements: base  vm ubuntu
52: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:arg_to_elements:199 :   /home/xion/gitRepo/openstack/env/bin/element-info base vm ubuntu
53: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:arg_to_elements:199 :   IMAGE_ELEMENT='dib-python install-types install-bin dib-run-parts vm manifests dib-init-system cache-url pkg-map base ubuntu cloud-init-datasources bootloader package-installs dpkg dkms'
54: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:arg_to_elements:200 :   export IMAGE_ELEMENT
55: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:arg_to_elements:202 :   echo 'Expanded element dependencies to: dib-python install-types install-bin dib-run-parts vm manifests dib-init-system cache-url pkg-map base ubuntu cloud-init-datasources bootloader package-installs dpkg dkms'
56: Expanded element dependencies to: dib-python install-types install-bin dib-run-parts vm manifests dib-init-system cache-url pkg-map base ubuntu cloud-init-datasources bootloader package-installs dpkg dkms
57: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:246                  :   '[' 1 = 1 ']'
58: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:247                  :   export IMAGE_NAME=image
59: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:247                  :   IMAGE_NAME=image
60: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:251                  :   for X in '${!IMAGE_TYPES[@]}'
61: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:252                  :   case "${IMAGE_TYPES[$X]}" in
62: ++ /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:254                  :   which qemu-img
63: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:254                  :   '[' -z /usr/bin/qemu-img ']'
64: ++ /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:280                  :   which fstrim
65: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:280                  :   [[ -z /sbin/fstrim ]]
66: ++ /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:288                  :   uuidgen -r
67: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:288                  :   export DIB_IMAGE_ROOT_FS_UUID=f2413b58-3335-446c-9096-ca863816bc5b
68: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:288                  :   DIB_IMAGE_ROOT_FS_UUID=f2413b58-3335-446c-9096-ca863816bc5b
69: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:289                  :   grep -q '^ext'
70: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:289                  :   echo ext4
71: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:289                  :   '[' -z f2413b58-3335-446c-9096-ca863816bc5b ']'
72: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:296                  :   '[' -z '' ']'
73: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:299                  :   '[' ext4 = xfs ']'
74: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:302                  :   DIB_ROOT_LABEL=cloudimg-rootfs
75: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:308                  :   [[ -n '' ]]
76: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:315                  :   mk_build_dir
77: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:mk_build_dir:33 :   mktemp -t -d --tmpdir=/tmp dib_build.XXXXXXXX
78: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:mk_build_dir:33 :   TMP_BUILD_DIR=/tmp/dib_build.1CFJZpLz
79: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:mk_build_dir:34 :   mktemp -t -d --tmpdir=/tmp dib_image.XXXXXXXX
80: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:mk_build_dir:34 :   TMP_IMAGE_DIR=/tmp/dib_image.rja54tUR
81: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:mk_build_dir:35 :   '[' 0 -eq 0 ']'
82: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:mk_build_dir:36 :   export TMP_BUILD_DIR
83: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:mk_build_dir:37 :   tmpfs_check
84: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:tmpfs_check:18 :   local echo_message=1
85: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:tmpfs_check:19 :   '[' 0 == 0 ']'
86: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:tmpfs_check:20 :   '[' -r /proc/meminfo ']'
87: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:tmpfs_check:21 :   awk '/^MemTotal/ { print $2 }' /proc/meminfo
88: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:tmpfs_check:21 :   total_kB=10220952
89: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:tmpfs_check:24 :   RAM_NEEDED=4
90: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:tmpfs_check:25 :   '[' 10220952 -lt 4194304 ']'
91: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:tmpfs_check:25 :   return 0
92: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:mk_build_dir:38 :   sudo mount -t tmpfs tmpfs /tmp/dib_build.1CFJZpLz
93: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:mk_build_dir:39 :   sudo mount -t tmpfs tmpfs /tmp/dib_image.rja54tUR
94: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:mk_build_dir:40 :   id -u
95: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:mk_build_dir:40 :   id -g
96: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:mk_build_dir:40 :   sudo chown 1000:1000 /tmp/dib_build.1CFJZpLz /tmp/dib_image.rja54tUR
97: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:mk_build_dir:42 :   trap trap_cleanup EXIT
98: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:mk_build_dir:43 :   echo Building in /tmp/dib_build.1CFJZpLz
99: Building in /tmp/dib_build.1CFJZpLz
100: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:mk_build_dir:44 :   export TMP_IMAGE_PATH=/tmp/dib_image.rja54tUR/image.raw
101: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:mk_build_dir:44 :   TMP_IMAGE_PATH=/tmp/dib_image.rja54tUR/image.raw
102: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:mk_build_dir:45 :   export OUT_IMAGE_PATH=/tmp/dib_image.rja54tUR/image.raw
103: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:mk_build_dir:45 :   OUT_IMAGE_PATH=/tmp/dib_image.rja54tUR/image.raw
104: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:mk_build_dir:46 :   export TMP_HOOKS_PATH=/tmp/dib_build.1CFJZpLz/hooks
105: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:mk_build_dir:46 :   TMP_HOOKS_PATH=/tmp/dib_build.1CFJZpLz/hooks
106: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:316                  :   create_base
107: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:create_base:206 :   mkdir /tmp/dib_build.1CFJZpLz/mnt
108: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:create_base:207 :   export TMP_MOUNT_PATH=/tmp/dib_build.1CFJZpLz/mnt
109: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:create_base:207 :   TMP_MOUNT_PATH=/tmp/dib_build.1CFJZpLz/mnt
110: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:create_base:209 :   TARGET_ROOT=/tmp/dib_build.1CFJZpLz/mnt
111: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:create_base:209 :   run_d root
112: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:run_d:148 :   check_element
113: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:check_element:109 :   '[' -d /tmp/dib_build.1CFJZpLz/hooks ']'
114: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:check_element:109 :   generate_hooks
115: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:78 :   mkdir -p /tmp/dib_build.1CFJZpLz/hooks
116: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:79 :   for _ELEMENT in '$IMAGE_ELEMENT'
117: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:80 :   for dir in '${ELEMENTS_PATH//:/ }'
118: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:81 :   '[' -d /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dib-python ']'
119: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   find /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dib-python -follow -mindepth 1 -maxdepth 1 -type d -not -name tests
120: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   for _DIR in '$(find $dir/$_ELEMENT -follow -mindepth 1 -maxdepth 1 -type d -not -name tests)'
121: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:83 :   copy_hooks_not_overwrite /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dib-python/pre-install.d
122: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   basename /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dib-python/pre-install.d
123: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   _DIR=pre-install.d
124: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   test -d /tmp/dib_build.1CFJZpLz/hooks/pre-install.d
125: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   mkdir /tmp/dib_build.1CFJZpLz/hooks/pre-install.d
126: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   ls /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dib-python/pre-install.d
127: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
128: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/pre-install.d/01-dib-python ']'
129: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/pre-install.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dib-python/pre-install.d/01-dib-python
130: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:85 :   find /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dib-python -follow -maxdepth 1 -type f
131: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:85 :   for _FILE in '$(find $dir/$_ELEMENT -follow -maxdepth 1 -type f)'
132: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:86 :   cp -t /tmp/dib_build.1CFJZpLz/hooks -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dib-python/README.rst
133: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:88 :   break
134: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:79 :   for _ELEMENT in '$IMAGE_ELEMENT'
135: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:80 :   for dir in '${ELEMENTS_PATH//:/ }'
136: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:81 :   '[' -d /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/install-types ']'
137: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   find /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/install-types -follow -mindepth 1 -maxdepth 1 -type d -not -name tests
138: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   for _DIR in '$(find $dir/$_ELEMENT -follow -mindepth 1 -maxdepth 1 -type d -not -name tests)'
139: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:83 :   copy_hooks_not_overwrite /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/install-types/extra-data.d
140: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   basename /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/install-types/extra-data.d
141: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   _DIR=extra-data.d
142: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   test -d /tmp/dib_build.1CFJZpLz/hooks/extra-data.d
143: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   mkdir /tmp/dib_build.1CFJZpLz/hooks/extra-data.d
144: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   ls /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/install-types/extra-data.d
145: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
146: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/99-enable-install-types ']'
147: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/extra-data.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/install-types/extra-data.d/99-enable-install-types
148: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:85 :   find /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/install-types -follow -maxdepth 1 -type f
149: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:85 :   for _FILE in '$(find $dir/$_ELEMENT -follow -maxdepth 1 -type f)'
150: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:86 :   cp -t /tmp/dib_build.1CFJZpLz/hooks -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/install-types/README.rst
151: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:88 :   break
152: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:79 :   for _ELEMENT in '$IMAGE_ELEMENT'
153: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:80 :   for dir in '${ELEMENTS_PATH//:/ }'
154: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:81 :   '[' -d /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/install-bin ']'
155: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   find /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/install-bin -follow -mindepth 1 -maxdepth 1 -type d -not -name tests
156: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   for _DIR in '$(find $dir/$_ELEMENT -follow -mindepth 1 -maxdepth 1 -type d -not -name tests)'
157: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:83 :   copy_hooks_not_overwrite /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/install-bin/pre-install.d
158: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   basename /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/install-bin/pre-install.d
159: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   _DIR=pre-install.d
160: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   test -d /tmp/dib_build.1CFJZpLz/hooks/pre-install.d
161: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   ls /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/install-bin/pre-install.d
162: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
163: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/pre-install.d/01-install-bin ']'
164: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/pre-install.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/install-bin/pre-install.d/01-install-bin
165: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:85 :   find /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/install-bin -follow -maxdepth 1 -type f
166: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:85 :   for _FILE in '$(find $dir/$_ELEMENT -follow -maxdepth 1 -type f)'
167: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:86 :   cp -t /tmp/dib_build.1CFJZpLz/hooks -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/install-bin/README.rst
168: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:88 :   break
169: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:79 :   for _ELEMENT in '$IMAGE_ELEMENT'
170: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:80 :   for dir in '${ELEMENTS_PATH//:/ }'
171: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:81 :   '[' -d /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dib-run-parts ']'
172: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   find /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dib-run-parts -follow -mindepth 1 -maxdepth 1 -type d -not -name tests
173: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   for _DIR in '$(find $dir/$_ELEMENT -follow -mindepth 1 -maxdepth 1 -type d -not -name tests)'
174: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:83 :   copy_hooks_not_overwrite /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dib-run-parts/root.d
175: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   basename /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dib-run-parts/root.d
176: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   _DIR=root.d
177: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   test -d /tmp/dib_build.1CFJZpLz/hooks/root.d
178: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   mkdir /tmp/dib_build.1CFJZpLz/hooks/root.d
179: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   ls /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dib-run-parts/root.d
180: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
181: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/root.d/90-base-dib-run-parts ']'
182: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/root.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dib-run-parts/root.d/90-base-dib-run-parts
183: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:85 :   find /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dib-run-parts -follow -maxdepth 1 -type f
184: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:88 :   break
185: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:79 :   for _ELEMENT in '$IMAGE_ELEMENT'
186: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:80 :   for dir in '${ELEMENTS_PATH//:/ }'
187: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:81 :   '[' -d /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/vm ']'
188: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   find /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/vm -follow -mindepth 1 -maxdepth 1 -type d -not -name tests
189: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   for _DIR in '$(find $dir/$_ELEMENT -follow -mindepth 1 -maxdepth 1 -type d -not -name tests)'
190: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:83 :   copy_hooks_not_overwrite /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/vm/finalise.d
191: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   basename /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/vm/finalise.d
192: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   _DIR=finalise.d
193: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   test -d /tmp/dib_build.1CFJZpLz/hooks/finalise.d
194: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   mkdir /tmp/dib_build.1CFJZpLz/hooks/finalise.d
195: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   ls /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/vm/finalise.d
196: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
197: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/finalise.d/50-remove-bogus-udev-links ']'
198: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/finalise.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/vm/finalise.d/50-remove-bogus-udev-links
199: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   for _DIR in '$(find $dir/$_ELEMENT -follow -mindepth 1 -maxdepth 1 -type d -not -name tests)'
200: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:83 :   copy_hooks_not_overwrite /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/vm/block-device.d
201: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   basename /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/vm/block-device.d
202: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   _DIR=block-device.d
203: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   test -d /tmp/dib_build.1CFJZpLz/hooks/block-device.d
204: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   mkdir /tmp/dib_build.1CFJZpLz/hooks/block-device.d
205: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   ls /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/vm/block-device.d
206: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
207: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/block-device.d/10-partition ']'
208: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/block-device.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/vm/block-device.d/10-partition
209: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:85 :   find /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/vm -follow -maxdepth 1 -type f
210: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:85 :   for _FILE in '$(find $dir/$_ELEMENT -follow -maxdepth 1 -type f)'
211: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:86 :   cp -t /tmp/dib_build.1CFJZpLz/hooks -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/vm/element-deps
212: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:85 :   for _FILE in '$(find $dir/$_ELEMENT -follow -maxdepth 1 -type f)'
213: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:86 :   cp -t /tmp/dib_build.1CFJZpLz/hooks -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/vm/README.rst
214: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:88 :   break
215: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:79 :   for _ELEMENT in '$IMAGE_ELEMENT'
216: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:80 :   for dir in '${ELEMENTS_PATH//:/ }'
217: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:81 :   '[' -d /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/manifests ']'
218: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   find /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/manifests -follow -mindepth 1 -maxdepth 1 -type d -not -name tests
219: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   for _DIR in '$(find $dir/$_ELEMENT -follow -mindepth 1 -maxdepth 1 -type d -not -name tests)'
220: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:83 :   copy_hooks_not_overwrite /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/manifests/extra-data.d
221: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   basename /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/manifests/extra-data.d
222: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   _DIR=extra-data.d
223: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   test -d /tmp/dib_build.1CFJZpLz/hooks/extra-data.d
224: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   ls /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/manifests/extra-data.d
225: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
226: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/20-manifest-dir ']'
227: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/extra-data.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/manifests/extra-data.d/20-manifest-dir
228: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   for _DIR in '$(find $dir/$_ELEMENT -follow -mindepth 1 -maxdepth 1 -type d -not -name tests)'
229: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:83 :   copy_hooks_not_overwrite /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/manifests/environment.d
230: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   basename /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/manifests/environment.d
231: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   _DIR=environment.d
232: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   test -d /tmp/dib_build.1CFJZpLz/hooks/environment.d
233: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   mkdir /tmp/dib_build.1CFJZpLz/hooks/environment.d
234: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   ls /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/manifests/environment.d
235: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
236: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/environment.d/14-manifests ']'
237: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/environment.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/manifests/environment.d/14-manifests
238: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   for _DIR in '$(find $dir/$_ELEMENT -follow -mindepth 1 -maxdepth 1 -type d -not -name tests)'
239: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:83 :   copy_hooks_not_overwrite /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/manifests/cleanup.d
240: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   basename /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/manifests/cleanup.d
241: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   _DIR=cleanup.d
242: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   test -d /tmp/dib_build.1CFJZpLz/hooks/cleanup.d
243: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   mkdir /tmp/dib_build.1CFJZpLz/hooks/cleanup.d
244: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   ls /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/manifests/cleanup.d
245: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
246: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/01-copy-manifests-dir ']'
247: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/cleanup.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/manifests/cleanup.d/01-copy-manifests-dir
248: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:85 :   find /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/manifests -follow -maxdepth 1 -type f
249: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:85 :   for _FILE in '$(find $dir/$_ELEMENT -follow -maxdepth 1 -type f)'
250: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:86 :   cp -t /tmp/dib_build.1CFJZpLz/hooks -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/manifests/README.rst
251: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:88 :   break
252: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:79 :   for _ELEMENT in '$IMAGE_ELEMENT'
253: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:80 :   for dir in '${ELEMENTS_PATH//:/ }'
254: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:81 :   '[' -d /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dib-init-system ']'
255: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   find /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dib-init-system -follow -mindepth 1 -maxdepth 1 -type d -not -name tests
256: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   for _DIR in '$(find $dir/$_ELEMENT -follow -mindepth 1 -maxdepth 1 -type d -not -name tests)'
257: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:83 :   copy_hooks_not_overwrite /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dib-init-system/post-install.d
258: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   basename /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dib-init-system/post-install.d
259: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   _DIR=post-install.d
260: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   test -d /tmp/dib_build.1CFJZpLz/hooks/post-install.d
261: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   mkdir /tmp/dib_build.1CFJZpLz/hooks/post-install.d
262: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   ls /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dib-init-system/post-install.d
263: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
264: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/post-install.d/10-enable-init-scripts ']'
265: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/post-install.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dib-init-system/post-install.d/10-enable-init-scripts
266: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   for _DIR in '$(find $dir/$_ELEMENT -follow -mindepth 1 -maxdepth 1 -type d -not -name tests)'
267: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:83 :   copy_hooks_not_overwrite /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dib-init-system/environment.d
268: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   basename /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dib-init-system/environment.d
269: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   _DIR=environment.d
270: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   test -d /tmp/dib_build.1CFJZpLz/hooks/environment.d
271: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   ls /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dib-init-system/environment.d
272: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
273: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/environment.d/10-dib-init-system.bash ']'
274: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/environment.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dib-init-system/environment.d/10-dib-init-system.bash
275: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   for _DIR in '$(find $dir/$_ELEMENT -follow -mindepth 1 -maxdepth 1 -type d -not -name tests)'
276: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:83 :   copy_hooks_not_overwrite /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dib-init-system/pre-install.d
277: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   basename /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dib-init-system/pre-install.d
278: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   _DIR=pre-install.d
279: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   test -d /tmp/dib_build.1CFJZpLz/hooks/pre-install.d
280: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   ls /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dib-init-system/pre-install.d
281: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
282: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/pre-install.d/04-dib-init-system ']'
283: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/pre-install.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dib-init-system/pre-install.d/04-dib-init-system
284: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   for _DIR in '$(find $dir/$_ELEMENT -follow -mindepth 1 -maxdepth 1 -type d -not -name tests)'
285: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:83 :   copy_hooks_not_overwrite /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dib-init-system/install.d
286: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   basename /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dib-init-system/install.d
287: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   _DIR=install.d
288: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   test -d /tmp/dib_build.1CFJZpLz/hooks/install.d
289: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   mkdir /tmp/dib_build.1CFJZpLz/hooks/install.d
290: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   ls /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dib-init-system/install.d
291: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
292: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/install.d/20-install-init-scripts ']'
293: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/install.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dib-init-system/install.d/20-install-init-scripts
294: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:85 :   find /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dib-init-system -follow -maxdepth 1 -type f
295: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:85 :   for _FILE in '$(find $dir/$_ELEMENT -follow -maxdepth 1 -type f)'
296: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:86 :   cp -t /tmp/dib_build.1CFJZpLz/hooks -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dib-init-system/README.rst
297: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:85 :   for _FILE in '$(find $dir/$_ELEMENT -follow -maxdepth 1 -type f)'
298: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:86 :   cp -t /tmp/dib_build.1CFJZpLz/hooks -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dib-init-system/dib-init-system
299: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:88 :   break
300: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:79 :   for _ELEMENT in '$IMAGE_ELEMENT'
301: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:80 :   for dir in '${ELEMENTS_PATH//:/ }'
302: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:81 :   '[' -d /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/cache-url ']'
303: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   find /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/cache-url -follow -mindepth 1 -maxdepth 1 -type d -not -name tests
304: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   for _DIR in '$(find $dir/$_ELEMENT -follow -mindepth 1 -maxdepth 1 -type d -not -name tests)'
305: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:83 :   copy_hooks_not_overwrite /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/cache-url/bin
306: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   basename /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/cache-url/bin
307: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   _DIR=bin
308: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   test -d /tmp/dib_build.1CFJZpLz/hooks/bin
309: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   mkdir /tmp/dib_build.1CFJZpLz/hooks/bin
310: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   ls /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/cache-url/bin
311: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
312: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url ']'
313: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/bin -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/cache-url/bin/cache-url
314: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:85 :   find /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/cache-url -follow -maxdepth 1 -type f
315: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:85 :   for _FILE in '$(find $dir/$_ELEMENT -follow -maxdepth 1 -type f)'
316: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:86 :   cp -t /tmp/dib_build.1CFJZpLz/hooks -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/cache-url/__init__.py
317: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:85 :   for _FILE in '$(find $dir/$_ELEMENT -follow -maxdepth 1 -type f)'
318: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:86 :   cp -t /tmp/dib_build.1CFJZpLz/hooks -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/cache-url/README.rst
319: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:85 :   for _FILE in '$(find $dir/$_ELEMENT -follow -maxdepth 1 -type f)'
320: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:86 :   cp -t /tmp/dib_build.1CFJZpLz/hooks -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/cache-url/__init__.pyc
321: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:88 :   break
322: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:79 :   for _ELEMENT in '$IMAGE_ELEMENT'
323: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:80 :   for dir in '${ELEMENTS_PATH//:/ }'
324: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:81 :   '[' -d /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/pkg-map ']'
325: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   find /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/pkg-map -follow -mindepth 1 -maxdepth 1 -type d -not -name tests
326: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   for _DIR in '$(find $dir/$_ELEMENT -follow -mindepth 1 -maxdepth 1 -type d -not -name tests)'
327: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:83 :   copy_hooks_not_overwrite /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/pkg-map/extra-data.d
328: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   basename /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/pkg-map/extra-data.d
329: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   _DIR=extra-data.d
330: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   test -d /tmp/dib_build.1CFJZpLz/hooks/extra-data.d
331: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   ls /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/pkg-map/extra-data.d
332: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
333: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir ']'
334: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/extra-data.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/pkg-map/extra-data.d/10-create-pkg-map-dir
335: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   for _DIR in '$(find $dir/$_ELEMENT -follow -mindepth 1 -maxdepth 1 -type d -not -name tests)'
336: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:83 :   copy_hooks_not_overwrite /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/pkg-map/bin
337: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   basename /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/pkg-map/bin
338: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   _DIR=bin
339: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   test -d /tmp/dib_build.1CFJZpLz/hooks/bin
340: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   ls /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/pkg-map/bin
341: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
342: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/bin/pkg-map ']'
343: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/bin -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/pkg-map/bin/pkg-map
344: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:85 :   find /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/pkg-map -follow -maxdepth 1 -type f
345: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:85 :   for _FILE in '$(find $dir/$_ELEMENT -follow -maxdepth 1 -type f)'
346: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:86 :   cp -t /tmp/dib_build.1CFJZpLz/hooks -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/pkg-map/element-deps
347: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:85 :   for _FILE in '$(find $dir/$_ELEMENT -follow -maxdepth 1 -type f)'
348: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:86 :   cp -t /tmp/dib_build.1CFJZpLz/hooks -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/pkg-map/README.rst
349: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:88 :   break
350: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:79 :   for _ELEMENT in '$IMAGE_ELEMENT'
351: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:80 :   for dir in '${ELEMENTS_PATH//:/ }'
352: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:81 :   '[' -d /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/base ']'
353: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   find /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/base -follow -mindepth 1 -maxdepth 1 -type d -not -name tests
354: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   for _DIR in '$(find $dir/$_ELEMENT -follow -mindepth 1 -maxdepth 1 -type d -not -name tests)'
355: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:83 :   copy_hooks_not_overwrite /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/base/extra-data.d
356: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   basename /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/base/extra-data.d
357: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   _DIR=extra-data.d
358: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   test -d /tmp/dib_build.1CFJZpLz/hooks/extra-data.d
359: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   ls /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/base/extra-data.d
360: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
361: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/50-store-build-settings ']'
362: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/extra-data.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/base/extra-data.d/50-store-build-settings
363: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   for _DIR in '$(find $dir/$_ELEMENT -follow -mindepth 1 -maxdepth 1 -type d -not -name tests)'
364: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:83 :   copy_hooks_not_overwrite /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/base/environment.d
365: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   basename /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/base/environment.d
366: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   _DIR=environment.d
367: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   test -d /tmp/dib_build.1CFJZpLz/hooks/environment.d
368: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   ls /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/base/environment.d
369: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
370: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/environment.d/10-ccache.bash ']'
371: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/environment.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/base/environment.d/10-ccache.bash
372: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   for _DIR in '$(find $dir/$_ELEMENT -follow -mindepth 1 -maxdepth 1 -type d -not -name tests)'
373: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:83 :   copy_hooks_not_overwrite /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/base/root.d
374: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   basename /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/base/root.d
375: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   _DIR=root.d
376: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   test -d /tmp/dib_build.1CFJZpLz/hooks/root.d
377: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   ls /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/base/root.d
378: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
379: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/root.d/01-ccache ']'
380: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/root.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/base/root.d/01-ccache
381: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   for _DIR in '$(find $dir/$_ELEMENT -follow -mindepth 1 -maxdepth 1 -type d -not -name tests)'
382: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:83 :   copy_hooks_not_overwrite /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/base/cleanup.d
383: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   basename /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/base/cleanup.d
384: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   _DIR=cleanup.d
385: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   test -d /tmp/dib_build.1CFJZpLz/hooks/cleanup.d
386: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   ls /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/base/cleanup.d
387: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
388: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/01-ccache ']'
389: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/cleanup.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/base/cleanup.d/01-ccache
390: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
391: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/99-tidy-logs ']'
392: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/cleanup.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/base/cleanup.d/99-tidy-logs
393: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   for _DIR in '$(find $dir/$_ELEMENT -follow -mindepth 1 -maxdepth 1 -type d -not -name tests)'
394: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:83 :   copy_hooks_not_overwrite /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/base/pre-install.d
395: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   basename /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/base/pre-install.d
396: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   _DIR=pre-install.d
397: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   test -d /tmp/dib_build.1CFJZpLz/hooks/pre-install.d
398: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   ls /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/base/pre-install.d
399: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
400: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/pre-install.d/03-baseline-tools ']'
401: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/pre-install.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/base/pre-install.d/03-baseline-tools
402: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   for _DIR in '$(find $dir/$_ELEMENT -follow -mindepth 1 -maxdepth 1 -type d -not -name tests)'
403: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:83 :   copy_hooks_not_overwrite /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/base/install.d
404: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   basename /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/base/install.d
405: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   _DIR=install.d
406: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   test -d /tmp/dib_build.1CFJZpLz/hooks/install.d
407: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   ls /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/base/install.d
408: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
409: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/install.d/00-baseline-environment ']'
410: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/install.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/base/install.d/00-baseline-environment
411: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
412: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/install.d/00-up-to-date ']'
413: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/install.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/base/install.d/00-up-to-date
414: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
415: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/install.d/10-cloud-init ']'
416: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/install.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/base/install.d/10-cloud-init
417: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
418: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/install.d/50-store-build-settings ']'
419: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/install.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/base/install.d/50-store-build-settings
420: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
421: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/install.d/80-disable-rfc3041 ']'
422: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/install.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/base/install.d/80-disable-rfc3041
423: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:85 :   find /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/base -follow -maxdepth 1 -type f
424: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:85 :   for _FILE in '$(find $dir/$_ELEMENT -follow -maxdepth 1 -type f)'
425: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:86 :   cp -t /tmp/dib_build.1CFJZpLz/hooks -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/base/element-deps
426: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:85 :   for _FILE in '$(find $dir/$_ELEMENT -follow -maxdepth 1 -type f)'
427: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:86 :   cp -t /tmp/dib_build.1CFJZpLz/hooks -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/base/pkg-map
428: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:85 :   for _FILE in '$(find $dir/$_ELEMENT -follow -maxdepth 1 -type f)'
429: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:86 :   cp -t /tmp/dib_build.1CFJZpLz/hooks -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/base/README.rst
430: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:85 :   for _FILE in '$(find $dir/$_ELEMENT -follow -maxdepth 1 -type f)'
431: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:86 :   cp -t /tmp/dib_build.1CFJZpLz/hooks -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/base/package-installs.yaml
432: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:88 :   break
433: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:79 :   for _ELEMENT in '$IMAGE_ELEMENT'
434: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:80 :   for dir in '${ELEMENTS_PATH//:/ }'
435: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:81 :   '[' -d /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/ubuntu ']'
436: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   find /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/ubuntu -follow -mindepth 1 -maxdepth 1 -type d -not -name tests
437: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   for _DIR in '$(find $dir/$_ELEMENT -follow -mindepth 1 -maxdepth 1 -type d -not -name tests)'
438: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:83 :   copy_hooks_not_overwrite /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/ubuntu/environment.d
439: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   basename /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/ubuntu/environment.d
440: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   _DIR=environment.d
441: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   test -d /tmp/dib_build.1CFJZpLz/hooks/environment.d
442: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   ls /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/ubuntu/environment.d
443: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
444: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/environment.d/10-ubuntu-distro-name.bash ']'
445: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/environment.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/ubuntu/environment.d/10-ubuntu-distro-name.bash
446: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
447: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/environment.d/99-cloud-init-datasources.bash ']'
448: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/environment.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/ubuntu/environment.d/99-cloud-init-datasources.bash
449: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   for _DIR in '$(find $dir/$_ELEMENT -follow -mindepth 1 -maxdepth 1 -type d -not -name tests)'
450: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:83 :   copy_hooks_not_overwrite /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/ubuntu/root.d
451: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   basename /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/ubuntu/root.d
452: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   _DIR=root.d
453: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   test -d /tmp/dib_build.1CFJZpLz/hooks/root.d
454: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   ls /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/ubuntu/root.d
455: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
456: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/root.d/10-cache-ubuntu-tarball ']'
457: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/root.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/ubuntu/root.d/10-cache-ubuntu-tarball
458: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   for _DIR in '$(find $dir/$_ELEMENT -follow -mindepth 1 -maxdepth 1 -type d -not -name tests)'
459: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:83 :   copy_hooks_not_overwrite /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/ubuntu/pre-install.d
460: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   basename /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/ubuntu/pre-install.d
461: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   _DIR=pre-install.d
462: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   test -d /tmp/dib_build.1CFJZpLz/hooks/pre-install.d
463: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   ls /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/ubuntu/pre-install.d
464: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
465: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/pre-install.d/00-remove-apt-xapian-index ']'
466: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/pre-install.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/ubuntu/pre-install.d/00-remove-apt-xapian-index
467: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
468: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/pre-install.d/00-remove-grub ']'
469: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/pre-install.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/ubuntu/pre-install.d/00-remove-grub
470: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
471: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/pre-install.d/01-set-ubuntu-mirror ']'
472: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/pre-install.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/ubuntu/pre-install.d/01-set-ubuntu-mirror
473: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   for _DIR in '$(find $dir/$_ELEMENT -follow -mindepth 1 -maxdepth 1 -type d -not -name tests)'
474: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:83 :   copy_hooks_not_overwrite /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/ubuntu/install.d
475: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   basename /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/ubuntu/install.d
476: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   _DIR=install.d
477: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   test -d /tmp/dib_build.1CFJZpLz/hooks/install.d
478: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   ls /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/ubuntu/install.d
479: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
480: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/install.d/99-autoremove ']'
481: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/install.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/ubuntu/install.d/99-autoremove
482: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   for _DIR in '$(find $dir/$_ELEMENT -follow -mindepth 1 -maxdepth 1 -type d -not -name tests)'
483: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:83 :   copy_hooks_not_overwrite /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/ubuntu/bin
484: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   basename /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/ubuntu/bin
485: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   _DIR=bin
486: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   test -d /tmp/dib_build.1CFJZpLz/hooks/bin
487: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   ls /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/ubuntu/bin
488: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
489: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/bin/map-services ']'
490: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/bin -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/ubuntu/bin/map-services
491: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:85 :   find /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/ubuntu -follow -maxdepth 1 -type f
492: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:85 :   for _FILE in '$(find $dir/$_ELEMENT -follow -maxdepth 1 -type f)'
493: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:86 :   cp -t /tmp/dib_build.1CFJZpLz/hooks -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/ubuntu/element-deps
494: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:85 :   for _FILE in '$(find $dir/$_ELEMENT -follow -maxdepth 1 -type f)'
495: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:86 :   cp -t /tmp/dib_build.1CFJZpLz/hooks -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/ubuntu/README.rst
496: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:85 :   for _FILE in '$(find $dir/$_ELEMENT -follow -maxdepth 1 -type f)'
497: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:86 :   cp -t /tmp/dib_build.1CFJZpLz/hooks -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/ubuntu/element-provides
498: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:85 :   for _FILE in '$(find $dir/$_ELEMENT -follow -maxdepth 1 -type f)'
499: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:86 :   cp -t /tmp/dib_build.1CFJZpLz/hooks -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/ubuntu/package-installs.yaml
500: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:88 :   break
501: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:79 :   for _ELEMENT in '$IMAGE_ELEMENT'
502: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:80 :   for dir in '${ELEMENTS_PATH//:/ }'
503: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:81 :   '[' -d /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/cloud-init-datasources ']'
504: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   find /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/cloud-init-datasources -follow -mindepth 1 -maxdepth 1 -type d -not -name tests
505: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   for _DIR in '$(find $dir/$_ELEMENT -follow -mindepth 1 -maxdepth 1 -type d -not -name tests)'
506: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:83 :   copy_hooks_not_overwrite /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/cloud-init-datasources/install.d
507: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   basename /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/cloud-init-datasources/install.d
508: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   _DIR=install.d
509: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   test -d /tmp/dib_build.1CFJZpLz/hooks/install.d
510: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   ls /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/cloud-init-datasources/install.d
511: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
512: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/install.d/05-set-cloud-init-sources ']'
513: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/install.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/cloud-init-datasources/install.d/05-set-cloud-init-sources
514: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:85 :   find /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/cloud-init-datasources -follow -maxdepth 1 -type f
515: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:85 :   for _FILE in '$(find $dir/$_ELEMENT -follow -maxdepth 1 -type f)'
516: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:86 :   cp -t /tmp/dib_build.1CFJZpLz/hooks -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/cloud-init-datasources/README.rst
517: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:88 :   break
518: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:79 :   for _ELEMENT in '$IMAGE_ELEMENT'
519: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:80 :   for dir in '${ELEMENTS_PATH//:/ }'
520: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:81 :   '[' -d /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/bootloader ']'
521: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   find /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/bootloader -follow -mindepth 1 -maxdepth 1 -type d -not -name tests
522: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   for _DIR in '$(find $dir/$_ELEMENT -follow -mindepth 1 -maxdepth 1 -type d -not -name tests)'
523: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:83 :   copy_hooks_not_overwrite /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/bootloader/cleanup.d
524: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   basename /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/bootloader/cleanup.d
525: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   _DIR=cleanup.d
526: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   test -d /tmp/dib_build.1CFJZpLz/hooks/cleanup.d
527: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   ls /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/bootloader/cleanup.d
528: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
529: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/51-bootloader ']'
530: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/cleanup.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/bootloader/cleanup.d/51-bootloader
531: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   for _DIR in '$(find $dir/$_ELEMENT -follow -mindepth 1 -maxdepth 1 -type d -not -name tests)'
532: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:83 :   copy_hooks_not_overwrite /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/bootloader/finalise.d
533: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   basename /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/bootloader/finalise.d
534: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   _DIR=finalise.d
535: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   test -d /tmp/dib_build.1CFJZpLz/hooks/finalise.d
536: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   ls /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/bootloader/finalise.d
537: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
538: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/finalise.d/50-bootloader ']'
539: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/finalise.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/bootloader/finalise.d/50-bootloader
540: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:85 :   find /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/bootloader -follow -maxdepth 1 -type f
541: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:85 :   for _FILE in '$(find $dir/$_ELEMENT -follow -maxdepth 1 -type f)'
542: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:86 :   cp -t /tmp/dib_build.1CFJZpLz/hooks -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/bootloader/pkg-map
543: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:85 :   for _FILE in '$(find $dir/$_ELEMENT -follow -maxdepth 1 -type f)'
544: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:86 :   cp -t /tmp/dib_build.1CFJZpLz/hooks -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/bootloader/README.rst
545: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:88 :   break
546: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:79 :   for _ELEMENT in '$IMAGE_ELEMENT'
547: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:80 :   for dir in '${ELEMENTS_PATH//:/ }'
548: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:81 :   '[' -d /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/package-installs ']'
549: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   find /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/package-installs -follow -mindepth 1 -maxdepth 1 -type d -not -name tests
550: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   for _DIR in '$(find $dir/$_ELEMENT -follow -mindepth 1 -maxdepth 1 -type d -not -name tests)'
551: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:83 :   copy_hooks_not_overwrite /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/package-installs/post-install.d
552: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   basename /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/package-installs/post-install.d
553: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   _DIR=post-install.d
554: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   test -d /tmp/dib_build.1CFJZpLz/hooks/post-install.d
555: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   ls /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/package-installs/post-install.d
556: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
557: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/post-install.d/00-package-installs ']'
558: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/post-install.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/package-installs/post-install.d/00-package-installs
559: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
560: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/post-install.d/95-package-uninstalls ']'
561: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/post-install.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/package-installs/post-install.d/95-package-uninstalls
562: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   for _DIR in '$(find $dir/$_ELEMENT -follow -mindepth 1 -maxdepth 1 -type d -not -name tests)'
563: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:83 :   copy_hooks_not_overwrite /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/package-installs/extra-data.d
564: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   basename /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/package-installs/extra-data.d
565: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   _DIR=extra-data.d
566: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   test -d /tmp/dib_build.1CFJZpLz/hooks/extra-data.d
567: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   ls /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/package-installs/extra-data.d
568: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
569: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/99-squash-package-install ']'
570: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/extra-data.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/package-installs/extra-data.d/99-squash-package-install
571: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   for _DIR in '$(find $dir/$_ELEMENT -follow -mindepth 1 -maxdepth 1 -type d -not -name tests)'
572: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:83 :   copy_hooks_not_overwrite /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/package-installs/pre-install.d
573: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   basename /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/package-installs/pre-install.d
574: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   _DIR=pre-install.d
575: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   test -d /tmp/dib_build.1CFJZpLz/hooks/pre-install.d
576: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   ls /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/package-installs/pre-install.d
577: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
578: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/pre-install.d/02-package-installs ']'
579: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/pre-install.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/package-installs/pre-install.d/02-package-installs
580: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
581: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/pre-install.d/99-package-uninstalls ']'
582: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/pre-install.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/package-installs/pre-install.d/99-package-uninstalls
583: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   for _DIR in '$(find $dir/$_ELEMENT -follow -mindepth 1 -maxdepth 1 -type d -not -name tests)'
584: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:83 :   copy_hooks_not_overwrite /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/package-installs/install.d
585: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   basename /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/package-installs/install.d
586: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   _DIR=install.d
587: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   test -d /tmp/dib_build.1CFJZpLz/hooks/install.d
588: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   ls /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/package-installs/install.d
589: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
590: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/install.d/01-package-installs ']'
591: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/install.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/package-installs/install.d/01-package-installs
592: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
593: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/install.d/99-package-uninstalls ']'
594: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/install.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/package-installs/install.d/99-package-uninstalls
595: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   for _DIR in '$(find $dir/$_ELEMENT -follow -mindepth 1 -maxdepth 1 -type d -not -name tests)'
596: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:83 :   copy_hooks_not_overwrite /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/package-installs/bin
597: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   basename /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/package-installs/bin
598: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   _DIR=bin
599: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   test -d /tmp/dib_build.1CFJZpLz/hooks/bin
600: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   ls /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/package-installs/bin
601: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
602: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/bin/package-installs ']'
603: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/bin -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/package-installs/bin/package-installs
604: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
605: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/bin/package-installs-squash ']'
606: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/bin -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/package-installs/bin/package-installs-squash
607: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
608: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/bin/package-installs-v2 ']'
609: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/bin -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/package-installs/bin/package-installs-v2
610: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
611: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/bin/package-uninstalls ']'
612: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/bin -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/package-installs/bin/package-uninstalls
613: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:85 :   find /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/package-installs -follow -maxdepth 1 -type f
614: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:85 :   for _FILE in '$(find $dir/$_ELEMENT -follow -maxdepth 1 -type f)'
615: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:86 :   cp -t /tmp/dib_build.1CFJZpLz/hooks -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/package-installs/element-deps
616: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:85 :   for _FILE in '$(find $dir/$_ELEMENT -follow -maxdepth 1 -type f)'
617: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:86 :   cp -t /tmp/dib_build.1CFJZpLz/hooks -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/package-installs/README.rst
618: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:88 :   break
619: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:79 :   for _ELEMENT in '$IMAGE_ELEMENT'
620: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:80 :   for dir in '${ELEMENTS_PATH//:/ }'
621: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:81 :   '[' -d /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dpkg ']'
622: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   find /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dpkg -follow -mindepth 1 -maxdepth 1 -type d -not -name tests
623: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   for _DIR in '$(find $dir/$_ELEMENT -follow -mindepth 1 -maxdepth 1 -type d -not -name tests)'
624: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:83 :   copy_hooks_not_overwrite /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dpkg/extra-data.d
625: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   basename /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dpkg/extra-data.d
626: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   _DIR=extra-data.d
627: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   test -d /tmp/dib_build.1CFJZpLz/hooks/extra-data.d
628: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   ls /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dpkg/extra-data.d
629: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
630: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/01-copy-apt-keys ']'
631: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/extra-data.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dpkg/extra-data.d/01-copy-apt-keys
632: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   for _DIR in '$(find $dir/$_ELEMENT -follow -mindepth 1 -maxdepth 1 -type d -not -name tests)'
633: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:83 :   copy_hooks_not_overwrite /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dpkg/root.d
634: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   basename /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dpkg/root.d
635: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   _DIR=root.d
636: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   test -d /tmp/dib_build.1CFJZpLz/hooks/root.d
637: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   ls /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dpkg/root.d
638: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
639: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/root.d/50-build-with-http-cache ']'
640: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/root.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dpkg/root.d/50-build-with-http-cache
641: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
642: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/root.d/60-block-apt-translations ']'
643: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/root.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dpkg/root.d/60-block-apt-translations
644: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
645: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/root.d/99-block-daemons ']'
646: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/root.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dpkg/root.d/99-block-daemons
647: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
648: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/root.d/99-shared_apt_cache ']'
649: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/root.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dpkg/root.d/99-shared_apt_cache
650: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
651: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/root.d/99-trim-dpkg ']'
652: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/root.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dpkg/root.d/99-trim-dpkg
653: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   for _DIR in '$(find $dir/$_ELEMENT -follow -mindepth 1 -maxdepth 1 -type d -not -name tests)'
654: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:83 :   copy_hooks_not_overwrite /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dpkg/cleanup.d
655: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   basename /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dpkg/cleanup.d
656: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   _DIR=cleanup.d
657: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   test -d /tmp/dib_build.1CFJZpLz/hooks/cleanup.d
658: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   ls /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dpkg/cleanup.d
659: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
660: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/40-unblock-daemons ']'
661: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/cleanup.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dpkg/cleanup.d/40-unblock-daemons
662: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
663: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/50-remove-img-build-proxy ']'
664: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/cleanup.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dpkg/cleanup.d/50-remove-img-build-proxy
665: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
666: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/60-untrim-dpkg ']'
667: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/cleanup.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dpkg/cleanup.d/60-untrim-dpkg
668: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   for _DIR in '$(find $dir/$_ELEMENT -follow -mindepth 1 -maxdepth 1 -type d -not -name tests)'
669: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:83 :   copy_hooks_not_overwrite /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dpkg/pre-install.d
670: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   basename /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dpkg/pre-install.d
671: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   _DIR=pre-install.d
672: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   test -d /tmp/dib_build.1CFJZpLz/hooks/pre-install.d
673: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   ls /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dpkg/pre-install.d
674: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
675: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/pre-install.d/00-disable-apt-recommends ']'
676: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/pre-install.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dpkg/pre-install.d/00-disable-apt-recommends
677: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
678: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/pre-install.d/02-add-apt-keys ']'
679: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/pre-install.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dpkg/pre-install.d/02-add-apt-keys
680: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
681: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/pre-install.d/99-apt-get-update ']'
682: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/pre-install.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dpkg/pre-install.d/99-apt-get-update
683: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   for _DIR in '$(find $dir/$_ELEMENT -follow -mindepth 1 -maxdepth 1 -type d -not -name tests)'
684: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:83 :   copy_hooks_not_overwrite /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dpkg/bin
685: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   basename /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dpkg/bin
686: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   _DIR=bin
687: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   test -d /tmp/dib_build.1CFJZpLz/hooks/bin
688: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   ls /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dpkg/bin
689: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
690: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/bin/install-packages ']'
691: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/bin -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dpkg/bin/install-packages
692: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   for _DIR in '$(find $dir/$_ELEMENT -follow -mindepth 1 -maxdepth 1 -type d -not -name tests)'
693: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:83 :   copy_hooks_not_overwrite /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dpkg/finalise.d
694: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   basename /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dpkg/finalise.d
695: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   _DIR=finalise.d
696: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   test -d /tmp/dib_build.1CFJZpLz/hooks/finalise.d
697: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   ls /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dpkg/finalise.d
698: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
699: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/finalise.d/99-clean-up-cache ']'
700: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/finalise.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dpkg/finalise.d/99-clean-up-cache
701: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
702: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/finalise.d/99-write-dpkg-manifest ']'
703: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/finalise.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dpkg/finalise.d/99-write-dpkg-manifest
704: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:85 :   find /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dpkg -follow -maxdepth 1 -type f
705: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:85 :   for _FILE in '$(find $dir/$_ELEMENT -follow -maxdepth 1 -type f)'
706: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:86 :   cp -t /tmp/dib_build.1CFJZpLz/hooks -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dpkg/element-deps
707: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:85 :   for _FILE in '$(find $dir/$_ELEMENT -follow -maxdepth 1 -type f)'
708: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:86 :   cp -t /tmp/dib_build.1CFJZpLz/hooks -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dpkg/README.rst
709: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:88 :   break
710: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:79 :   for _ELEMENT in '$IMAGE_ELEMENT'
711: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:80 :   for dir in '${ELEMENTS_PATH//:/ }'
712: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:81 :   '[' -d /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dkms ']'
713: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   find /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dkms -follow -mindepth 1 -maxdepth 1 -type d -not -name tests
714: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:82 :   for _DIR in '$(find $dir/$_ELEMENT -follow -mindepth 1 -maxdepth 1 -type d -not -name tests)'
715: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:83 :   copy_hooks_not_overwrite /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dkms/post-install.d
716: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   basename /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dkms/post-install.d
717: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:65 :   _DIR=post-install.d
718: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:66 :   test -d /tmp/dib_build.1CFJZpLz/hooks/post-install.d
719: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   ls /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dkms/post-install.d
720: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:67 :   for _HOOK in '$(ls $1)'
721: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:68 :   '[' '!' -f /tmp/dib_build.1CFJZpLz/hooks/post-install.d/97-dkms ']'
722: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:copy_hooks_not_overwrite:69 :   cp -t /tmp/dib_build.1CFJZpLz/hooks/post-install.d -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dkms/post-install.d/97-dkms
723: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:85 :   find /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dkms -follow -maxdepth 1 -type f
724: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:85 :   for _FILE in '$(find $dir/$_ELEMENT -follow -maxdepth 1 -type f)'
725: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:86 :   cp -t /tmp/dib_build.1CFJZpLz/hooks -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dkms/element-deps
726: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:85 :   for _FILE in '$(find $dir/$_ELEMENT -follow -maxdepth 1 -type f)'
727: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:86 :   cp -t /tmp/dib_build.1CFJZpLz/hooks -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dkms/README.rst
728: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:85 :   for _FILE in '$(find $dir/$_ELEMENT -follow -maxdepth 1 -type f)'
729: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:86 :   cp -t /tmp/dib_build.1CFJZpLz/hooks -a /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dkms/package-installs.yaml
730: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:generate_hooks:88 :   break
731: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:run_d:149 :   check_break before-root bash
732: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:check_break:98 :   echo ''
733: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:check_break:98 :   egrep -e '(,|^)before-root(,|$)' -q
734: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:run_d:150 :   '[' -d /tmp/dib_build.1CFJZpLz/hooks/root.d ']'
735: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:run_d:151 :   '[' -n '' ']'
736: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:run_d:157 :   dib-run-parts /tmp/dib_build.1CFJZpLz/hooks/root.d
737: + /tmp/dib_build.1CFJZpLz/hooks/dib-init-system:main:6                             :   set -eu
738: + /tmp/dib_build.1CFJZpLz/hooks/dib-init-system:main:7                             :   set -o pipefail
739: + /tmp/dib_build.1CFJZpLz/hooks/dib-init-system:main:9                             :   [[ -f /usr/bin/systemctl ]]
740: + /tmp/dib_build.1CFJZpLz/hooks/dib-init-system:main:11                            :   [[ -f /sbin/initctl ]]
741: + /tmp/dib_build.1CFJZpLz/hooks/dib-init-system:main:12                            :   echo upstart
742: ++ /tmp/dib_build.1CFJZpLz/hooks/environment.d/14-manifests:source:21               :   set -eu
743: ++ /tmp/dib_build.1CFJZpLz/hooks/environment.d/14-manifests:source:22               :   set -o pipefail
744: ++ /tmp/dib_build.1CFJZpLz/hooks/environment.d/14-manifests:source:24               :   export DIB_MANIFEST_IMAGE_DIR=/etc/dib-manifests
745: ++ /tmp/dib_build.1CFJZpLz/hooks/environment.d/14-manifests:source:24               :   DIB_MANIFEST_IMAGE_DIR=/etc/dib-manifests
746: ++ /tmp/dib_build.1CFJZpLz/hooks/environment.d/14-manifests:source:25               :   export DIB_MANIFEST_SAVE_DIR=image.d/
747: ++ /tmp/dib_build.1CFJZpLz/hooks/environment.d/14-manifests:source:25               :   DIB_MANIFEST_SAVE_DIR=image.d/
748: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:source_environment:65         :   for env_file in '$env_files'
749: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:source_environment:66         :   source /tmp/dib_build.1CFJZpLz/hooks/root.d/../environment.d/99-cloud-init-datasources.bash
750: ++ /tmp/dib_build.1CFJZpLz/hooks/environment.d/99-cloud-init-datasources.bash:source:4 :   export DIB_CLOUD_INIT_DATASOURCES=Ec2
751: ++ /tmp/dib_build.1CFJZpLz/hooks/environment.d/99-cloud-init-datasources.bash:source:4 :   DIB_CLOUD_INIT_DATASOURCES=Ec2
752: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:108                      :   for target in '$targets'
753: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:109                      :   output 'Running /tmp/dib_build.1CFJZpLz/hooks/root.d/01-ccache'
754: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:43                     :   output_prefix
755: ++ /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   date
756: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   printf '%s %s ' dib-run-parts '2016年 10月 03日 星期一 23:09:49 CST'
757: dib-run-parts 2016年 10月 03日 星期一 23:09:49 CST + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:44                     :   echo Running /tmp/dib_build.1CFJZpLz/hooks/root.d/01-ccache
758: Running /tmp/dib_build.1CFJZpLz/hooks/root.d/01-ccache
759: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:110                      :   target_tag=01-ccache
760: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:111                      :   date +%s.%N
761: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:112                      :   /tmp/dib_build.1CFJZpLz/hooks/root.d/01-ccache
762: + /tmp/dib_build.1CFJZpLz/hooks/root.d/01-ccache:main:6                            :   set -eu
763: + /tmp/dib_build.1CFJZpLz/hooks/root.d/01-ccache:main:7                            :   set -o pipefail
764: + /tmp/dib_build.1CFJZpLz/hooks/root.d/01-ccache:main:13                           :   grep ' /tmp/dib_build.1CFJZpLz/mnt/tmp/ccache' /proc/mounts
765: + /tmp/dib_build.1CFJZpLz/hooks/root.d/01-ccache:main:15                           :   DIB_CCACHE_DIR=/home/xion/.cache/image-create/ccache
766: + /tmp/dib_build.1CFJZpLz/hooks/root.d/01-ccache:main:16                           :   mkdir -p /home/xion/.cache/image-create/ccache
767: + /tmp/dib_build.1CFJZpLz/hooks/root.d/01-ccache:main:18                           :   sudo mkdir -p /tmp/dib_build.1CFJZpLz/mnt/tmp/ccache
768: + /tmp/dib_build.1CFJZpLz/hooks/root.d/01-ccache:main:19                           :   sudo mount --bind /home/xion/.cache/image-create/ccache /tmp/dib_build.1CFJZpLz/mnt/tmp/ccache
769: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:113                      :   target_tag=01-ccache
770: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:114                      :   date +%s.%N
771: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:115                      :   output '01-ccache completed'
772: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:43                     :   output_prefix
773: ++ /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   date
774: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   printf '%s %s ' dib-run-parts '2016年 10月 03日 星期一 23:09:49 CST'
775: dib-run-parts 2016年 10月 03日 星期一 23:09:49 CST + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:44                     :   echo 01-ccache completed
776: 01-ccache completed
777: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:108                      :   for target in '$targets'
778: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:109                      :   output 'Running /tmp/dib_build.1CFJZpLz/hooks/root.d/10-cache-ubuntu-tarball'
779: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:43                     :   output_prefix
780: ++ /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   date
781: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   printf '%s %s ' dib-run-parts '2016年 10月 03日 星期一 23:09:49 CST'
782: dib-run-parts 2016年 10月 03日 星期一 23:09:49 CST + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:44                     :   echo Running /tmp/dib_build.1CFJZpLz/hooks/root.d/10-cache-ubuntu-tarball
783: Running /tmp/dib_build.1CFJZpLz/hooks/root.d/10-cache-ubuntu-tarball
784: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:110                      :   target_tag=10-cache-ubuntu-tarball
785: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:111                      :   date +%s.%N
786: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:112                      :   /tmp/dib_build.1CFJZpLz/hooks/root.d/10-cache-ubuntu-tarball
787: + /tmp/dib_build.1CFJZpLz/hooks/root.d/10-cache-ubuntu-tarball:main:7              :   set -eu
788: + /tmp/dib_build.1CFJZpLz/hooks/root.d/10-cache-ubuntu-tarball:main:8              :   set -o pipefail
789: + /tmp/dib_build.1CFJZpLz/hooks/root.d/10-cache-ubuntu-tarball:main:10             :   '[' -n amd64 ']'
790: + /tmp/dib_build.1CFJZpLz/hooks/root.d/10-cache-ubuntu-tarball:main:11             :   '[' -n /tmp/dib_build.1CFJZpLz/mnt ']'
791: + /tmp/dib_build.1CFJZpLz/hooks/root.d/10-cache-ubuntu-tarball:main:13             :   shopt -s extglob
792: + /tmp/dib_build.1CFJZpLz/hooks/root.d/10-cache-ubuntu-tarball:main:15             :   DIB_CLOUD_IMAGES=http://cloud-images.ubuntu.com
793: + /tmp/dib_build.1CFJZpLz/hooks/root.d/10-cache-ubuntu-tarball:main:16             :   DIB_RELEASE=trusty
794: + /tmp/dib_build.1CFJZpLz/hooks/root.d/10-cache-ubuntu-tarball:main:17             :   BASE_IMAGE_FILE=trusty-server-cloudimg-amd64-root.tar.gz
795: + /tmp/dib_build.1CFJZpLz/hooks/root.d/10-cache-ubuntu-tarball:main:18             :   SHA256SUMS=https://cloud-images.ubuntu.com/trusty/current/SHA256SUMS
796: + /tmp/dib_build.1CFJZpLz/hooks/root.d/10-cache-ubuntu-tarball:main:19             :   CACHED_FILE=/home/xion/.cache/image-create/trusty-server-cloudimg-amd64-root.tar.gz
797: + /tmp/dib_build.1CFJZpLz/hooks/root.d/10-cache-ubuntu-tarball:main:20             :   CACHED_FILE_LOCK=/home/xion/.cache/image-create/trusty-server-cloudimg-amd64-root.tar.gz.lock
798: + /tmp/dib_build.1CFJZpLz/hooks/root.d/10-cache-ubuntu-tarball:main:21             :   CACHED_SUMS=/home/xion/.cache/image-create/SHA256SUMS.ubuntu.trusty.amd64
799: ++ /tmp/dib_build.1CFJZpLz/hooks/root.d/10-cache-ubuntu-tarball:main:54             :   date
800: + /tmp/dib_build.1CFJZpLz/hooks/root.d/10-cache-ubuntu-tarball:main:54             :   echo 'Getting /home/xion/.cache/image-create/trusty-server-cloudimg-amd64-root.tar.gz.lock: 2016年 10月 03日 星期一 23:09:49 CST'
801: Getting /home/xion/.cache/image-create/trusty-server-cloudimg-amd64-root.tar.gz.lock: 2016年 10月 03日 星期一 23:09:49 CST
802: + /tmp/dib_build.1CFJZpLz/hooks/root.d/10-cache-ubuntu-tarball:main:56             :   flock -w 1200 9
803: + /tmp/dib_build.1CFJZpLz/hooks/root.d/10-cache-ubuntu-tarball:main:60             :   get_ubuntu_tarball
804: + /tmp/dib_build.1CFJZpLz/hooks/root.d/10-cache-ubuntu-tarball:get_ubuntu_tarball:24 :   '[' -n '' -a -f /home/xion/.cache/image-create/trusty-server-cloudimg-amd64-root.tar.gz ']'
805: + /tmp/dib_build.1CFJZpLz/hooks/root.d/10-cache-ubuntu-tarball:get_ubuntu_tarball:27 :   echo 'Fetching Base Image'
806: Fetching Base Image
807: + /tmp/dib_build.1CFJZpLz/hooks/root.d/10-cache-ubuntu-tarball:get_ubuntu_tarball:28 :   /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url https://cloud-images.ubuntu.com/trusty/current/SHA256SUMS /home/xion/.cache/image-create/SHA256SUMS.ubuntu.trusty.amd64
808: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:21                              :   set -eu
809: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:22                              :   set -o pipefail
810: ++ /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:27                              :   basename /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url
811: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:27                              :   SCRIPT_NAME=cache-url
812: ++ /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:28                              :   dirname /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url
813: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:28                              :   SCRIPT_HOME=/tmp/dib_build.1CFJZpLz/hooks/bin
814: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:29                              :   FORCE_REVALIDATE=0
815: ++ /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:46                              :   getopt -o hf -n cache-url -- https://cloud-images.ubuntu.com/trusty/current/SHA256SUMS /home/xion/.cache/image-create/SHA256SUMS.ubuntu.trusty.amd64
816: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:46                              :   TEMP=' -- '\''https://cloud-images.ubuntu.com/trusty/current/SHA256SUMS'\'' '\''/home/xion/.cache/image-create/SHA256SUMS.ubuntu.trusty.amd64'\'''
817: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:47                              :   '[' 0 '!=' 0 ']'
818: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:50                              :   eval set -- ' -- '\''https://cloud-images.ubuntu.com/trusty/current/SHA256SUMS'\'' '\''/home/xion/.cache/image-create/SHA256SUMS.ubuntu.trusty.amd64'\'''
819: ++ /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:50                              :   set -- -- https://cloud-images.ubuntu.com/trusty/current/SHA256SUMS /home/xion/.cache/image-create/SHA256SUMS.ubuntu.trusty.amd64
820: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:52                              :   true
821: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:53                              :   case "$1" in
822: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:56                              :   shift
823: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:56                              :   break
824: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:61                              :   url=https://cloud-images.ubuntu.com/trusty/current/SHA256SUMS
825: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:62                              :   dest=/home/xion/.cache/image-create/SHA256SUMS.ubuntu.trusty.amd64
826: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:63                              :   time_cond=
827: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:64                              :   curl_opts=
828: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:66                              :   '[' -z https://cloud-images.ubuntu.com/trusty/current/SHA256SUMS -o -z /home/xion/.cache/image-create/SHA256SUMS.ubuntu.trusty.amd64 ']'
829: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:70                              :   '[' -p /home/xion/.cache/image-create/SHA256SUMS.ubuntu.trusty.amd64 ']'
830: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:74                              :   type=normal
831: ++ /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:75                              :   dirname /home/xion/.cache/image-create/SHA256SUMS.ubuntu.trusty.amd64
832: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:75                              :   mkdir -p /home/xion/.cache/image-create
833: +++ /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:76                              :   dirname /home/xion/.cache/image-create/SHA256SUMS.ubuntu.trusty.amd64
834: ++ /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:76                              :   mktemp /home/xion/.cache/image-create/.download.XXXXXXXX
835: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:76                              :   tmp=/home/xion/.cache/image-create/.download.fMMc1cM1
836: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:79                              :   '[' 0 = 1 ']'
837: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:82                              :   '[' -f /home/xion/.cache/image-create/SHA256SUMS.ubuntu.trusty.amd64 -a -s /home/xion/.cache/image-create/SHA256SUMS.ubuntu.trusty.amd64 ']'
838: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:83                              :   time_cond='-z /home/xion/.cache/image-create/SHA256SUMS.ubuntu.trusty.amd64'
839: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:84                              :   success='Server copy has changed. Using server version of https://cloud-images.ubuntu.com/trusty/current/SHA256SUMS'
840: ++ /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:89                              :   eval curl -v -L -o /home/xion/.cache/image-create/.download.fMMc1cM1 -w '%{http_code}' https://cloud-images.ubuntu.com/trusty/current/SHA256SUMS -z /home/xion/.cache/image-create/SHA256SUMS.ubuntu.trusty.amd64
841: +++ /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:89                              :   curl -v -L -o /home/xion/.cache/image-create/.download.fMMc1cM1 -w '%{http_code}' https://cloud-images.ubuntu.com/trusty/current/SHA256SUMS -z /home/xion/.cache/image-create/SHA256SUMS.ubuntu.trusty.amd64
842:   % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
843:                                  Dload  Upload   Total   Spent    Left  Speed
844:
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*   Trying 91.189.88.141...
845:
  0     0    0     0    0     0      0      0 --:--:--  0:00:01 --:--:--     0* Connected to cloud-images.ubuntu.com (91.189.88.141) port 443 (#0)
846: * found 173 certificates in /etc/ssl/certs/ca-certificates.crt
847: * found 697 certificates in /etc/ssl/certs
848: * ALPN, offering http/1.1
849:
  0     0    0     0    0     0      0      0 --:--:--  0:00:02 --:--:--     0* SSL connection using TLS1.2 / ECDHE_RSA_AES_128_GCM_SHA256
850: * 	 server certificate verification OK
851: * 	 server certificate status verification SKIPPED
852: * 	 common name: cloud-images.ubuntu.com (matched)
853: * 	 server certificate expiration date OK
854: * 	 server certificate activation date OK
855: * 	 certificate public key: RSA
856: * 	 certificate version: #3
857: * 	 subject: C=GB,L=London,O=Canonical Group Ltd,CN=cloud-images.ubuntu.com
858: * 	 start date: Fri, 08 Jul 2016 00:00:00 GMT
859: * 	 expire date: Wed, 09 Aug 2017 12:00:00 GMT
860: * 	 issuer: C=US,O=DigiCert Inc,CN=DigiCert SHA2 Secure Server CA
861: * 	 compression: NULL
862: * ALPN, server did not agree to a protocol
863:
  0     0    0     0    0     0      0      0 --:--:--  0:00:03 --:--:--     0> GET /trusty/current/SHA256SUMS HTTP/1.1
864: > Host: cloud-images.ubuntu.com
865: > User-Agent: curl/7.47.0
866: > Accept: */*
867: > If-Modified-Since: Sat, 01 Oct 2016 10:48:53 GMT
868: >
869: < HTTP/1.1 304 Not Modified
870: < Date: Mon, 03 Oct 2016 15:09:53 GMT
871: < Server: Apache
872: < ETag: "14806e4-c54-53d9acea91a40"
873: <
874:
  0     0    0     0    0     0      0      0 --:--:--  0:00:03 --:--:--     0
875: * Connection #0 to host cloud-images.ubuntu.com left intact
876: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:89                              :   rcode=304
877: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:90                              :   '[' 304 == 200 -o https:/ == file:// ']'
878: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:108                             :   '[' 304 = 304 -o 304 = 213 ']'
879: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:109                             :   echo 'Server copy has not changed. Using locally cached https://cloud-images.ubuntu.com/trusty/current/SHA256SUMS'
880: Server copy has not changed. Using locally cached https://cloud-images.ubuntu.com/trusty/current/SHA256SUMS
881: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:110                             :   rm -f /home/xion/.cache/image-create/.download.fMMc1cM1
882: + /tmp/dib_build.1CFJZpLz/hooks/root.d/10-cache-ubuntu-tarball:get_ubuntu_tarball:30 :   /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url http://cloud-images.ubuntu.com/trusty/current/trusty-server-cloudimg-amd64-root.tar.gz /home/xion/.cache/image-create/trusty-server-cloudimg-amd64-root.tar.gz
883: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:21                              :   set -eu
884: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:22                              :   set -o pipefail
885: ++ /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:27                              :   basename /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url
886: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:27                              :   SCRIPT_NAME=cache-url
887: ++ /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:28                              :   dirname /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url
888: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:28                              :   SCRIPT_HOME=/tmp/dib_build.1CFJZpLz/hooks/bin
889: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:29                              :   FORCE_REVALIDATE=0
890: ++ /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:46                              :   getopt -o hf -n cache-url -- http://cloud-images.ubuntu.com/trusty/current/trusty-server-cloudimg-amd64-root.tar.gz /home/xion/.cache/image-create/trusty-server-cloudimg-amd64-root.tar.gz
891: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:46                              :   TEMP=' -- '\''http://cloud-images.ubuntu.com/trusty/current/trusty-server-cloudimg-amd64-root.tar.gz'\'' '\''/home/xion/.cache/image-create/trusty-server-cloudimg-amd64-root.tar.gz'\'''
892: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:47                              :   '[' 0 '!=' 0 ']'
893: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:50                              :   eval set -- ' -- '\''http://cloud-images.ubuntu.com/trusty/current/trusty-server-cloudimg-amd64-root.tar.gz'\'' '\''/home/xion/.cache/image-create/trusty-server-cloudimg-amd64-root.tar.gz'\'''
894: ++ /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:50                              :   set -- -- http://cloud-images.ubuntu.com/trusty/current/trusty-server-cloudimg-amd64-root.tar.gz /home/xion/.cache/image-create/trusty-server-cloudimg-amd64-root.tar.gz
895: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:52                              :   true
896: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:53                              :   case "$1" in
897: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:56                              :   shift
898: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:56                              :   break
899: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:61                              :   url=http://cloud-images.ubuntu.com/trusty/current/trusty-server-cloudimg-amd64-root.tar.gz
900: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:62                              :   dest=/home/xion/.cache/image-create/trusty-server-cloudimg-amd64-root.tar.gz
901: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:63                              :   time_cond=
902: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:64                              :   curl_opts=
903: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:66                              :   '[' -z http://cloud-images.ubuntu.com/trusty/current/trusty-server-cloudimg-amd64-root.tar.gz -o -z /home/xion/.cache/image-create/trusty-server-cloudimg-amd64-root.tar.gz ']'
904: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:70                              :   '[' -p /home/xion/.cache/image-create/trusty-server-cloudimg-amd64-root.tar.gz ']'
905: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:74                              :   type=normal
906: ++ /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:75                              :   dirname /home/xion/.cache/image-create/trusty-server-cloudimg-amd64-root.tar.gz
907: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:75                              :   mkdir -p /home/xion/.cache/image-create
908: +++ /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:76                              :   dirname /home/xion/.cache/image-create/trusty-server-cloudimg-amd64-root.tar.gz
909: ++ /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:76                              :   mktemp /home/xion/.cache/image-create/.download.XXXXXXXX
910: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:76                              :   tmp=/home/xion/.cache/image-create/.download.8LTzsfyU
911: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:79                              :   '[' 0 = 1 ']'
912: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:82                              :   '[' -f /home/xion/.cache/image-create/trusty-server-cloudimg-amd64-root.tar.gz -a -s /home/xion/.cache/image-create/trusty-server-cloudimg-amd64-root.tar.gz ']'
913: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:83                              :   time_cond='-z /home/xion/.cache/image-create/trusty-server-cloudimg-amd64-root.tar.gz'
914: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:84                              :   success='Server copy has changed. Using server version of http://cloud-images.ubuntu.com/trusty/current/trusty-server-cloudimg-amd64-root.tar.gz'
915: ++ /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:89                              :   eval curl -v -L -o /home/xion/.cache/image-create/.download.8LTzsfyU -w '%{http_code}' http://cloud-images.ubuntu.com/trusty/current/trusty-server-cloudimg-amd64-root.tar.gz -z /home/xion/.cache/image-create/trusty-server-cloudimg-amd64-root.tar.gz
916: +++ /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:89                              :   curl -v -L -o /home/xion/.cache/image-create/.download.8LTzsfyU -w '%{http_code}' http://cloud-images.ubuntu.com/trusty/current/trusty-server-cloudimg-amd64-root.tar.gz -z /home/xion/.cache/image-create/trusty-server-cloudimg-amd64-root.tar.gz
917:   % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
918:                                  Dload  Upload   Total   Spent    Left  Speed
919:
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*   Trying 91.189.88.141...
920: * Connected to cloud-images.ubuntu.com (91.189.88.141) port 80 (#0)
921:
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0> GET /trusty/current/trusty-server-cloudimg-amd64-root.tar.gz HTTP/1.1
922: > Host: cloud-images.ubuntu.com
923: > User-Agent: curl/7.47.0
924: > Accept: */*
925: > If-Modified-Since: Sat, 01 Oct 2016 11:12:57 GMT
926: >
927: < HTTP/1.1 304 Not Modified
928: < Date: Mon, 03 Oct 2016 15:09:54 GMT
929: < Server: Apache
930: < ETag: "14806ee-b51ded3-53d97d22bdfc0"
931: <
932:
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
933: * Connection #0 to host cloud-images.ubuntu.com left intact
934: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:89                              :   rcode=304
935: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:90                              :   '[' 304 == 200 -o http:// == file:// ']'
936: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:108                             :   '[' 304 = 304 -o 304 = 213 ']'
937: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:109                             :   echo 'Server copy has not changed. Using locally cached http://cloud-images.ubuntu.com/trusty/current/trusty-server-cloudimg-amd64-root.tar.gz'
938: Server copy has not changed. Using locally cached http://cloud-images.ubuntu.com/trusty/current/trusty-server-cloudimg-amd64-root.tar.gz
939: + /tmp/dib_build.1CFJZpLz/hooks/bin/cache-url:main:110                             :   rm -f /home/xion/.cache/image-create/.download.8LTzsfyU
940: + /tmp/dib_build.1CFJZpLz/hooks/root.d/10-cache-ubuntu-tarball:get_ubuntu_tarball:31 :   pushd /home/xion/.cache/image-create
941: ~/.cache/image-create ~/gitRepo/openstack
942: + /tmp/dib_build.1CFJZpLz/hooks/root.d/10-cache-ubuntu-tarball:get_ubuntu_tarball:32 :   grep trusty-server-cloudimg-amd64-root.tar.gz /home/xion/.cache/image-create/SHA256SUMS.ubuntu.trusty.amd64
943: + /tmp/dib_build.1CFJZpLz/hooks/root.d/10-cache-ubuntu-tarball:get_ubuntu_tarball:32 :   sha256sum --check -
944: trusty-server-cloudimg-amd64-root.tar.gz: OK
945: + /tmp/dib_build.1CFJZpLz/hooks/root.d/10-cache-ubuntu-tarball:get_ubuntu_tarball:46 :   popd
946: ~/gitRepo/openstack
947: + /tmp/dib_build.1CFJZpLz/hooks/root.d/10-cache-ubuntu-tarball:get_ubuntu_tarball:50 :   sudo tar -C /tmp/dib_build.1CFJZpLz/mnt --numeric-owner -xzf /home/xion/.cache/image-create/trusty-server-cloudimg-amd64-root.tar.gz
948: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:113                      :   target_tag=10-cache-ubuntu-tarball
949: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:114                      :   date +%s.%N
950: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:115                      :   output '10-cache-ubuntu-tarball completed'
951: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:43                     :   output_prefix
952: ++ /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   date
953: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   printf '%s %s ' dib-run-parts '2016年 10月 03日 星期一 23:10:02 CST'
954: dib-run-parts 2016年 10月 03日 星期一 23:10:02 CST + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:44                     :   echo 10-cache-ubuntu-tarball completed
955: 10-cache-ubuntu-tarball completed
956: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:108                      :   for target in '$targets'
957: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:109                      :   output 'Running /tmp/dib_build.1CFJZpLz/hooks/root.d/50-build-with-http-cache'
958: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:43                     :   output_prefix
959: ++ /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   date
960: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   printf '%s %s ' dib-run-parts '2016年 10月 03日 星期一 23:10:02 CST'
961: dib-run-parts 2016年 10月 03日 星期一 23:10:02 CST + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:44                     :   echo Running /tmp/dib_build.1CFJZpLz/hooks/root.d/50-build-with-http-cache
962: Running /tmp/dib_build.1CFJZpLz/hooks/root.d/50-build-with-http-cache
963: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:110                      :   target_tag=50-build-with-http-cache
964: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:111                      :   date +%s.%N
965: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:112                      :   /tmp/dib_build.1CFJZpLz/hooks/root.d/50-build-with-http-cache
966: + /tmp/dib_build.1CFJZpLz/hooks/root.d/50-build-with-http-cache:main:6             :   set -eu
967: + /tmp/dib_build.1CFJZpLz/hooks/root.d/50-build-with-http-cache:main:7             :   set -o pipefail
968: + /tmp/dib_build.1CFJZpLz/hooks/root.d/50-build-with-http-cache:main:9             :   '[' -n /tmp/dib_build.1CFJZpLz/mnt ']'
969: + /tmp/dib_build.1CFJZpLz/hooks/root.d/50-build-with-http-cache:main:12            :   '[' -n '' ']'
970: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:113                      :   target_tag=50-build-with-http-cache
971: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:114                      :   date +%s.%N
972: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:115                      :   output '50-build-with-http-cache completed'
973: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:43                     :   output_prefix
974: ++ /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   date
975: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   printf '%s %s ' dib-run-parts '2016年 10月 03日 星期一 23:10:02 CST'
976: dib-run-parts 2016年 10月 03日 星期一 23:10:02 CST + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:44                     :   echo 50-build-with-http-cache completed
977: 50-build-with-http-cache completed
978: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:108                      :   for target in '$targets'
979: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:109                      :   output 'Running /tmp/dib_build.1CFJZpLz/hooks/root.d/60-block-apt-translations'
980: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:43                     :   output_prefix
981: ++ /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   date
982: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   printf '%s %s ' dib-run-parts '2016年 10月 03日 星期一 23:10:02 CST'
983: dib-run-parts 2016年 10月 03日 星期一 23:10:02 CST + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:44                     :   echo Running /tmp/dib_build.1CFJZpLz/hooks/root.d/60-block-apt-translations
984: Running /tmp/dib_build.1CFJZpLz/hooks/root.d/60-block-apt-translations
985: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:110                      :   target_tag=60-block-apt-translations
986: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:111                      :   date +%s.%N
987: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:112                      :   /tmp/dib_build.1CFJZpLz/hooks/root.d/60-block-apt-translations
988: + /tmp/dib_build.1CFJZpLz/hooks/root.d/60-block-apt-translations:main:6            :   set -eu
989: + /tmp/dib_build.1CFJZpLz/hooks/root.d/60-block-apt-translations:main:7            :   set -o pipefail
990: + /tmp/dib_build.1CFJZpLz/hooks/root.d/60-block-apt-translations:main:9            :   '[' -n /tmp/dib_build.1CFJZpLz/mnt ']'
991: + /tmp/dib_build.1CFJZpLz/hooks/root.d/60-block-apt-translations:main:12           :   sudo dd of=/tmp/dib_build.1CFJZpLz/mnt/etc/apt/apt.conf.d/95no-translations
992: 0+1 records in
993: 0+1 records out
994: 27 bytes copied, 8.7065e-05 s, 310 kB/s
995: + /tmp/dib_build.1CFJZpLz/hooks/root.d/60-block-apt-translations:main:17           :   find /tmp/dib_build.1CFJZpLz/mnt/var/lib/apt/lists/ -path /tmp/dib_build.1CFJZpLz/mnt/var/lib/apt/lists/partial -prune -o -type f -name '*_i18n_Translation-*' -print -exec sudo rm -f '{}' +
996: /tmp/dib_build.1CFJZpLz/mnt/var/lib/apt/lists/archive.ubuntu.com_ubuntu_dists_trusty-backports_main_i18n_Translation-en
997: /tmp/dib_build.1CFJZpLz/mnt/var/lib/apt/lists/security.ubuntu.com_ubuntu_dists_trusty-security_universe_i18n_Translation-en
998: /tmp/dib_build.1CFJZpLz/mnt/var/lib/apt/lists/security.ubuntu.com_ubuntu_dists_trusty-security_multiverse_i18n_Translation-en
999: /tmp/dib_build.1CFJZpLz/mnt/var/lib/apt/lists/archive.ubuntu.com_ubuntu_dists_trusty-updates_multiverse_i18n_Translation-en
1000: /tmp/dib_build.1CFJZpLz/mnt/var/lib/apt/lists/archive.ubuntu.com_ubuntu_dists_trusty-backports_universe_i18n_Translation-en
1001: /tmp/dib_build.1CFJZpLz/mnt/var/lib/apt/lists/archive.ubuntu.com_ubuntu_dists_trusty-backports_multiverse_i18n_Translation-en
1002: /tmp/dib_build.1CFJZpLz/mnt/var/lib/apt/lists/archive.ubuntu.com_ubuntu_dists_trusty-updates_universe_i18n_Translation-en
1003: /tmp/dib_build.1CFJZpLz/mnt/var/lib/apt/lists/archive.ubuntu.com_ubuntu_dists_trusty-updates_main_i18n_Translation-en
1004: /tmp/dib_build.1CFJZpLz/mnt/var/lib/apt/lists/archive.ubuntu.com_ubuntu_dists_trusty_universe_i18n_Translation-en
1005: /tmp/dib_build.1CFJZpLz/mnt/var/lib/apt/lists/archive.ubuntu.com_ubuntu_dists_trusty_multiverse_i18n_Translation-en
1006: /tmp/dib_build.1CFJZpLz/mnt/var/lib/apt/lists/security.ubuntu.com_ubuntu_dists_trusty-security_restricted_i18n_Translation-en
1007: /tmp/dib_build.1CFJZpLz/mnt/var/lib/apt/lists/archive.ubuntu.com_ubuntu_dists_trusty-backports_restricted_i18n_Translation-en
1008: /tmp/dib_build.1CFJZpLz/mnt/var/lib/apt/lists/archive.ubuntu.com_ubuntu_dists_trusty_main_i18n_Translation-en
1009: /tmp/dib_build.1CFJZpLz/mnt/var/lib/apt/lists/archive.ubuntu.com_ubuntu_dists_trusty_restricted_i18n_Translation-en
1010: /tmp/dib_build.1CFJZpLz/mnt/var/lib/apt/lists/security.ubuntu.com_ubuntu_dists_trusty-security_main_i18n_Translation-en
1011: /tmp/dib_build.1CFJZpLz/mnt/var/lib/apt/lists/archive.ubuntu.com_ubuntu_dists_trusty-updates_restricted_i18n_Translation-en
1012: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:113                      :   target_tag=60-block-apt-translations
1013: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:114                      :   date +%s.%N
1014: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:115                      :   output '60-block-apt-translations completed'
1015: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:43                     :   output_prefix
1016: ++ /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   date
1017: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   printf '%s %s ' dib-run-parts '2016年 10月 03日 星期一 23:10:02 CST'
1018: dib-run-parts 2016年 10月 03日 星期一 23:10:02 CST + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:44                     :   echo 60-block-apt-translations completed
1019: 60-block-apt-translations completed
1020: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:108                      :   for target in '$targets'
1021: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:109                      :   output 'Running /tmp/dib_build.1CFJZpLz/hooks/root.d/90-base-dib-run-parts'
1022: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:43                     :   output_prefix
1023: ++ /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   date
1024: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   printf '%s %s ' dib-run-parts '2016年 10月 03日 星期一 23:10:02 CST'
1025: dib-run-parts 2016年 10月 03日 星期一 23:10:02 CST + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:44                     :   echo Running /tmp/dib_build.1CFJZpLz/hooks/root.d/90-base-dib-run-parts
1026: Running /tmp/dib_build.1CFJZpLz/hooks/root.d/90-base-dib-run-parts
1027: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:110                      :   target_tag=90-base-dib-run-parts
1028: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:111                      :   date +%s.%N
1029: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:112                      :   /tmp/dib_build.1CFJZpLz/hooks/root.d/90-base-dib-run-parts
1030: + /tmp/dib_build.1CFJZpLz/hooks/root.d/90-base-dib-run-parts:main:6                :   set -eu
1031: + /tmp/dib_build.1CFJZpLz/hooks/root.d/90-base-dib-run-parts:main:7                :   set -o pipefail
1032: ++ /tmp/dib_build.1CFJZpLz/hooks/root.d/90-base-dib-run-parts:main:11               :   which dib-run-parts
1033: + /tmp/dib_build.1CFJZpLz/hooks/root.d/90-base-dib-run-parts:main:11               :   DIB_RUN_PARTS=/home/xion/gitRepo/openstack/env/bin/dib-run-parts
1034: + /tmp/dib_build.1CFJZpLz/hooks/root.d/90-base-dib-run-parts:main:13               :   exec sudo install -m 0755 -o root -g root -D /home/xion/gitRepo/openstack/env/bin/dib-run-parts /tmp/dib_build.1CFJZpLz/mnt/usr/local/bin/dib-run-parts
1035: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:113                      :   target_tag=90-base-dib-run-parts
1036: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:114                      :   date +%s.%N
1037: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:115                      :   output '90-base-dib-run-parts completed'
1038: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:43                     :   output_prefix
1039: ++ /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   date
1040: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   printf '%s %s ' dib-run-parts '2016年 10月 03日 星期一 23:10:02 CST'
1041: dib-run-parts 2016年 10月 03日 星期一 23:10:02 CST + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:44                     :   echo 90-base-dib-run-parts completed
1042: 90-base-dib-run-parts completed
1043: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:108                      :   for target in '$targets'
1044: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:109                      :   output 'Running /tmp/dib_build.1CFJZpLz/hooks/root.d/99-block-daemons'
1045: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:43                     :   output_prefix
1046: ++ /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   date
1047: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   printf '%s %s ' dib-run-parts '2016年 10月 03日 星期一 23:10:02 CST'
1048: dib-run-parts 2016年 10月 03日 星期一 23:10:02 CST + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:44                     :   echo Running /tmp/dib_build.1CFJZpLz/hooks/root.d/99-block-daemons
1049: Running /tmp/dib_build.1CFJZpLz/hooks/root.d/99-block-daemons
1050: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:110                      :   target_tag=99-block-daemons
1051: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:111                      :   date +%s.%N
1052: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:112                      :   /tmp/dib_build.1CFJZpLz/hooks/root.d/99-block-daemons
1053: + /tmp/dib_build.1CFJZpLz/hooks/root.d/99-block-daemons:main:6                     :   set -eu
1054: + /tmp/dib_build.1CFJZpLz/hooks/root.d/99-block-daemons:main:7                     :   set -o pipefail
1055: + /tmp/dib_build.1CFJZpLz/hooks/root.d/99-block-daemons:main:9                     :   '[' -n /tmp/dib_build.1CFJZpLz/mnt ']'
1056: + /tmp/dib_build.1CFJZpLz/hooks/root.d/99-block-daemons:main:12                    :   sudo mv /tmp/dib_build.1CFJZpLz/mnt/sbin/start-stop-daemon /tmp/dib_build.1CFJZpLz/mnt/sbin/start-stop-daemon.REAL
1057: + /tmp/dib_build.1CFJZpLz/hooks/root.d/99-block-daemons:main:13                    :   sudo dd of=/tmp/dib_build.1CFJZpLz/mnt/sbin/start-stop-daemon
1058: 0+1 records in
1059: 0+1 records out
1060: 76 bytes copied, 0.000331997 s, 229 kB/s
1061: + /tmp/dib_build.1CFJZpLz/hooks/root.d/99-block-daemons:main:18                    :   sudo chmod 755 /tmp/dib_build.1CFJZpLz/mnt/sbin/start-stop-daemon
1062: + /tmp/dib_build.1CFJZpLz/hooks/root.d/99-block-daemons:main:20                    :   '[' -f /tmp/dib_build.1CFJZpLz/mnt/sbin/initctl ']'
1063: + /tmp/dib_build.1CFJZpLz/hooks/root.d/99-block-daemons:main:21                    :   sudo mv /tmp/dib_build.1CFJZpLz/mnt/sbin/initctl /tmp/dib_build.1CFJZpLz/mnt/sbin/initctl.REAL
1064: + /tmp/dib_build.1CFJZpLz/hooks/root.d/99-block-daemons:main:22                    :   sudo dd of=/tmp/dib_build.1CFJZpLz/mnt/sbin/initctl
1065: 0+1 records in
1066: 0+1 records out
1067: 90 bytes copied, 0.000101733 s, 885 kB/s
1068: + /tmp/dib_build.1CFJZpLz/hooks/root.d/99-block-daemons:main:27                    :   sudo chmod 755 /tmp/dib_build.1CFJZpLz/mnt/sbin/initctl
1069: + /tmp/dib_build.1CFJZpLz/hooks/root.d/99-block-daemons:main:30                    :   sudo dd of=/tmp/dib_build.1CFJZpLz/mnt/usr/sbin/policy-rc.d
1070: 0+1 records in
1071: 0+1 records out
1072: 143 bytes copied, 3.585e-05 s, 4.0 MB/s
1073: + /tmp/dib_build.1CFJZpLz/hooks/root.d/99-block-daemons:main:36                    :   sudo chmod 755 /tmp/dib_build.1CFJZpLz/mnt/usr/sbin/policy-rc.d
1074: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:113                      :   target_tag=99-block-daemons
1075: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:114                      :   date +%s.%N
1076: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:115                      :   output '99-block-daemons completed'
1077: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:43                     :   output_prefix
1078: ++ /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   date
1079: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   printf '%s %s ' dib-run-parts '2016年 10月 03日 星期一 23:10:02 CST'
1080: dib-run-parts 2016年 10月 03日 星期一 23:10:02 CST + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:44                     :   echo 99-block-daemons completed
1081: 99-block-daemons completed
1082: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:108                      :   for target in '$targets'
1083: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:109                      :   output 'Running /tmp/dib_build.1CFJZpLz/hooks/root.d/99-shared_apt_cache'
1084: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:43                     :   output_prefix
1085: ++ /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   date
1086: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   printf '%s %s ' dib-run-parts '2016年 10月 03日 星期一 23:10:02 CST'
1087: dib-run-parts 2016年 10月 03日 星期一 23:10:02 CST + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:44                     :   echo Running /tmp/dib_build.1CFJZpLz/hooks/root.d/99-shared_apt_cache
1088: Running /tmp/dib_build.1CFJZpLz/hooks/root.d/99-shared_apt_cache
1089: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:110                      :   target_tag=99-shared_apt_cache
1090: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:111                      :   date +%s.%N
1091: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:112                      :   /tmp/dib_build.1CFJZpLz/hooks/root.d/99-shared_apt_cache
1092: + /tmp/dib_build.1CFJZpLz/hooks/root.d/99-shared_apt_cache:main:6                  :   set -eu
1093: + /tmp/dib_build.1CFJZpLz/hooks/root.d/99-shared_apt_cache:main:7                  :   set -o pipefail
1094: + /tmp/dib_build.1CFJZpLz/hooks/root.d/99-shared_apt_cache:main:9                  :   DIB_APT_LOCAL_CACHE=1
1095: + /tmp/dib_build.1CFJZpLz/hooks/root.d/99-shared_apt_cache:main:11                 :   '[' 1 = 0 ']'
1096: + /tmp/dib_build.1CFJZpLz/hooks/root.d/99-shared_apt_cache:main:15                 :   apt_cache_dir=/home/xion/.cache/image-create/apt/ubuntu
1097: + /tmp/dib_build.1CFJZpLz/hooks/root.d/99-shared_apt_cache:main:16                 :   '[' '!' -d /home/xion/.cache/image-create/apt/ubuntu ']'
1098: + /tmp/dib_build.1CFJZpLz/hooks/root.d/99-shared_apt_cache:main:19                 :   sudo mount --bind /home/xion/.cache/image-create/apt/ubuntu /tmp/dib_build.1CFJZpLz/mnt/var/cache/apt/archives
1099: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:113                      :   target_tag=99-shared_apt_cache
1100: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:114                      :   date +%s.%N
1101: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:115                      :   output '99-shared_apt_cache completed'
1102: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:43                     :   output_prefix
1103: ++ /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   date
1104: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   printf '%s %s ' dib-run-parts '2016年 10月 03日 星期一 23:10:02 CST'
1105: dib-run-parts 2016年 10月 03日 星期一 23:10:02 CST + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:44                     :   echo 99-shared_apt_cache completed
1106: 99-shared_apt_cache completed
1107: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:108                      :   for target in '$targets'
1108: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:109                      :   output 'Running /tmp/dib_build.1CFJZpLz/hooks/root.d/99-trim-dpkg'
1109: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:43                     :   output_prefix
1110: ++ /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   date
1111: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   printf '%s %s ' dib-run-parts '2016年 10月 03日 星期一 23:10:02 CST'
1112: dib-run-parts 2016年 10月 03日 星期一 23:10:02 CST + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:44                     :   echo Running /tmp/dib_build.1CFJZpLz/hooks/root.d/99-trim-dpkg
1113: Running /tmp/dib_build.1CFJZpLz/hooks/root.d/99-trim-dpkg
1114: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:110                      :   target_tag=99-trim-dpkg
1115: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:111                      :   date +%s.%N
1116: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:112                      :   /tmp/dib_build.1CFJZpLz/hooks/root.d/99-trim-dpkg
1117: + /tmp/dib_build.1CFJZpLz/hooks/root.d/99-trim-dpkg:main:6                         :   set -eu
1118: + /tmp/dib_build.1CFJZpLz/hooks/root.d/99-trim-dpkg:main:7                         :   set -o pipefail
1119: + /tmp/dib_build.1CFJZpLz/hooks/root.d/99-trim-dpkg:main:9                         :   '[' -n /tmp/dib_build.1CFJZpLz/mnt ']'
1120: + /tmp/dib_build.1CFJZpLz/hooks/root.d/99-trim-dpkg:main:12                        :   sudo tee /tmp/dib_build.1CFJZpLz/mnt/etc/dpkg/dpkg.cfg.d/02apt-speedup
1121: + /tmp/dib_build.1CFJZpLz/hooks/root.d/99-trim-dpkg:main:12                        :   echo force-unsafe-io
1122: + /tmp/dib_build.1CFJZpLz/hooks/root.d/99-trim-dpkg:main:15                        :   sudo tee /tmp/dib_build.1CFJZpLz/mnt/etc/apt/apt.conf.d/no-languages
1123: + /tmp/dib_build.1CFJZpLz/hooks/root.d/99-trim-dpkg:main:15                        :   echo 'Acquire::Languages "none";'
1124: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:113                      :   target_tag=99-trim-dpkg
1125: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:114                      :   date +%s.%N
1126: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:115                      :   output '99-trim-dpkg completed'
1127: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:43                     :   output_prefix
1128: ++ /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   date
1129: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   printf '%s %s ' dib-run-parts '2016年 10月 03日 星期一 23:10:03 CST'
1130: dib-run-parts 2016年 10月 03日 星期一 23:10:03 CST + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:44                     :   echo 99-trim-dpkg completed
1131: 99-trim-dpkg completed
1132: dib-run-parts 2016年 10月 03日 星期一 23:10:03 CST ----------------------- PROFILING -----------------------
1133: dib-run-parts 2016年 10月 03日 星期一 23:10:03 CST
1134: dib-run-parts 2016年 10月 03日 星期一 23:10:03 CST Target: root.d
1135: dib-run-parts 2016年 10月 03日 星期一 23:10:03 CST
1136: dib-run-parts 2016年 10月 03日 星期一 23:10:03 CST Script                                     Seconds
1137: dib-run-parts 2016年 10月 03日 星期一 23:10:03 CST ---------------------------------------  ----------
1138: dib-run-parts 2016年 10月 03日 星期一 23:10:03 CST
1139: dib-run-parts Mon Oct  3 23:10:03 CST 2016 01-ccache                                     0.037
1140: dib-run-parts Mon Oct  3 23:10:03 CST 2016 10-cache-ubuntu-tarball                      12.488
1141: dib-run-parts Mon Oct  3 23:10:03 CST 2016 50-build-with-http-cache                      0.016
1142: dib-run-parts Mon Oct  3 23:10:03 CST 2016 60-block-apt-translations                     0.118
1143: dib-run-parts Mon Oct  3 23:10:03 CST 2016 90-base-dib-run-parts                         0.112
1144: dib-run-parts Mon Oct  3 23:10:03 CST 2016 99-block-daemons                              0.170
1145: dib-run-parts Mon Oct  3 23:10:03 CST 2016 99-shared_apt_cache                           0.045
1146: dib-run-parts Mon Oct  3 23:10:03 CST 2016 99-trim-dpkg                                  0.137
1147: dib-run-parts 2016年 10月 03日 星期一 23:10:03 CST
1148: dib-run-parts 2016年 10月 03日 星期一 23:10:03 CST --------------------- END PROFILING ---------------------
1149: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:run_d:160 :   check_break after-root bash
1150: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:check_break:98 :   egrep -e '(,|^)after-root(,|$)' -q
1151: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:check_break:98 :   echo ''
1152: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:create_base:210 :   ls /tmp/dib_build.1CFJZpLz/mnt
1153: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:create_base:210 :   grep -v '^lost+found\|tmp$'
1154: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:create_base:210 :   '[' -z 'bin
1155: boot
1156: dev
1157: etc
1158: home
1159: lib
1160: lib64
1161: media
1162: mnt
1163: opt
1164: proc
1165: root
1166: run
1167: sbin
1168: srv
1169: sys
1170: usr
1171: var' ']'
1172: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:create_base:219 :   '[' -L /tmp/dib_build.1CFJZpLz/mnt/etc/resolv.conf ']'
1173: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:create_base:220 :   sudo mv /tmp/dib_build.1CFJZpLz/mnt/etc/resolv.conf /tmp/dib_build.1CFJZpLz/mnt/etc/resolv.conf.ORIG
1174: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:create_base:224 :   sudo touch /tmp/dib_build.1CFJZpLz/mnt/etc/resolv.conf
1175: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:create_base:225 :   sudo chmod 777 /tmp/dib_build.1CFJZpLz/mnt/etc/resolv.conf
1176: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:create_base:227 :   '[' -e /etc/resolv.conf ']'
1177: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:create_base:228 :   cat /etc/resolv.conf
1178: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:create_base:232 :   mount_proc_dev_sys
1179: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:mount_proc_dev_sys:237 :   sudo mount -t proc none /tmp/dib_build.1CFJZpLz/mnt/proc
1180: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:mount_proc_dev_sys:238 :   sudo mount --bind /dev /tmp/dib_build.1CFJZpLz/mnt/dev
1181: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:mount_proc_dev_sys:239 :   sudo mount --bind /dev/pts /tmp/dib_build.1CFJZpLz/mnt/dev/pts
1182: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:mount_proc_dev_sys:240 :   sudo mount -t sysfs none /tmp/dib_build.1CFJZpLz/mnt/sys
1183: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:318                  :   mkdir -p /tmp/dib_build.1CFJZpLz/hooks/environment.d
1184: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:319                  :   echo 'export DIB_DEFAULT_INSTALLTYPE=${DIB_DEFAULT_INSTALLTYPE:-"source"}'
1185: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:320                  :   run_d extra-data
1186: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:run_d:148 :   check_element
1187: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:check_element:109 :   '[' -d /tmp/dib_build.1CFJZpLz/hooks ']'
1188: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:run_d:149 :   check_break before-extra-data bash
1189: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:check_break:98 :   echo ''
1190: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:check_break:98 :   egrep -e '(,|^)before-extra-data(,|$)' -q
1191: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:run_d:150 :   '[' -d /tmp/dib_build.1CFJZpLz/hooks/extra-data.d ']'
1192: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:run_d:151 :   '[' -n '' ']'
1193: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:run_d:157 :   dib-run-parts /tmp/dib_build.1CFJZpLz/hooks/extra-data.d
1194: + /tmp/dib_build.1CFJZpLz/hooks/dib-init-system:main:6                             :   set -eu
1195: + /tmp/dib_build.1CFJZpLz/hooks/dib-init-system:main:7                             :   set -o pipefail
1196: + /tmp/dib_build.1CFJZpLz/hooks/dib-init-system:main:9                             :   [[ -f /usr/bin/systemctl ]]
1197: + /tmp/dib_build.1CFJZpLz/hooks/dib-init-system:main:11                            :   [[ -f /sbin/initctl ]]
1198: + /tmp/dib_build.1CFJZpLz/hooks/dib-init-system:main:12                            :   echo upstart
1199: ++ /tmp/dib_build.1CFJZpLz/hooks/environment.d/14-manifests:source:21               :   set -eu
1200: ++ /tmp/dib_build.1CFJZpLz/hooks/environment.d/14-manifests:source:22               :   set -o pipefail
1201: ++ /tmp/dib_build.1CFJZpLz/hooks/environment.d/14-manifests:source:24               :   export DIB_MANIFEST_IMAGE_DIR=/etc/dib-manifests
1202: ++ /tmp/dib_build.1CFJZpLz/hooks/environment.d/14-manifests:source:24               :   DIB_MANIFEST_IMAGE_DIR=/etc/dib-manifests
1203: ++ /tmp/dib_build.1CFJZpLz/hooks/environment.d/14-manifests:source:25               :   export DIB_MANIFEST_SAVE_DIR=image.d/
1204: ++ /tmp/dib_build.1CFJZpLz/hooks/environment.d/14-manifests:source:25               :   DIB_MANIFEST_SAVE_DIR=image.d/
1205: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:source_environment:65         :   for env_file in '$env_files'
1206: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:source_environment:66         :   source /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/../environment.d/99-cloud-init-datasources.bash
1207: ++ /tmp/dib_build.1CFJZpLz/hooks/environment.d/99-cloud-init-datasources.bash:source:4 :   export DIB_CLOUD_INIT_DATASOURCES=Ec2
1208: ++ /tmp/dib_build.1CFJZpLz/hooks/environment.d/99-cloud-init-datasources.bash:source:4 :   DIB_CLOUD_INIT_DATASOURCES=Ec2
1209: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:108                      :   for target in '$targets'
1210: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:109                      :   output 'Running /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/01-copy-apt-keys'
1211: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:43                     :   output_prefix
1212: ++ /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   date
1213: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   printf '%s %s ' dib-run-parts '2016年 10月 03日 星期一 23:10:03 CST'
1214: dib-run-parts 2016年 10月 03日 星期一 23:10:03 CST + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:44                     :   echo Running /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/01-copy-apt-keys
1215: Running /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/01-copy-apt-keys
1216: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:110                      :   target_tag=01-copy-apt-keys
1217: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:111                      :   date +%s.%N
1218: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:112                      :   /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/01-copy-apt-keys
1219: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/01-copy-apt-keys:main:20              :   set -eu
1220: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/01-copy-apt-keys:main:21              :   set -o pipefail
1221: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/01-copy-apt-keys:main:23              :   DIB_ADD_APT_KEYS=
1222: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/01-copy-apt-keys:main:24              :   '[' -z '' ']'
1223: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/01-copy-apt-keys:main:25              :   echo 'DIB_ADD_APT_KEYS is not set - not importing keys'
1224: DIB_ADD_APT_KEYS is not set - not importing keys
1225: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/01-copy-apt-keys:main:26              :   exit 0
1226: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:113                      :   target_tag=01-copy-apt-keys
1227: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:114                      :   date +%s.%N
1228: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:115                      :   output '01-copy-apt-keys completed'
1229: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:43                     :   output_prefix
1230: ++ /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   date
1231: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   printf '%s %s ' dib-run-parts '2016年 10月 03日 星期一 23:10:03 CST'
1232: dib-run-parts 2016年 10月 03日 星期一 23:10:03 CST + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:44                     :   echo 01-copy-apt-keys completed
1233: 01-copy-apt-keys completed
1234: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:108                      :   for target in '$targets'
1235: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:109                      :   output 'Running /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir'
1236: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:43                     :   output_prefix
1237: ++ /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   date
1238: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   printf '%s %s ' dib-run-parts '2016年 10月 03日 星期一 23:10:03 CST'
1239: dib-run-parts 2016年 10月 03日 星期一 23:10:03 CST + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:44                     :   echo Running /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir
1240: Running /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir
1241: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:110                      :   target_tag=10-create-pkg-map-dir
1242: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:111                      :   date +%s.%N
1243: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:112                      :   /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir
1244: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:6          :   set -eu
1245: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:7          :   set -o pipefail
1246: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:9          :   sudo mkdir -p /tmp/dib_build.1CFJZpLz/mnt/usr/share/pkg-map/
1247: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:11         :   for ELEMENT in '$IMAGE_ELEMENT'
1248: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:12         :   for DIR in '${ELEMENTS_PATH//:/ }'
1249: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:13         :   '[' -f /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dib-python/pkg-map ']'
1250: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:11         :   for ELEMENT in '$IMAGE_ELEMENT'
1251: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:12         :   for DIR in '${ELEMENTS_PATH//:/ }'
1252: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:13         :   '[' -f /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/install-types/pkg-map ']'
1253: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:11         :   for ELEMENT in '$IMAGE_ELEMENT'
1254: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:12         :   for DIR in '${ELEMENTS_PATH//:/ }'
1255: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:13         :   '[' -f /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/install-bin/pkg-map ']'
1256: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:11         :   for ELEMENT in '$IMAGE_ELEMENT'
1257: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:12         :   for DIR in '${ELEMENTS_PATH//:/ }'
1258: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:13         :   '[' -f /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dib-run-parts/pkg-map ']'
1259: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:11         :   for ELEMENT in '$IMAGE_ELEMENT'
1260: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:12         :   for DIR in '${ELEMENTS_PATH//:/ }'
1261: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:13         :   '[' -f /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/vm/pkg-map ']'
1262: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:11         :   for ELEMENT in '$IMAGE_ELEMENT'
1263: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:12         :   for DIR in '${ELEMENTS_PATH//:/ }'
1264: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:13         :   '[' -f /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/manifests/pkg-map ']'
1265: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:11         :   for ELEMENT in '$IMAGE_ELEMENT'
1266: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:12         :   for DIR in '${ELEMENTS_PATH//:/ }'
1267: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:13         :   '[' -f /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dib-init-system/pkg-map ']'
1268: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:11         :   for ELEMENT in '$IMAGE_ELEMENT'
1269: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:12         :   for DIR in '${ELEMENTS_PATH//:/ }'
1270: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:13         :   '[' -f /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/cache-url/pkg-map ']'
1271: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:11         :   for ELEMENT in '$IMAGE_ELEMENT'
1272: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:12         :   for DIR in '${ELEMENTS_PATH//:/ }'
1273: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:13         :   '[' -f /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/pkg-map/pkg-map ']'
1274: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:11         :   for ELEMENT in '$IMAGE_ELEMENT'
1275: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:12         :   for DIR in '${ELEMENTS_PATH//:/ }'
1276: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:13         :   '[' -f /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/base/pkg-map ']'
1277: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:14         :   sudo cp /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/base/pkg-map /tmp/dib_build.1CFJZpLz/mnt/usr/share/pkg-map/base
1278: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:11         :   for ELEMENT in '$IMAGE_ELEMENT'
1279: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:12         :   for DIR in '${ELEMENTS_PATH//:/ }'
1280: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:13         :   '[' -f /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/ubuntu/pkg-map ']'
1281: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:11         :   for ELEMENT in '$IMAGE_ELEMENT'
1282: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:12         :   for DIR in '${ELEMENTS_PATH//:/ }'
1283: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:13         :   '[' -f /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/cloud-init-datasources/pkg-map ']'
1284: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:11         :   for ELEMENT in '$IMAGE_ELEMENT'
1285: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:12         :   for DIR in '${ELEMENTS_PATH//:/ }'
1286: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:13         :   '[' -f /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/bootloader/pkg-map ']'
1287: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:14         :   sudo cp /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/bootloader/pkg-map /tmp/dib_build.1CFJZpLz/mnt/usr/share/pkg-map/bootloader
1288: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:11         :   for ELEMENT in '$IMAGE_ELEMENT'
1289: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:12         :   for DIR in '${ELEMENTS_PATH//:/ }'
1290: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:13         :   '[' -f /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/package-installs/pkg-map ']'
1291: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:11         :   for ELEMENT in '$IMAGE_ELEMENT'
1292: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:12         :   for DIR in '${ELEMENTS_PATH//:/ }'
1293: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:13         :   '[' -f /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dpkg/pkg-map ']'
1294: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:11         :   for ELEMENT in '$IMAGE_ELEMENT'
1295: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:12         :   for DIR in '${ELEMENTS_PATH//:/ }'
1296: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/10-create-pkg-map-dir:main:13         :   '[' -f /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dkms/pkg-map ']'
1297: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:113                      :   target_tag=10-create-pkg-map-dir
1298: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:114                      :   date +%s.%N
1299: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:115                      :   output '10-create-pkg-map-dir completed'
1300: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:43                     :   output_prefix
1301: ++ /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   date
1302: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   printf '%s %s ' dib-run-parts '2016年 10月 03日 星期一 23:10:04 CST'
1303: dib-run-parts 2016年 10月 03日 星期一 23:10:04 CST + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:44                     :   echo 10-create-pkg-map-dir completed
1304: 10-create-pkg-map-dir completed
1305: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:108                      :   for target in '$targets'
1306: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:109                      :   output 'Running /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/20-manifest-dir'
1307: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:43                     :   output_prefix
1308: ++ /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   date
1309: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   printf '%s %s ' dib-run-parts '2016年 10月 03日 星期一 23:10:04 CST'
1310: dib-run-parts 2016年 10月 03日 星期一 23:10:04 CST + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:44                     :   echo Running /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/20-manifest-dir
1311: Running /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/20-manifest-dir
1312: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:110                      :   target_tag=20-manifest-dir
1313: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:111                      :   date +%s.%N
1314: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:112                      :   /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/20-manifest-dir
1315: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/20-manifest-dir:main:21               :   set -eu
1316: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/20-manifest-dir:main:22               :   set -o pipefail
1317: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/20-manifest-dir:main:24               :   sudo mkdir -p /tmp/dib_build.1CFJZpLz/mnt//etc/dib-manifests
1318: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:113                      :   target_tag=20-manifest-dir
1319: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:114                      :   date +%s.%N
1320: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:115                      :   output '20-manifest-dir completed'
1321: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:43                     :   output_prefix
1322: ++ /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   date
1323: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   printf '%s %s ' dib-run-parts '2016年 10月 03日 星期一 23:10:04 CST'
1324: dib-run-parts 2016年 10月 03日 星期一 23:10:04 CST + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:44                     :   echo 20-manifest-dir completed
1325: 20-manifest-dir completed
1326: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:108                      :   for target in '$targets'
1327: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:109                      :   output 'Running /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/50-store-build-settings'
1328: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:43                     :   output_prefix
1329: ++ /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   date
1330: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   printf '%s %s ' dib-run-parts '2016年 10月 03日 星期一 23:10:04 CST'
1331: dib-run-parts 2016年 10月 03日 星期一 23:10:04 CST + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:44                     :   echo Running /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/50-store-build-settings
1332: Running /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/50-store-build-settings
1333: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:110                      :   target_tag=50-store-build-settings
1334: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:111                      :   date +%s.%N
1335: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:112                      :   /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/50-store-build-settings
1336: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/50-store-build-settings:main:7        :   set -eu
1337: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/50-store-build-settings:main:8        :   set -o pipefail
1338: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/50-store-build-settings:main:10       :   '[' -n /tmp/dib_build.1CFJZpLz/hooks ']'
1339: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/50-store-build-settings:main:12       :   echo 'declare -x DIB_ARGS="-x vm ubuntu"'
1340: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/50-store-build-settings:main:13       :   echo '-x vm ubuntu'
1341: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:113                      :   target_tag=50-store-build-settings
1342: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:114                      :   date +%s.%N
1343: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:115                      :   output '50-store-build-settings completed'
1344: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:43                     :   output_prefix
1345: ++ /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   date
1346: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   printf '%s %s ' dib-run-parts '2016年 10月 03日 星期一 23:10:04 CST'
1347: dib-run-parts 2016年 10月 03日 星期一 23:10:04 CST + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:44                     :   echo 50-store-build-settings completed
1348: 50-store-build-settings completed
1349: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:108                      :   for target in '$targets'
1350: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:109                      :   output 'Running /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/99-enable-install-types'
1351: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:43                     :   output_prefix
1352: ++ /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   date
1353: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   printf '%s %s ' dib-run-parts '2016年 10月 03日 星期一 23:10:04 CST'
1354: dib-run-parts 2016年 10月 03日 星期一 23:10:04 CST + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:44                     :   echo Running /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/99-enable-install-types
1355: Running /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/99-enable-install-types
1356: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:110                      :   target_tag=99-enable-install-types
1357: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:111                      :   date +%s.%N
1358: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:112                      :   /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/99-enable-install-types
1359: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/99-enable-install-types:main:19       :   set -eu
1360: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/99-enable-install-types:main:20       :   set -o pipefail
1361: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/99-enable-install-types:main:22       :   declare -a SPECIFIED_ELEMS
1362: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/99-enable-install-types:main:26       :   SPECIFIED_ELEMS[0]=
1363: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/99-enable-install-types:main:29       :   PREFIX=DIB_INSTALLTYPE_
1364: ++ /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/99-enable-install-types:main:30       :   grep '^DIB_INSTALLTYPE_'
1365: ++ /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/99-enable-install-types:main:30       :   env
1366: ++ /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/99-enable-install-types:main:30       :   cut -d= -f1
1367: ++ /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/99-enable-install-types:main:30       :   echo ''
1368: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/99-enable-install-types:main:30       :   INSTALL_TYPE_VARS=
1369: ++ /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/99-enable-install-types:main:53       :   find /tmp/dib_build.1CFJZpLz/hooks/install.d -maxdepth 1 -name '*-source-install' -type d
1370: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/99-enable-install-types:main:53       :   default_install_type_dirs=
1371: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:113                      :   target_tag=99-enable-install-types
1372: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:114                      :   date +%s.%N
1373: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:115                      :   output '99-enable-install-types completed'
1374: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:43                     :   output_prefix
1375: ++ /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   date
1376: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   printf '%s %s ' dib-run-parts '2016年 10月 03日 星期一 23:10:04 CST'
1377: dib-run-parts 2016年 10月 03日 星期一 23:10:04 CST + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:44                     :   echo 99-enable-install-types completed
1378: 99-enable-install-types completed
1379: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:108                      :   for target in '$targets'
1380: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:109                      :   output 'Running /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/99-squash-package-install'
1381: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:43                     :   output_prefix
1382: ++ /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   date
1383: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   printf '%s %s ' dib-run-parts '2016年 10月 03日 星期一 23:10:04 CST'
1384: dib-run-parts 2016年 10月 03日 星期一 23:10:04 CST + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:44                     :   echo Running /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/99-squash-package-install
1385: Running /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/99-squash-package-install
1386: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:110                      :   target_tag=99-squash-package-install
1387: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:111                      :   date +%s.%N
1388: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:112                      :   /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/99-squash-package-install
1389: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/99-squash-package-install:main:5      :   set -eu
1390: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/99-squash-package-install:main:6      :   set -o pipefail
1391: ++ /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/99-squash-package-install:main:10     :   command -v python
1392: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/99-squash-package-install:main:10     :   python_path=/home/xion/gitRepo/openstack/env/bin/python
1393: ++ /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/99-squash-package-install:main:12     :   dirname /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/99-squash-package-install
1394: + /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/99-squash-package-install:main:12     :   sudo -E /home/xion/gitRepo/openstack/env/bin/python /tmp/dib_build.1CFJZpLz/hooks/extra-data.d/../bin/package-installs-squash '--elements=dib-python install-types install-bin dib-run-parts vm manifests dib-init-system cache-url pkg-map base ubuntu cloud-init-datasources bootloader package-installs dpkg dkms' --path=/home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements /tmp/dib_build.1CFJZpLz/mnt/tmp/package-installs.json
1395: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:113                      :   target_tag=99-squash-package-install
1396: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:114                      :   date +%s.%N
1397: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:115                      :   output '99-squash-package-install completed'
1398: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:43                     :   output_prefix
1399: ++ /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   date
1400: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   printf '%s %s ' dib-run-parts '2016年 10月 03日 星期一 23:10:04 CST'
1401: dib-run-parts 2016年 10月 03日 星期一 23:10:04 CST + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:44                     :   echo 99-squash-package-install completed
1402: 99-squash-package-install completed
1403: dib-run-parts 2016年 10月 03日 星期一 23:10:04 CST ----------------------- PROFILING -----------------------
1404: dib-run-parts 2016年 10月 03日 星期一 23:10:04 CST
1405: dib-run-parts 2016年 10月 03日 星期一 23:10:04 CST Target: extra-data.d
1406: dib-run-parts 2016年 10月 03日 星期一 23:10:04 CST
1407: dib-run-parts 2016年 10月 03日 星期一 23:10:04 CST Script                                     Seconds
1408: dib-run-parts 2016年 10月 03日 星期一 23:10:04 CST ---------------------------------------  ----------
1409: dib-run-parts 2016年 10月 03日 星期一 23:10:04 CST
1410: dib-run-parts Mon Oct  3 23:10:04 CST 2016 01-copy-apt-keys                              0.069
1411: dib-run-parts Mon Oct  3 23:10:04 CST 2016 10-create-pkg-map-dir                         0.276
1412: dib-run-parts Mon Oct  3 23:10:04 CST 2016 20-manifest-dir                               0.059
1413: dib-run-parts Mon Oct  3 23:10:04 CST 2016 50-store-build-settings                       0.044
1414: dib-run-parts Mon Oct  3 23:10:04 CST 2016 99-enable-install-types                       0.073
1415: dib-run-parts Mon Oct  3 23:10:04 CST 2016 99-squash-package-install                     0.264
1416: dib-run-parts 2016年 10月 03日 星期一 23:10:04 CST
1417: dib-run-parts 2016年 10月 03日 星期一 23:10:04 CST --------------------- END PROFILING ---------------------
1418: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:run_d:160 :   check_break after-extra-data bash
1419: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:check_break:98 :   egrep -e '(,|^)after-extra-data(,|$)' -q
1420: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:check_break:98 :   echo ''
1421: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:322                  :   run_d_in_target pre-install
1422: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:72 :   check_element
1423: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:check_element:109 :   '[' -d /tmp/dib_build.1CFJZpLz/hooks ']'
1424: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:75 :   '[' -d /tmp/dib_build.1CFJZpLz/hooks/pre-install.d ']'
1425: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:76 :   sudo mkdir /tmp/dib_build.1CFJZpLz/mnt/tmp/in_target.d
1426: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:77 :   sudo mount --bind /tmp/dib_build.1CFJZpLz/hooks /tmp/dib_build.1CFJZpLz/mnt/tmp/in_target.d
1427: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:78 :   sudo mount -o remount,ro,bind /tmp/dib_build.1CFJZpLz/hooks /tmp/dib_build.1CFJZpLz/mnt/tmp/in_target.d
1428: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:79 :   check_break before-pre-install run_in_target bash
1429: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:check_break:98 :   egrep -e '(,|^)before-pre-install(,|$)' -q
1430: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:check_break:98 :   echo ''
1431: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:80 :   '[' -z '' ']'
1432: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:80 :   in_target_arg=run_in_target
1433: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:81 :   trap 'check_break after-error run_in_target bash' ERR
1434: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:82 :   run_in_target dib-run-parts /tmp/in_target.d/pre-install.d
1435: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_in_target:57 :   cmd='dib-run-parts /tmp/in_target.d/pre-install.d'
1436: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_in_target:59 :   ORIG_HOME=/home/xion
1437: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_in_target:60 :   export HOME=/root
1438: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_in_target:60 :   HOME=/root
1439: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_in_target:66 :   sudo -E chroot /tmp/dib_build.1CFJZpLz/mnt env -u TMPDIR 'PATH=$PATH:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin' sh -c 'dib-run-parts /tmp/in_target.d/pre-install.d'
1440: + set -eu
1441: + set -o pipefail
1442: + [[ -f /usr/bin/systemctl ]]
1443: + [[ -f /sbin/initctl ]]
1444: + echo upstart
1445: ++ set -eu
1446: ++ set -o pipefail
1447: ++ export DIB_MANIFEST_IMAGE_DIR=/etc/dib-manifests
1448: ++ DIB_MANIFEST_IMAGE_DIR=/etc/dib-manifests
1449: ++ export DIB_MANIFEST_SAVE_DIR=image.d/
1450: ++ DIB_MANIFEST_SAVE_DIR=image.d/
1451: + for env_file in '$env_files'
1452: + source /tmp/in_target.d/pre-install.d/../environment.d/99-cloud-init-datasources.bash
1453: ++ export DIB_CLOUD_INIT_DATASOURCES=Ec2
1454: ++ DIB_CLOUD_INIT_DATASOURCES=Ec2
1455: + for target in '$targets'
1456: + output 'Running /tmp/in_target.d/pre-install.d/00-disable-apt-recommends'
1457: + output_prefix
1458: ++ date
1459: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:10:04 UTC 2016'
1460: dib-run-parts Mon Oct  3 15:10:04 UTC 2016 + echo Running /tmp/in_target.d/pre-install.d/00-disable-apt-recommends
1461: Running /tmp/in_target.d/pre-install.d/00-disable-apt-recommends
1462: + target_tag=00-disable-apt-recommends
1463: + date +%s.%N
1464: + /tmp/in_target.d/pre-install.d/00-disable-apt-recommends
1465: + set -eu
1466: + set -o pipefail
1467: + dd of=/etc/apt/apt.conf.d/95disable-recommends
1468: 0+1 records in
1469: 0+1 records out
1470: 56 bytes (56 B) copied, 6.3666e-05 s, 880 kB/s
1471: + target_tag=00-disable-apt-recommends
1472: + date +%s.%N
1473: + output '00-disable-apt-recommends completed'
1474: + output_prefix
1475: ++ date
1476: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:10:04 UTC 2016'
1477: dib-run-parts Mon Oct  3 15:10:04 UTC 2016 + echo 00-disable-apt-recommends completed
1478: 00-disable-apt-recommends completed
1479: + for target in '$targets'
1480: + output 'Running /tmp/in_target.d/pre-install.d/00-remove-apt-xapian-index'
1481: + output_prefix
1482: ++ date
1483: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:10:04 UTC 2016'
1484: dib-run-parts Mon Oct  3 15:10:04 UTC 2016 + echo Running /tmp/in_target.d/pre-install.d/00-remove-apt-xapian-index
1485: Running /tmp/in_target.d/pre-install.d/00-remove-apt-xapian-index
1486: + target_tag=00-remove-apt-xapian-index
1487: + date +%s.%N
1488: + /tmp/in_target.d/pre-install.d/00-remove-apt-xapian-index
1489: + set -eu
1490: + set -o pipefail
1491: + apt-get --yes remove apt-xapian-index
1492: Reading package lists...
1493: Building dependency tree...
1494: Reading state information...
1495: The following packages were automatically installed and are no longer required:
1496:   libfreetype6 os-prober
1497: Use 'apt-get autoremove' to remove them.
1498: The following packages will be REMOVED:
1499:   apt-xapian-index
1500: perl: warning: Setting locale failed.
1501: perl: warning: Please check that your locale settings:
1502: 	LANGUAGE = "en_US",
1503: 	LC_ALL = (unset),
1504: 	LC_TIME = "zh_CN.UTF-8",
1505: 	LC_MONETARY = "zh_CN.UTF-8",
1506: 	LC_CTYPE = "en_US.UTF-8",
1507: 	LC_ADDRESS = "zh_CN.UTF-8",
1508: 	LC_TELEPHONE = "zh_CN.UTF-8",
1509: 	LC_NAME = "zh_CN.UTF-8",
1510: 	LC_MEASUREMENT = "zh_CN.UTF-8",
1511: 	LC_IDENTIFICATION = "zh_CN.UTF-8",
1512: 	LC_NUMERIC = "zh_CN.UTF-8",
1513: 	LC_PAPER = "zh_CN.UTF-8",
1514: 	LANG = "C"
1515:     are supported and installed on your system.
1516: perl: warning: Falling back to the standard locale ("C").
1517: locale: Cannot set LC_ALL to default locale: No such file or directory
1518: 0 upgraded, 0 newly installed, 1 to remove and 0 not upgraded.
1519: After this operation, 336 kB disk space will be freed.
1520: (Reading database ... 25010 files and directories currently installed.)
1521: Removing apt-xapian-index (0.45ubuntu4) ...
1522: Removing index /var/lib/apt-xapian-index...
1523: Processing triggers for man-db (2.6.7.1-1ubuntu1) ...
1524: + target_tag=00-remove-apt-xapian-index
1525: + date +%s.%N
1526: + output '00-remove-apt-xapian-index completed'
1527: + output_prefix
1528: ++ date
1529: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:10:06 UTC 2016'
1530: dib-run-parts Mon Oct  3 15:10:06 UTC 2016 + echo 00-remove-apt-xapian-index completed
1531: 00-remove-apt-xapian-index completed
1532: + for target in '$targets'
1533: + output 'Running /tmp/in_target.d/pre-install.d/00-remove-grub'
1534: + output_prefix
1535: ++ date
1536: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:10:06 UTC 2016'
1537: dib-run-parts Mon Oct  3 15:10:06 UTC 2016 + echo Running /tmp/in_target.d/pre-install.d/00-remove-grub
1538: Running /tmp/in_target.d/pre-install.d/00-remove-grub
1539: + target_tag=00-remove-grub
1540: + date +%s.%N
1541: + /tmp/in_target.d/pre-install.d/00-remove-grub
1542: + set -eu
1543: + set -o pipefail
1544: + dpkg-query -W grub-pc
1545: dpkg-query: no packages found matching grub-pc
1546: + dpkg-query -W grub2-common
1547: dpkg-query: no packages found matching grub2-common
1548: + target_tag=00-remove-grub
1549: + date +%s.%N
1550: + output '00-remove-grub completed'
1551: + output_prefix
1552: ++ date
1553: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:10:06 UTC 2016'
1554: dib-run-parts Mon Oct  3 15:10:06 UTC 2016 + echo 00-remove-grub completed
1555: 00-remove-grub completed
1556: + for target in '$targets'
1557: + output 'Running /tmp/in_target.d/pre-install.d/01-dib-python'
1558: + output_prefix
1559: ++ date
1560: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:10:06 UTC 2016'
1561: dib-run-parts Mon Oct  3 15:10:06 UTC 2016 + echo Running /tmp/in_target.d/pre-install.d/01-dib-python
1562: Running /tmp/in_target.d/pre-install.d/01-dib-python
1563: + target_tag=01-dib-python
1564: + date +%s.%N
1565: + /tmp/in_target.d/pre-install.d/01-dib-python
1566: + set -eu
1567: + set -o pipefail
1568: ++ command -v python2
1569: + python_path=/usr/bin/python2
1570: + '[' -z /usr/bin/python2 ']'
1571: + ln -sf /usr/bin/python2 /usr/local/bin/dib-python
1572: + target_tag=01-dib-python
1573: + date +%s.%N
1574: + output '01-dib-python completed'
1575: + output_prefix
1576: ++ date
1577: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:10:06 UTC 2016'
1578: dib-run-parts Mon Oct  3 15:10:06 UTC 2016 + echo 01-dib-python completed
1579: 01-dib-python completed
1580: + for target in '$targets'
1581: + output 'Running /tmp/in_target.d/pre-install.d/01-install-bin'
1582: + output_prefix
1583: ++ date
1584: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:10:06 UTC 2016'
1585: dib-run-parts Mon Oct  3 15:10:06 UTC 2016 + echo Running /tmp/in_target.d/pre-install.d/01-install-bin
1586: Running /tmp/in_target.d/pre-install.d/01-install-bin
1587: + target_tag=01-install-bin
1588: + date +%s.%N
1589: + /tmp/in_target.d/pre-install.d/01-install-bin
1590: + set -eu
1591: + set -o pipefail
1592: ++ dirname /tmp/in_target.d/pre-install.d/01-install-bin
1593: + install -m 0755 -o root -g root /tmp/in_target.d/pre-install.d/../bin/cache-url /tmp/in_target.d/pre-install.d/../bin/install-packages /tmp/in_target.d/pre-install.d/../bin/map-services /tmp/in_target.d/pre-install.d/../bin/package-installs /tmp/in_target.d/pre-install.d/../bin/package-installs-squash /tmp/in_target.d/pre-install.d/../bin/package-installs-v2 /tmp/in_target.d/pre-install.d/../bin/package-uninstalls /tmp/in_target.d/pre-install.d/../bin/pkg-map /usr/local/bin
1594: + target_tag=01-install-bin
1595: + date +%s.%N
1596: + output '01-install-bin completed'
1597: + output_prefix
1598: ++ date
1599: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:10:06 UTC 2016'
1600: dib-run-parts Mon Oct  3 15:10:06 UTC 2016 + echo 01-install-bin completed
1601: 01-install-bin completed
1602: + for target in '$targets'
1603: + output 'Running /tmp/in_target.d/pre-install.d/01-set-ubuntu-mirror'
1604: + output_prefix
1605: ++ date
1606: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:10:06 UTC 2016'
1607: dib-run-parts Mon Oct  3 15:10:06 UTC 2016 + echo Running /tmp/in_target.d/pre-install.d/01-set-ubuntu-mirror
1608: Running /tmp/in_target.d/pre-install.d/01-set-ubuntu-mirror
1609: + target_tag=01-set-ubuntu-mirror
1610: + date +%s.%N
1611: + /tmp/in_target.d/pre-install.d/01-set-ubuntu-mirror
1612: + set -eu
1613: + set -o pipefail
1614: + DIB_DISTRIBUTION_MIRROR=
1615: + '[' -n '' ']'
1616: + exit 0
1617: + target_tag=01-set-ubuntu-mirror
1618: + date +%s.%N
1619: + output '01-set-ubuntu-mirror completed'
1620: + output_prefix
1621: ++ date
1622: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:10:06 UTC 2016'
1623: dib-run-parts Mon Oct  3 15:10:06 UTC 2016 + echo 01-set-ubuntu-mirror completed
1624: 01-set-ubuntu-mirror completed
1625: + for target in '$targets'
1626: + output 'Running /tmp/in_target.d/pre-install.d/02-add-apt-keys'
1627: + output_prefix
1628: ++ date
1629: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:10:06 UTC 2016'
1630: dib-run-parts Mon Oct  3 15:10:06 UTC 2016 + echo Running /tmp/in_target.d/pre-install.d/02-add-apt-keys
1631: Running /tmp/in_target.d/pre-install.d/02-add-apt-keys
1632: + target_tag=02-add-apt-keys
1633: + date +%s.%N
1634: + /tmp/in_target.d/pre-install.d/02-add-apt-keys
1635: + set -eu
1636: + set -o pipefail
1637: + KEY_DIRECTORY=/tmp/apt_keys
1638: + '[' '!' -d /tmp/apt_keys ']'
1639: + exit 0
1640: + target_tag=02-add-apt-keys
1641: + date +%s.%N
1642: + output '02-add-apt-keys completed'
1643: + output_prefix
1644: ++ date
1645: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:10:06 UTC 2016'
1646: dib-run-parts Mon Oct  3 15:10:06 UTC 2016 + echo 02-add-apt-keys completed
1647: 02-add-apt-keys completed
1648: + for target in '$targets'
1649: + output 'Running /tmp/in_target.d/pre-install.d/02-package-installs'
1650: + output_prefix
1651: ++ date
1652: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:10:06 UTC 2016'
1653: dib-run-parts Mon Oct  3 15:10:06 UTC 2016 + echo Running /tmp/in_target.d/pre-install.d/02-package-installs
1654: Running /tmp/in_target.d/pre-install.d/02-package-installs
1655: + target_tag=02-package-installs
1656: + date +%s.%N
1657: + /tmp/in_target.d/pre-install.d/02-package-installs
1658: + set -eu
1659: + set -o pipefail
1660: ++ dirname /tmp/in_target.d/pre-install.d/02-package-installs
1661: + package-installs -d /tmp/in_target.d/pre-install.d
1662: + set -eu
1663: + set -o pipefail
1664: ++ basename /usr/local/bin/package-installs
1665: + SCRIPTNAME=package-installs
1666: ++ getopt -o hd: -n package-installs -- -d /tmp/in_target.d/pre-install.d
1667: + TEMP=' -d '\''/tmp/in_target.d/pre-install.d'\'' --'
1668: + '[' 0 '!=' 0 ']'
1669: + eval set -- ' -d '\''/tmp/in_target.d/pre-install.d'\'' --'
1670: ++ set -- -d /tmp/in_target.d/pre-install.d --
1671: + WORKDIR=
1672: + true
1673: + case "$1" in
1674: + WORKDIR=/tmp/in_target.d/pre-install.d
1675: + shift 2
1676: + true
1677: + case "$1" in
1678: + shift
1679: + break
1680: + '[' -z /tmp/in_target.d/pre-install.d ']'
1681: + PACKAGES=
1682: ++ find /tmp/in_target.d/pre-install.d -maxdepth 1 -name 'package-installs-*'
1683: + '[' -n '' ']'
1684: + package-installs-v2 --phase pre-install.d /tmp/package-installs.json
1685: Nothing to install
1686: + target_tag=02-package-installs
1687: + date +%s.%N
1688: + output '02-package-installs completed'
1689: + output_prefix
1690: ++ date
1691: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:10:06 UTC 2016'
1692: dib-run-parts Mon Oct  3 15:10:06 UTC 2016 + echo 02-package-installs completed
1693: 02-package-installs completed
1694: + for target in '$targets'
1695: + output 'Running /tmp/in_target.d/pre-install.d/03-baseline-tools'
1696: + output_prefix
1697: ++ date
1698: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:10:06 UTC 2016'
1699: dib-run-parts Mon Oct  3 15:10:06 UTC 2016 + echo Running /tmp/in_target.d/pre-install.d/03-baseline-tools
1700: Running /tmp/in_target.d/pre-install.d/03-baseline-tools
1701: + target_tag=03-baseline-tools
1702: + date +%s.%N
1703: + /tmp/in_target.d/pre-install.d/03-baseline-tools
1704: + set -eu
1705: + set -o pipefail
1706: + case $DISTRO_NAME in
1707: + apt-get -y update
1708: Ign http://archive.ubuntu.com trusty InRelease
1709: Get:1 http://archive.ubuntu.com trusty-updates InRelease [65.9 kB]
1710: Hit http://archive.ubuntu.com trusty-backports InRelease
1711: Hit http://archive.ubuntu.com trusty Release.gpg
1712: Get:2 http://archive.ubuntu.com trusty-updates/main amd64 Packages [901 kB]
1713: Get:3 http://security.ubuntu.com trusty-security InRelease [65.9 kB]
1714: Get:4 http://archive.ubuntu.com trusty-updates/restricted amd64 Packages [15.9 kB]
1715: Get:5 http://archive.ubuntu.com trusty-updates/universe amd64 Packages [376 kB]
1716: Get:6 http://archive.ubuntu.com trusty-updates/multiverse amd64 Packages [15.0 kB]
1717: Hit http://archive.ubuntu.com trusty-backports/main amd64 Packages
1718: Hit http://archive.ubuntu.com trusty-backports/restricted amd64 Packages
1719: Hit http://archive.ubuntu.com trusty-backports/universe amd64 Packages
1720: Hit http://archive.ubuntu.com trusty-backports/multiverse amd64 Packages
1721: Hit http://archive.ubuntu.com trusty Release
1722: Hit http://archive.ubuntu.com trusty/main amd64 Packages
1723: Hit http://archive.ubuntu.com trusty/restricted amd64 Packages
1724: Hit http://archive.ubuntu.com trusty/universe amd64 Packages
1725: Hit http://archive.ubuntu.com trusty/multiverse amd64 Packages
1726: Get:7 http://security.ubuntu.com trusty-security InRelease [65.9 kB]
1727: Get:8 http://security.ubuntu.com trusty-security/main amd64 Packages [531 kB]
1728: Get:9 http://security.ubuntu.com trusty-security/restricted amd64 Packages [13.0 kB]
1729: Get:10 http://security.ubuntu.com trusty-security/universe amd64 Packages [138 kB]
1730: Get:11 http://security.ubuntu.com trusty-security/multiverse amd64 Packages [5198 B]
1731: Fetched 2095 kB in 2min 47s (12.5 kB/s)
1732: Reading package lists...
1733: + '[' trusty = precise ']'
1734: + install-packages software-properties-common
1735: + set -eu
1736: + set -o pipefail
1737: + ACTION=install
1738: + MAP_ELEMENT=
1739: ++ basename /usr/local/bin/install-packages
1740: + SCRIPTNAME=install-packages
1741: ++ getopt -o hudem: -n install-packages -- software-properties-common
1742: + TEMP=' -- '\''software-properties-common'\'''
1743: + '[' 0 '!=' 0 ']'
1744: + eval set -- ' -- '\''software-properties-common'\'''
1745: ++ set -- -- software-properties-common
1746: + true
1747: + case "$1" in
1748: + shift
1749: + break
1750: + PKGS=software-properties-common
1751: + '[' -n '' ']'
1752: + '[' -z software-properties-common ']'
1753: + install_deb_packages install software-properties-common
1754: + DEBIAN_FRONTEND=noninteractive
1755: + http_proxy=
1756: + https_proxy=
1757: + no_proxy=
1758: + apt-get --option Dpkg::Options::=--force-confold --option Dpkg::Options::=--force-confdef --assume-yes install software-properties-common
1759: Reading package lists...
1760: Building dependency tree...
1761: Reading state information...
1762: software-properties-common is already the newest version.
1763: The following packages were automatically installed and are no longer required:
1764:   libfreetype6 os-prober
1765: Use 'apt-get autoremove' to remove them.
1766: 0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
1767: + target_tag=03-baseline-tools
1768: + date +%s.%N
1769: + output '03-baseline-tools completed'
1770: + output_prefix
1771: ++ date
1772: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:12:55 UTC 2016'
1773: dib-run-parts Mon Oct  3 15:12:55 UTC 2016 + echo 03-baseline-tools completed
1774: 03-baseline-tools completed
1775: + for target in '$targets'
1776: + output 'Running /tmp/in_target.d/pre-install.d/04-dib-init-system'
1777: + output_prefix
1778: ++ date
1779: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:12:55 UTC 2016'
1780: dib-run-parts Mon Oct  3 15:12:55 UTC 2016 + echo Running /tmp/in_target.d/pre-install.d/04-dib-init-system
1781: Running /tmp/in_target.d/pre-install.d/04-dib-init-system
1782: + target_tag=04-dib-init-system
1783: + date +%s.%N
1784: + /tmp/in_target.d/pre-install.d/04-dib-init-system
1785: + set -eu
1786: + set -o pipefail
1787: ++ dirname /tmp/in_target.d/pre-install.d/04-dib-init-system
1788: + install -m 0755 -o root -g root /tmp/in_target.d/pre-install.d/../dib-init-system /usr/bin/
1789: + target_tag=04-dib-init-system
1790: + date +%s.%N
1791: + output '04-dib-init-system completed'
1792: + output_prefix
1793: ++ date
1794: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:12:55 UTC 2016'
1795: dib-run-parts Mon Oct  3 15:12:55 UTC 2016 + echo 04-dib-init-system completed
1796: 04-dib-init-system completed
1797: + for target in '$targets'
1798: + output 'Running /tmp/in_target.d/pre-install.d/99-apt-get-update'
1799: + output_prefix
1800: ++ date
1801: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:12:55 UTC 2016'
1802: dib-run-parts Mon Oct  3 15:12:55 UTC 2016 + echo Running /tmp/in_target.d/pre-install.d/99-apt-get-update
1803: Running /tmp/in_target.d/pre-install.d/99-apt-get-update
1804: + target_tag=99-apt-get-update
1805: + date +%s.%N
1806: + /tmp/in_target.d/pre-install.d/99-apt-get-update
1807: + set -eu
1808: + set -o pipefail
1809: + apt-get -y update
1810: Ign http://archive.ubuntu.com trusty InRelease
1811: Hit http://archive.ubuntu.com trusty-updates InRelease
1812: Hit http://security.ubuntu.com trusty-security InRelease
1813: Hit http://archive.ubuntu.com trusty-backports InRelease
1814: Hit http://security.ubuntu.com trusty-security/main amd64 Packages
1815: Hit http://archive.ubuntu.com trusty Release.gpg
1816: Hit http://archive.ubuntu.com trusty-updates/main amd64 Packages
1817: Hit http://security.ubuntu.com trusty-security/restricted amd64 Packages
1818: Hit http://archive.ubuntu.com trusty-updates/restricted amd64 Packages
1819: Hit http://security.ubuntu.com trusty-security/universe amd64 Packages
1820: Hit http://archive.ubuntu.com trusty-updates/universe amd64 Packages
1821: Hit http://archive.ubuntu.com trusty-updates/multiverse amd64 Packages
1822: Hit http://security.ubuntu.com trusty-security/multiverse amd64 Packages
1823: Hit http://archive.ubuntu.com trusty-backports/main amd64 Packages
1824: Hit http://archive.ubuntu.com trusty-backports/restricted amd64 Packages
1825: Hit http://archive.ubuntu.com trusty-backports/universe amd64 Packages
1826: Hit http://archive.ubuntu.com trusty-backports/multiverse amd64 Packages
1827: Hit http://archive.ubuntu.com trusty Release
1828: Hit http://archive.ubuntu.com trusty/main amd64 Packages
1829: Hit http://archive.ubuntu.com trusty/restricted amd64 Packages
1830: Hit http://archive.ubuntu.com trusty/universe amd64 Packages
1831: Hit http://archive.ubuntu.com trusty/multiverse amd64 Packages
1832: Reading package lists...
1833: + target_tag=99-apt-get-update
1834: + date +%s.%N
1835: + output '99-apt-get-update completed'
1836: + output_prefix
1837: ++ date
1838: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:13:01 UTC 2016'
1839: dib-run-parts Mon Oct  3 15:13:01 UTC 2016 + echo 99-apt-get-update completed
1840: 99-apt-get-update completed
1841: + for target in '$targets'
1842: + output 'Running /tmp/in_target.d/pre-install.d/99-package-uninstalls'
1843: + output_prefix
1844: ++ date
1845: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:13:01 UTC 2016'
1846: dib-run-parts Mon Oct  3 15:13:01 UTC 2016 + echo Running /tmp/in_target.d/pre-install.d/99-package-uninstalls
1847: Running /tmp/in_target.d/pre-install.d/99-package-uninstalls
1848: + target_tag=99-package-uninstalls
1849: + date +%s.%N
1850: + /tmp/in_target.d/pre-install.d/99-package-uninstalls
1851: + set -eu
1852: + set -o pipefail
1853: ++ dirname /tmp/in_target.d/pre-install.d/99-package-uninstalls
1854: + package-uninstalls -d /tmp/in_target.d/pre-install.d
1855: + set -eu
1856: + set -o pipefail
1857: ++ basename /usr/local/bin/package-uninstalls
1858: + SCRIPTNAME=package-uninstalls
1859: ++ getopt -o hd: -n package-uninstalls -- -d /tmp/in_target.d/pre-install.d
1860: + TEMP=' -d '\''/tmp/in_target.d/pre-install.d'\'' --'
1861: + '[' 0 '!=' 0 ']'
1862: + eval set -- ' -d '\''/tmp/in_target.d/pre-install.d'\'' --'
1863: ++ set -- -d /tmp/in_target.d/pre-install.d --
1864: + WORKDIR=
1865: + true
1866: + case "$1" in
1867: + WORKDIR=/tmp/in_target.d/pre-install.d
1868: + shift 2
1869: + true
1870: + case "$1" in
1871: + shift
1872: + break
1873: + '[' -z /tmp/in_target.d/pre-install.d ']'
1874: + PACKAGES=
1875: ++ find /tmp/in_target.d/pre-install.d -maxdepth 1 -name 'package-installs-*'
1876: + install-packages -e
1877: + set -eu
1878: + set -o pipefail
1879: + ACTION=install
1880: + MAP_ELEMENT=
1881: ++ basename /usr/local/bin/install-packages
1882: + SCRIPTNAME=install-packages
1883: ++ getopt -o hudem: -n install-packages -- -e
1884: + TEMP=' -e --'
1885: + '[' 0 '!=' 0 ']'
1886: + eval set -- ' -e --'
1887: ++ set -- -e --
1888: + true
1889: + case "$1" in
1890: + ACTION=remove
1891: + shift
1892: + true
1893: + case "$1" in
1894: + shift
1895: + break
1896: + PKGS=
1897: + '[' -n '' ']'
1898: + '[' -z '' ']'
1899: + echo 'Not running install-packages remove with empty packages list'
1900: Not running install-packages remove with empty packages list
1901: + package-installs-v2 --phase pre-install.d --uninstall /tmp/package-installs.json
1902: Nothing to uninstall
1903: + target_tag=99-package-uninstalls
1904: + date +%s.%N
1905: + output '99-package-uninstalls completed'
1906: + output_prefix
1907: ++ date
1908: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:13:01 UTC 2016'
1909: dib-run-parts Mon Oct  3 15:13:01 UTC 2016 + echo 99-package-uninstalls completed
1910: 99-package-uninstalls completed
1911: dib-run-parts Mon Oct  3 15:13:01 UTC 2016 ----------------------- PROFILING -----------------------
1912: dib-run-parts Mon Oct  3 15:13:01 UTC 2016
1913: dib-run-parts Mon Oct  3 15:13:01 UTC 2016 Target: pre-install.d
1914: dib-run-parts Mon Oct  3 15:13:01 UTC 2016
1915: dib-run-parts Mon Oct  3 15:13:01 UTC 2016 Script                                     Seconds
1916: dib-run-parts Mon Oct  3 15:13:01 UTC 2016 ---------------------------------------  ----------
1917: dib-run-parts Mon Oct  3 15:13:01 UTC 2016
1918: dib-run-parts Mon Oct  3 15:13:01 UTC 2016 00-disable-apt-recommends                     0.006
1919: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
1920: dib-run-parts Mon Oct  3 15:13:01 UTC 2016 00-remove-apt-xapian-index                    1.909
1921: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
1922: dib-run-parts Mon Oct  3 15:13:01 UTC 2016 00-remove-grub                                0.019
1923: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
1924: dib-run-parts Mon Oct  3 15:13:01 UTC 2016 01-dib-python                                 0.004
1925: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
1926: dib-run-parts Mon Oct  3 15:13:01 UTC 2016 01-install-bin                                0.005
1927: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
1928: dib-run-parts Mon Oct  3 15:13:01 UTC 2016 01-set-ubuntu-mirror                          0.002
1929: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
1930: dib-run-parts Mon Oct  3 15:13:01 UTC 2016 02-add-apt-keys                               0.002
1931: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
1932: dib-run-parts Mon Oct  3 15:13:01 UTC 2016 02-package-installs                           0.031
1933: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
1934: dib-run-parts Mon Oct  3 15:13:01 UTC 2016 03-baseline-tools                           168.584
1935: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
1936: dib-run-parts Mon Oct  3 15:13:01 UTC 2016 04-dib-init-system                            0.004
1937: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
1938: dib-run-parts Mon Oct  3 15:13:01 UTC 2016 99-apt-get-update                             5.683
1939: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
1940: dib-run-parts Mon Oct  3 15:13:01 UTC 2016 99-package-uninstalls                         0.037
1941: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
1942: dib-run-parts Mon Oct  3 15:13:01 UTC 2016
1943: dib-run-parts Mon Oct  3 15:13:01 UTC 2016 --------------------- END PROFILING ---------------------
1944: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_in_target:67 :   export HOME=/home/xion
1945: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_in_target:67 :   HOME=/home/xion
1946: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:83 :   trap - ERR
1947: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:84 :   check_break after-pre-install run_in_target bash
1948: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:check_break:98 :   echo ''
1949: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:check_break:98 :   egrep -e '(,|^)after-pre-install(,|$)' -q
1950: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:85 :   sudo umount -f /tmp/dib_build.1CFJZpLz/mnt/tmp/in_target.d
1951: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:86 :   timeout 5 sh -c ' while ! sudo rmdir /tmp/dib_build.1CFJZpLz/mnt/tmp/in_target.d; do sleep 1; done'
1952: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:323                  :   do_extra_package_install
1953: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:do_extra_package_install:143 :   '[' '' '!=' '' ']'
1954: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:325                  :   run_d_in_target install
1955: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:72 :   check_element
1956: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:check_element:109 :   '[' -d /tmp/dib_build.1CFJZpLz/hooks ']'
1957: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:75 :   '[' -d /tmp/dib_build.1CFJZpLz/hooks/install.d ']'
1958: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:76 :   sudo mkdir /tmp/dib_build.1CFJZpLz/mnt/tmp/in_target.d
1959: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:77 :   sudo mount --bind /tmp/dib_build.1CFJZpLz/hooks /tmp/dib_build.1CFJZpLz/mnt/tmp/in_target.d
1960: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:78 :   sudo mount -o remount,ro,bind /tmp/dib_build.1CFJZpLz/hooks /tmp/dib_build.1CFJZpLz/mnt/tmp/in_target.d
1961: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:79 :   check_break before-install run_in_target bash
1962: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:check_break:98 :   echo ''
1963: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:check_break:98 :   egrep -e '(,|^)before-install(,|$)' -q
1964: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:80 :   '[' -z '' ']'
1965: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:80 :   in_target_arg=run_in_target
1966: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:81 :   trap 'check_break after-error run_in_target bash' ERR
1967: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:82 :   run_in_target dib-run-parts /tmp/in_target.d/install.d
1968: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_in_target:57 :   cmd='dib-run-parts /tmp/in_target.d/install.d'
1969: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_in_target:59 :   ORIG_HOME=/home/xion
1970: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_in_target:60 :   export HOME=/root
1971: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_in_target:60 :   HOME=/root
1972: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_in_target:66 :   sudo -E chroot /tmp/dib_build.1CFJZpLz/mnt env -u TMPDIR 'PATH=$PATH:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin' sh -c 'dib-run-parts /tmp/in_target.d/install.d'
1973: + set -eu
1974: + set -o pipefail
1975: + [[ -f /usr/bin/systemctl ]]
1976: + [[ -f /sbin/initctl ]]
1977: + echo upstart
1978: ++ set -eu
1979: ++ set -o pipefail
1980: ++ export DIB_MANIFEST_IMAGE_DIR=/etc/dib-manifests
1981: ++ DIB_MANIFEST_IMAGE_DIR=/etc/dib-manifests
1982: ++ export DIB_MANIFEST_SAVE_DIR=image.d/
1983: ++ DIB_MANIFEST_SAVE_DIR=image.d/
1984: + for env_file in '$env_files'
1985: + source /tmp/in_target.d/install.d/../environment.d/99-cloud-init-datasources.bash
1986: ++ export DIB_CLOUD_INIT_DATASOURCES=Ec2
1987: ++ DIB_CLOUD_INIT_DATASOURCES=Ec2
1988: + for target in '$targets'
1989: + output 'Running /tmp/in_target.d/install.d/00-baseline-environment'
1990: + output_prefix
1991: ++ date
1992: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:13:01 UTC 2016'
1993: dib-run-parts Mon Oct  3 15:13:01 UTC 2016 + echo Running /tmp/in_target.d/install.d/00-baseline-environment
1994: Running /tmp/in_target.d/install.d/00-baseline-environment
1995: + target_tag=00-baseline-environment
1996: + date +%s.%N
1997: + /tmp/in_target.d/install.d/00-baseline-environment
1998: + set -eu
1999: + set -o pipefail
2000: + install-packages -m base iscsi_package
2001: + set -eu
2002: + set -o pipefail
2003: + ACTION=install
2004: + MAP_ELEMENT=
2005: ++ basename /usr/local/bin/install-packages
2006: + SCRIPTNAME=install-packages
2007: ++ getopt -o hudem: -n install-packages -- -m base iscsi_package
2008: + TEMP=' -m '\''base'\'' -- '\''iscsi_package'\'''
2009: + '[' 0 '!=' 0 ']'
2010: + eval set -- ' -m '\''base'\'' -- '\''iscsi_package'\'''
2011: ++ set -- -m base -- iscsi_package
2012: + true
2013: + case "$1" in
2014: + MAP_ELEMENT=base
2015: + shift 2
2016: + true
2017: + case "$1" in
2018: + shift
2019: + break
2020: + PKGS=iscsi_package
2021: + '[' -n base ']'
2022: ++ pkg-map --element base iscsi_package
2023: + PKGS=open-iscsi
2024: + '[' -z open-iscsi ']'
2025: + install_deb_packages install open-iscsi
2026: + DEBIAN_FRONTEND=noninteractive
2027: + http_proxy=
2028: + https_proxy=
2029: + no_proxy=
2030: + apt-get --option Dpkg::Options::=--force-confold --option Dpkg::Options::=--force-confdef --assume-yes install open-iscsi
2031: Reading package lists...
2032: Building dependency tree...
2033: Reading state information...
2034: The following packages were automatically installed and are no longer required:
2035:   libfreetype6 os-prober
2036: Use 'apt-get autoremove' to remove them.
2037: The following NEW packages will be installed:
2038:   open-iscsi
2039: perl: warning: Setting locale failed.
2040: perl: warning: Please check that your locale settings:
2041: 	LANGUAGE = "en_US",
2042: 	LC_ALL = (unset),
2043: 	LC_TIME = "zh_CN.UTF-8",
2044: 	LC_MONETARY = "zh_CN.UTF-8",
2045: 	LC_CTYPE = "en_US.UTF-8",
2046: 	LC_ADDRESS = "zh_CN.UTF-8",
2047: 	LC_TELEPHONE = "zh_CN.UTF-8",
2048: 	LC_NAME = "zh_CN.UTF-8",
2049: 	LC_MEASUREMENT = "zh_CN.UTF-8",
2050: 	LC_IDENTIFICATION = "zh_CN.UTF-8",
2051: 	LC_NUMERIC = "zh_CN.UTF-8",
2052: 	LC_PAPER = "zh_CN.UTF-8",
2053: 	LANG = "C"
2054:     are supported and installed on your system.
2055: perl: warning: Falling back to the standard locale ("C").
2056: locale: Cannot set LC_ALL to default locale: No such file or directory
2057: 0 upgraded, 1 newly installed, 0 to remove and 0 not upgraded.
2058: Need to get 0 B/268 kB of archives.
2059: After this operation, 2221 kB of additional disk space will be used.
2060: Selecting previously unselected package open-iscsi.
2061: (Reading database ... 24956 files and directories currently installed.)
2062: Preparing to unpack .../open-iscsi_2.0.873-3ubuntu9_amd64.deb ...
2063: Unpacking open-iscsi (2.0.873-3ubuntu9) ...
2064: Processing triggers for man-db (2.6.7.1-1ubuntu1) ...
2065: Processing triggers for ureadahead (0.100.0-16) ...
2066: Setting up open-iscsi (2.0.873-3ubuntu9) ...
2067: Processing triggers for ureadahead (0.100.0-16) ...
2068: + target_tag=00-baseline-environment
2069: + date +%s.%N
2070: + output '00-baseline-environment completed'
2071: + output_prefix
2072: ++ date
2073: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:13:02 UTC 2016'
2074: dib-run-parts Mon Oct  3 15:13:02 UTC 2016 + echo 00-baseline-environment completed
2075: 00-baseline-environment completed
2076: + for target in '$targets'
2077: + output 'Running /tmp/in_target.d/install.d/00-up-to-date'
2078: + output_prefix
2079: ++ date
2080: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:13:02 UTC 2016'
2081: dib-run-parts Mon Oct  3 15:13:02 UTC 2016 + echo Running /tmp/in_target.d/install.d/00-up-to-date
2082: Running /tmp/in_target.d/install.d/00-up-to-date
2083: + target_tag=00-up-to-date
2084: + date +%s.%N
2085: + /tmp/in_target.d/install.d/00-up-to-date
2086: + set -eu
2087: + set -o pipefail
2088: + install-packages -u
2089: + set -eu
2090: + set -o pipefail
2091: + ACTION=install
2092: + MAP_ELEMENT=
2093: ++ basename /usr/local/bin/install-packages
2094: + SCRIPTNAME=install-packages
2095: ++ getopt -o hudem: -n install-packages -- -u
2096: + TEMP=' -u --'
2097: + '[' 0 '!=' 0 ']'
2098: + eval set -- ' -u --'
2099: ++ set -- -u --
2100: + true
2101: + case "$1" in
2102: + install_deb_packages dist-upgrade
2103: + DEBIAN_FRONTEND=noninteractive
2104: + http_proxy=
2105: + https_proxy=
2106: + no_proxy=
2107: + apt-get --option Dpkg::Options::=--force-confold --option Dpkg::Options::=--force-confdef --assume-yes dist-upgrade
2108: Reading package lists...
2109: Building dependency tree...
2110: Reading state information...
2111: The following packages were automatically installed and are no longer required:
2112:   libfreetype6 os-prober
2113: Use 'apt-get autoremove' to remove them.
2114: 0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
2115: + exit 0
2116: + target_tag=00-up-to-date
2117: + date +%s.%N
2118: + output '00-up-to-date completed'
2119: + output_prefix
2120: ++ date
2121: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:13:03 UTC 2016'
2122: dib-run-parts Mon Oct  3 15:13:03 UTC 2016 + echo 00-up-to-date completed
2123: 00-up-to-date completed
2124: + for target in '$targets'
2125: + output 'Running /tmp/in_target.d/install.d/01-package-installs'
2126: + output_prefix
2127: ++ date
2128: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:13:03 UTC 2016'
2129: dib-run-parts Mon Oct  3 15:13:03 UTC 2016 + echo Running /tmp/in_target.d/install.d/01-package-installs
2130: Running /tmp/in_target.d/install.d/01-package-installs
2131: + target_tag=01-package-installs
2132: + date +%s.%N
2133: + /tmp/in_target.d/install.d/01-package-installs
2134: + set -eu
2135: + set -o pipefail
2136: ++ dirname /tmp/in_target.d/install.d/01-package-installs
2137: + package-installs -d /tmp/in_target.d/install.d
2138: + set -eu
2139: + set -o pipefail
2140: ++ basename /usr/local/bin/package-installs
2141: + SCRIPTNAME=package-installs
2142: ++ getopt -o hd: -n package-installs -- -d /tmp/in_target.d/install.d
2143: + TEMP=' -d '\''/tmp/in_target.d/install.d'\'' --'
2144: + '[' 0 '!=' 0 ']'
2145: + eval set -- ' -d '\''/tmp/in_target.d/install.d'\'' --'
2146: ++ set -- -d /tmp/in_target.d/install.d --
2147: + WORKDIR=
2148: + true
2149: + case "$1" in
2150: + WORKDIR=/tmp/in_target.d/install.d
2151: + shift 2
2152: + true
2153: + case "$1" in
2154: + shift
2155: + break
2156: + '[' -z /tmp/in_target.d/install.d ']'
2157: + PACKAGES=
2158: ++ find /tmp/in_target.d/install.d -maxdepth 1 -name 'package-installs-*'
2159: + '[' -n '' ']'
2160: + package-installs-v2 --phase install.d /tmp/package-installs.json
2161: Map file for ubuntu element does not exist.
2162: Map file for dkms element does not exist.
2163: + set -eu
2164: + set -o pipefail
2165: + ACTION=install
2166: + MAP_ELEMENT=
2167: ++ basename /usr/local/bin/install-packages
2168: + SCRIPTNAME=install-packages
2169: ++ getopt -o hudem: -n install-packages -- linux-image-generic ccache dkms
2170: + TEMP=' -- '\''linux-image-generic'\'' '\''ccache'\'' '\''dkms'\'''
2171: + '[' 0 '!=' 0 ']'
2172: + eval set -- ' -- '\''linux-image-generic'\'' '\''ccache'\'' '\''dkms'\'''
2173: ++ set -- -- linux-image-generic ccache dkms
2174: + true
2175: + case "$1" in
2176: + shift
2177: + break
2178: + PKGS='linux-image-generic ccache dkms'
2179: + '[' -n '' ']'
2180: + '[' -z 'linux-image-generic ccache dkms' ']'
2181: + install_deb_packages install linux-image-generic ccache dkms
2182: + DEBIAN_FRONTEND=noninteractive
2183: + http_proxy=
2184: + https_proxy=
2185: + no_proxy=
2186: + apt-get --option Dpkg::Options::=--force-confold --option Dpkg::Options::=--force-confdef --assume-yes install linux-image-generic ccache dkms
2187: perl: warning: Setting locale failed.
2188: perl: warning: Please check that your locale settings:
2189: 	LANGUAGE = "en_US",
2190: 	LC_ALL = (unset),
2191: 	LC_TIME = "zh_CN.UTF-8",
2192: 	LC_MONETARY = "zh_CN.UTF-8",
2193: 	LC_CTYPE = "en_US.UTF-8",
2194: 	LC_ADDRESS = "zh_CN.UTF-8",
2195: 	LC_TELEPHONE = "zh_CN.UTF-8",
2196: 	LC_NAME = "zh_CN.UTF-8",
2197: 	LC_MEASUREMENT = "zh_CN.UTF-8",
2198: 	LC_IDENTIFICATION = "zh_CN.UTF-8",
2199: 	LC_NUMERIC = "zh_CN.UTF-8",
2200: 	LC_PAPER = "zh_CN.UTF-8",
2201: 	LANG = "C"
2202:     are supported and installed on your system.
2203: perl: warning: Falling back to the standard locale ("C").
2204: locale: Cannot set LC_ALL to default locale: No such file or directory
2205: locale: Cannot set LC_ALL to default locale: No such file or directory
2206: Done.
2207: Running depmod.
2208: update-initramfs: deferring update (hook will be called later)
2209: Examining /etc/kernel/postinst.d.
2210: run-parts: executing /etc/kernel/postinst.d/apt-auto-removal 3.13.0-96-generic /boot/vmlinuz-3.13.0-96-generic
2211: run-parts: executing /etc/kernel/postinst.d/initramfs-tools 3.13.0-96-generic /boot/vmlinuz-3.13.0-96-generic
2212: update-initramfs: Generating /boot/initrd.img-3.13.0-96-generic
2213: run-parts: executing /etc/kernel/postinst.d/update-notifier 3.13.0-96-generic /boot/vmlinuz-3.13.0-96-generic
2214: run-parts: executing /etc/kernel/postinst.d/apt-auto-removal 3.13.0-96-generic /boot/vmlinuz-3.13.0-96-generic
2215: run-parts: executing /etc/kernel/postinst.d/dkms 3.13.0-96-generic /boot/vmlinuz-3.13.0-96-generic
2216: run-parts: executing /etc/kernel/postinst.d/initramfs-tools 3.13.0-96-generic /boot/vmlinuz-3.13.0-96-generic
2217: update-initramfs: Generating /boot/initrd.img-3.13.0-96-generic
2218: run-parts: executing /etc/kernel/postinst.d/update-notifier 3.13.0-96-generic /boot/vmlinuz-3.13.0-96-generic
2219: installing ccache_package from base
2220: installing linux-image-generic from ubuntu
2221: installing dkms from dkms
2222: + target_tag=01-package-installs
2223: + date +%s.%N
2224: + output '01-package-installs completed'
2225: + output_prefix
2226: ++ date
2227: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:13:35 UTC 2016'
2228: dib-run-parts Mon Oct  3 15:13:35 UTC 2016 + echo 01-package-installs completed
2229: 01-package-installs completed
2230: + for target in '$targets'
2231: + output 'Running /tmp/in_target.d/install.d/05-set-cloud-init-sources'
2232: + output_prefix
2233: ++ date
2234: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:13:35 UTC 2016'
2235: dib-run-parts Mon Oct  3 15:13:35 UTC 2016 + echo Running /tmp/in_target.d/install.d/05-set-cloud-init-sources
2236: Running /tmp/in_target.d/install.d/05-set-cloud-init-sources
2237: + target_tag=05-set-cloud-init-sources
2238: + date +%s.%N
2239: + /tmp/in_target.d/install.d/05-set-cloud-init-sources
2240: + set -eu
2241: + set -o pipefail
2242: + DIB_CLOUD_INIT_DATASOURCES=Ec2
2243: + '[' -z Ec2 ']'
2244: + '[' -d /etc/cloud/cloud.cfg.d ']'
2245: ++ lsb_release -cs
2246: + '[' trusty = precise ']'
2247: + cat
2248: + target_tag=05-set-cloud-init-sources
2249: + date +%s.%N
2250: + output '05-set-cloud-init-sources completed'
2251: + output_prefix
2252: ++ date
2253: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:13:35 UTC 2016'
2254: dib-run-parts Mon Oct  3 15:13:35 UTC 2016 + echo 05-set-cloud-init-sources completed
2255: 05-set-cloud-init-sources completed
2256: + for target in '$targets'
2257: + output 'Running /tmp/in_target.d/install.d/10-cloud-init'
2258: + output_prefix
2259: ++ date
2260: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:13:35 UTC 2016'
2261: dib-run-parts Mon Oct  3 15:13:35 UTC 2016 + echo Running /tmp/in_target.d/install.d/10-cloud-init
2262: Running /tmp/in_target.d/install.d/10-cloud-init
2263: + target_tag=10-cloud-init
2264: + date +%s.%N
2265: + /tmp/in_target.d/install.d/10-cloud-init
2266: + set -eu
2267: + set -o pipefail
2268: + mkdir -p /etc/cloud/cloud.cfg.d
2269: + '[' -n '' ']'
2270: + target_tag=10-cloud-init
2271: + date +%s.%N
2272: + output '10-cloud-init completed'
2273: + output_prefix
2274: ++ date
2275: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:13:35 UTC 2016'
2276: dib-run-parts Mon Oct  3 15:13:35 UTC 2016 + echo 10-cloud-init completed
2277: 10-cloud-init completed
2278: + for target in '$targets'
2279: + output 'Running /tmp/in_target.d/install.d/20-install-init-scripts'
2280: + output_prefix
2281: ++ date
2282: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:13:35 UTC 2016'
2283: dib-run-parts Mon Oct  3 15:13:35 UTC 2016 + echo Running /tmp/in_target.d/install.d/20-install-init-scripts
2284: Running /tmp/in_target.d/install.d/20-install-init-scripts
2285: + target_tag=20-install-init-scripts
2286: + date +%s.%N
2287: + /tmp/in_target.d/install.d/20-install-init-scripts
2288: + set -eu
2289: + set -o pipefail
2290: ++ dirname /tmp/in_target.d/install.d/20-install-init-scripts
2291: + scripts_dir=/tmp/in_target.d/install.d/../init-scripts/upstart/
2292: + '[' -d /tmp/in_target.d/install.d/../init-scripts/upstart/ ']'
2293: + target_tag=20-install-init-scripts
2294: + date +%s.%N
2295: + output '20-install-init-scripts completed'
2296: + output_prefix
2297: ++ date
2298: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:13:35 UTC 2016'
2299: dib-run-parts Mon Oct  3 15:13:35 UTC 2016 + echo 20-install-init-scripts completed
2300: 20-install-init-scripts completed
2301: + for target in '$targets'
2302: + output 'Running /tmp/in_target.d/install.d/50-store-build-settings'
2303: + output_prefix
2304: ++ date
2305: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:13:35 UTC 2016'
2306: dib-run-parts Mon Oct  3 15:13:35 UTC 2016 + echo Running /tmp/in_target.d/install.d/50-store-build-settings
2307: Running /tmp/in_target.d/install.d/50-store-build-settings
2308: + target_tag=50-store-build-settings
2309: + date +%s.%N
2310: + /tmp/in_target.d/install.d/50-store-build-settings
2311: + set -eu
2312: + set -o pipefail
2313: + '[' -e /tmp/in_target.d/dib_environment ']'
2314: + cp /tmp/in_target.d/dib_environment /etc/
2315: + '[' -e /tmp/in_target.d/dib_arguments ']'
2316: + cp /tmp/in_target.d/dib_arguments /etc/
2317: + target_tag=50-store-build-settings
2318: + date +%s.%N
2319: + output '50-store-build-settings completed'
2320: + output_prefix
2321: ++ date
2322: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:13:35 UTC 2016'
2323: dib-run-parts Mon Oct  3 15:13:35 UTC 2016 + echo 50-store-build-settings completed
2324: 50-store-build-settings completed
2325: + for target in '$targets'
2326: + output 'Running /tmp/in_target.d/install.d/80-disable-rfc3041'
2327: + output_prefix
2328: ++ date
2329: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:13:35 UTC 2016'
2330: dib-run-parts Mon Oct  3 15:13:35 UTC 2016 + echo Running /tmp/in_target.d/install.d/80-disable-rfc3041
2331: Running /tmp/in_target.d/install.d/80-disable-rfc3041
2332: + target_tag=80-disable-rfc3041
2333: + date +%s.%N
2334: + /tmp/in_target.d/install.d/80-disable-rfc3041
2335: + set -e
2336: + cat
2337: + target_tag=80-disable-rfc3041
2338: + date +%s.%N
2339: + output '80-disable-rfc3041 completed'
2340: + output_prefix
2341: ++ date
2342: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:13:35 UTC 2016'
2343: dib-run-parts Mon Oct  3 15:13:35 UTC 2016 + echo 80-disable-rfc3041 completed
2344: 80-disable-rfc3041 completed
2345: + for target in '$targets'
2346: + output 'Running /tmp/in_target.d/install.d/99-autoremove'
2347: + output_prefix
2348: ++ date
2349: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:13:35 UTC 2016'
2350: dib-run-parts Mon Oct  3 15:13:35 UTC 2016 + echo Running /tmp/in_target.d/install.d/99-autoremove
2351: Running /tmp/in_target.d/install.d/99-autoremove
2352: + target_tag=99-autoremove
2353: + date +%s.%N
2354: + /tmp/in_target.d/install.d/99-autoremove
2355: + set -eu
2356: + set -o pipefail
2357: + apt-get -y autoremove
2358: Reading package lists...
2359: Building dependency tree...
2360: Reading state information...
2361: The following packages will be REMOVED:
2362:   libfreetype6 os-prober
2363: perl: warning: Setting locale failed.
2364: perl: warning: Please check that your locale settings:
2365: 	LANGUAGE = "en_US",
2366: 	LC_ALL = (unset),
2367: 	LC_TIME = "zh_CN.UTF-8",
2368: 	LC_MONETARY = "zh_CN.UTF-8",
2369: 	LC_CTYPE = "en_US.UTF-8",
2370: 	LC_ADDRESS = "zh_CN.UTF-8",
2371: 	LC_TELEPHONE = "zh_CN.UTF-8",
2372: 	LC_NAME = "zh_CN.UTF-8",
2373: 	LC_MEASUREMENT = "zh_CN.UTF-8",
2374: 	LC_IDENTIFICATION = "zh_CN.UTF-8",
2375: 	LC_NUMERIC = "zh_CN.UTF-8",
2376: 	LC_PAPER = "zh_CN.UTF-8",
2377: 	LANG = "C"
2378:     are supported and installed on your system.
2379: perl: warning: Falling back to the standard locale ("C").
2380: locale: Cannot set LC_ALL to default locale: No such file or directory
2381: 0 upgraded, 0 newly installed, 2 to remove and 0 not upgraded.
2382: After this operation, 1063 kB disk space will be freed.
2383: (Reading database ... 31518 files and directories currently installed.)
2384: Removing libfreetype6:amd64 (2.5.2-1ubuntu2.5) ...
2385: Removing os-prober (1.63ubuntu1.1) ...
2386: Processing triggers for libc-bin (2.19-0ubuntu6.9) ...
2387: + target_tag=99-autoremove
2388: + date +%s.%N
2389: + output '99-autoremove completed'
2390: + output_prefix
2391: ++ date
2392: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:13:36 UTC 2016'
2393: dib-run-parts Mon Oct  3 15:13:36 UTC 2016 + echo 99-autoremove completed
2394: 99-autoremove completed
2395: + for target in '$targets'
2396: + output 'Running /tmp/in_target.d/install.d/99-package-uninstalls'
2397: + output_prefix
2398: ++ date
2399: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:13:36 UTC 2016'
2400: dib-run-parts Mon Oct  3 15:13:36 UTC 2016 + echo Running /tmp/in_target.d/install.d/99-package-uninstalls
2401: Running /tmp/in_target.d/install.d/99-package-uninstalls
2402: + target_tag=99-package-uninstalls
2403: + date +%s.%N
2404: + /tmp/in_target.d/install.d/99-package-uninstalls
2405: + set -eu
2406: + set -o pipefail
2407: ++ dirname /tmp/in_target.d/install.d/99-package-uninstalls
2408: + package-uninstalls -d /tmp/in_target.d/install.d
2409: + set -eu
2410: + set -o pipefail
2411: ++ basename /usr/local/bin/package-uninstalls
2412: + SCRIPTNAME=package-uninstalls
2413: ++ getopt -o hd: -n package-uninstalls -- -d /tmp/in_target.d/install.d
2414: + TEMP=' -d '\''/tmp/in_target.d/install.d'\'' --'
2415: + '[' 0 '!=' 0 ']'
2416: + eval set -- ' -d '\''/tmp/in_target.d/install.d'\'' --'
2417: ++ set -- -d /tmp/in_target.d/install.d --
2418: + WORKDIR=
2419: + true
2420: + case "$1" in
2421: + WORKDIR=/tmp/in_target.d/install.d
2422: + shift 2
2423: + true
2424: + case "$1" in
2425: + shift
2426: + break
2427: + '[' -z /tmp/in_target.d/install.d ']'
2428: + PACKAGES=
2429: ++ find /tmp/in_target.d/install.d -maxdepth 1 -name 'package-installs-*'
2430: + install-packages -e
2431: + set -eu
2432: + set -o pipefail
2433: + ACTION=install
2434: + MAP_ELEMENT=
2435: ++ basename /usr/local/bin/install-packages
2436: + SCRIPTNAME=install-packages
2437: ++ getopt -o hudem: -n install-packages -- -e
2438: + TEMP=' -e --'
2439: + '[' 0 '!=' 0 ']'
2440: + eval set -- ' -e --'
2441: ++ set -- -e --
2442: + true
2443: + case "$1" in
2444: + ACTION=remove
2445: + shift
2446: + true
2447: + case "$1" in
2448: + shift
2449: + break
2450: + PKGS=
2451: + '[' -n '' ']'
2452: + '[' -z '' ']'
2453: + echo 'Not running install-packages remove with empty packages list'
2454: Not running install-packages remove with empty packages list
2455: + package-installs-v2 --phase install.d --uninstall /tmp/package-installs.json
2456: Nothing to uninstall
2457: + target_tag=99-package-uninstalls
2458: + date +%s.%N
2459: + output '99-package-uninstalls completed'
2460: + output_prefix
2461: ++ date
2462: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:13:36 UTC 2016'
2463: dib-run-parts Mon Oct  3 15:13:36 UTC 2016 + echo 99-package-uninstalls completed
2464: 99-package-uninstalls completed
2465: dib-run-parts Mon Oct  3 15:13:36 UTC 2016 ----------------------- PROFILING -----------------------
2466: dib-run-parts Mon Oct  3 15:13:36 UTC 2016
2467: dib-run-parts Mon Oct  3 15:13:36 UTC 2016 Target: install.d
2468: dib-run-parts Mon Oct  3 15:13:36 UTC 2016
2469: dib-run-parts Mon Oct  3 15:13:36 UTC 2016 Script                                     Seconds
2470: dib-run-parts Mon Oct  3 15:13:36 UTC 2016 ---------------------------------------  ----------
2471: dib-run-parts Mon Oct  3 15:13:36 UTC 2016
2472: dib-run-parts Mon Oct  3 15:13:36 UTC 2016 00-baseline-environment                       1.131
2473: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
2474: dib-run-parts Mon Oct  3 15:13:36 UTC 2016 00-up-to-date                                 0.454
2475: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
2476: dib-run-parts Mon Oct  3 15:13:36 UTC 2016 01-package-installs                          32.723
2477: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
2478: dib-run-parts Mon Oct  3 15:13:36 UTC 2016 05-set-cloud-init-sources                     0.046
2479: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
2480: dib-run-parts Mon Oct  3 15:13:36 UTC 2016 10-cloud-init                                 0.004
2481: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
2482: dib-run-parts Mon Oct  3 15:13:36 UTC 2016 20-install-init-scripts                       0.004
2483: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
2484: dib-run-parts Mon Oct  3 15:13:36 UTC 2016 50-store-build-settings                       0.005
2485: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
2486: dib-run-parts Mon Oct  3 15:13:36 UTC 2016 80-disable-rfc3041                            0.003
2487: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
2488: dib-run-parts Mon Oct  3 15:13:36 UTC 2016 99-autoremove                                 0.527
2489: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
2490: dib-run-parts Mon Oct  3 15:13:36 UTC 2016 99-package-uninstalls                         0.035
2491: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
2492: dib-run-parts Mon Oct  3 15:13:36 UTC 2016
2493: dib-run-parts Mon Oct  3 15:13:36 UTC 2016 --------------------- END PROFILING ---------------------
2494: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_in_target:67 :   export HOME=/home/xion
2495: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_in_target:67 :   HOME=/home/xion
2496: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:83 :   trap - ERR
2497: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:84 :   check_break after-install run_in_target bash
2498: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:check_break:98 :   egrep -e '(,|^)after-install(,|$)' -q
2499: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:check_break:98 :   echo ''
2500: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:85 :   sudo umount -f /tmp/dib_build.1CFJZpLz/mnt/tmp/in_target.d
2501: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:86 :   timeout 5 sh -c ' while ! sudo rmdir /tmp/dib_build.1CFJZpLz/mnt/tmp/in_target.d; do sleep 1; done'
2502: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:326                  :   run_d_in_target post-install
2503: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:72 :   check_element
2504: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:check_element:109 :   '[' -d /tmp/dib_build.1CFJZpLz/hooks ']'
2505: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:75 :   '[' -d /tmp/dib_build.1CFJZpLz/hooks/post-install.d ']'
2506: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:76 :   sudo mkdir /tmp/dib_build.1CFJZpLz/mnt/tmp/in_target.d
2507: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:77 :   sudo mount --bind /tmp/dib_build.1CFJZpLz/hooks /tmp/dib_build.1CFJZpLz/mnt/tmp/in_target.d
2508: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:78 :   sudo mount -o remount,ro,bind /tmp/dib_build.1CFJZpLz/hooks /tmp/dib_build.1CFJZpLz/mnt/tmp/in_target.d
2509: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:79 :   check_break before-post-install run_in_target bash
2510: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:check_break:98 :   echo ''
2511: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:check_break:98 :   egrep -e '(,|^)before-post-install(,|$)' -q
2512: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:80 :   '[' -z '' ']'
2513: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:80 :   in_target_arg=run_in_target
2514: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:81 :   trap 'check_break after-error run_in_target bash' ERR
2515: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:82 :   run_in_target dib-run-parts /tmp/in_target.d/post-install.d
2516: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_in_target:57 :   cmd='dib-run-parts /tmp/in_target.d/post-install.d'
2517: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_in_target:59 :   ORIG_HOME=/home/xion
2518: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_in_target:60 :   export HOME=/root
2519: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_in_target:60 :   HOME=/root
2520: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_in_target:66 :   sudo -E chroot /tmp/dib_build.1CFJZpLz/mnt env -u TMPDIR 'PATH=$PATH:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin' sh -c 'dib-run-parts /tmp/in_target.d/post-install.d'
2521: + set -eu
2522: + set -o pipefail
2523: + [[ -f /usr/bin/systemctl ]]
2524: + [[ -f /sbin/initctl ]]
2525: + echo upstart
2526: ++ set -eu
2527: ++ set -o pipefail
2528: ++ export DIB_MANIFEST_IMAGE_DIR=/etc/dib-manifests
2529: ++ DIB_MANIFEST_IMAGE_DIR=/etc/dib-manifests
2530: ++ export DIB_MANIFEST_SAVE_DIR=image.d/
2531: ++ DIB_MANIFEST_SAVE_DIR=image.d/
2532: + for env_file in '$env_files'
2533: + source /tmp/in_target.d/post-install.d/../environment.d/99-cloud-init-datasources.bash
2534: ++ export DIB_CLOUD_INIT_DATASOURCES=Ec2
2535: ++ DIB_CLOUD_INIT_DATASOURCES=Ec2
2536: + for target in '$targets'
2537: + output 'Running /tmp/in_target.d/post-install.d/00-package-installs'
2538: + output_prefix
2539: ++ date
2540: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:13:36 UTC 2016'
2541: dib-run-parts Mon Oct  3 15:13:36 UTC 2016 + echo Running /tmp/in_target.d/post-install.d/00-package-installs
2542: Running /tmp/in_target.d/post-install.d/00-package-installs
2543: + target_tag=00-package-installs
2544: + date +%s.%N
2545: + /tmp/in_target.d/post-install.d/00-package-installs
2546: + set -eu
2547: + set -o pipefail
2548: ++ dirname /tmp/in_target.d/post-install.d/00-package-installs
2549: + package-installs -d /tmp/in_target.d/post-install.d
2550: + set -eu
2551: + set -o pipefail
2552: ++ basename /usr/local/bin/package-installs
2553: + SCRIPTNAME=package-installs
2554: ++ getopt -o hd: -n package-installs -- -d /tmp/in_target.d/post-install.d
2555: + TEMP=' -d '\''/tmp/in_target.d/post-install.d'\'' --'
2556: + '[' 0 '!=' 0 ']'
2557: + eval set -- ' -d '\''/tmp/in_target.d/post-install.d'\'' --'
2558: ++ set -- -d /tmp/in_target.d/post-install.d --
2559: + WORKDIR=
2560: + true
2561: + case "$1" in
2562: + WORKDIR=/tmp/in_target.d/post-install.d
2563: + shift 2
2564: + true
2565: + case "$1" in
2566: + shift
2567: + break
2568: + '[' -z /tmp/in_target.d/post-install.d ']'
2569: + PACKAGES=
2570: ++ find /tmp/in_target.d/post-install.d -maxdepth 1 -name 'package-installs-*'
2571: + '[' -n '' ']'
2572: + package-installs-v2 --phase post-install.d /tmp/package-installs.json
2573: Nothing to install
2574: + target_tag=00-package-installs
2575: + date +%s.%N
2576: + output '00-package-installs completed'
2577: + output_prefix
2578: ++ date
2579: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:13:36 UTC 2016'
2580: dib-run-parts Mon Oct  3 15:13:36 UTC 2016 + echo 00-package-installs completed
2581: 00-package-installs completed
2582: + for target in '$targets'
2583: + output 'Running /tmp/in_target.d/post-install.d/10-enable-init-scripts'
2584: + output_prefix
2585: ++ date
2586: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:13:36 UTC 2016'
2587: dib-run-parts Mon Oct  3 15:13:36 UTC 2016 + echo Running /tmp/in_target.d/post-install.d/10-enable-init-scripts
2588: Running /tmp/in_target.d/post-install.d/10-enable-init-scripts
2589: + target_tag=10-enable-init-scripts
2590: + date +%s.%N
2591: + /tmp/in_target.d/post-install.d/10-enable-init-scripts
2592: + set -eu
2593: + set -o pipefail
2594: ++ dirname /tmp/in_target.d/post-install.d/10-enable-init-scripts
2595: + SCRIPTS_DIR=/tmp/in_target.d/post-install.d/../init-scripts/upstart/
2596: + [[ -d /tmp/in_target.d/post-install.d/../init-scripts/upstart/ ]]
2597: + target_tag=10-enable-init-scripts
2598: + date +%s.%N
2599: + output '10-enable-init-scripts completed'
2600: + output_prefix
2601: ++ date
2602: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:13:36 UTC 2016'
2603: dib-run-parts Mon Oct  3 15:13:36 UTC 2016 + echo 10-enable-init-scripts completed
2604: 10-enable-init-scripts completed
2605: + for target in '$targets'
2606: + output 'Running /tmp/in_target.d/post-install.d/95-package-uninstalls'
2607: + output_prefix
2608: ++ date
2609: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:13:36 UTC 2016'
2610: dib-run-parts Mon Oct  3 15:13:36 UTC 2016 + echo Running /tmp/in_target.d/post-install.d/95-package-uninstalls
2611: Running /tmp/in_target.d/post-install.d/95-package-uninstalls
2612: + target_tag=95-package-uninstalls
2613: + date +%s.%N
2614: + /tmp/in_target.d/post-install.d/95-package-uninstalls
2615: + set -eu
2616: + set -o pipefail
2617: ++ dirname /tmp/in_target.d/post-install.d/95-package-uninstalls
2618: + package-uninstalls -d /tmp/in_target.d/post-install.d
2619: + set -eu
2620: + set -o pipefail
2621: ++ basename /usr/local/bin/package-uninstalls
2622: + SCRIPTNAME=package-uninstalls
2623: ++ getopt -o hd: -n package-uninstalls -- -d /tmp/in_target.d/post-install.d
2624: + TEMP=' -d '\''/tmp/in_target.d/post-install.d'\'' --'
2625: + '[' 0 '!=' 0 ']'
2626: + eval set -- ' -d '\''/tmp/in_target.d/post-install.d'\'' --'
2627: ++ set -- -d /tmp/in_target.d/post-install.d --
2628: + WORKDIR=
2629: + true
2630: + case "$1" in
2631: + WORKDIR=/tmp/in_target.d/post-install.d
2632: + shift 2
2633: + true
2634: + case "$1" in
2635: + shift
2636: + break
2637: + '[' -z /tmp/in_target.d/post-install.d ']'
2638: + PACKAGES=
2639: ++ find /tmp/in_target.d/post-install.d -maxdepth 1 -name 'package-installs-*'
2640: + install-packages -e
2641: + set -eu
2642: + set -o pipefail
2643: + ACTION=install
2644: + MAP_ELEMENT=
2645: ++ basename /usr/local/bin/install-packages
2646: + SCRIPTNAME=install-packages
2647: ++ getopt -o hudem: -n install-packages -- -e
2648: + TEMP=' -e --'
2649: + '[' 0 '!=' 0 ']'
2650: + eval set -- ' -e --'
2651: ++ set -- -e --
2652: + true
2653: + case "$1" in
2654: + ACTION=remove
2655: + shift
2656: + true
2657: + case "$1" in
2658: + shift
2659: + break
2660: + PKGS=
2661: + '[' -n '' ']'
2662: + '[' -z '' ']'
2663: + echo 'Not running install-packages remove with empty packages list'
2664: Not running install-packages remove with empty packages list
2665: + package-installs-v2 --phase post-install.d --uninstall /tmp/package-installs.json
2666: Nothing to uninstall
2667: + target_tag=95-package-uninstalls
2668: + date +%s.%N
2669: + output '95-package-uninstalls completed'
2670: + output_prefix
2671: ++ date
2672: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:13:36 UTC 2016'
2673: dib-run-parts Mon Oct  3 15:13:36 UTC 2016 + echo 95-package-uninstalls completed
2674: 95-package-uninstalls completed
2675: + for target in '$targets'
2676: + output 'Running /tmp/in_target.d/post-install.d/97-dkms'
2677: + output_prefix
2678: ++ date
2679: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:13:36 UTC 2016'
2680: dib-run-parts Mon Oct  3 15:13:36 UTC 2016 + echo Running /tmp/in_target.d/post-install.d/97-dkms
2681: Running /tmp/in_target.d/post-install.d/97-dkms
2682: + target_tag=97-dkms
2683: + date +%s.%N
2684: + /tmp/in_target.d/post-install.d/97-dkms
2685: + set -eu
2686: + set -o pipefail
2687: ++ dkms status
2688: ++ tr ,: ' '
2689: ++ awk '{ print $1 "/" $2 }'
2690: + modules=
2691: ++ sed -e 's|/usr/src/linux-headers-||'
2692: ++ ls '/usr/src/linux-headers-*-*-*' -d
2693: ls: cannot access /usr/src/linux-headers-*-*-*: No such file or directory
2694: ++ echo ''
2695: + kernels=
2696: + '[' -z '' ']'
2697: ++ ls '/usr/src/kernels/*' -d
2698: ++ sed -e 's|/usr/src/kernels/||'
2699: ls: cannot access /usr/src/kernels/*: No such file or directory
2700: ++ echo ''
2701: + kernels=
2702: + '[' -z '' ']'
2703: + echo 'Warning: No kernel versions found for DKMS'
2704: Warning: No kernel versions found for DKMS
2705: + __ARCH=amd64
2706: + unset ARCH
2707: + ARCH=amd64
2708: + dkms status
2709: + target_tag=97-dkms
2710: + date +%s.%N
2711: + output '97-dkms completed'
2712: + output_prefix
2713: ++ date
2714: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:13:36 UTC 2016'
2715: dib-run-parts Mon Oct  3 15:13:36 UTC 2016 + echo 97-dkms completed
2716: 97-dkms completed
2717: dib-run-parts Mon Oct  3 15:13:36 UTC 2016 ----------------------- PROFILING -----------------------
2718: dib-run-parts Mon Oct  3 15:13:36 UTC 2016
2719: dib-run-parts Mon Oct  3 15:13:36 UTC 2016 Target: post-install.d
2720: dib-run-parts Mon Oct  3 15:13:36 UTC 2016
2721: dib-run-parts Mon Oct  3 15:13:36 UTC 2016 Script                                     Seconds
2722: dib-run-parts Mon Oct  3 15:13:36 UTC 2016 ---------------------------------------  ----------
2723: dib-run-parts Mon Oct  3 15:13:36 UTC 2016
2724: dib-run-parts Mon Oct  3 15:13:36 UTC 2016 00-package-installs                           0.033
2725: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
2726: dib-run-parts Mon Oct  3 15:13:36 UTC 2016 10-enable-init-scripts                        0.003
2727: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
2728: dib-run-parts Mon Oct  3 15:13:36 UTC 2016 95-package-uninstalls                         0.035
2729: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
2730: dib-run-parts Mon Oct  3 15:13:36 UTC 2016 97-dkms                                       0.054
2731: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
2732: dib-run-parts Mon Oct  3 15:13:36 UTC 2016
2733: dib-run-parts Mon Oct  3 15:13:36 UTC 2016 --------------------- END PROFILING ---------------------
2734: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_in_target:67 :   export HOME=/home/xion
2735: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_in_target:67 :   HOME=/home/xion
2736: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:83 :   trap - ERR
2737: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:84 :   check_break after-post-install run_in_target bash
2738: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:check_break:98 :   echo ''
2739: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:check_break:98 :   egrep -e '(,|^)after-post-install(,|$)' -q
2740: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:85 :   sudo umount -f /tmp/dib_build.1CFJZpLz/mnt/tmp/in_target.d
2741: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:86 :   timeout 5 sh -c ' while ! sudo rmdir /tmp/dib_build.1CFJZpLz/mnt/tmp/in_target.d; do sleep 1; done'
2742: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:330                  :   '[' -e /tmp/dib_build.1CFJZpLz/mnt/lost+found ']'
2743: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:331                  :   sudo rm -rf /tmp/dib_build.1CFJZpLz/mnt/lost+found
2744: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:334                  :   unmount_image
2745: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:unmount_image:22 :   sync
2746: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:unmount_image:26 :   unmount_dir /tmp/dib_build.1CFJZpLz/mnt
2747: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:247 :   local dir=/tmp/dib_build.1CFJZpLz/mnt
2748: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:248 :   local real_dir
2749: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:249 :   local mnts
2750: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:251 :   '[' '!' -d /tmp/dib_build.1CFJZpLz/mnt ']'
2751: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:258 :   readlink -e /tmp/dib_build.1CFJZpLz/mnt
2752: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:258 :   real_dir=/tmp/dib_build.1CFJZpLz/mnt
2753: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:260 :   sort -r
2754: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:260 :   grep '^/tmp/dib_build.1CFJZpLz/mnt'
2755: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:260 :   awk '{print $2}'
2756: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:260 :   mnts='/tmp/dib_build.1CFJZpLz/mnt/var/cache/apt/archives
2757: /tmp/dib_build.1CFJZpLz/mnt/tmp/ccache
2758: /tmp/dib_build.1CFJZpLz/mnt/sys
2759: /tmp/dib_build.1CFJZpLz/mnt/proc
2760: /tmp/dib_build.1CFJZpLz/mnt/dev/pts
2761: /tmp/dib_build.1CFJZpLz/mnt/dev'
2762: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:261 :   for m in '$mnts'
2763: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:262 :   echo 'Unmount /tmp/dib_build.1CFJZpLz/mnt/var/cache/apt/archives'
2764: Unmount /tmp/dib_build.1CFJZpLz/mnt/var/cache/apt/archives
2765: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:263 :   sudo umount -fl /tmp/dib_build.1CFJZpLz/mnt/var/cache/apt/archives
2766: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:261 :   for m in '$mnts'
2767: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:262 :   echo 'Unmount /tmp/dib_build.1CFJZpLz/mnt/tmp/ccache'
2768: Unmount /tmp/dib_build.1CFJZpLz/mnt/tmp/ccache
2769: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:263 :   sudo umount -fl /tmp/dib_build.1CFJZpLz/mnt/tmp/ccache
2770: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:261 :   for m in '$mnts'
2771: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:262 :   echo 'Unmount /tmp/dib_build.1CFJZpLz/mnt/sys'
2772: Unmount /tmp/dib_build.1CFJZpLz/mnt/sys
2773: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:263 :   sudo umount -fl /tmp/dib_build.1CFJZpLz/mnt/sys
2774: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:261 :   for m in '$mnts'
2775: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:262 :   echo 'Unmount /tmp/dib_build.1CFJZpLz/mnt/proc'
2776: Unmount /tmp/dib_build.1CFJZpLz/mnt/proc
2777: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:263 :   sudo umount -fl /tmp/dib_build.1CFJZpLz/mnt/proc
2778: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:261 :   for m in '$mnts'
2779: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:262 :   echo 'Unmount /tmp/dib_build.1CFJZpLz/mnt/dev/pts'
2780: Unmount /tmp/dib_build.1CFJZpLz/mnt/dev/pts
2781: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:263 :   sudo umount -fl /tmp/dib_build.1CFJZpLz/mnt/dev/pts
2782: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:261 :   for m in '$mnts'
2783: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:262 :   echo 'Unmount /tmp/dib_build.1CFJZpLz/mnt/dev'
2784: Unmount /tmp/dib_build.1CFJZpLz/mnt/dev
2785: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:263 :   sudo umount -fl /tmp/dib_build.1CFJZpLz/mnt/dev
2786: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:unmount_image:27 :   '[' -n '' ']'
2787: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:335                  :   mv /tmp/dib_build.1CFJZpLz/mnt /tmp/dib_build.1CFJZpLz/built
2788: ++ /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:339                  :   grep xtrace
2789: ++ /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:339                  :   set +o
2790: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:339                  :   xtrace='set -o xtrace'
2791: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:342                  :   du_output=/tmp/dib_build.1CFJZpLz/du_output.tmp
2792: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:344                  :   '[' -n '' ']'
2793: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:347                  :   set +o xtrace
2794: Calculating image size (this may take a minute)...
2795: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:356                  :   [[ 0 != 0 ]]
2796: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:390                  :   rm -f /tmp/dib_build.1CFJZpLz/du_output.tmp
2797: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:392                  :   '[' ext4 = ext4 ']'
2798: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:396                  :   MKFS_OPTS='-i 4096 -J size=64 '
2799: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:399                  :   '[' -z '' ']'
2800: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:400                  :   du_size=1667809
2801: ++ /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:407                  :   echo 1667809
2802: ++ /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:407                  :   awk ' { if ($1 % 64 != 0) print $1 + 64 - ( $1 % 64); else print $1; } '
2803: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:407                  :   du_size=1667840
2804: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:408                  :   truncate -s1667840K /tmp/dib_image.rja54tUR/image.raw
2805: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:410                  :   '[' -n '' ']'
2806: ++ /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:414                  :   sudo losetup --show -f /tmp/dib_image.rja54tUR/image.raw
2807: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:414                  :   LOOPDEV=/dev/loop0
2808: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:415                  :   export 'EXTRA_UNMOUNT=detach_loopback /dev/loop0'
2809: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:415                  :   EXTRA_UNMOUNT='detach_loopback /dev/loop0'
2810: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:416                  :   export IMAGE_BLOCK_DEVICE=/dev/loop0
2811: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:416                  :   IMAGE_BLOCK_DEVICE=/dev/loop0
2812: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:417                  :   eval_run_d block-device IMAGE_BLOCK_DEVICE=
2813: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:eval_run_d:116 :   mktemp
2814: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:eval_run_d:116 :   local run_output=/tmp/tmp.SsHcH25KgJ
2815: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:eval_run_d:117 :   trap 'rm -f /tmp/tmp.SsHcH25KgJ; check_break after-error bash' ERR
2816: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:eval_run_d:118 :   run_d block-device /tmp/tmp.SsHcH25KgJ
2817: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:run_d:148 :   check_element
2818: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:check_element:109 :   '[' -d /tmp/dib_build.1CFJZpLz/hooks ']'
2819: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:run_d:149 :   check_break before-block-device bash
2820: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:check_break:98 :   egrep -e '(,|^)before-block-device(,|$)' -q
2821: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:check_break:98 :   echo ''
2822: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:run_d:150 :   '[' -d /tmp/dib_build.1CFJZpLz/hooks/block-device.d ']'
2823: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:run_d:151 :   '[' -n /tmp/tmp.SsHcH25KgJ ']'
2824: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:run_d:152 :   dib-run-parts /tmp/dib_build.1CFJZpLz/hooks/block-device.d
2825: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:run_d:152 :   tee /tmp/tmp.SsHcH25KgJ
2826: + /tmp/dib_build.1CFJZpLz/hooks/dib-init-system:main:6                             :   set -eu
2827: + /tmp/dib_build.1CFJZpLz/hooks/dib-init-system:main:7                             :   set -o pipefail
2828: + /tmp/dib_build.1CFJZpLz/hooks/dib-init-system:main:9                             :   [[ -f /usr/bin/systemctl ]]
2829: + /tmp/dib_build.1CFJZpLz/hooks/dib-init-system:main:11                            :   [[ -f /sbin/initctl ]]
2830: + /tmp/dib_build.1CFJZpLz/hooks/dib-init-system:main:12                            :   echo upstart
2831: ++ /tmp/dib_build.1CFJZpLz/hooks/environment.d/14-manifests:source:21               :   set -eu
2832: ++ /tmp/dib_build.1CFJZpLz/hooks/environment.d/14-manifests:source:22               :   set -o pipefail
2833: ++ /tmp/dib_build.1CFJZpLz/hooks/environment.d/14-manifests:source:24               :   export DIB_MANIFEST_IMAGE_DIR=/etc/dib-manifests
2834: ++ /tmp/dib_build.1CFJZpLz/hooks/environment.d/14-manifests:source:24               :   DIB_MANIFEST_IMAGE_DIR=/etc/dib-manifests
2835: ++ /tmp/dib_build.1CFJZpLz/hooks/environment.d/14-manifests:source:25               :   export DIB_MANIFEST_SAVE_DIR=image.d/
2836: ++ /tmp/dib_build.1CFJZpLz/hooks/environment.d/14-manifests:source:25               :   DIB_MANIFEST_SAVE_DIR=image.d/
2837: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:source_environment:65         :   for env_file in '$env_files'
2838: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:source_environment:66         :   source /tmp/dib_build.1CFJZpLz/hooks/block-device.d/../environment.d/99-cloud-init-datasources.bash
2839: ++ /tmp/dib_build.1CFJZpLz/hooks/environment.d/99-cloud-init-datasources.bash:source:4 :   export DIB_CLOUD_INIT_DATASOURCES=Ec2
2840: ++ /tmp/dib_build.1CFJZpLz/hooks/environment.d/99-cloud-init-datasources.bash:source:4 :   DIB_CLOUD_INIT_DATASOURCES=Ec2
2841: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:108                      :   for target in '$targets'
2842: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:109                      :   output 'Running /tmp/dib_build.1CFJZpLz/hooks/block-device.d/10-partition'
2843: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:43                     :   output_prefix
2844: ++ /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   date
2845: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   printf '%s %s ' dib-run-parts '2016年 10月 03日 星期一 23:13:37 CST'
2846: dib-run-parts 2016年 10月 03日 星期一 23:13:37 CST + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:44                     :   echo Running /tmp/dib_build.1CFJZpLz/hooks/block-device.d/10-partition
2847: Running /tmp/dib_build.1CFJZpLz/hooks/block-device.d/10-partition
2848: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:110                      :   target_tag=10-partition
2849: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:111                      :   date +%s.%N
2850: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:112                      :   /tmp/dib_build.1CFJZpLz/hooks/block-device.d/10-partition
2851: + /tmp/dib_build.1CFJZpLz/hooks/block-device.d/10-partition:main:8                 :   set -eu
2852: + /tmp/dib_build.1CFJZpLz/hooks/block-device.d/10-partition:main:9                 :   set -o pipefail
2853: + /tmp/dib_build.1CFJZpLz/hooks/block-device.d/10-partition:main:11                :   '[' -n /dev/loop0 ']'
2854: + /tmp/dib_build.1CFJZpLz/hooks/block-device.d/10-partition:main:14                :   [[ amd64 =~ ppc ]]
2855: + /tmp/dib_build.1CFJZpLz/hooks/block-device.d/10-partition:main:22                :   sudo parted -a optimal -s /dev/loop0 mklabel msdos mkpart primary 1MiB 100% set 1 boot on
2856: + /tmp/dib_build.1CFJZpLz/hooks/block-device.d/10-partition:main:28                :   sudo partprobe /dev/loop0
2857: + /tmp/dib_build.1CFJZpLz/hooks/block-device.d/10-partition:main:31                :   sudo udevadm settle
2858: + /tmp/dib_build.1CFJZpLz/hooks/block-device.d/10-partition:main:34                :   DM=
2859: + /tmp/dib_build.1CFJZpLz/hooks/block-device.d/10-partition:main:35                :   '[' '!' -e /dev/loop0p1 ']'
2860: + /tmp/dib_build.1CFJZpLz/hooks/block-device.d/10-partition:main:45                :   [[ amd64 =~ ppc ]]
2861: + /tmp/dib_build.1CFJZpLz/hooks/block-device.d/10-partition:main:49                :   '[' -n '' ']'
2862: + /tmp/dib_build.1CFJZpLz/hooks/block-device.d/10-partition:main:51                :   [[ amd64 =~ ppc ]]
2863: + /tmp/dib_build.1CFJZpLz/hooks/block-device.d/10-partition:main:55                :   echo IMAGE_BLOCK_DEVICE=/dev/loop0p1
2864: IMAGE_BLOCK_DEVICE=/dev/loop0p1
2865: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:113                      :   target_tag=10-partition
2866: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:114                      :   date +%s.%N
2867: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:115                      :   output '10-partition completed'
2868: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:43                     :   output_prefix
2869: ++ /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   date
2870: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   printf '%s %s ' dib-run-parts '2016年 10月 03日 星期一 23:13:38 CST'
2871: dib-run-parts 2016年 10月 03日 星期一 23:13:38 CST + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:44                     :   echo 10-partition completed
2872: 10-partition completed
2873: dib-run-parts 2016年 10月 03日 星期一 23:13:38 CST ----------------------- PROFILING -----------------------
2874: dib-run-parts 2016年 10月 03日 星期一 23:13:38 CST
2875: dib-run-parts 2016年 10月 03日 星期一 23:13:38 CST Target: block-device.d
2876: dib-run-parts 2016年 10月 03日 星期一 23:13:38 CST
2877: dib-run-parts 2016年 10月 03日 星期一 23:13:38 CST Script                                     Seconds
2878: dib-run-parts 2016年 10月 03日 星期一 23:13:38 CST ---------------------------------------  ----------
2879: dib-run-parts 2016年 10月 03日 星期一 23:13:38 CST
2880: dib-run-parts Mon Oct  3 23:13:38 CST 2016 10-partition                                  0.293
2881: dib-run-parts 2016年 10月 03日 星期一 23:13:38 CST
2882: dib-run-parts 2016年 10月 03日 星期一 23:13:38 CST --------------------- END PROFILING ---------------------
2883: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:run_d:153 :   [[ 0 != 0 ]]
2884: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:run_d:160 :   check_break after-block-device bash
2885: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:check_break:98 :   egrep -e '(,|^)after-block-device(,|$)' -q
2886: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:check_break:98 :   echo ''
2887: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:eval_run_d:119 :   grep -q IMAGE_BLOCK_DEVICE= /tmp/tmp.SsHcH25KgJ
2888: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:eval_run_d:120 :   grep IMAGE_BLOCK_DEVICE= /tmp/tmp.SsHcH25KgJ
2889: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:eval_run_d:120 :   local temp=IMAGE_BLOCK_DEVICE=/dev/loop0p1
2890: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:eval_run_d:121 :   eval IMAGE_BLOCK_DEVICE=/dev/loop0p1
2891: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:eval_run_d:121 :   IMAGE_BLOCK_DEVICE=/dev/loop0p1
2892: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:eval_run_d:123 :   rm /tmp/tmp.SsHcH25KgJ
2893: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:eval_run_d:124 :   trap - ERR
2894: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:418                  :   sudo mkfs -i 4096 -J size=64 -t ext4 -L cloudimg-rootfs /dev/loop0p1
2895: mke2fs 1.42.13 (17-May-2015)
2896: Discarding device blocks:   4096/416512             done
2897: Creating filesystem with 416512 4k blocks and 416624 inodes
2898: Filesystem UUID: 82f90125-a3b0-4939-82e9-644bfde16d0b
2899: Superblock backups stored on blocks:
2900: 	32768, 98304, 163840, 229376, 294912
2901:
2902: Allocating group tables:  0/13     done
2903: Writing inode tables:  0/13     done
2904: Creating journal (16384 blocks): done
2905: Writing superblocks and filesystem accounting information:  0/13     done
2906:
2907: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:420                  :   echo ext4
2908: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:420                  :   grep -q '^ext'
2909: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:421                  :   sudo tune2fs -U f2413b58-3335-446c-9096-ca863816bc5b /dev/loop0p1
2910: tune2fs 1.42.13 (17-May-2015)
2911: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:423                  :   mkdir /tmp/dib_build.1CFJZpLz/mnt
2912: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:424                  :   sudo mount /dev/loop0p1 /tmp/dib_build.1CFJZpLz/mnt
2913: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:425                  :   sudo mv -t /tmp/dib_build.1CFJZpLz/mnt /tmp/dib_build.1CFJZpLz/built/bin /tmp/dib_build.1CFJZpLz/built/boot /tmp/dib_build.1CFJZpLz/built/dev /tmp/dib_build.1CFJZpLz/built/etc /tmp/dib_build.1CFJZpLz/built/home /tmp/dib_build.1CFJZpLz/built/initrd.img /tmp/dib_build.1CFJZpLz/built/lib /tmp/dib_build.1CFJZpLz/built/lib64 /tmp/dib_build.1CFJZpLz/built/media /tmp/dib_build.1CFJZpLz/built/mnt /tmp/dib_build.1CFJZpLz/built/opt /tmp/dib_build.1CFJZpLz/built/proc /tmp/dib_build.1CFJZpLz/built/root /tmp/dib_build.1CFJZpLz/built/run /tmp/dib_build.1CFJZpLz/built/sbin /tmp/dib_build.1CFJZpLz/built/srv /tmp/dib_build.1CFJZpLz/built/sys /tmp/dib_build.1CFJZpLz/built/tmp /tmp/dib_build.1CFJZpLz/built/usr /tmp/dib_build.1CFJZpLz/built/var /tmp/dib_build.1CFJZpLz/built/vmlinuz
2914: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:426                  :   mount_proc_dev_sys
2915: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:mount_proc_dev_sys:237 :   sudo mount -t proc none /tmp/dib_build.1CFJZpLz/mnt/proc
2916: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:mount_proc_dev_sys:238 :   sudo mount --bind /dev /tmp/dib_build.1CFJZpLz/mnt/dev
2917: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:mount_proc_dev_sys:239 :   sudo mount --bind /dev/pts /tmp/dib_build.1CFJZpLz/mnt/dev/pts
2918: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:mount_proc_dev_sys:240 :   sudo mount -t sysfs none /tmp/dib_build.1CFJZpLz/mnt/sys
2919: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:427                  :   run_d_in_target finalise
2920: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:72 :   check_element
2921: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:check_element:109 :   '[' -d /tmp/dib_build.1CFJZpLz/hooks ']'
2922: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:75 :   '[' -d /tmp/dib_build.1CFJZpLz/hooks/finalise.d ']'
2923: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:76 :   sudo mkdir /tmp/dib_build.1CFJZpLz/mnt/tmp/in_target.d
2924: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:77 :   sudo mount --bind /tmp/dib_build.1CFJZpLz/hooks /tmp/dib_build.1CFJZpLz/mnt/tmp/in_target.d
2925: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:78 :   sudo mount -o remount,ro,bind /tmp/dib_build.1CFJZpLz/hooks /tmp/dib_build.1CFJZpLz/mnt/tmp/in_target.d
2926: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:79 :   check_break before-finalise run_in_target bash
2927: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:check_break:98 :   egrep -e '(,|^)before-finalise(,|$)' -q
2928: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:check_break:98 :   echo ''
2929: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:80 :   '[' -z '' ']'
2930: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:80 :   in_target_arg=run_in_target
2931: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:81 :   trap 'check_break after-error run_in_target bash' ERR
2932: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:82 :   run_in_target dib-run-parts /tmp/in_target.d/finalise.d
2933: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_in_target:57 :   cmd='dib-run-parts /tmp/in_target.d/finalise.d'
2934: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_in_target:59 :   ORIG_HOME=/home/xion
2935: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_in_target:60 :   export HOME=/root
2936: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_in_target:60 :   HOME=/root
2937: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_in_target:66 :   sudo -E chroot /tmp/dib_build.1CFJZpLz/mnt env -u TMPDIR 'PATH=$PATH:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin' sh -c 'dib-run-parts /tmp/in_target.d/finalise.d'
2938: + set -eu
2939: + set -o pipefail
2940: + [[ -f /usr/bin/systemctl ]]
2941: + [[ -f /sbin/initctl ]]
2942: + echo upstart
2943: ++ set -eu
2944: ++ set -o pipefail
2945: ++ export DIB_MANIFEST_IMAGE_DIR=/etc/dib-manifests
2946: ++ DIB_MANIFEST_IMAGE_DIR=/etc/dib-manifests
2947: ++ export DIB_MANIFEST_SAVE_DIR=image.d/
2948: ++ DIB_MANIFEST_SAVE_DIR=image.d/
2949: + for env_file in '$env_files'
2950: + source /tmp/in_target.d/finalise.d/../environment.d/99-cloud-init-datasources.bash
2951: ++ export DIB_CLOUD_INIT_DATASOURCES=Ec2
2952: ++ DIB_CLOUD_INIT_DATASOURCES=Ec2
2953: + for target in '$targets'
2954: + output 'Running /tmp/in_target.d/finalise.d/50-bootloader'
2955: + output_prefix
2956: ++ date
2957: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:13:46 UTC 2016'
2958: dib-run-parts Mon Oct  3 15:13:46 UTC 2016 + echo Running /tmp/in_target.d/finalise.d/50-bootloader
2959: Running /tmp/in_target.d/finalise.d/50-bootloader
2960: + target_tag=50-bootloader
2961: + date +%s.%N
2962: + /tmp/in_target.d/finalise.d/50-bootloader
2963: + set -eu
2964: + set -o pipefail
2965: + '[' -n /dev/loop0p1 ']'
2966: + PART_DEV=/dev/loop0p1
2967: + [[ amd64 =~ ppc ]]
2968: ++ echo /dev/loop0p1
2969: ++ sed -e s#mapper/##
2970: ++ sed -e s#p1##
2971: + BOOT_DEV=/dev/loop0
2972: + DIB_EXTLINUX=0
2973: + '[' 0 '!=' 0 ']'
2974: + install_grub2
2975: + '[' -f /tmp/grub/install ']'
2976: + [[ amd64 =~ ppc ]]
2977: + install-packages -m bootloader grub-pc
2978: + set -eu
2979: + set -o pipefail
2980: + ACTION=install
2981: + MAP_ELEMENT=
2982: ++ basename /usr/local/bin/install-packages
2983: + SCRIPTNAME=install-packages
2984: ++ getopt -o hudem: -n install-packages -- -m bootloader grub-pc
2985: + TEMP=' -m '\''bootloader'\'' -- '\''grub-pc'\'''
2986: + '[' 0 '!=' 0 ']'
2987: + eval set -- ' -m '\''bootloader'\'' -- '\''grub-pc'\'''
2988: ++ set -- -m bootloader -- grub-pc
2989: + true
2990: + case "$1" in
2991: + MAP_ELEMENT=bootloader
2992: + shift 2
2993: + true
2994: + case "$1" in
2995: + shift
2996: + break
2997: + PKGS=grub-pc
2998: + '[' -n bootloader ']'
2999: ++ pkg-map --element bootloader grub-pc
3000: + PKGS=grub-pc
3001: + '[' -z grub-pc ']'
3002: + install_deb_packages install grub-pc
3003: + DEBIAN_FRONTEND=noninteractive
3004: + http_proxy=
3005: + https_proxy=
3006: + no_proxy=
3007: + apt-get --option Dpkg::Options::=--force-confold --option Dpkg::Options::=--force-confdef --assume-yes install grub-pc
3008: Reading package lists...
3009: Building dependency tree...
3010: Reading state information...
3011: The following extra packages will be installed:
3012:   grub-common grub-gfxpayload-lists grub-pc-bin grub2-common libfreetype6
3013: Suggested packages:
3014:   multiboot-doc grub-emu xorriso desktop-base
3015: Recommended packages:
3016:   os-prober
3017: The following NEW packages will be installed:
3018:   grub-common grub-gfxpayload-lists grub-pc grub-pc-bin grub2-common
3019:   libfreetype6
3020: 0 upgraded, 6 newly installed, 0 to remove and 0 not upgraded.
3021: Need to get 3543 kB of archives.
3022: After this operation, 17.3 MB of additional disk space will be used.
3023: Get:1 http://archive.ubuntu.com/ubuntu/ trusty-updates/main libfreetype6 amd64 2.5.2-1ubuntu2.5 [304 kB]
3024: Get:2 http://archive.ubuntu.com/ubuntu/ trusty-updates/main grub-common amd64 2.02~beta2-9ubuntu1.12 [1681 kB]
3025: Get:3 http://archive.ubuntu.com/ubuntu/ trusty-updates/main grub2-common amd64 2.02~beta2-9ubuntu1.12 [501 kB]
3026: Get:4 http://archive.ubuntu.com/ubuntu/ trusty-updates/main grub-pc-bin amd64 2.02~beta2-9ubuntu1.12 [880 kB]
3027: Get:5 http://archive.ubuntu.com/ubuntu/ trusty-updates/main grub-pc amd64 2.02~beta2-9ubuntu1.12 [173 kB]
3028: Get:6 http://archive.ubuntu.com/ubuntu/ trusty/main grub-gfxpayload-lists amd64 0.6 [3506 B]
3029: perl: warning: Setting locale failed.
3030: perl: warning: Please check that your locale settings:
3031: 	LANGUAGE = "en_US",
3032: 	LC_ALL = (unset),
3033: 	LC_TIME = "zh_CN.UTF-8",
3034: 	LC_MONETARY = "zh_CN.UTF-8",
3035: 	LC_CTYPE = "en_US.UTF-8",
3036: 	LC_ADDRESS = "zh_CN.UTF-8",
3037: 	LC_TELEPHONE = "zh_CN.UTF-8",
3038: 	LC_NAME = "zh_CN.UTF-8",
3039: 	LC_MEASUREMENT = "zh_CN.UTF-8",
3040: 	LC_IDENTIFICATION = "zh_CN.UTF-8",
3041: 	LC_NUMERIC = "zh_CN.UTF-8",
3042: 	LC_PAPER = "zh_CN.UTF-8",
3043: 	LANG = "C"
3044:     are supported and installed on your system.
3045: perl: warning: Falling back to the standard locale ("C").
3046: locale: Cannot set LC_ALL to default locale: No such file or directory
3047: Preconfiguring packages ...
3048: Fetched 3543 kB in 11s (306 kB/s)
3049: Selecting previously unselected package libfreetype6:amd64.
3050: (Reading database ... 31469 files and directories currently installed.)
3051: Preparing to unpack .../libfreetype6_2.5.2-1ubuntu2.5_amd64.deb ...
3052: Unpacking libfreetype6:amd64 (2.5.2-1ubuntu2.5) ...
3053: Selecting previously unselected package grub-common.
3054: Preparing to unpack .../grub-common_2.02~beta2-9ubuntu1.12_amd64.deb ...
3055: Unpacking grub-common (2.02~beta2-9ubuntu1.12) ...
3056: Selecting previously unselected package grub2-common.
3057: Preparing to unpack .../grub2-common_2.02~beta2-9ubuntu1.12_amd64.deb ...
3058: Unpacking grub2-common (2.02~beta2-9ubuntu1.12) ...
3059: Selecting previously unselected package grub-pc-bin.
3060: Preparing to unpack .../grub-pc-bin_2.02~beta2-9ubuntu1.12_amd64.deb ...
3061: Unpacking grub-pc-bin (2.02~beta2-9ubuntu1.12) ...
3062: Selecting previously unselected package grub-pc.
3063: Preparing to unpack .../grub-pc_2.02~beta2-9ubuntu1.12_amd64.deb ...
3064: Unpacking grub-pc (2.02~beta2-9ubuntu1.12) ...
3065: Selecting previously unselected package grub-gfxpayload-lists.
3066: Preparing to unpack .../grub-gfxpayload-lists_0.6_amd64.deb ...
3067: Unpacking grub-gfxpayload-lists (0.6) ...
3068: Processing triggers for ureadahead (0.100.0-16) ...
3069: Processing triggers for man-db (2.6.7.1-1ubuntu1) ...
3070: Processing triggers for install-info (5.2.0.dfsg.1-2) ...
3071: Setting up libfreetype6:amd64 (2.5.2-1ubuntu2.5) ...
3072: Setting up grub-common (2.02~beta2-9ubuntu1.12) ...
3073: runlevel:/var/run/utmp: No such file or directory
3074: invoke-rc.d: policy-rc.d denied execution of start.
3075: Processing triggers for ureadahead (0.100.0-16) ...
3076: Setting up grub2-common (2.02~beta2-9ubuntu1.12) ...
3077: Setting up grub-pc-bin (2.02~beta2-9ubuntu1.12) ...
3078: Setting up grub-gfxpayload-lists (0.6) ...
3079: Setting up grub-pc (2.02~beta2-9ubuntu1.12) ...
3080: locale: Cannot set LC_ALL to default locale: No such file or directory
3081:
3082: Creating config file /etc/default/grub with new version
3083: Generating grub configuration file ...
3084: Found linux image: /boot/vmlinuz-3.13.0-96-generic
3085: Found initrd image: /boot/initrd.img-3.13.0-96-generic
3086: done
3087: Processing triggers for libc-bin (2.19-0ubuntu6.9) ...
3088: ++ which grub-install
3089: + GRUBNAME=/usr/sbin/grub-install
3090: + '[' -z /usr/sbin/grub-install ']'
3091: + '[' -z /usr/sbin/grub-install ']'
3092: ++ /usr/sbin/grub-install --version
3093: ++ grep 0.97
3094: ++ wc -l
3095: + '[' 0 -ne 0 ']'
3096: + echo 'Installing GRUB2...'
3097: Installing GRUB2...
3098: + GRUB_OPTS=--force
3099: + [[ ! --force == *--target* ]]
3100: ++ /usr/sbin/grub-install --version
3101: + [[ /usr/sbin/grub-install (GRUB) 2.02~beta2-9ubuntu1.12 =~  2\. ]]
3102: + '[' -d /sys/firmware/efi ']'
3103: + [[ amd64 =~ ppc ]]
3104: + /usr/sbin/grub-install '--modules=biosdisk part_msdos' --force /dev/loop0
3105: Installing for i386-pc platform.
3106: Installation finished. No error reported.
3107: + '[' -d /boot/grub2 ']'
3108: + '[' -d /boot/grub ']'
3109: + GRUB_CFG=/boot/grub/grub.cfg
3110: + echo 'GRUB_TERMINAL="serial console"'
3111: + echo GRUB_GFXPAYLOAD_LINUX=text
3112: + echo 'GRUB_CMDLINE_LINUX_DEFAULT="console=tty0 console=ttyS0,115200 no_timer_check"'
3113: + echo 'GRUB_SERIAL_COMMAND="serial --speed=115200 --unit=0 --word=8 --parity=no --stop=1"'
3114: + which grub2-mkconfig
3115: + GRUB_MKCONFIG='grub-mkconfig -o /boot/grub/grub.cfg'
3116: + DISTRO_NAME=ubuntu
3117: + case $DISTRO_NAME in
3118: + sed -i -e 's/\(^GRUB_CMDLINE_LINUX.*\)"$/\1 nofb nomodeset vga=normal"/' /etc/default/grub
3119: + GRUB_MKCONFIG=update-grub
3120: + PROBER_DISABLED=
3121: + grep -qe '^\s*GRUB_DISABLE_OS_PROBER=true' /etc/default/grub
3122: + PROBER_DISABLED=true
3123: + echo GRUB_DISABLE_OS_PROBER=true
3124: + update-grub
3125: Generating grub configuration file ...
3126: Found linux image: /boot/vmlinuz-3.13.0-96-generic
3127: Found initrd image: /boot/initrd.img-3.13.0-96-generic
3128: done
3129: + '[' -n true ']'
3130: + sed -i '$d' /etc/default/grub
3131: + DIB_RELEASE=trusty
3132: + '[' trusty = precise ']'
3133: + '[' trusty = wheezy ']'
3134: + sed -i s%/dev/loop0p1%LABEL=cloudimg-rootfs% /boot/grub/grub.cfg
3135: + sed -i 's%search --no-floppy --fs-uuid --set=root .*$%search --no-floppy --set=root --label cloudimg-rootfs%' /boot/grub/grub.cfg
3136: + sed -i 's%root=UUID=[A-Za-z0-9\-]*%root=LABEL=cloudimg-rootfs%' /boot/grub/grub.cfg
3137: + '[' ubuntu = fedora ']'
3138: + '[' -d /sys/firmware/efi ']'
3139: + target_tag=50-bootloader
3140: + date +%s.%N
3141: + output '50-bootloader completed'
3142: + output_prefix
3143: ++ date
3144: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:14:02 UTC 2016'
3145: dib-run-parts Mon Oct  3 15:14:02 UTC 2016 + echo 50-bootloader completed
3146: 50-bootloader completed
3147: + for target in '$targets'
3148: + output 'Running /tmp/in_target.d/finalise.d/50-remove-bogus-udev-links'
3149: + output_prefix
3150: ++ date
3151: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:14:02 UTC 2016'
3152: dib-run-parts Mon Oct  3 15:14:02 UTC 2016 + echo Running /tmp/in_target.d/finalise.d/50-remove-bogus-udev-links
3153: Running /tmp/in_target.d/finalise.d/50-remove-bogus-udev-links
3154: + target_tag=50-remove-bogus-udev-links
3155: + date +%s.%N
3156: + /tmp/in_target.d/finalise.d/50-remove-bogus-udev-links
3157: + set -eu
3158: + set -o pipefail
3159: + '[' ubuntu = opensuse ']'
3160: + target_tag=50-remove-bogus-udev-links
3161: + date +%s.%N
3162: + output '50-remove-bogus-udev-links completed'
3163: + output_prefix
3164: ++ date
3165: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:14:02 UTC 2016'
3166: dib-run-parts Mon Oct  3 15:14:02 UTC 2016 + echo 50-remove-bogus-udev-links completed
3167: 50-remove-bogus-udev-links completed
3168: + for target in '$targets'
3169: + output 'Running /tmp/in_target.d/finalise.d/99-clean-up-cache'
3170: + output_prefix
3171: ++ date
3172: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:14:02 UTC 2016'
3173: dib-run-parts Mon Oct  3 15:14:02 UTC 2016 + echo Running /tmp/in_target.d/finalise.d/99-clean-up-cache
3174: Running /tmp/in_target.d/finalise.d/99-clean-up-cache
3175: + target_tag=99-clean-up-cache
3176: + date +%s.%N
3177: + /tmp/in_target.d/finalise.d/99-clean-up-cache
3178: + set -eu
3179: + set -o pipefail
3180: + '[' 0 '!=' 1 ']'
3181: + apt-get clean
3182: + target_tag=99-clean-up-cache
3183: + date +%s.%N
3184: + output '99-clean-up-cache completed'
3185: + output_prefix
3186: ++ date
3187: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:14:02 UTC 2016'
3188: dib-run-parts Mon Oct  3 15:14:02 UTC 2016 + echo 99-clean-up-cache completed
3189: 99-clean-up-cache completed
3190: + for target in '$targets'
3191: + output 'Running /tmp/in_target.d/finalise.d/99-write-dpkg-manifest'
3192: + output_prefix
3193: ++ date
3194: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:14:02 UTC 2016'
3195: dib-run-parts Mon Oct  3 15:14:02 UTC 2016 + echo Running /tmp/in_target.d/finalise.d/99-write-dpkg-manifest
3196: Running /tmp/in_target.d/finalise.d/99-write-dpkg-manifest
3197: + target_tag=99-write-dpkg-manifest
3198: + date +%s.%N
3199: + /tmp/in_target.d/finalise.d/99-write-dpkg-manifest
3200: + set -eu
3201: + set -o pipefail
3202: ++ basename image
3203: + DPKG_MANIFEST_NAME=dib-manifest-dpkg-image
3204: + echo '{"packages": ['
3205: + format='{"package": "${binary:Package}","arch": "${Architecture}","version": "${Version}","status": "${db:Status-Abbrev}"},'
3206: + dpkg-query --show '--showformat={"package": "${binary:Package}","arch": "${Architecture}","version": "${Version}","status": "${db:Status-Abbrev}"},'
3207: + tee -a /etc/dib-manifests/dib-manifest-dpkg-image
3208: {"package": "accountsservice","arch": "amd64","version": "0.6.35-0ubuntu7.2","status": "ii "},{"package": "acpid","arch": "amd64","version": "1:2.0.21-1ubuntu2","status": "ii "},{"package": "adduser","arch": "all","version": "3.113+nmu3ubuntu3","status": "ii "},{"package": "apparmor","arch": "amd64","version": "2.8.95~2430-0ubuntu5.3","status": "ii "},{"package": "apport","arch": "all","version": "2.14.1-0ubuntu3.21","status": "ii "},{"package": "apport-symptoms","arch": "all","version": "0.20","status": "ii "},{"package": "apt","arch": "amd64","version": "1.0.1ubuntu2.14","status": "ii "},{"package": "apt-transport-https","arch": "amd64","version": "1.0.1ubuntu2.14","status": "ii "},{"package": "apt-utils","arch": "amd64","version": "1.0.1ubuntu2.14","status": "ii "},{"package": "apt-xapian-index","arch": "all","version": "0.45ubuntu4","status": "rc "},{"package": "aptitude","arch": "amd64","version": "0.6.8.2-1ubuntu4","status": "ii "},{"package": "aptitude-common","arch": "all","version": "0.6.8.2-1ubuntu4","status": "ii "},{"package": "at","arch": "amd64","version": "3.1.14-1ubuntu1","status": "ii "},{"package": "base-files","arch": "amd64","version": "7.2ubuntu5.5","status": "ii "},{"package": "base-passwd","arch": "amd64","version": "3.5.33","status": "ii "},{"package": "bash","arch": "amd64","version": "4.3-7ubuntu1.5","status": "ii "},{"package": "bash-completion","arch": "all","version": "1:2.1-4ubuntu0.2","status": "ii "},{"package": "bc","arch": "amd64","version": "1.06.95-8ubuntu1","status": "ii "},{"package": "bind9-host","arch": "amd64","version": "1:9.9.5.dfsg-3ubuntu0.9","status": "ii "},{"package": "binutils","arch": "amd64","version": "2.24-5ubuntu14.1","status": "ii "},{"package": "bsdmainutils","arch": "amd64","version": "9.0.5ubuntu1","status": "ii "},{"package": "bsdutils","arch": "amd64","version": "1:2.20.1-5.1ubuntu20.7","status": "ii "},{"package": "busybox-initramfs","arch": "amd64","version": "1:1.21.0-1ubuntu1","status": "ii "},{"package": "busybox-static","arch": "amd64","version": "1:1.21.0-1ubuntu1","status": "ii "},{"package": "byobu","arch": "all","version": "5.77-0ubuntu1.2","status": "ii "},{"package": "bzip2","arch": "amd64","version": "1.0.6-5","status": "ii "},{"package": "ca-certificates","arch": "all","version": "20160104ubuntu0.14.04.1","status": "ii "},{"package": "ccache","arch": "amd64","version": "3.1.9-1","status": "ii "},{"package": "cloud-guest-utils","arch": "all","version": "0.27-0ubuntu9.2","status": "ii "},{"package": "cloud-init","arch": "all","version": "0.7.5-0ubuntu1.20","status": "ii "},{"package": "command-not-found","arch": "all","version": "0.3ubuntu12","status": "ii "},{"package": "command-not-found-data","arch": "amd64","version": "0.3ubuntu12","status": "ii "},{"package": "console-setup","arch": "all","version": "1.70ubuntu8","status": "ii "},{"package": "coreutils","arch": "amd64","version": "8.21-1ubuntu5.4","status": "ii "},{"package": "cpio","arch": "amd64","version": "2.11+dfsg-1ubuntu1.2","status": "ii "},{"package": "cpp","arch": "amd64","version": "4:4.8.2-1ubuntu6","status": "ii "},{"package": "cpp-4.8","arch": "amd64","version": "4.8.4-2ubuntu1~14.04.3","status": "ii "},{"package": "crda","arch": "amd64","version": "1.1.2-1ubuntu2","status": "ii "},{"package": "cron","arch": "amd64","version": "3.0pl1-124ubuntu2","status": "ii "},{"package": "cryptsetup","arch": "amd64","version": "2:1.6.1-1ubuntu1","status": "ii "},{"package": "cryptsetup-bin","arch": "amd64","version": "2:1.6.1-1ubuntu1","status": "ii "},{"package": "curl","arch": "amd64","version": "7.35.0-1ubuntu2.9","status": "ii "},{"package": "dash","arch": "amd64","version": "0.5.7-4ubuntu1","status": "ii "},{"package": "dbus","arch": "amd64","version": "1.6.18-0ubuntu4.3","status": "ii "},{"package": "debconf","arch": "all","version": "1.5.51ubuntu2","status": "ii "},{"package": "debconf-i18n","arch": "all","version": "1.5.51ubuntu2","status": "ii "},{"package": "debianutils","arch": "amd64","version": "4.4","status": "ii "},{"package": "dh-python","arch": "all","version": "1.20140128-1ubuntu8.2","status": "ii "},{"package": "diffutils","arch": "amd64","version": "1:3.3-1","status": "ii "},{"package": "dkms","arch": "all","version": "2.2.0.3-1.1ubuntu5.14.04.8","status": "ii "},{"package": "dmidecode","arch": "amd64","version": "2.12-2","status": "ii "},{"package": "dmsetup","arch": "amd64","version": "2:1.02.77-6ubuntu2","status": "ii "},{"package": "dnsutils","arch": "amd64","version": "1:9.9.5.dfsg-3ubuntu0.9","status": "ii "},{"package": "dosfstools","arch": "amd64","version": "3.0.26-1ubuntu0.1","status": "ii "},{"package": "dpkg","arch": "amd64","version": "1.17.5ubuntu5.7","status": "ii "},{"package": "e2fslibs:amd64","arch": "amd64","version": "1.42.9-3ubuntu1.3","status": "ii "},{"package": "e2fsprogs","arch": "amd64","version": "1.42.9-3ubuntu1.3","status": "ii "},{"package": "eatmydata","arch": "amd64","version": "26-2","status": "ii "},{"package": "ed","arch": "amd64","version": "1.9-2","status": "ii "},{"package": "eject","arch": "amd64","version": "2.1.5+deb1+cvs20081104-13.1","status": "ii "},{"package": "ethtool","arch": "amd64","version": "1:3.13-1","status": "ii "},{"package": "file","arch": "amd64","version": "1:5.14-2ubuntu3.3","status": "ii "},{"package": "findutils","arch": "amd64","version": "4.4.2-7","status": "ii "},{"package": "fonts-ubuntu-font-family-console","arch": "all","version": "0.80-0ubuntu6","status": "ii "},{"package": "friendly-recovery","arch": "all","version": "0.2.25","status": "ii "},{"package": "ftp","arch": "amd64","version": "0.17-28","status": "ii "},{"package": "fuse","arch": "amd64","version": "2.9.2-4ubuntu4.14.04.1","status": "ii "},{"package": "gawk","arch": "amd64","version": "1:4.0.1+dfsg-2.1ubuntu2","status": "ii "},{"package": "gcc","arch": "amd64","version": "4:4.8.2-1ubuntu6","status": "ii "},{"package": "gcc-4.8","arch": "amd64","version": "4.8.4-2ubuntu1~14.04.3","status": "ii "},{"package": "gcc-4.8-base:amd64","arch": "amd64","version": "4.8.4-2ubuntu1~14.04.3","status": "ii "},{"package": "gcc-4.9-base:amd64","arch": "amd64","version": "4.9.3-0ubuntu4","status": "ii "},{"package": "gdisk","arch": "amd64","version": "0.8.8-1ubuntu0.1","status": "ii "},{"package": "geoip-database","arch": "all","version": "20140313-1","status": "ii "},{"package": "gettext-base","arch": "amd64","version": "0.18.3.1-1ubuntu3","status": "ii "},{"package": "gir1.2-glib-2.0","arch": "amd64","version": "1.40.0-1ubuntu0.2","status": "ii "},{"package": "gnupg","arch": "amd64","version": "1.4.16-1ubuntu2.4","status": "ii "},{"package": "gpgv","arch": "amd64","version": "1.4.16-1ubuntu2.4","status": "ii "},{"package": "grep","arch": "amd64","version": "2.16-1","status": "ii "},{"package": "groff-base","arch": "amd64","version": "1.22.2-5","status": "ii "},{"package": "grub-common","arch": "amd64","version": "2.02~beta2-9ubuntu1.12","status": "ii "},{"package": "grub-gfxpayload-lists","arch": "amd64","version": "0.6","status": "ii "},{"package": "grub-pc","arch": "amd64","version": "2.02~beta2-9ubuntu1.12","status": "ii "},{"package": "grub-pc-bin","arch": "amd64","version": "2.02~beta2-9ubuntu1.12","status": "ii "},{"package": "grub2-common","arch": "amd64","version": "2.02~beta2-9ubuntu1.12","status": "ii "},{"package": "gzip","arch": "amd64","version": "1.6-3ubuntu1","status": "ii "},{"package": "hdparm","arch": "amd64","version": "9.43-1ubuntu3","status": "ii "},{"package": "hostname","arch": "amd64","version": "3.15ubuntu1","status": "ii "},{"package": "ifupdown","arch": "amd64","version": "0.7.47.2ubuntu4.4","status": "ii "},{"package": "info","arch": "amd64","version": "5.2.0.dfsg.1-2","status": "ii "},{"package": "init-system-helpers","arch": "all","version": "1.14","status": "ii "},{"package": "initramfs-tools","arch": "all","version": "0.103ubuntu4.4","status": "ii "},{"package": "initramfs-tools-bin","arch": "amd64","version": "0.103ubuntu4.4","status": "ii "},{"package": "initscripts","arch": "amd64","version": "2.88dsf-41ubuntu6.3","status": "ii "},{"package": "insserv","arch": "amd64","version": "1.14.0-5ubuntu2","status": "ii "},{"package": "install-info","arch": "amd64","version": "5.2.0.dfsg.1-2","status": "ii "},{"package": "iproute2","arch": "amd64","version": "3.12.0-2ubuntu1","status": "ii "},{"package": "iptables","arch": "amd64","version": "1.4.21-1ubuntu1","status": "ii "},{"package": "iputils-ping","arch": "amd64","version": "3:20121221-4ubuntu1.1","status": "ii "},{"package": "iputils-tracepath","arch": "amd64","version": "3:20121221-4ubuntu1.1","status": "ii "},{"package": "irqbalance","arch": "amd64","version": "1.0.6-2ubuntu0.14.04.4","status": "ii "},{"package": "isc-dhcp-client","arch": "amd64","version": "4.2.4-7ubuntu12.7","status": "ii "},{"package": "isc-dhcp-common","arch": "amd64","version": "4.2.4-7ubuntu12.7","status": "ii "},{"package": "iso-codes","arch": "all","version": "3.52-1","status": "ii "},{"package": "kbd","arch": "amd64","version": "1.15.5-1ubuntu1","status": "ii "},{"package": "keyboard-configuration","arch": "all","version": "1.70ubuntu8","status": "ii "},{"package": "klibc-utils","arch": "amd64","version": "2.0.3-0ubuntu1.14.04.1","status": "ii "},{"package": "kmod","arch": "amd64","version": "15-0ubuntu6","status": "ii "},{"package": "krb5-locales","arch": "all","version": "1.12+dfsg-2ubuntu5.2","status": "ii "},{"package": "landscape-client","arch": "amd64","version": "14.12-0ubuntu0.14.04","status": "ii "},{"package": "landscape-common","arch": "amd64","version": "14.12-0ubuntu0.14.04","status": "ii "},{"package": "language-selector-common","arch": "all","version": "0.129.3","status": "ii "},{"package": "laptop-detect","arch": "amd64","version": "0.13.7ubuntu2","status": "ii "},{"package": "less","arch": "amd64","version": "458-2","status": "ii "},{"package": "libaccountsservice0:amd64","arch": "amd64","version": "0.6.35-0ubuntu7.2","status": "ii "},{"package": "libacl1:amd64","arch": "amd64","version": "2.2.52-1","status": "ii "},{"package": "libapparmor-perl","arch": "amd64","version": "2.8.95~2430-0ubuntu5.3","status": "ii "},{"package": "libapparmor1:amd64","arch": "amd64","version": "2.8.95~2430-0ubuntu5.3","status": "ii "},{"package": "libapt-inst1.5:amd64","arch": "amd64","version": "1.0.1ubuntu2.14","status": "ii "},{"package": "libapt-pkg4.12:amd64","arch": "amd64","version": "1.0.1ubuntu2.14","status": "ii "},{"package": "libarchive-extract-perl","arch": "all","version": "0.70-1","status": "ii "},{"package": "libasan0:amd64","arch": "amd64","version": "4.8.4-2ubuntu1~14.04.3","status": "ii "},{"package": "libasn1-8-heimdal:amd64","arch": "amd64","version": "1.6~git20131207+dfsg-1ubuntu1.1","status": "ii "},{"package": "libasprintf0c2:amd64","arch": "amd64","version": "0.18.3.1-1ubuntu3","status": "ii "},{"package": "libatomic1:amd64","arch": "amd64","version": "4.8.4-2ubuntu1~14.04.3","status": "ii "},{"package": "libattr1:amd64","arch": "amd64","version": "1:2.4.47-1ubuntu1","status": "ii "},{"package": "libaudit-common","arch": "all","version": "1:2.3.2-2ubuntu1","status": "ii "},{"package": "libaudit1:amd64","arch": "amd64","version": "1:2.3.2-2ubuntu1","status": "ii "},{"package": "libbind9-90","arch": "amd64","version": "1:9.9.5.dfsg-3ubuntu0.9","status": "ii "},{"package": "libblkid1:amd64","arch": "amd64","version": "2.20.1-5.1ubuntu20.7","status": "ii "},{"package": "libboost-iostreams1.54.0:amd64","arch": "amd64","version": "1.54.0-4ubuntu3.1","status": "ii "},{"package": "libbsd0:amd64","arch": "amd64","version": "0.6.0-2ubuntu1","status": "ii "},{"package": "libbz2-1.0:amd64","arch": "amd64","version": "1.0.6-5","status": "ii "},{"package": "libc-bin","arch": "amd64","version": "2.19-0ubuntu6.9","status": "ii "},{"package": "libc6:amd64","arch": "amd64","version": "2.19-0ubuntu6.9","status": "ii "},{"package": "libcap-ng0","arch": "amd64","version": "0.7.3-1ubuntu2","status": "ii "},{"package": "libcap2:amd64","arch": "amd64","version": "1:2.24-0ubuntu2","status": "ii "},{"package": "libcap2-bin","arch": "amd64","version": "1:2.24-0ubuntu2","status": "ii "},{"package": "libcgmanager0:amd64","arch": "amd64","version": "0.24-0ubuntu7.5","status": "ii "},{"package": "libck-connector0:amd64","arch": "amd64","version": "0.4.5-3.1ubuntu2","status": "ii "},{"package": "libclass-accessor-perl","arch": "all","version": "0.34-1","status": "ii "},{"package": "libcloog-isl4:amd64","arch": "amd64","version": "0.18.2-1","status": "ii "},{"package": "libcomerr2:amd64","arch": "amd64","version": "1.42.9-3ubuntu1.3","status": "ii "},{"package": "libcryptsetup4","arch": "amd64","version": "2:1.6.1-1ubuntu1","status": "ii "},{"package": "libcurl3:amd64","arch": "amd64","version": "7.35.0-1ubuntu2.9","status": "ii "},{"package": "libcurl3-gnutls:amd64","arch": "amd64","version": "7.35.0-1ubuntu2.9","status": "ii "},{"package": "libcwidget3","arch": "amd64","version": "0.5.16-3.5ubuntu1","status": "ii "},{"package": "libdb5.3:amd64","arch": "amd64","version": "5.3.28-3ubuntu3","status": "ii "},{"package": "libdbus-1-3:amd64","arch": "amd64","version": "1.6.18-0ubuntu4.3","status": "ii "},{"package": "libdbus-glib-1-2:amd64","arch": "amd64","version": "0.100.2-1","status": "ii "},{"package": "libdebconfclient0:amd64","arch": "amd64","version": "0.187ubuntu1","status": "ii "},{"package": "libdevmapper1.02.1:amd64","arch": "amd64","version": "2:1.02.77-6ubuntu2","status": "ii "},{"package": "libdns100","arch": "amd64","version": "1:9.9.5.dfsg-3ubuntu0.9","status": "ii "},{"package": "libdrm2:amd64","arch": "amd64","version": "2.4.67-1ubuntu0.14.04.1","status": "ii "},{"package": "libdumbnet1","arch": "amd64","version": "1.12-4build1","status": "ii "},{"package": "libedit2:amd64","arch": "amd64","version": "3.1-20130712-2","status": "ii "},{"package": "libelf1:amd64","arch": "amd64","version": "0.158-0ubuntu5.2","status": "ii "},{"package": "libept1.4.12:amd64","arch": "amd64","version": "1.0.12","status": "ii "},{"package": "libestr0","arch": "amd64","version": "0.1.9-0ubuntu2","status": "ii "},{"package": "libevent-2.0-5:amd64","arch": "amd64","version": "2.0.21-stable-1ubuntu1.14.04.1","status": "ii "},{"package": "libexpat1:amd64","arch": "amd64","version": "2.1.0-4ubuntu1.3","status": "ii "},{"package": "libffi6:amd64","arch": "amd64","version": "3.1~rc1+r3.0.13-12ubuntu0.1","status": "ii "},{"package": "libfreetype6:amd64","arch": "amd64","version": "2.5.2-1ubuntu2.5","status": "ii "},{"package": "libfribidi0:amd64","arch": "amd64","version": "0.19.6-1","status": "ii "},{"package": "libfuse2:amd64","arch": "amd64","version": "2.9.2-4ubuntu4.14.04.1","status": "ii "},{"package": "libgc1c2:amd64","arch": "amd64","version": "1:7.2d-5ubuntu2","status": "ii "},{"package": "libgcc-4.8-dev:amd64","arch": "amd64","version": "4.8.4-2ubuntu1~14.04.3","status": "ii "},{"package": "libgcc1:amd64","arch": "amd64","version": "1:4.9.3-0ubuntu4","status": "ii "},{"package": "libgck-1-0:amd64","arch": "amd64","version": "3.10.1-1","status": "ii "},{"package": "libgcr-3-common","arch": "all","version": "3.10.1-1","status": "ii "},{"package": "libgcr-base-3-1:amd64","arch": "amd64","version": "3.10.1-1","status": "ii "},{"package": "libgcrypt11:amd64","arch": "amd64","version": "1.5.3-2ubuntu4.4","status": "ii "},{"package": "libgdbm3:amd64","arch": "amd64","version": "1.8.3-12build1","status": "ii "},{"package": "libgeoip1:amd64","arch": "amd64","version": "1.6.0-1","status": "ii "},{"package": "libgirepository-1.0-1","arch": "amd64","version": "1.40.0-1ubuntu0.2","status": "ii "},{"package": "libglib2.0-0:amd64","arch": "amd64","version": "2.40.2-0ubuntu1","status": "ii "},{"package": "libglib2.0-data","arch": "all","version": "2.40.2-0ubuntu1","status": "ii "},{"package": "libgmp10:amd64","arch": "amd64","version": "2:5.1.3+dfsg-1ubuntu1","status": "ii "},{"package": "libgnutls-openssl27:amd64","arch": "amd64","version": "2.12.23-12ubuntu2.5","status": "ii "},{"package": "libgnutls26:amd64","arch": "amd64","version": "2.12.23-12ubuntu2.5","status": "ii "},{"package": "libgomp1:amd64","arch": "amd64","version": "4.8.4-2ubuntu1~14.04.3","status": "ii "},{"package": "libgpg-error0:amd64","arch": "amd64","version": "1.12-0.2ubuntu1","status": "ii "},{"package": "libgpm2:amd64","arch": "amd64","version": "1.20.4-6.1","status": "ii "},{"package": "libgssapi-krb5-2:amd64","arch": "amd64","version": "1.12+dfsg-2ubuntu5.2","status": "ii "},{"package": "libgssapi3-heimdal:amd64","arch": "amd64","version": "1.6~git20131207+dfsg-1ubuntu1.1","status": "ii "},{"package": "libhcrypto4-heimdal:amd64","arch": "amd64","version": "1.6~git20131207+dfsg-1ubuntu1.1","status": "ii "},{"package": "libheimbase1-heimdal:amd64","arch": "amd64","version": "1.6~git20131207+dfsg-1ubuntu1.1","status": "ii "},{"package": "libheimntlm0-heimdal:amd64","arch": "amd64","version": "1.6~git20131207+dfsg-1ubuntu1.1","status": "ii "},{"package": "libhx509-5-heimdal:amd64","arch": "amd64","version": "1.6~git20131207+dfsg-1ubuntu1.1","status": "ii "},{"package": "libicu52:amd64","arch": "amd64","version": "52.1-3ubuntu0.4","status": "ii "},{"package": "libidn11:amd64","arch": "amd64","version": "1.28-1ubuntu2.1","status": "ii "},{"package": "libio-string-perl","arch": "all","version": "1.08-3","status": "ii "},{"package": "libisc95","arch": "amd64","version": "1:9.9.5.dfsg-3ubuntu0.9","status": "ii "},{"package": "libisccc90","arch": "amd64","version": "1:9.9.5.dfsg-3ubuntu0.9","status": "ii "},{"package": "libisccfg90","arch": "amd64","version": "1:9.9.5.dfsg-3ubuntu0.9","status": "ii "},{"package": "libisl10:amd64","arch": "amd64","version": "0.12.2-1","status": "ii "},{"package": "libitm1:amd64","arch": "amd64","version": "4.8.4-2ubuntu1~14.04.3","status": "ii "},{"package": "libjson-c2:amd64","arch": "amd64","version": "0.11-3ubuntu1.2","status": "ii "},{"package": "libjson0:amd64","arch": "amd64","version": "0.11-3ubuntu1.2","status": "ii "},{"package": "libk5crypto3:amd64","arch": "amd64","version": "1.12+dfsg-2ubuntu5.2","status": "ii "},{"package": "libkeyutils1:amd64","arch": "amd64","version": "1.5.6-1","status": "ii "},{"package": "libklibc","arch": "amd64","version": "2.0.3-0ubuntu1.14.04.1","status": "ii "},{"package": "libkmod2:amd64","arch": "amd64","version": "15-0ubuntu6","status": "ii "},{"package": "libkrb5-26-heimdal:amd64","arch": "amd64","version": "1.6~git20131207+dfsg-1ubuntu1.1","status": "ii "},{"package": "libkrb5-3:amd64","arch": "amd64","version": "1.12+dfsg-2ubuntu5.2","status": "ii "},{"package": "libkrb5support0:amd64","arch": "amd64","version": "1.12+dfsg-2ubuntu5.2","status": "ii "},{"package": "libldap-2.4-2:amd64","arch": "amd64","version": "2.4.31-1+nmu2ubuntu8.3","status": "ii "},{"package": "liblocale-gettext-perl","arch": "amd64","version": "1.05-7build3","status": "ii "},{"package": "liblockfile-bin","arch": "amd64","version": "1.09-6ubuntu1","status": "ii "},{"package": "liblockfile1:amd64","arch": "amd64","version": "1.09-6ubuntu1","status": "ii "},{"package": "liblog-message-simple-perl","arch": "all","version": "0.10-1","status": "ii "},{"package": "liblwres90","arch": "amd64","version": "1:9.9.5.dfsg-3ubuntu0.9","status": "ii "},{"package": "liblzma5:amd64","arch": "amd64","version": "5.1.1alpha+20120614-2ubuntu2","status": "ii "},{"package": "libmagic1:amd64","arch": "amd64","version": "1:5.14-2ubuntu3.3","status": "ii "},{"package": "libmodule-pluggable-perl","arch": "all","version": "5.1-1","status": "ii "},{"package": "libmount1:amd64","arch": "amd64","version": "2.20.1-5.1ubuntu20.7","status": "ii "},{"package": "libmpc3:amd64","arch": "amd64","version": "1.0.1-1ubuntu1","status": "ii "},{"package": "libmpdec2:amd64","arch": "amd64","version": "2.4.0-6","status": "ii "},{"package": "libmpfr4:amd64","arch": "amd64","version": "3.1.2-1","status": "ii "},{"package": "libncurses5:amd64","arch": "amd64","version": "5.9+20140118-1ubuntu1","status": "ii "},{"package": "libncursesw5:amd64","arch": "amd64","version": "5.9+20140118-1ubuntu1","status": "ii "},{"package": "libnewt0.52:amd64","arch": "amd64","version": "0.52.15-2ubuntu5","status": "ii "},{"package": "libnfnetlink0:amd64","arch": "amd64","version": "1.0.1-2","status": "ii "},{"package": "libnih-dbus1:amd64","arch": "amd64","version": "1.0.3-4ubuntu25","status": "ii "},{"package": "libnih1:amd64","arch": "amd64","version": "1.0.3-4ubuntu25","status": "ii "},{"package": "libnl-3-200:amd64","arch": "amd64","version": "3.2.21-1ubuntu3","status": "ii "},{"package": "libnl-genl-3-200:amd64","arch": "amd64","version": "3.2.21-1ubuntu3","status": "ii "},{"package": "libnuma1:amd64","arch": "amd64","version": "2.0.9~rc5-1ubuntu3.14.04.2","status": "ii "},{"package": "libp11-kit0:amd64","arch": "amd64","version": "0.20.2-2ubuntu2","status": "ii "},{"package": "libpam-cap:amd64","arch": "amd64","version": "1:2.24-0ubuntu2","status": "ii "},{"package": "libpam-modules:amd64","arch": "amd64","version": "1.1.8-1ubuntu2.2","status": "ii "},{"package": "libpam-modules-bin","arch": "amd64","version": "1.1.8-1ubuntu2.2","status": "ii "},{"package": "libpam-runtime","arch": "all","version": "1.1.8-1ubuntu2.2","status": "ii "},{"package": "libpam-systemd:amd64","arch": "amd64","version": "204-5ubuntu20.19","status": "ii "},{"package": "libpam0g:amd64","arch": "amd64","version": "1.1.8-1ubuntu2.2","status": "ii "},{"package": "libparse-debianchangelog-perl","arch": "all","version": "1.2.0-1ubuntu1","status": "ii "},{"package": "libparted0debian1:amd64","arch": "amd64","version": "2.3-19ubuntu1.14.04.1","status": "ii "},{"package": "libpcap0.8:amd64","arch": "amd64","version": "1.5.3-2","status": "ii "},{"package": "libpci3:amd64","arch": "amd64","version": "1:3.2.1-1ubuntu5.1","status": "ii "},{"package": "libpcre3:amd64","arch": "amd64","version": "1:8.31-2ubuntu2.3","status": "ii "},{"package": "libpipeline1:amd64","arch": "amd64","version": "1.3.0-1","status": "ii "},{"package": "libplymouth2:amd64","arch": "amd64","version": "0.8.8-0ubuntu17.1","status": "ii "},{"package": "libpng12-0:amd64","arch": "amd64","version": "1.2.50-1ubuntu2.14.04.2","status": "ii "},{"package": "libpod-latex-perl","arch": "all","version": "0.61-1","status": "ii "},{"package": "libpolkit-agent-1-0:amd64","arch": "amd64","version": "0.105-4ubuntu3.14.04.1","status": "ii "},{"package": "libpolkit-backend-1-0:amd64","arch": "amd64","version": "0.105-4ubuntu3.14.04.1","status": "ii "},{"package": "libpolkit-gobject-1-0:amd64","arch": "amd64","version": "0.105-4ubuntu3.14.04.1","status": "ii "},{"package": "libpopt0:amd64","arch": "amd64","version": "1.16-8ubuntu1","status": "ii "},{"package": "libprocps3:amd64","arch": "amd64","version": "1:3.3.9-1ubuntu2.2","status": "ii "},{"package": "libpython-stdlib:amd64","arch": "amd64","version": "2.7.5-5ubuntu3","status": "ii "},{"package": "libpython2.7:amd64","arch": "amd64","version": "2.7.6-8ubuntu0.2","status": "ii "},{"package": "libpython2.7-minimal:amd64","arch": "amd64","version": "2.7.6-8ubuntu0.2","status": "ii "},{"package": "libpython2.7-stdlib:amd64","arch": "amd64","version": "2.7.6-8ubuntu0.2","status": "ii "},{"package": "libpython3-stdlib:amd64","arch": "amd64","version": "3.4.0-0ubuntu2","status": "ii "},{"package": "libpython3.4-minimal:amd64","arch": "amd64","version": "3.4.3-1ubuntu1~14.04.4","status": "ii "},{"package": "libpython3.4-stdlib:amd64","arch": "amd64","version": "3.4.3-1ubuntu1~14.04.4","status": "ii "},{"package": "libquadmath0:amd64","arch": "amd64","version": "4.8.4-2ubuntu1~14.04.3","status": "ii "},{"package": "libreadline6:amd64","arch": "amd64","version": "6.3-4ubuntu2","status": "ii "},{"package": "libroken18-heimdal:amd64","arch": "amd64","version": "1.6~git20131207+dfsg-1ubuntu1.1","status": "ii "},{"package": "librtmp0:amd64","arch": "amd64","version": "2.4+20121230.gitdf6c518-1","status": "ii "},{"package": "libsasl2-2:amd64","arch": "amd64","version": "2.1.25.dfsg1-17build1","status": "ii "},{"package": "libsasl2-modules:amd64","arch": "amd64","version": "2.1.25.dfsg1-17build1","status": "ii "},{"package": "libsasl2-modules-db:amd64","arch": "amd64","version": "2.1.25.dfsg1-17build1","status": "ii "},{"package": "libselinux1:amd64","arch": "amd64","version": "2.2.2-1ubuntu0.1","status": "ii "},{"package": "libsemanage-common","arch": "all","version": "2.2-1","status": "ii "},{"package": "libsemanage1:amd64","arch": "amd64","version": "2.2-1","status": "ii "},{"package": "libsepol1:amd64","arch": "amd64","version": "2.2-1ubuntu0.1","status": "ii "},{"package": "libsigc++-2.0-0c2a:amd64","arch": "amd64","version": "2.2.10-0.2ubuntu2","status": "ii "},{"package": "libsigsegv2:amd64","arch": "amd64","version": "2.10-2","status": "ii "},{"package": "libslang2:amd64","arch": "amd64","version": "2.2.4-15ubuntu1","status": "ii "},{"package": "libsqlite3-0:amd64","arch": "amd64","version": "3.8.2-1ubuntu2.1","status": "ii "},{"package": "libss2:amd64","arch": "amd64","version": "1.42.9-3ubuntu1.3","status": "ii "},{"package": "libssl1.0.0:amd64","arch": "amd64","version": "1.0.1f-1ubuntu2.21","status": "ii "},{"package": "libstdc++6:amd64","arch": "amd64","version": "4.8.4-2ubuntu1~14.04.3","status": "ii "},{"package": "libsub-name-perl","arch": "amd64","version": "0.05-1build4","status": "ii "},{"package": "libsystemd-daemon0:amd64","arch": "amd64","version": "204-5ubuntu20.19","status": "ii "},{"package": "libsystemd-login0:amd64","arch": "amd64","version": "204-5ubuntu20.19","status": "ii "},{"package": "libtasn1-6:amd64","arch": "amd64","version": "3.4-3ubuntu0.4","status": "ii "},{"package": "libterm-ui-perl","arch": "all","version": "0.42-1","status": "ii "},{"package": "libtext-charwidth-perl","arch": "amd64","version": "0.04-7build3","status": "ii "},{"package": "libtext-iconv-perl","arch": "amd64","version": "1.7-5build2","status": "ii "},{"package": "libtext-soundex-perl","arch": "amd64","version": "3.4-1build1","status": "ii "},{"package": "libtext-wrapi18n-perl","arch": "all","version": "0.06-7","status": "ii "},{"package": "libtimedate-perl","arch": "all","version": "2.3000-1","status": "ii "},{"package": "libtinfo5:amd64","arch": "amd64","version": "5.9+20140118-1ubuntu1","status": "ii "},{"package": "libtsan0:amd64","arch": "amd64","version": "4.8.4-2ubuntu1~14.04.3","status": "ii "},{"package": "libudev1:amd64","arch": "amd64","version": "204-5ubuntu20.19","status": "ii "},{"package": "libusb-0.1-4:amd64","arch": "amd64","version": "2:0.1.12-23.3ubuntu1","status": "ii "},{"package": "libusb-1.0-0:amd64","arch": "amd64","version": "2:1.0.17-1ubuntu2","status": "ii "},{"package": "libustr-1.0-1:amd64","arch": "amd64","version": "1.0.4-3ubuntu2","status": "ii "},{"package": "libuuid1:amd64","arch": "amd64","version": "2.20.1-5.1ubuntu20.7","status": "ii "},{"package": "libwind0-heimdal:amd64","arch": "amd64","version": "1.6~git20131207+dfsg-1ubuntu1.1","status": "ii "},{"package": "libwrap0:amd64","arch": "amd64","version": "7.6.q-25","status": "ii "},{"package": "libx11-6:amd64","arch": "amd64","version": "2:1.6.2-1ubuntu2","status": "ii "},{"package": "libx11-data","arch": "all","version": "2:1.6.2-1ubuntu2","status": "ii "},{"package": "libxapian22","arch": "amd64","version": "1.2.16-2ubuntu1","status": "ii "},{"package": "libxau6:amd64","arch": "amd64","version": "1:1.0.8-1","status": "ii "},{"package": "libxcb1:amd64","arch": "amd64","version": "1.10-2ubuntu1","status": "ii "},{"package": "libxdmcp6:amd64","arch": "amd64","version": "1:1.1.1-1","status": "ii "},{"package": "libxext6:amd64","arch": "amd64","version": "2:1.3.2-1ubuntu0.0.14.04.1","status": "ii "},{"package": "libxml2:amd64","arch": "amd64","version": "2.9.1+dfsg1-3ubuntu4.8","status": "ii "},{"package": "libxmuu1:amd64","arch": "amd64","version": "2:1.1.1-1","status": "ii "},{"package": "libxtables10","arch": "amd64","version": "1.4.21-1ubuntu1","status": "ii "},{"package": "libyaml-0-2:amd64","arch": "amd64","version": "0.1.4-3ubuntu3.1","status": "ii "},{"package": "linux-firmware","arch": "all","version": "1.127.22","status": "ii "},{"package": "linux-image-3.13.0-96-generic","arch": "amd64","version": "3.13.0-96.143","status": "ii "},{"package": "linux-image-extra-3.13.0-96-generic","arch": "amd64","version": "3.13.0-96.143","status": "ii "},{"package": "linux-image-generic","arch": "amd64","version": "3.13.0.96.104","status": "ii "},{"package": "locales","arch": "all","version": "2.13+git20120306-12.1","status": "ii "},{"package": "lockfile-progs","arch": "amd64","version": "0.1.17","status": "ii "},{"package": "login","arch": "amd64","version": "1:4.1.5.1-1ubuntu9.2","status": "ii "},{"package": "logrotate","arch": "amd64","version": "3.8.7-1ubuntu1","status": "ii "},{"package": "lsb-base","arch": "all","version": "4.1+Debian11ubuntu6.2","status": "ii "},{"package": "lsb-release","arch": "all","version": "4.1+Debian11ubuntu6.2","status": "ii "},{"package": "lshw","arch": "amd64","version": "02.16-2ubuntu1.3","status": "ii "},{"package": "lsof","arch": "amd64","version": "4.86+dfsg-1ubuntu2","status": "ii "},{"package": "ltrace","arch": "amd64","version": "0.7.3-4ubuntu5.1","status": "ii "},{"package": "make","arch": "amd64","version": "3.81-8.2ubuntu3","status": "ii "},{"package": "makedev","arch": "all","version": "2.3.1-93ubuntu1","status": "ii "},{"package": "man-db","arch": "amd64","version": "2.6.7.1-1ubuntu1","status": "ii "},{"package": "manpages","arch": "all","version": "3.54-1ubuntu1","status": "ii "},{"package": "mawk","arch": "amd64","version": "1.3.3-17ubuntu2","status": "ii "},{"package": "mime-support","arch": "all","version": "3.54ubuntu1.1","status": "ii "},{"package": "mlocate","arch": "amd64","version": "0.26-1ubuntu1","status": "ii "},{"package": "module-init-tools","arch": "all","version": "15-0ubuntu6","status": "ii "},{"package": "mount","arch": "amd64","version": "2.20.1-5.1ubuntu20.7","status": "ii "},{"package": "mountall","arch": "amd64","version": "2.53","status": "ii "},{"package": "mtr-tiny","arch": "amd64","version": "0.85-2","status": "ii "},{"package": "multiarch-support","arch": "amd64","version": "2.19-0ubuntu6.9","status": "ii "},{"package": "nano","arch": "amd64","version": "2.2.6-1ubuntu1","status": "ii "},{"package": "ncurses-base","arch": "all","version": "5.9+20140118-1ubuntu1","status": "ii "},{"package": "ncurses-bin","arch": "amd64","version": "5.9+20140118-1ubuntu1","status": "ii "},{"package": "ncurses-term","arch": "all","version": "5.9+20140118-1ubuntu1","status": "ii "},{"package": "net-tools","arch": "amd64","version": "1.60-25ubuntu2.1","status": "ii "},{"package": "netbase","arch": "all","version": "5.2","status": "ii "},{"package": "netcat-openbsd","arch": "amd64","version": "1.105-7ubuntu1","status": "ii "},{"package": "ntfs-3g","arch": "amd64","version": "1:2013.1.13AR.1-2ubuntu2","status": "ii "},{"package": "ntpdate","arch": "amd64","version": "1:4.2.6.p5+dfsg-3ubuntu2.14.04.8","status": "ii "},{"package": "open-iscsi","arch": "amd64","version": "2.0.873-3ubuntu9","status": "ii "},{"package": "open-vm-tools","arch": "amd64","version": "2:9.4.0-1280544-5ubuntu6.2","status": "ii "},{"package": "openssh-client","arch": "amd64","version": "1:6.6p1-2ubuntu2.8","status": "ii "},{"package": "openssh-server","arch": "amd64","version": "1:6.6p1-2ubuntu2.8","status": "ii "},{"package": "openssh-sftp-server","arch": "amd64","version": "1:6.6p1-2ubuntu2.8","status": "ii "},{"package": "openssl","arch": "amd64","version": "1.0.1f-1ubuntu2.21","status": "ii "},{"package": "overlayroot","arch": "all","version": "0.25ubuntu1.14.04.1","status": "ii "},{"package": "parted","arch": "amd64","version": "2.3-19ubuntu1.14.04.1","status": "ii "},{"package": "passwd","arch": "amd64","version": "1:4.1.5.1-1ubuntu9.2","status": "ii "},{"package": "patch","arch": "amd64","version": "2.7.1-4ubuntu2.3","status": "ii "},{"package": "pciutils","arch": "amd64","version": "1:3.2.1-1ubuntu5.1","status": "ii "},{"package": "perl","arch": "amd64","version": "5.18.2-2ubuntu1.1","status": "ii "},{"package": "perl-base","arch": "amd64","version": "5.18.2-2ubuntu1.1","status": "ii "},{"package": "perl-modules","arch": "all","version": "5.18.2-2ubuntu1.1","status": "ii "},{"package": "plymouth","arch": "amd64","version": "0.8.8-0ubuntu17.1","status": "ii "},{"package": "plymouth-theme-ubuntu-text","arch": "amd64","version": "0.8.8-0ubuntu17.1","status": "ii "},{"package": "policykit-1","arch": "amd64","version": "0.105-4ubuntu3.14.04.1","status": "ii "},{"package": "pollinate","arch": "all","version": "4.21-0ubuntu1~14.04","status": "ii "},{"package": "popularity-contest","arch": "all","version": "1.57ubuntu1","status": "ii "},{"package": "powermgmt-base","arch": "amd64","version": "1.31build1","status": "ii "},{"package": "ppp","arch": "amd64","version": "2.4.5-5.1ubuntu2.2","status": "ii "},{"package": "pppconfig","arch": "all","version": "2.3.19ubuntu1","status": "ii "},{"package": "pppoeconf","arch": "all","version": "1.20ubuntu1","status": "ii "},{"package": "procps","arch": "amd64","version": "1:3.3.9-1ubuntu2.2","status": "ii "},{"package": "psmisc","arch": "amd64","version": "22.20-1ubuntu2","status": "ii "},{"package": "python","arch": "amd64","version": "2.7.5-5ubuntu3","status": "ii "},{"package": "python-apt","arch": "amd64","version": "0.9.3.5ubuntu2","status": "ii "},{"package": "python-apt-common","arch": "all","version": "0.9.3.5ubuntu2","status": "ii "},{"package": "python-chardet","arch": "all","version": "2.0.1-2build2","status": "ii "},{"package": "python-cheetah","arch": "amd64","version": "2.4.4-3.fakesyncbuild1","status": "ii "},{"package": "python-configobj","arch": "all","version": "4.7.2+ds-5build1","status": "ii "},{"package": "python-debian","arch": "all","version": "0.1.21+nmu2ubuntu2","status": "ii "},{"package": "python-gdbm","arch": "amd64","version": "2.7.5-1ubuntu1","status": "ii "},{"package": "python-json-pointer","arch": "all","version": "1.0-2build1","status": "ii "},{"package": "python-jsonpatch","arch": "all","version": "1.3-4","status": "ii "},{"package": "python-minimal","arch": "amd64","version": "2.7.5-5ubuntu3","status": "ii "},{"package": "python-oauth","arch": "all","version": "1.0.1-3build2","status": "ii "},{"package": "python-openssl","arch": "amd64","version": "0.13-2ubuntu6","status": "ii "},{"package": "python-pam","arch": "amd64","version": "0.4.2-13.1ubuntu3","status": "ii "},{"package": "python-pkg-resources","arch": "all","version": "3.3-1ubuntu2","status": "ii "},{"package": "python-prettytable","arch": "all","version": "0.7.2-2ubuntu2","status": "ii "},{"package": "python-pycurl","arch": "amd64","version": "7.19.3-0ubuntu3","status": "ii "},{"package": "python-requests","arch": "all","version": "2.2.1-1ubuntu0.3","status": "ii "},{"package": "python-serial","arch": "all","version": "2.6-1build1","status": "ii "},{"package": "python-six","arch": "all","version": "1.5.2-1ubuntu1","status": "ii "},{"package": "python-twisted-bin","arch": "amd64","version": "13.2.0-1ubuntu1","status": "ii "},{"package": "python-twisted-core","arch": "all","version": "13.2.0-1ubuntu1","status": "ii "},{"package": "python-twisted-names","arch": "all","version": "13.2.0-1ubuntu1","status": "ii "},{"package": "python-twisted-web","arch": "all","version": "13.2.0-1ubuntu1","status": "ii "},{"package": "python-urllib3","arch": "all","version": "1.7.1-1ubuntu4","status": "ii "},{"package": "python-xapian","arch": "amd64","version": "1.2.16-2ubuntu1","status": "ii "},{"package": "python-yaml","arch": "amd64","version": "3.10-4ubuntu0.1","status": "ii "},{"package": "python-zope.interface","arch": "amd64","version": "4.0.5-1ubuntu4","status": "ii "},{"package": "python2.7","arch": "amd64","version": "2.7.6-8ubuntu0.2","status": "ii "},{"package": "python2.7-minimal","arch": "amd64","version": "2.7.6-8ubuntu0.2","status": "ii "},{"package": "python3","arch": "amd64","version": "3.4.0-0ubuntu2","status": "ii "},{"package": "python3-apport","arch": "all","version": "2.14.1-0ubuntu3.21","status": "ii "},{"package": "python3-apt","arch": "amd64","version": "0.9.3.5ubuntu2","status": "ii "},{"package": "python3-commandnotfound","arch": "all","version": "0.3ubuntu12","status": "ii "},{"package": "python3-dbus","arch": "amd64","version": "1.2.0-2build2","status": "ii "},{"package": "python3-distupgrade","arch": "all","version": "1:0.220.8","status": "ii "},{"package": "python3-gdbm:amd64","arch": "amd64","version": "3.4.3-1~14.04.2","status": "ii "},{"package": "python3-gi","arch": "amd64","version": "3.12.0-1ubuntu1","status": "ii "},{"package": "python3-minimal","arch": "amd64","version": "3.4.0-0ubuntu2","status": "ii "},{"package": "python3-newt","arch": "amd64","version": "0.52.15-2ubuntu5","status": "ii "},{"package": "python3-problem-report","arch": "all","version": "2.14.1-0ubuntu3.21","status": "ii "},{"package": "python3-pycurl","arch": "amd64","version": "7.19.3-0ubuntu3","status": "ii "},{"package": "python3-software-properties","arch": "all","version": "0.92.37.7","status": "ii "},{"package": "python3-update-manager","arch": "all","version": "1:0.196.21","status": "ii "},{"package": "python3.4","arch": "amd64","version": "3.4.3-1ubuntu1~14.04.4","status": "ii "},{"package": "python3.4-minimal","arch": "amd64","version": "3.4.3-1ubuntu1~14.04.4","status": "ii "},{"package": "readline-common","arch": "all","version": "6.3-4ubuntu2","status": "ii "},{"package": "resolvconf","arch": "all","version": "1.69ubuntu1.1","status": "ii "},{"package": "rsync","arch": "amd64","version": "3.1.0-2ubuntu0.2","status": "ii "},{"package": "rsyslog","arch": "amd64","version": "7.4.4-1ubuntu2.6","status": "ii "},{"package": "run-one","arch": "all","version": "1.17-0ubuntu1","status": "ii "},{"package": "screen","arch": "amd64","version": "4.1.0~20120320gitdb59704-9","status": "ii "},{"package": "sed","arch": "amd64","version": "4.2.2-4ubuntu1","status": "ii "},{"package": "sensible-utils","arch": "all","version": "0.0.9","status": "ii "},{"package": "sgml-base","arch": "all","version": "1.26+nmu4ubuntu1","status": "ii "},{"package": "shared-mime-info","arch": "amd64","version": "1.2-0ubuntu3","status": "ii "},{"package": "software-properties-common","arch": "all","version": "0.92.37.7","status": "ii "},{"package": "ssh-import-id","arch": "all","version": "3.21-0ubuntu1","status": "ii "},{"package": "strace","arch": "amd64","version": "4.8-1ubuntu5","status": "ii "},{"package": "sudo","arch": "amd64","version": "1.8.9p5-1ubuntu1.2","status": "ii "},{"package": "systemd-services","arch": "amd64","version": "204-5ubuntu20.19","status": "ii "},{"package": "systemd-shim","arch": "amd64","version": "6-2bzr1","status": "ii "},{"package": "sysv-rc","arch": "all","version": "2.88dsf-41ubuntu6.3","status": "ii "},{"package": "sysvinit-utils","arch": "amd64","version": "2.88dsf-41ubuntu6.3","status": "ii "},{"package": "tar","arch": "amd64","version": "1.27.1-1","status": "ii "},{"package": "tasksel","arch": "all","version": "2.88ubuntu15","status": "ii "},{"package": "tasksel-data","arch": "all","version": "2.88ubuntu15","status": "ii "},{"package": "tcpd","arch": "amd64","version": "7.6.q-25","status": "ii "},{"package": "tcpdump","arch": "amd64","version": "4.5.1-2ubuntu1.2","status": "ii "},{"package": "telnet","arch": "amd64","version": "0.17-36build2","status": "ii "},{"package": "time","arch": "amd64","version": "1.7-24","status": "ii "},{"package": "tmux","arch": "amd64","version": "1.8-5","status": "ii "},{"package": "tzdata","arch": "all","version": "2016f-0ubuntu0.14.04","status": "ii "},{"package": "ubuntu-keyring","arch": "all","version": "2012.05.19","status": "ii "},{"package": "ubuntu-minimal","arch": "amd64","version": "1.325","status": "ii "},{"package": "ubuntu-release-upgrader-core","arch": "all","version": "1:0.220.8","status": "ii "},{"package": "ubuntu-standard","arch": "amd64","version": "1.325","status": "ii "},{"package": "ucf","arch": "all","version": "3.0027+nmu1","status": "ii "},{"package": "udev","arch": "amd64","version": "204-5ubuntu20.19","status": "ii "},{"package": "ufw","arch": "all","version": "0.34~rc-0ubuntu2","status": "ii "},{"package": "unattended-upgrades","arch": "all","version": "0.82.1ubuntu2.4","status": "ii "},{"package": "update-manager-core","arch": "all","version": "1:0.196.21","status": "ii "},{"package": "update-notifier-common","arch": "all","version": "0.154.1ubuntu2","status": "ii "},{"package": "upstart","arch": "amd64","version": "1.12.1-0ubuntu4.2","status": "ii "},{"package": "ureadahead","arch": "amd64","version": "0.100.0-16","status": "ii "},{"package": "usbutils","arch": "amd64","version": "1:007-2ubuntu1.1","status": "ii "},{"package": "util-linux","arch": "amd64","version": "2.20.1-5.1ubuntu20.7","status": "ii "},{"package": "uuid-runtime","arch": "amd64","version": "2.20.1-5.1ubuntu20.7","status": "ii "},{"package": "vim","arch": "amd64","version": "2:7.4.052-1ubuntu3","status": "ii "},{"package": "vim-common","arch": "amd64","version": "2:7.4.052-1ubuntu3","status": "ii "},{"package": "vim-runtime","arch": "all","version": "2:7.4.052-1ubuntu3","status": "ii "},{"package": "vim-tiny","arch": "amd64","version": "2:7.4.052-1ubuntu3","status": "ii "},{"package": "w3m","arch": "amd64","version": "0.5.3-15","status": "ii "},{"package": "wget","arch": "amd64","version": "1.15-1ubuntu1.14.04.2","status": "ii "},{"package": "whiptail","arch": "amd64","version": "0.52.15-2ubuntu5","status": "ii "},{"package": "wireless-regdb","arch": "all","version": "2013.02.13-1ubuntu1","status": "ii "},{"package": "xauth","arch": "amd64","version": "1:1.0.7-1ubuntu1","status": "ii "},{"package": "xkb-data","arch": "all","version": "2.10.1-1ubuntu1","status": "ii "},{"package": "xml-core","arch": "all","version": "0.13+nmu2","status": "ii "},{"package": "xz-utils","arch": "amd64","version": "5.1.1alpha+20120614-2ubuntu2","status": "ii "},{"package": "zerofree","arch": "amd64","version": "1.0.2-1ubuntu1","status": "ii "},{"package": "zlib1g:amd64","arch": "amd64","version": "1:1.2.8.dfsg-1ubuntu1","status": "ii "},+ sed -i -e 's/,$/\n]}/g' -e 's/\(},\)/    \1\n/g' /etc/dib-manifests/dib-manifest-dpkg-image
3209: + target_tag=99-write-dpkg-manifest
3210: + date +%s.%N
3211: + output '99-write-dpkg-manifest completed'
3212: + output_prefix
3213: ++ date
3214: + printf '%s %s ' dib-run-parts 'Mon Oct  3 15:14:02 UTC 2016'
3215: dib-run-parts Mon Oct  3 15:14:02 UTC 2016 + echo 99-write-dpkg-manifest completed
3216: 99-write-dpkg-manifest completed
3217: dib-run-parts Mon Oct  3 15:14:02 UTC 2016 ----------------------- PROFILING -----------------------
3218: dib-run-parts Mon Oct  3 15:14:02 UTC 2016
3219: dib-run-parts Mon Oct  3 15:14:02 UTC 2016 Target: finalise.d
3220: dib-run-parts Mon Oct  3 15:14:02 UTC 2016
3221: dib-run-parts Mon Oct  3 15:14:02 UTC 2016 Script                                     Seconds
3222: dib-run-parts Mon Oct  3 15:14:02 UTC 2016 ---------------------------------------  ----------
3223: dib-run-parts Mon Oct  3 15:14:02 UTC 2016
3224: dib-run-parts Mon Oct  3 15:14:02 UTC 2016 50-bootloader                                15.690
3225: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
3226: dib-run-parts Mon Oct  3 15:14:02 UTC 2016 50-remove-bogus-udev-links                    0.002
3227: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
3228: dib-run-parts Mon Oct  3 15:14:02 UTC 2016 99-clean-up-cache                             0.013
3229: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
3230: dib-run-parts Mon Oct  3 15:14:02 UTC 2016 99-write-dpkg-manifest                        0.016
3231: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
3232: dib-run-parts Mon Oct  3 15:14:02 UTC 2016
3233: dib-run-parts Mon Oct  3 15:14:02 UTC 2016 --------------------- END PROFILING ---------------------
3234: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_in_target:67 :   export HOME=/home/xion
3235: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_in_target:67 :   HOME=/home/xion
3236: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:83 :   trap - ERR
3237: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:84 :   check_break after-finalise run_in_target bash
3238: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:check_break:98 :   egrep -e '(,|^)after-finalise(,|$)' -q
3239: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:check_break:98 :   echo ''
3240: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:85 :   sudo umount -f /tmp/dib_build.1CFJZpLz/mnt/tmp/in_target.d
3241: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:run_d_in_target:86 :   timeout 5 sh -c ' while ! sudo rmdir /tmp/dib_build.1CFJZpLz/mnt/tmp/in_target.d; do sleep 1; done'
3242: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:428                  :   finalise_base
3243: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:finalise_base:94 :   TARGET_ROOT=/tmp/dib_build.1CFJZpLz/mnt
3244: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:finalise_base:94 :   run_d cleanup
3245: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:run_d:148 :   check_element
3246: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:check_element:109 :   '[' -d /tmp/dib_build.1CFJZpLz/hooks ']'
3247: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:run_d:149 :   check_break before-cleanup bash
3248: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:check_break:98 :   echo ''
3249: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:check_break:98 :   egrep -e '(,|^)before-cleanup(,|$)' -q
3250: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:run_d:150 :   '[' -d /tmp/dib_build.1CFJZpLz/hooks/cleanup.d ']'
3251: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:run_d:151 :   '[' -n '' ']'
3252: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:run_d:157 :   dib-run-parts /tmp/dib_build.1CFJZpLz/hooks/cleanup.d
3253: + /tmp/dib_build.1CFJZpLz/hooks/dib-init-system:main:6                             :   set -eu
3254: + /tmp/dib_build.1CFJZpLz/hooks/dib-init-system:main:7                             :   set -o pipefail
3255: + /tmp/dib_build.1CFJZpLz/hooks/dib-init-system:main:9                             :   [[ -f /usr/bin/systemctl ]]
3256: + /tmp/dib_build.1CFJZpLz/hooks/dib-init-system:main:11                            :   [[ -f /sbin/initctl ]]
3257: + /tmp/dib_build.1CFJZpLz/hooks/dib-init-system:main:12                            :   echo upstart
3258: ++ /tmp/dib_build.1CFJZpLz/hooks/environment.d/14-manifests:source:21               :   set -eu
3259: ++ /tmp/dib_build.1CFJZpLz/hooks/environment.d/14-manifests:source:22               :   set -o pipefail
3260: ++ /tmp/dib_build.1CFJZpLz/hooks/environment.d/14-manifests:source:24               :   export DIB_MANIFEST_IMAGE_DIR=/etc/dib-manifests
3261: ++ /tmp/dib_build.1CFJZpLz/hooks/environment.d/14-manifests:source:24               :   DIB_MANIFEST_IMAGE_DIR=/etc/dib-manifests
3262: ++ /tmp/dib_build.1CFJZpLz/hooks/environment.d/14-manifests:source:25               :   export DIB_MANIFEST_SAVE_DIR=image.d/
3263: ++ /tmp/dib_build.1CFJZpLz/hooks/environment.d/14-manifests:source:25               :   DIB_MANIFEST_SAVE_DIR=image.d/
3264: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:source_environment:65         :   for env_file in '$env_files'
3265: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:source_environment:66         :   source /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/../environment.d/99-cloud-init-datasources.bash
3266: ++ /tmp/dib_build.1CFJZpLz/hooks/environment.d/99-cloud-init-datasources.bash:source:4 :   export DIB_CLOUD_INIT_DATASOURCES=Ec2
3267: ++ /tmp/dib_build.1CFJZpLz/hooks/environment.d/99-cloud-init-datasources.bash:source:4 :   DIB_CLOUD_INIT_DATASOURCES=Ec2
3268: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:108                      :   for target in '$targets'
3269: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:109                      :   output 'Running /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/01-ccache'
3270: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:43                     :   output_prefix
3271: ++ /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   date
3272: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   printf '%s %s ' dib-run-parts '2016年 10月 03日 星期一 23:14:02 CST'
3273: dib-run-parts 2016年 10月 03日 星期一 23:14:02 CST + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:44                     :   echo Running /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/01-ccache
3274: Running /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/01-ccache
3275: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:110                      :   target_tag=01-ccache
3276: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:111                      :   date +%s.%N
3277: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:112                      :   /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/01-ccache
3278: + /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/01-ccache:main:6                         :   set -eu
3279: + /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/01-ccache:main:7                         :   set -o pipefail
3280: + /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/01-ccache:main:11                        :   sudo rmdir /tmp/dib_build.1CFJZpLz/mnt/tmp/ccache
3281: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:113                      :   target_tag=01-ccache
3282: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:114                      :   date +%s.%N
3283: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:115                      :   output '01-ccache completed'
3284: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:43                     :   output_prefix
3285: ++ /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   date
3286: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   printf '%s %s ' dib-run-parts '2016年 10月 03日 星期一 23:14:02 CST'
3287: dib-run-parts 2016年 10月 03日 星期一 23:14:02 CST + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:44                     :   echo 01-ccache completed
3288: 01-ccache completed
3289: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:108                      :   for target in '$targets'
3290: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:109                      :   output 'Running /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/01-copy-manifests-dir'
3291: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:43                     :   output_prefix
3292: ++ /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   date
3293: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   printf '%s %s ' dib-run-parts '2016年 10月 03日 星期一 23:14:02 CST'
3294: dib-run-parts 2016年 10月 03日 星期一 23:14:02 CST + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:44                     :   echo Running /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/01-copy-manifests-dir
3295: Running /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/01-copy-manifests-dir
3296: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:110                      :   target_tag=01-copy-manifests-dir
3297: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:111                      :   date +%s.%N
3298: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:112                      :   /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/01-copy-manifests-dir
3299: + /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/01-copy-manifests-dir:main:21            :   set -eu
3300: + /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/01-copy-manifests-dir:main:22            :   set -o pipefail
3301: + /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/01-copy-manifests-dir:main:24            :   '[' -d /tmp/dib_build.1CFJZpLz/mnt//etc/dib-manifests ']'
3302: + /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/01-copy-manifests-dir:main:26            :   '[' -e /tmp/dib_build.1CFJZpLz/mnt/etc/dib_arguments ']'
3303: + /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/01-copy-manifests-dir:main:27            :   sudo mv /tmp/dib_build.1CFJZpLz/mnt/etc/dib_arguments /tmp/dib_build.1CFJZpLz/mnt//etc/dib-manifests
3304: + /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/01-copy-manifests-dir:main:29            :   '[' -e /tmp/dib_build.1CFJZpLz/mnt/etc/dib_environment ']'
3305: + /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/01-copy-manifests-dir:main:30            :   sudo mv /tmp/dib_build.1CFJZpLz/mnt/etc/dib_environment /tmp/dib_build.1CFJZpLz/mnt//etc/dib-manifests
3306: + /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/01-copy-manifests-dir:main:32            :   mkdir -p image.d/
3307: + /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/01-copy-manifests-dir:main:33            :   cp --no-preserve=ownership -rv /tmp/dib_build.1CFJZpLz/mnt//etc/dib-manifests image.d/
3308: '/tmp/dib_build.1CFJZpLz/mnt//etc/dib-manifests' -> 'image.d/dib-manifests'
3309: '/tmp/dib_build.1CFJZpLz/mnt//etc/dib-manifests/dib_environment' -> 'image.d/dib-manifests/dib_environment'
3310: '/tmp/dib_build.1CFJZpLz/mnt//etc/dib-manifests/dib_arguments' -> 'image.d/dib-manifests/dib_arguments'
3311: '/tmp/dib_build.1CFJZpLz/mnt//etc/dib-manifests/dib-manifest-dpkg-image' -> 'image.d/dib-manifests/dib-manifest-dpkg-image'
3312: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:113                      :   target_tag=01-copy-manifests-dir
3313: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:114                      :   date +%s.%N
3314: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:115                      :   output '01-copy-manifests-dir completed'
3315: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:43                     :   output_prefix
3316: ++ /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   date
3317: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   printf '%s %s ' dib-run-parts '2016年 10月 03日 星期一 23:14:02 CST'
3318: dib-run-parts 2016年 10月 03日 星期一 23:14:02 CST + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:44                     :   echo 01-copy-manifests-dir completed
3319: 01-copy-manifests-dir completed
3320: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:108                      :   for target in '$targets'
3321: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:109                      :   output 'Running /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/40-unblock-daemons'
3322: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:43                     :   output_prefix
3323: ++ /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   date
3324: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   printf '%s %s ' dib-run-parts '2016年 10月 03日 星期一 23:14:02 CST'
3325: dib-run-parts 2016年 10月 03日 星期一 23:14:02 CST + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:44                     :   echo Running /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/40-unblock-daemons
3326: Running /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/40-unblock-daemons
3327: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:110                      :   target_tag=40-unblock-daemons
3328: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:111                      :   date +%s.%N
3329: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:112                      :   /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/40-unblock-daemons
3330: + /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/40-unblock-daemons:main:6                :   set -eu
3331: + /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/40-unblock-daemons:main:7                :   set -o pipefail
3332: + /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/40-unblock-daemons:main:9                :   '[' -n /tmp/dib_build.1CFJZpLz/mnt ']'
3333: + /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/40-unblock-daemons:main:11               :   sudo mv /tmp/dib_build.1CFJZpLz/mnt/sbin/start-stop-daemon.REAL /tmp/dib_build.1CFJZpLz/mnt/sbin/start-stop-daemon
3334: + /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/40-unblock-daemons:main:13               :   '[' -f /tmp/dib_build.1CFJZpLz/mnt/sbin/initctl.REAL ']'
3335: + /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/40-unblock-daemons:main:14               :   sudo mv /tmp/dib_build.1CFJZpLz/mnt/sbin/initctl.REAL /tmp/dib_build.1CFJZpLz/mnt/sbin/initctl
3336: + /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/40-unblock-daemons:main:17               :   sudo rm /tmp/dib_build.1CFJZpLz/mnt/usr/sbin/policy-rc.d
3337: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:113                      :   target_tag=40-unblock-daemons
3338: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:114                      :   date +%s.%N
3339: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:115                      :   output '40-unblock-daemons completed'
3340: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:43                     :   output_prefix
3341: ++ /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   date
3342: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   printf '%s %s ' dib-run-parts '2016年 10月 03日 星期一 23:14:02 CST'
3343: dib-run-parts 2016年 10月 03日 星期一 23:14:02 CST + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:44                     :   echo 40-unblock-daemons completed
3344: 40-unblock-daemons completed
3345: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:108                      :   for target in '$targets'
3346: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:109                      :   output 'Running /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/50-remove-img-build-proxy'
3347: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:43                     :   output_prefix
3348: ++ /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   date
3349: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   printf '%s %s ' dib-run-parts '2016年 10月 03日 星期一 23:14:02 CST'
3350: dib-run-parts 2016年 10月 03日 星期一 23:14:02 CST + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:44                     :   echo Running /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/50-remove-img-build-proxy
3351: Running /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/50-remove-img-build-proxy
3352: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:110                      :   target_tag=50-remove-img-build-proxy
3353: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:111                      :   date +%s.%N
3354: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:112                      :   /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/50-remove-img-build-proxy
3355: + /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/50-remove-img-build-proxy:main:6         :   set -eu
3356: + /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/50-remove-img-build-proxy:main:7         :   set -o pipefail
3357: + /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/50-remove-img-build-proxy:main:9         :   '[' -n /tmp/dib_build.1CFJZpLz/mnt ']'
3358: + /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/50-remove-img-build-proxy:main:12        :   sudo rm -f /tmp/dib_build.1CFJZpLz/mnt/etc/apt/apt.conf.d/60img-build-proxy
3359: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:113                      :   target_tag=50-remove-img-build-proxy
3360: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:114                      :   date +%s.%N
3361: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:115                      :   output '50-remove-img-build-proxy completed'
3362: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:43                     :   output_prefix
3363: ++ /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   date
3364: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   printf '%s %s ' dib-run-parts '2016年 10月 03日 星期一 23:14:02 CST'
3365: dib-run-parts 2016年 10月 03日 星期一 23:14:02 CST + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:44                     :   echo 50-remove-img-build-proxy completed
3366: 50-remove-img-build-proxy completed
3367: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:108                      :   for target in '$targets'
3368: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:109                      :   output 'Running /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/51-bootloader'
3369: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:43                     :   output_prefix
3370: ++ /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   date
3371: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   printf '%s %s ' dib-run-parts '2016年 10月 03日 星期一 23:14:02 CST'
3372: dib-run-parts 2016年 10月 03日 星期一 23:14:02 CST + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:44                     :   echo Running /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/51-bootloader
3373: Running /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/51-bootloader
3374: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:110                      :   target_tag=51-bootloader
3375: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:111                      :   date +%s.%N
3376: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:112                      :   /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/51-bootloader
3377: + /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/51-bootloader:main:23                    :   set -eu
3378: + /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/51-bootloader:main:24                    :   set -o pipefail
3379: + /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/51-bootloader:main:26                    :   '[' -n /tmp/dib_build.1CFJZpLz/mnt ']'
3380: + /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/51-bootloader:main:28                    :   source /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/lib/img-functions
3381: + /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/51-bootloader:main:30                    :   '[' -d /tmp/dib_build.1CFJZpLz/mnt/boot/extlinux ']'
3382: + /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/51-bootloader:main:32                    :   '[' -d /tmp/dib_build.1CFJZpLz/mnt/boot/syslinux ']'
3383: + /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/51-bootloader:main:35                    :   exit 0
3384: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:113                      :   target_tag=51-bootloader
3385: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:114                      :   date +%s.%N
3386: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:115                      :   output '51-bootloader completed'
3387: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:43                     :   output_prefix
3388: ++ /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   date
3389: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   printf '%s %s ' dib-run-parts '2016年 10月 03日 星期一 23:14:03 CST'
3390: dib-run-parts 2016年 10月 03日 星期一 23:14:03 CST + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:44                     :   echo 51-bootloader completed
3391: 51-bootloader completed
3392: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:108                      :   for target in '$targets'
3393: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:109                      :   output 'Running /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/60-untrim-dpkg'
3394: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:43                     :   output_prefix
3395: ++ /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   date
3396: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   printf '%s %s ' dib-run-parts '2016年 10月 03日 星期一 23:14:03 CST'
3397: dib-run-parts 2016年 10月 03日 星期一 23:14:03 CST + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:44                     :   echo Running /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/60-untrim-dpkg
3398: Running /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/60-untrim-dpkg
3399: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:110                      :   target_tag=60-untrim-dpkg
3400: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:111                      :   date +%s.%N
3401: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:112                      :   /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/60-untrim-dpkg
3402: + /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/60-untrim-dpkg:main:6                    :   set -eu
3403: + /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/60-untrim-dpkg:main:7                    :   set -o pipefail
3404: + /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/60-untrim-dpkg:main:9                    :   '[' -n /tmp/dib_build.1CFJZpLz/mnt ']'
3405: + /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/60-untrim-dpkg:main:11                   :   sudo rm /tmp/dib_build.1CFJZpLz/mnt/etc/dpkg/dpkg.cfg.d/02apt-speedup
3406: + /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/60-untrim-dpkg:main:12                   :   sudo rm /tmp/dib_build.1CFJZpLz/mnt/etc/apt/apt.conf.d/no-languages
3407: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:113                      :   target_tag=60-untrim-dpkg
3408: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:114                      :   date +%s.%N
3409: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:115                      :   output '60-untrim-dpkg completed'
3410: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:43                     :   output_prefix
3411: ++ /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   date
3412: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   printf '%s %s ' dib-run-parts '2016年 10月 03日 星期一 23:14:03 CST'
3413: dib-run-parts 2016年 10月 03日 星期一 23:14:03 CST + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:44                     :   echo 60-untrim-dpkg completed
3414: 60-untrim-dpkg completed
3415: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:108                      :   for target in '$targets'
3416: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:109                      :   output 'Running /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/99-tidy-logs'
3417: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:43                     :   output_prefix
3418: ++ /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   date
3419: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   printf '%s %s ' dib-run-parts '2016年 10月 03日 星期一 23:14:03 CST'
3420: dib-run-parts 2016年 10月 03日 星期一 23:14:03 CST + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:44                     :   echo Running /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/99-tidy-logs
3421: Running /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/99-tidy-logs
3422: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:110                      :   target_tag=99-tidy-logs
3423: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:111                      :   date +%s.%N
3424: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:112                      :   /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/99-tidy-logs
3425: + /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/99-tidy-logs:main:22                     :   set -eu
3426: + /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/99-tidy-logs:main:23                     :   set -o pipefail
3427: + /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/99-tidy-logs:main:26                     :   sudo find /tmp/dib_build.1CFJZpLz/mnt/var/log -type f -exec cp /dev/null '{}' ';'
3428: + /tmp/dib_build.1CFJZpLz/hooks/cleanup.d/99-tidy-logs:main:29                     :   sudo find /tmp/dib_build.1CFJZpLz/mnt/root -name '*.log' -type f -delete
3429: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:113                      :   target_tag=99-tidy-logs
3430: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:114                      :   date +%s.%N
3431: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:main:115                      :   output '99-tidy-logs completed'
3432: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:43                     :   output_prefix
3433: ++ /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   date
3434: + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output_prefix:39              :   printf '%s %s ' dib-run-parts '2016年 10月 03日 星期一 23:14:03 CST'
3435: dib-run-parts 2016年 10月 03日 星期一 23:14:03 CST + /home/xion/gitRepo/openstack/env/bin/dib-run-parts:output:44                     :   echo 99-tidy-logs completed
3436: 99-tidy-logs completed
3437: dib-run-parts 2016年 10月 03日 星期一 23:14:03 CST ----------------------- PROFILING -----------------------
3438: dib-run-parts 2016年 10月 03日 星期一 23:14:03 CST
3439: dib-run-parts 2016年 10月 03日 星期一 23:14:03 CST Target: cleanup.d
3440: dib-run-parts 2016年 10月 03日 星期一 23:14:03 CST
3441: dib-run-parts 2016年 10月 03日 星期一 23:14:03 CST Script                                     Seconds
3442: dib-run-parts 2016年 10月 03日 星期一 23:14:03 CST ---------------------------------------  ----------
3443: dib-run-parts 2016年 10月 03日 星期一 23:14:03 CST
3444: dib-run-parts Mon Oct  3 23:14:03 CST 2016 01-ccache                                     0.025
3445: dib-run-parts Mon Oct  3 23:14:03 CST 2016 01-copy-manifests-dir                         0.129
3446: dib-run-parts Mon Oct  3 23:14:03 CST 2016 40-unblock-daemons                            0.079
3447: dib-run-parts Mon Oct  3 23:14:03 CST 2016 50-remove-img-build-proxy                     0.025
3448: dib-run-parts Mon Oct  3 23:14:03 CST 2016 51-bootloader                                 0.033
3449: dib-run-parts Mon Oct  3 23:14:03 CST 2016 60-untrim-dpkg                                0.028
3450: dib-run-parts Mon Oct  3 23:14:03 CST 2016 99-tidy-logs                                  0.034
3451: dib-run-parts 2016年 10月 03日 星期一 23:14:03 CST
3452: dib-run-parts 2016年 10月 03日 星期一 23:14:03 CST --------------------- END PROFILING ---------------------
3453: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:run_d:160 :   check_break after-cleanup bash
3454: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:check_break:98 :   egrep -e '(,|^)after-cleanup(,|$)' -q
3455: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:check_break:98 :   echo ''
3456: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:finalise_base:96 :   grep '^....i'
3457: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:finalise_base:96 :   lsattr /tmp/dib_build.1CFJZpLz/mnt/etc/resolv.conf
3458: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:finalise_base:102 :   sudo rm -f /tmp/dib_build.1CFJZpLz/mnt/etc/resolv.conf
3459: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:finalise_base:104 :   '[' -L /tmp/dib_build.1CFJZpLz/mnt/etc/resolv.conf.ORIG ']'
3460: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:finalise_base:105 :   sudo mv /tmp/dib_build.1CFJZpLz/mnt/etc/resolv.conf.ORIG /tmp/dib_build.1CFJZpLz/mnt/etc/resolv.conf
3461: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:finalise_base:109 :   '[' -d /tmp/dib_build.1CFJZpLz/mnt/tmp ']'
3462: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:finalise_base:110 :   unmount_dir /tmp/dib_build.1CFJZpLz/mnt/tmp
3463: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:247 :   local dir=/tmp/dib_build.1CFJZpLz/mnt/tmp
3464: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:248 :   local real_dir
3465: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:249 :   local mnts
3466: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:251 :   '[' '!' -d /tmp/dib_build.1CFJZpLz/mnt/tmp ']'
3467: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:258 :   readlink -e /tmp/dib_build.1CFJZpLz/mnt/tmp
3468: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:258 :   real_dir=/tmp/dib_build.1CFJZpLz/mnt/tmp
3469: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:260 :   grep '^/tmp/dib_build.1CFJZpLz/mnt/tmp'
3470: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:260 :   awk '{print $2}'
3471: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:260 :   sort -r
3472: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:260 :   mnts=
3473: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:finalise_base:112 :   xargs sudo rm -rf --one-file-system
3474: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:finalise_base:112 :   find /tmp/dib_build.1CFJZpLz/mnt/tmp -maxdepth 1 -mindepth 1
3475: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:430                  :   for X in '${!IMAGE_TYPES[@]}'
3476: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:431                  :   [[  tar aci  =~ qcow2 ]]
3477: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:449                  :   '[' qcow2 == docker ']'
3478: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:457                  :   [[ ! dib-python install-types install-bin dib-run-parts vm manifests dib-init-system cache-url pkg-map base ubuntu cloud-init-datasources bootloader package-installs dpkg dkms =~ no-final-image ]]
3479: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:459                  :   fstrim_image
3480: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:fstrim_image:37 :   sync
3481: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:fstrim_image:40 :   sudo fstrim /tmp/dib_build.1CFJZpLz/mnt
3482: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:464                  :   unmount_image
3483: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:unmount_image:22 :   sync
3484: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:unmount_image:26 :   unmount_dir /tmp/dib_build.1CFJZpLz/mnt
3485: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:247 :   local dir=/tmp/dib_build.1CFJZpLz/mnt
3486: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:248 :   local real_dir
3487: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:249 :   local mnts
3488: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:251 :   '[' '!' -d /tmp/dib_build.1CFJZpLz/mnt ']'
3489: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:258 :   readlink -e /tmp/dib_build.1CFJZpLz/mnt
3490: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:258 :   real_dir=/tmp/dib_build.1CFJZpLz/mnt
3491: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:260 :   awk '{print $2}'
3492: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:260 :   sort -r
3493: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:260 :   grep '^/tmp/dib_build.1CFJZpLz/mnt'
3494: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:260 :   mnts='/tmp/dib_build.1CFJZpLz/mnt/sys
3495: /tmp/dib_build.1CFJZpLz/mnt/proc
3496: /tmp/dib_build.1CFJZpLz/mnt/dev/pts
3497: /tmp/dib_build.1CFJZpLz/mnt/dev
3498: /tmp/dib_build.1CFJZpLz/mnt'
3499: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:261 :   for m in '$mnts'
3500: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:262 :   echo 'Unmount /tmp/dib_build.1CFJZpLz/mnt/sys'
3501: Unmount /tmp/dib_build.1CFJZpLz/mnt/sys
3502: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:263 :   sudo umount -fl /tmp/dib_build.1CFJZpLz/mnt/sys
3503: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:261 :   for m in '$mnts'
3504: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:262 :   echo 'Unmount /tmp/dib_build.1CFJZpLz/mnt/proc'
3505: Unmount /tmp/dib_build.1CFJZpLz/mnt/proc
3506: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:263 :   sudo umount -fl /tmp/dib_build.1CFJZpLz/mnt/proc
3507: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:261 :   for m in '$mnts'
3508: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:262 :   echo 'Unmount /tmp/dib_build.1CFJZpLz/mnt/dev/pts'
3509: Unmount /tmp/dib_build.1CFJZpLz/mnt/dev/pts
3510: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:263 :   sudo umount -fl /tmp/dib_build.1CFJZpLz/mnt/dev/pts
3511: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:261 :   for m in '$mnts'
3512: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:262 :   echo 'Unmount /tmp/dib_build.1CFJZpLz/mnt/dev'
3513: Unmount /tmp/dib_build.1CFJZpLz/mnt/dev
3514: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:263 :   sudo umount -fl /tmp/dib_build.1CFJZpLz/mnt/dev
3515: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:261 :   for m in '$mnts'
3516: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:262 :   echo 'Unmount /tmp/dib_build.1CFJZpLz/mnt'
3517: Unmount /tmp/dib_build.1CFJZpLz/mnt
3518: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:unmount_dir:263 :   sudo umount -fl /tmp/dib_build.1CFJZpLz/mnt
3519: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:unmount_image:27 :   '[' -n 'detach_loopback /dev/loop0' ']'
3520: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:unmount_image:28 :   detach_loopback /dev/loop0
3521: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:detach_loopback:164 :   local loopdev=/dev/loop0
3522: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:detach_loopback:169 :   echo /dev/loop0
3523: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:detach_loopback:169 :   sed 's/\/dev\///g'
3524: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:detach_loopback:169 :   loopdev_name=loop0
3525: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:detach_loopback:171 :   grep loop0
3526: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:detach_loopback:171 :   sudo dmsetup ls
3527: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:detach_loopback:177 :   seq 10 -1 1
3528: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:detach_loopback:177 :   for try in '$(seq 10 -1 1)'
3529: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:detach_loopback:178 :   sudo losetup /dev/loop0
3530: /dev/loop0: [0083]:3 (/tmp/dib_image.rja54tUR/image.raw)
3531: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:detach_loopback:178 :   sudo losetup -d /dev/loop0
3532: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:detach_loopback:179 :   return 0
3533: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:465                  :   cleanup_build_dir
3534: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:cleanup_build_dir:128 :   timeout 5 sh -c ' while ! sudo rm -rf /tmp/dib_build.1CFJZpLz/built; do sleep 1; done'
3535: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:cleanup_build_dir:132 :   sudo rm -rf /tmp/dib_build.1CFJZpLz/mnt
3536: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:cleanup_build_dir:133 :   tmpfs_check 0
3537: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:tmpfs_check:18 :   local echo_message=0
3538: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:tmpfs_check:19 :   '[' 0 == 0 ']'
3539: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:tmpfs_check:20 :   '[' -r /proc/meminfo ']'
3540: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:tmpfs_check:21 :   awk '/^MemTotal/ { print $2 }' /proc/meminfo
3541: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:tmpfs_check:21 :   total_kB=10220952
3542: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:tmpfs_check:24 :   RAM_NEEDED=4
3543: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:tmpfs_check:25 :   '[' 10220952 -lt 4194304 ']'
3544: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:tmpfs_check:25 :   return 0
3545: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:cleanup_build_dir:134 :   sudo umount -f /tmp/dib_build.1CFJZpLz
3546: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:cleanup_build_dir:136 :   rm -rf --one-file-system /tmp/dib_build.1CFJZpLz
3547: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:467                  :   [[ ! dib-python install-types install-bin dib-run-parts vm manifests dib-init-system cache-url pkg-map base ubuntu cloud-init-datasources bootloader package-installs dpkg dkms =~ no-final-image ]]
3548: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:467                  :   [[ 0 == \0 ]]
3549: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:468                  :   has_raw_type=
3550: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:469                  :   for IMAGE_TYPE in '${IMAGE_TYPES[@]}'
3551: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:471                  :   '[' qcow2 = raw ']'
3552: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:474                  :   compress_and_save_image image.qcow2
3553: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:compress_and_save_image:117 :   test qcow2 '!=' qcow2
3554: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:compress_and_save_image:118 :   '[' -n '' ']'
3555: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:compress_and_save_image:121 :   EXTRA_OPTIONS=
3556: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:compress_and_save_image:123 :   '[' qcow2 = raw ']'
3557: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:compress_and_save_image:125 :   '[' qcow2 == vhd ']'
3558: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:compress_and_save_image:133 :   echo 'Converting image using qemu-img convert'
3559: Converting image using qemu-img convert
3560: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:compress_and_save_image:134 :   qemu-img convert -c -f raw -O qcow2 /tmp/dib_image.rja54tUR/image.raw image.qcow2-new
3561: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:compress_and_save_image:137 :   OUT_IMAGE_PATH=image.qcow2-new
3562: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/img-functions:compress_and_save_image:138 :   finish_image image.qcow2
3563: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:finish_image:50 :   '[' -f image.qcow2 -a 0 -eq 0 ']'
3564: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:finish_image:56 :   mv image.qcow2-new image.qcow2
3565: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:finish_image:57 :   echo 'Image file image.qcow2 created...'
3566: Image file image.qcow2 created...
3567: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:477                  :   '[' -n '' ']'
3568: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:484                  :   cleanup_image_dir
3569: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:cleanup_image_dir:140 :   tmpfs_check 0
3570: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:tmpfs_check:18 :   local echo_message=0
3571: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:tmpfs_check:19 :   '[' 0 == 0 ']'
3572: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:tmpfs_check:20 :   '[' -r /proc/meminfo ']'
3573: ++ /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:tmpfs_check:21 :   awk '/^MemTotal/ { print $2 }' /proc/meminfo
3574: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:tmpfs_check:21 :   total_kB=10220952
3575: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:tmpfs_check:24 :   RAM_NEEDED=4
3576: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:tmpfs_check:25 :   '[' 10220952 -lt 4194304 ']'
3577: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:tmpfs_check:25 :   return 0
3578: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:cleanup_image_dir:141 :   sudo umount -f /tmp/dib_image.rja54tUR
3579: + /home/xion/gitRepo/openstack/env/share/diskimage-builder/lib/common-functions:cleanup_image_dir:143 :   rm -rf --one-file-system /tmp/dib_image.rja54tUR
3580: + /home/xion/gitRepo/openstack/env/bin/disk-image-create:main:487                  :   trap EXIT
```
