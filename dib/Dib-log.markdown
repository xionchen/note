```
1: Building elements: base  vm ubuntu
2: Expanded element dependencies to: dib-python install-types install-bin dib-run-parts vm manifests dib-init-system cache-url pkg-map base ubuntu cloud-init-datasources bootloader package-installs dpkg dkms
3: Building in /tmp/dib_build.Y0FGIa3a
4: dib-run-parts 2016年 10月 02日 星期日 12:16:38 CST Running /tmp/dib_build.Y0FGIa3a/hooks/root.d/01-ccache
5: dib-run-parts 2016年 10月 02日 星期日 12:16:38 CST 01-ccache completed
6: dib-run-parts 2016年 10月 02日 星期日 12:16:38 CST Running /tmp/dib_build.Y0FGIa3a/hooks/root.d/10-cache-ubuntu-tarball
7: + /tmp/dib_build.Y0FGIa3a/hooks/root.d/10-cache-ubuntu-tarball:main:7              :   set -eu
8: + /tmp/dib_build.Y0FGIa3a/hooks/root.d/10-cache-ubuntu-tarball:main:8              :   set -o pipefail
9: + /tmp/dib_build.Y0FGIa3a/hooks/root.d/10-cache-ubuntu-tarball:main:10             :   '[' -n amd64 ']'
10: + /tmp/dib_build.Y0FGIa3a/hooks/root.d/10-cache-ubuntu-tarball:main:11             :   '[' -n /tmp/dib_build.Y0FGIa3a/mnt ']'
11: + /tmp/dib_build.Y0FGIa3a/hooks/root.d/10-cache-ubuntu-tarball:main:13             :   shopt -s extglob
12: + /tmp/dib_build.Y0FGIa3a/hooks/root.d/10-cache-ubuntu-tarball:main:15             :   DIB_CLOUD_IMAGES=http://cloud-images.ubuntu.com
13: + /tmp/dib_build.Y0FGIa3a/hooks/root.d/10-cache-ubuntu-tarball:main:16             :   DIB_RELEASE=trusty
14: + /tmp/dib_build.Y0FGIa3a/hooks/root.d/10-cache-ubuntu-tarball:main:17             :   BASE_IMAGE_FILE=trusty-server-cloudimg-amd64-root.tar.gz
15: + /tmp/dib_build.Y0FGIa3a/hooks/root.d/10-cache-ubuntu-tarball:main:18             :   SHA256SUMS=https://cloud-images.ubuntu.com/trusty/current/SHA256SUMS
16: + /tmp/dib_build.Y0FGIa3a/hooks/root.d/10-cache-ubuntu-tarball:main:19             :   CACHED_FILE=/home/xion/.cache/image-create/trusty-server-cloudimg-amd64-root.tar.gz
17: + /tmp/dib_build.Y0FGIa3a/hooks/root.d/10-cache-ubuntu-tarball:main:20             :   CACHED_FILE_LOCK=/home/xion/.cache/image-create/trusty-server-cloudimg-amd64-root.tar.gz.lock
18: + /tmp/dib_build.Y0FGIa3a/hooks/root.d/10-cache-ubuntu-tarball:main:21             :   CACHED_SUMS=/home/xion/.cache/image-create/SHA256SUMS.ubuntu.trusty.amd64
19: ++ /tmp/dib_build.Y0FGIa3a/hooks/root.d/10-cache-ubuntu-tarball:main:54             :   date
20: + /tmp/dib_build.Y0FGIa3a/hooks/root.d/10-cache-ubuntu-tarball:main:54             :   echo 'Getting /home/xion/.cache/image-create/trusty-server-cloudimg-amd64-root.tar.gz.lock: 2016年 10月 02日 星期日 12:16:38 CST'
21: Getting /home/xion/.cache/image-create/trusty-server-cloudimg-amd64-root.tar.gz.lock: 2016年 10月 02日 星期日 12:16:38 CST
22: + /tmp/dib_build.Y0FGIa3a/hooks/root.d/10-cache-ubuntu-tarball:main:56             :   flock -w 1200 9
23: + /tmp/dib_build.Y0FGIa3a/hooks/root.d/10-cache-ubuntu-tarball:main:60             :   get_ubuntu_tarball
24: + /tmp/dib_build.Y0FGIa3a/hooks/root.d/10-cache-ubuntu-tarball:get_ubuntu_tarball:24 :   '[' -n '' -a -f /home/xion/.cache/image-create/trusty-server-cloudimg-amd64-root.tar.gz ']'
25: + /tmp/dib_build.Y0FGIa3a/hooks/root.d/10-cache-ubuntu-tarball:get_ubuntu_tarball:27 :   echo 'Fetching Base Image'
26: Fetching Base Image
27: + /tmp/dib_build.Y0FGIa3a/hooks/root.d/10-cache-ubuntu-tarball:get_ubuntu_tarball:28 :   /tmp/dib_build.Y0FGIa3a/hooks/bin/cache-url https://cloud-images.ubuntu.com/trusty/current/SHA256SUMS /home/xion/.cache/image-create/SHA256SUMS.ubuntu.trusty.amd64
28:   % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
29:                                  Dload  Upload   Total   Spent    Left  Speed
30:
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*   Trying 43.241.225.182...
31: * Connected to rosewood.h.xduotai.com (43.241.225.182) port 20105 (#0)
32: * Establish HTTP proxy tunnel to cloud-images.ubuntu.com:443
33: * Proxy auth using Basic with user 'duotai'
34: > CONNECT cloud-images.ubuntu.com:443 HTTP/1.1
35: > Host: cloud-images.ubuntu.com:443
36: > Proxy-Authorization: Basic ZHVvdGFpOnhFR3lMS05HUml1
37: > User-Agent: curl/7.47.0
38: > Proxy-Connection: Keep-Alive
39: >
40: < HTTP/1.1 200 Connection established
41: <
42: * Proxy replied OK to CONNECT request
43: * found 173 certificates in /etc/ssl/certs/ca-certificates.crt
44: * found 697 certificates in /etc/ssl/certs
45: * ALPN, offering http/1.1
46:
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0* SSL connection using TLS1.2 / ECDHE_RSA_AES_128_GCM_SHA256
47: * 	 server certificate verification OK
48: * 	 server certificate status verification SKIPPED
49: * 	 common name: cloud-images.ubuntu.com (matched)
50: * 	 server certificate expiration date OK
51: * 	 server certificate activation date OK
52: * 	 certificate public key: RSA
53: * 	 certificate version: #3
54: * 	 subject: C=GB,L=London,O=Canonical Group Ltd,CN=cloud-images.ubuntu.com
55: * 	 start date: Fri, 08 Jul 2016 00:00:00 GMT
56: * 	 expire date: Wed, 09 Aug 2017 12:00:00 GMT
57: * 	 issuer: C=US,O=DigiCert Inc,CN=DigiCert SHA2 Secure Server CA
58: * 	 compression: NULL
59: * ALPN, server did not agree to a protocol
60: > GET /trusty/current/SHA256SUMS HTTP/1.1
61: > Host: cloud-images.ubuntu.com
62: > User-Agent: curl/7.47.0
63: > Accept: */*
64: > If-Modified-Since: Sat, 01 Oct 2016 10:48:53 GMT
65: >
66: < HTTP/1.1 304 Not Modified
67: < Date: Sun, 02 Oct 2016 04:16:40 GMT
68: < Server: Apache
69: < ETag: "14806e4-c54-53d9acea91a40"
70: <
71:
  0     0    0     0    0     0      0      0 --:--:--  0:00:01 --:--:--     0
  0     0    0     0    0     0      0      0 --:--:--  0:00:01 --:--:--     0
72: * Connection #0 to host rosewood.h.xduotai.com left intact
73: Server copy has not changed. Using locally cached https://cloud-images.ubuntu.com/trusty/current/SHA256SUMS
74: + /tmp/dib_build.Y0FGIa3a/hooks/root.d/10-cache-ubuntu-tarball:get_ubuntu_tarball:30 :   /tmp/dib_build.Y0FGIa3a/hooks/bin/cache-url http://cloud-images.ubuntu.com/trusty/current/trusty-server-cloudimg-amd64-root.tar.gz /home/xion/.cache/image-create/trusty-server-cloudimg-amd64-root.tar.gz
75:   % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
76:                                  Dload  Upload   Total   Spent    Left  Speed
77:
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*   Trying 43.241.225.182...
78: * Connected to rosewood.h.xduotai.com (43.241.225.182) port 20105 (#0)
79: * Proxy auth using Basic with user 'duotai'
80: > GET http://cloud-images.ubuntu.com/trusty/current/trusty-server-cloudimg-amd64-root.tar.gz HTTP/1.1
81: > Host: cloud-images.ubuntu.com
82: > Proxy-Authorization: Basic ZHVvdGFpOnhFR3lMS05HUml1
83: > User-Agent: curl/7.47.0
84: > Accept: */*
85: > Proxy-Connection: Keep-Alive
86: > If-Modified-Since: Sat, 01 Oct 2016 11:12:57 GMT
87: >
88: < HTTP/1.1 304 Not Modified
89: < Date: Sun, 02 Oct 2016 04:16:41 GMT
90: < Server: Apache
91: < ETag: "14806ee-b51ded3-53d97d22bdfc0"
92: < X-Cache: MISS from 45-32-25-208
93: < X-Cache-Lookup: MISS from 45-32-25-208:1434
94: < Connection: keep-alive
95: <
96:
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
97: * Connection #0 to host rosewood.h.xduotai.com left intact
98: Server copy has not changed. Using locally cached http://cloud-images.ubuntu.com/trusty/current/trusty-server-cloudimg-amd64-root.tar.gz
99: + /tmp/dib_build.Y0FGIa3a/hooks/root.d/10-cache-ubuntu-tarball:get_ubuntu_tarball:31 :   pushd /home/xion/.cache/image-create
100: ~/.cache/image-create ~/gitRepo/openstack/diskimage-builder/elements
101: + /tmp/dib_build.Y0FGIa3a/hooks/root.d/10-cache-ubuntu-tarball:get_ubuntu_tarball:32 :   grep trusty-server-cloudimg-amd64-root.tar.gz /home/xion/.cache/image-create/SHA256SUMS.ubuntu.trusty.amd64
102: + /tmp/dib_build.Y0FGIa3a/hooks/root.d/10-cache-ubuntu-tarball:get_ubuntu_tarball:32 :   sha256sum --check -
103: trusty-server-cloudimg-amd64-root.tar.gz: OK
104: + /tmp/dib_build.Y0FGIa3a/hooks/root.d/10-cache-ubuntu-tarball:get_ubuntu_tarball:46 :   popd
105: ~/gitRepo/openstack/diskimage-builder/elements
106: + /tmp/dib_build.Y0FGIa3a/hooks/root.d/10-cache-ubuntu-tarball:get_ubuntu_tarball:50 :   sudo tar -C /tmp/dib_build.Y0FGIa3a/mnt --numeric-owner -xzf /home/xion/.cache/image-create/trusty-server-cloudimg-amd64-root.tar.gz
107: dib-run-parts 2016年 10月 02日 星期日 12:16:48 CST 10-cache-ubuntu-tarball completed
108: dib-run-parts 2016年 10月 02日 星期日 12:16:48 CST Running /tmp/dib_build.Y0FGIa3a/hooks/root.d/50-build-with-http-cache
109: 0+1 records in
110: 0+1 records out
111: 79 bytes copied, 3.4358e-05 s, 2.3 MB/s
112: dib-run-parts 2016年 10月 02日 星期日 12:16:48 CST 50-build-with-http-cache completed
113: dib-run-parts 2016年 10月 02日 星期日 12:16:48 CST Running /tmp/dib_build.Y0FGIa3a/hooks/root.d/60-block-apt-translations
114: 0+1 records in
115: 0+1 records out
116: 27 bytes copied, 4.0419e-05 s, 668 kB/s
117: /tmp/dib_build.Y0FGIa3a/mnt/var/lib/apt/lists/archive.ubuntu.com_ubuntu_dists_trusty-backports_main_i18n_Translation-en
118: /tmp/dib_build.Y0FGIa3a/mnt/var/lib/apt/lists/security.ubuntu.com_ubuntu_dists_trusty-security_universe_i18n_Translation-en
119: /tmp/dib_build.Y0FGIa3a/mnt/var/lib/apt/lists/security.ubuntu.com_ubuntu_dists_trusty-security_multiverse_i18n_Translation-en
120: /tmp/dib_build.Y0FGIa3a/mnt/var/lib/apt/lists/archive.ubuntu.com_ubuntu_dists_trusty-updates_multiverse_i18n_Translation-en
121: /tmp/dib_build.Y0FGIa3a/mnt/var/lib/apt/lists/archive.ubuntu.com_ubuntu_dists_trusty-backports_universe_i18n_Translation-en
122: /tmp/dib_build.Y0FGIa3a/mnt/var/lib/apt/lists/archive.ubuntu.com_ubuntu_dists_trusty-backports_multiverse_i18n_Translation-en
123: /tmp/dib_build.Y0FGIa3a/mnt/var/lib/apt/lists/archive.ubuntu.com_ubuntu_dists_trusty-updates_universe_i18n_Translation-en
124: /tmp/dib_build.Y0FGIa3a/mnt/var/lib/apt/lists/archive.ubuntu.com_ubuntu_dists_trusty-updates_main_i18n_Translation-en
125: /tmp/dib_build.Y0FGIa3a/mnt/var/lib/apt/lists/archive.ubuntu.com_ubuntu_dists_trusty_universe_i18n_Translation-en
126: /tmp/dib_build.Y0FGIa3a/mnt/var/lib/apt/lists/archive.ubuntu.com_ubuntu_dists_trusty_multiverse_i18n_Translation-en
127: /tmp/dib_build.Y0FGIa3a/mnt/var/lib/apt/lists/security.ubuntu.com_ubuntu_dists_trusty-security_restricted_i18n_Translation-en
128: /tmp/dib_build.Y0FGIa3a/mnt/var/lib/apt/lists/archive.ubuntu.com_ubuntu_dists_trusty-backports_restricted_i18n_Translation-en
129: /tmp/dib_build.Y0FGIa3a/mnt/var/lib/apt/lists/archive.ubuntu.com_ubuntu_dists_trusty_main_i18n_Translation-en
130: /tmp/dib_build.Y0FGIa3a/mnt/var/lib/apt/lists/archive.ubuntu.com_ubuntu_dists_trusty_restricted_i18n_Translation-en
131: /tmp/dib_build.Y0FGIa3a/mnt/var/lib/apt/lists/security.ubuntu.com_ubuntu_dists_trusty-security_main_i18n_Translation-en
132: /tmp/dib_build.Y0FGIa3a/mnt/var/lib/apt/lists/archive.ubuntu.com_ubuntu_dists_trusty-updates_restricted_i18n_Translation-en
133: dib-run-parts 2016年 10月 02日 星期日 12:16:48 CST 60-block-apt-translations completed
134: dib-run-parts 2016年 10月 02日 星期日 12:16:48 CST Running /tmp/dib_build.Y0FGIa3a/hooks/root.d/90-base-dib-run-parts
135: dib-run-parts 2016年 10月 02日 星期日 12:16:48 CST 90-base-dib-run-parts completed
136: dib-run-parts 2016年 10月 02日 星期日 12:16:48 CST Running /tmp/dib_build.Y0FGIa3a/hooks/root.d/99-block-daemons
137: 0+1 records in
138: 0+1 records out
139: 76 bytes copied, 3.9509e-05 s, 1.9 MB/s
140: 0+1 records in
141: 0+1 records out
142: 90 bytes copied, 3.4754e-05 s, 2.6 MB/s
143: 0+1 records in
144: 0+1 records out
145: 143 bytes copied, 3.3598e-05 s, 4.3 MB/s
146: dib-run-parts 2016年 10月 02日 星期日 12:16:48 CST 99-block-daemons completed
147: dib-run-parts 2016年 10月 02日 星期日 12:16:48 CST Running /tmp/dib_build.Y0FGIa3a/hooks/root.d/99-shared_apt_cache
148: dib-run-parts 2016年 10月 02日 星期日 12:16:48 CST 99-shared_apt_cache completed
149: dib-run-parts 2016年 10月 02日 星期日 12:16:48 CST Running /tmp/dib_build.Y0FGIa3a/hooks/root.d/99-trim-dpkg
150: dib-run-parts 2016年 10月 02日 星期日 12:16:48 CST 99-trim-dpkg completed
151: dib-run-parts 2016年 10月 02日 星期日 12:16:48 CST ----------------------- PROFILING -----------------------
152: dib-run-parts 2016年 10月 02日 星期日 12:16:48 CST
153: dib-run-parts 2016年 10月 02日 星期日 12:16:48 CST Target: root.d
154: dib-run-parts 2016年 10月 02日 星期日 12:16:48 CST
155: dib-run-parts 2016年 10月 02日 星期日 12:16:48 CST Script                                     Seconds
156: dib-run-parts 2016年 10月 02日 星期日 12:16:48 CST ---------------------------------------  ----------
157: dib-run-parts 2016年 10月 02日 星期日 12:16:48 CST
158: dib-run-parts Sun Oct  2 12:16:48 CST 2016 01-ccache                                     0.022
159: dib-run-parts Sun Oct  2 12:16:48 CST 2016 10-cache-ubuntu-tarball                       9.241
160: dib-run-parts Sun Oct  2 12:16:48 CST 2016 50-build-with-http-cache                      0.007
161: dib-run-parts Sun Oct  2 12:16:48 CST 2016 60-block-apt-translations                     0.016
162: dib-run-parts Sun Oct  2 12:16:48 CST 2016 90-base-dib-run-parts                         0.009
163: dib-run-parts Sun Oct  2 12:16:48 CST 2016 99-block-daemons                              0.047
164: dib-run-parts Sun Oct  2 12:16:48 CST 2016 99-shared_apt_cache                           0.016
165: dib-run-parts Sun Oct  2 12:16:48 CST 2016 99-trim-dpkg                                  0.012
166: dib-run-parts 2016年 10月 02日 星期日 12:16:48 CST
167: dib-run-parts 2016年 10月 02日 星期日 12:16:48 CST --------------------- END PROFILING ---------------------
168: dib-run-parts 2016年 10月 02日 星期日 12:16:48 CST Running /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/01-copy-apt-keys
169: DIB_ADD_APT_KEYS is not set - not importing keys
170: dib-run-parts 2016年 10月 02日 星期日 12:16:48 CST 01-copy-apt-keys completed
171: dib-run-parts 2016年 10月 02日 星期日 12:16:48 CST Running /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir
172: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:6          :   set -eu
173: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:7          :   set -o pipefail
174: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:9          :   sudo mkdir -p /tmp/dib_build.Y0FGIa3a/mnt/usr/share/pkg-map/
175: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:11         :   for ELEMENT in '$IMAGE_ELEMENT'
176: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:12         :   for DIR in '${ELEMENTS_PATH//:/ }'
177: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:13         :   '[' -f /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dib-python/pkg-map ']'
178: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:11         :   for ELEMENT in '$IMAGE_ELEMENT'
179: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:12         :   for DIR in '${ELEMENTS_PATH//:/ }'
180: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:13         :   '[' -f /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/install-types/pkg-map ']'
181: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:11         :   for ELEMENT in '$IMAGE_ELEMENT'
182: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:12         :   for DIR in '${ELEMENTS_PATH//:/ }'
183: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:13         :   '[' -f /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/install-bin/pkg-map ']'
184: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:11         :   for ELEMENT in '$IMAGE_ELEMENT'
185: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:12         :   for DIR in '${ELEMENTS_PATH//:/ }'
186: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:13         :   '[' -f /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dib-run-parts/pkg-map ']'
187: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:11         :   for ELEMENT in '$IMAGE_ELEMENT'
188: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:12         :   for DIR in '${ELEMENTS_PATH//:/ }'
189: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:13         :   '[' -f /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/vm/pkg-map ']'
190: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:11         :   for ELEMENT in '$IMAGE_ELEMENT'
191: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:12         :   for DIR in '${ELEMENTS_PATH//:/ }'
192: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:13         :   '[' -f /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/manifests/pkg-map ']'
193: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:11         :   for ELEMENT in '$IMAGE_ELEMENT'
194: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:12         :   for DIR in '${ELEMENTS_PATH//:/ }'
195: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:13         :   '[' -f /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dib-init-system/pkg-map ']'
196: +pmakr /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:11         :   for ELEMENT in '$IMAGE_ELEMENT'
197: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:12         :   for DIR in '${ELEMENTS_PATH//:/ }'
198: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:13         :   '[' -f /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/cache-url/pkg-map ']'
199: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:11         :   for ELEMENT in '$IMAGE_ELEMENT'
200: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:12         :   for DIR in '${ELEMENTS_PATH//:/ }'
201: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:13         :   '[' -f /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/pkg-map/pkg-map ']'
202: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:11         :   for ELEMENT in '$IMAGE_ELEMENT'
203: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:12         :   for DIR in '${ELEMENTS_PATH//:/ }'
204: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:13         :   '[' -f /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/base/pkg-map ']'
205: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:14         :   sudo cp /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/base/pkg-map /tmp/dib_build.Y0FGIa3a/mnt/usr/share/pkg-map/base
206: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:11         :   for ELEMENT in '$IMAGE_ELEMENT'
207: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:12         :   for DIR in '${ELEMENTS_PATH//:/ }'
208: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:13         :   '[' -f /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/ubuntu/pkg-map ']'
209: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:11         :   for ELEMENT in '$IMAGE_ELEMENT'
210: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:12         :   for DIR in '${ELEMENTS_PATH//:/ }'
211: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:13         :   '[' -f /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/cloud-init-datasources/pkg-map ']'
212: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:11         :   for ELEMENT in '$IMAGE_ELEMENT'
213: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:12         :   for DIR in '${ELEMENTS_PATH//:/ }'
214: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:13         :   '[' -f /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/bootloader/pkg-map ']'
215: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:14         :   sudo cp /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/bootloader/pkg-map /tmp/dib_build.Y0FGIa3a/mnt/usr/share/pkg-map/bootloader
216: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:11         :   for ELEMENT in '$IMAGE_ELEMENT'
217: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:12         :   for DIR in '${ELEMENTS_PATH//:/ }'
218: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:13         :   '[' -f /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/package-installs/pkg-map ']'
219: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:11         :   for ELEMENT in '$IMAGE_ELEMENT'
220: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:12         :   for DIR in '${ELEMENTS_PATH//:/ }'
221: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:13         :   '[' -f /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dpkg/pkg-map ']'
222: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:11         :   for ELEMENT in '$IMAGE_ELEMENT'
223: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:12         :   for DIR in '${ELEMENTS_PATH//:/ }'
224: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/10-create-pkg-map-dir:main:13         :   '[' -f /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/elements/dkms/pkg-map ']'
225: dib-run-parts 2016年 10月 02日 星期日 12:16:48 CST 10-create-pkg-map-dir completed
226: dib-run-parts 2016年 10月 02日 星期日 12:16:48 CST Running /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/20-manifest-dir
227: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/20-manifest-dir:main:21               :   set -eu
228: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/20-manifest-dir:main:22               :   set -o pipefail
229: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/20-manifest-dir:main:24               :   sudo mkdir -p /tmp/dib_build.Y0FGIa3a/mnt//etc/dib-manifests
230: dib-run-parts 2016年 10月 02日 星期日 12:16:48 CST 20-manifest-dir completed
231: dib-run-parts 2016年 10月 02日 星期日 12:16:48 CST Running /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/50-store-build-settings
232: dib-run-parts 2016年 10月 02日 星期日 12:16:48 CST 50-store-build-settings completed
233: dib-run-parts 2016年 10月 02日 星期日 12:16:48 CST Running /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/99-enable-install-types
234: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/99-enable-install-types:main:19       :   set -eu
235: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/99-enable-install-types:main:20       :   set -o pipefail
236: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/99-enable-install-types:main:22       :   declare -a SPECIFIED_ELEMS
237: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/99-enable-install-types:main:26       :   SPECIFIED_ELEMS[0]=
238: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/99-enable-install-types:main:29       :   PREFIX=DIB_INSTALLTYPE_
239: ++ /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/99-enable-install-types:main:30       :   cut -d= -f1
240: ++ /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/99-enable-install-types:main:30       :   env
241: ++ /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/99-enable-install-types:main:30       :   grep '^DIB_INSTALLTYPE_'
242: ++ /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/99-enable-install-types:main:30       :   echo ''
243: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/99-enable-install-types:main:30       :   INSTALL_TYPE_VARS=
244: ++ /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/99-enable-install-types:main:53       :   find /tmp/dib_build.Y0FGIa3a/hooks/install.d -maxdepth 1 -name '*-source-install' -type d
245: + /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/99-enable-install-types:main:53       :   default_install_type_dirs=
246: dib-run-parts 2016年 10月 02日 星期日 12:16:48 CST 99-enable-install-types completed
247: dib-run-parts 2016年 10月 02日 星期日 12:16:48 CST Running /tmp/dib_build.Y0FGIa3a/hooks/extra-data.d/99-squash-package-install
248: dib-run-parts 2016年 10月 02日 星期日 12:16:48 CST 99-squash-package-install completed
249: dib-run-parts 2016年 10月 02日 星期日 12:16:48 CST ----------------------- PROFILING -----------------------
250: dib-run-parts 2016年 10月 02日 星期日 12:16:48 CST
251: dib-run-parts 2016年 10月 02日 星期日 12:16:48 CST Target: extra-data.d
252: dib-run-parts 2016年 10月 02日 星期日 12:16:48 CST
253: dib-run-parts 2016年 10月 02日 星期日 12:16:48 CST Script                                     Seconds
254: dib-run-parts 2016年 10月 02日 星期日 12:16:48 CST ---------------------------------------  ----------
255: dib-run-parts 2016年 10月 02日 星期日 12:16:48 CST
256: dib-run-parts Sun Oct  2 12:16:48 CST 2016 01-copy-apt-keys                              0.002
257: dib-run-parts Sun Oct  2 12:16:48 CST 2016 10-create-pkg-map-dir                         0.111
258: dib-run-parts Sun Oct  2 12:16:48 CST 2016 20-manifest-dir                               0.014
259: dib-run-parts Sun Oct  2 12:16:48 CST 2016 50-store-build-settings                       0.004
260: dib-run-parts Sun Oct  2 12:16:48 CST 2016 99-enable-install-types                       0.022
261: dib-run-parts Sun Oct  2 12:16:48 CST 2016 99-squash-package-install                     0.085
262: dib-run-parts 2016年 10月 02日 星期日 12:16:48 CST
263: dib-run-parts 2016年 10月 02日 星期日 12:16:48 CST --------------------- END PROFILING ---------------------
264: dib-run-parts Sun Oct  2 04:16:48 UTC 2016 Running /tmp/in_target.d/pre-install.d/00-disable-apt-recommends
265: 0+1 records in
266: 0+1 records out
267: 56 bytes (56 B) copied, 3.4879e-05 s, 1.6 MB/s
268: dib-run-parts Sun Oct  2 04:16:48 UTC 2016 00-disable-apt-recommends completed
269: dib-run-parts Sun Oct  2 04:16:48 UTC 2016 Running /tmp/in_target.d/pre-install.d/00-remove-apt-xapian-index
270: Reading package lists...
271: Building dependency tree...
272: Reading state information...
273: The following packages were automatically installed and are no longer required:
274:   libfreetype6 os-prober
275: Use 'apt-get autoremove' to remove them.
276: The following packages will be REMOVED:
277:   apt-xapian-index
278: perl: warning: Setting locale failed.
279: perl: warning: Please check that your locale settings:
280: 	LANGUAGE = "en_US",
281: 	LC_ALL = (unset),
282: 	LC_TIME = "zh_CN.UTF-8",
283: 	LC_MONETARY = "zh_CN.UTF-8",
284: 	LC_CTYPE = "en_US.UTF-8",
285: 	LC_ADDRESS = "zh_CN.UTF-8",
286: 	LC_TELEPHONE = "zh_CN.UTF-8",
287: 	LC_NAME = "zh_CN.UTF-8",
288: 	LC_MEASUREMENT = "zh_CN.UTF-8",
289: 	LC_IDENTIFICATION = "zh_CN.UTF-8",
290: 	LC_NUMERIC = "zh_CN.UTF-8",
291: 	LC_PAPER = "zh_CN.UTF-8",
292: 	LANG = "C"
293:     are supported and installed on your system.
294: perl: warning: Falling back to the standard locale ("C").
295: locale: Cannot set LC_ALL to default locale: No such file or directory
296: 0 upgraded, 0 newly installed, 1 to remove and 0 not upgraded.
297: After this operation, 336 kB disk space will be freed.
298: (Reading database ... 25010 files and directories currently installed.)
299: Removing apt-xapian-index (0.45ubuntu4) ...
300: Removing index /var/lib/apt-xapian-index...
301: Processing triggers for man-db (2.6.7.1-1ubuntu1) ...
302: dib-run-parts Sun Oct  2 04:16:50 UTC 2016 00-remove-apt-xapian-index completed
303: dib-run-parts Sun Oct  2 04:16:50 UTC 2016 Running /tmp/in_target.d/pre-install.d/00-remove-grub
304: dpkg-query: no packages found matching grub-pc
305: dpkg-query: no packages found matching grub2-common
306: dib-run-parts Sun Oct  2 04:16:50 UTC 2016 00-remove-grub completed
307: dib-run-parts Sun Oct  2 04:16:50 UTC 2016 Running /tmp/in_target.d/pre-install.d/01-dib-python
308: dib-run-parts Sun Oct  2 04:16:50 UTC 2016 01-dib-python completed
309: dib-run-parts Sun Oct  2 04:16:50 UTC 2016 Running /tmp/in_target.d/pre-install.d/01-install-bin
310: dib-run-parts Sun Oct  2 04:16:50 UTC 2016 01-install-bin completed
311: dib-run-parts Sun Oct  2 04:16:50 UTC 2016 Running /tmp/in_target.d/pre-install.d/01-set-ubuntu-mirror
312: dib-run-parts Sun Oct  2 04:16:50 UTC 2016 01-set-ubuntu-mirror completed
313: dib-run-parts Sun Oct  2 04:16:50 UTC 2016 Running /tmp/in_target.d/pre-install.d/02-add-apt-keys
314: dib-run-parts Sun Oct  2 04:16:50 UTC 2016 02-add-apt-keys completed
315: dib-run-parts Sun Oct  2 04:16:50 UTC 2016 Running /tmp/in_target.d/pre-install.d/02-package-installs
316: + set -eu
317: + set -o pipefail
318: ++ basename /usr/local/bin/package-installs
319: + SCRIPTNAME=package-installs
320: ++ getopt -o hd: -n package-installs -- -d /tmp/in_target.d/pre-install.d
321: + TEMP=' -d '\''/tmp/in_target.d/pre-install.d'\'' --'
322: + '[' 0 '!=' 0 ']'
323: + eval set -- ' -d '\''/tmp/in_target.d/pre-install.d'\'' --'
324: ++ set -- -d /tmp/in_target.d/pre-install.d --
325: + WORKDIR=
326: + true
327: + case "$1" in
328: + WORKDIR=/tmp/in_target.d/pre-install.d
329: + shift 2
330: + true
331: + case "$1" in
332: + shift
333: + break
334: + '[' -z /tmp/in_target.d/pre-install.d ']'
335: + PACKAGES=
336: ++ find /tmp/in_target.d/pre-install.d -maxdepth 1 -name 'package-installs-*'
337: + '[' -n '' ']'
338: Nothing to install
339: dib-run-parts Sun Oct  2 04:16:50 UTC 2016 02-package-installs completed
340: dib-run-parts Sun Oct  2 04:16:50 UTC 2016 Running /tmp/in_target.d/pre-install.d/03-baseline-tools
341: Get:1 http://security.ubuntu.com trusty-security InRelease [65.9 kB]
342: Ign http://archive.ubuntu.com trusty InRelease
343: Get:2 http://archive.ubuntu.com trusty-updates InRelease [65.9 kB]
344: Get:3 http://security.ubuntu.com trusty-security/main amd64 Packages [531 kB]
345: Hit http://archive.ubuntu.com trusty-backports InRelease
346: Hit http://archive.ubuntu.com trusty Release.gpg
347: Get:4 http://archive.ubuntu.com trusty-updates/main amd64 Packages [901 kB]
348: Get:5 http://security.ubuntu.com trusty-security/restricted amd64 Packages [13.0 kB]
349: Get:6 http://security.ubuntu.com trusty-security/universe amd64 Packages [138 kB]
350: Get:7 http://security.ubuntu.com trusty-security/multiverse amd64 Packages [5198 B]
351: Get:8 http://archive.ubuntu.com trusty-updates/restricted amd64 Packages [15.9 kB]
352: Get:9 http://archive.ubuntu.com trusty-updates/universe amd64 Packages [376 kB]
353: Get:10 http://archive.ubuntu.com trusty-updates/multiverse amd64 Packages [15.0 kB]
354: Hit http://archive.ubuntu.com trusty-backports/main amd64 Packages
355: Hit http://archive.ubuntu.com trusty-backports/restricted amd64 Packages
356: Hit http://archive.ubuntu.com trusty-backports/universe amd64 Packages
357: Hit http://archive.ubuntu.com trusty-backports/multiverse amd64 Packages
358: Hit http://archive.ubuntu.com trusty Release
359: Hit http://archive.ubuntu.com trusty/main amd64 Packages
360: Hit http://archive.ubuntu.com trusty/restricted amd64 Packages
361: Hit http://archive.ubuntu.com trusty/universe amd64 Packages
362: Hit http://archive.ubuntu.com trusty/multiverse amd64 Packages
363: Fetched 2126 kB in 1min 12s (29.2 kB/s)
364: Reading package lists...
365: Reading package lists...
366: Building dependency tree...
367: Reading state information...
368: software-properties-common is already the newest version.
369: The following packages were automatically installed and are no longer required:
370:   libfreetype6 os-prober
371: Use 'apt-get autoremove' to remove them.
372: 0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
373: dib-run-parts Sun Oct  2 04:18:04 UTC 2016 03-baseline-tools completed
374: dib-run-parts Sun Oct  2 04:18:04 UTC 2016 Running /tmp/in_target.d/pre-install.d/04-dib-init-system
375: dib-run-parts Sun Oct  2 04:18:04 UTC 2016 04-dib-init-system completed
376: dib-run-parts Sun Oct  2 04:18:04 UTC 2016 Running /tmp/in_target.d/pre-install.d/99-apt-get-update
377: Ign http://archive.ubuntu.com trusty InRelease
378: Hit http://security.ubuntu.com trusty-security InRelease
379: Hit http://archive.ubuntu.com trusty-updates InRelease
380: Hit http://security.ubuntu.com trusty-security/main amd64 Packages
381: Hit http://archive.ubuntu.com trusty-backports InRelease
382: Hit http://security.ubuntu.com trusty-security/restricted amd64 Packages
383: Hit http://archive.ubuntu.com trusty Release.gpg
384: Hit http://security.ubuntu.com trusty-security/universe amd64 Packages
385: Hit http://archive.ubuntu.com trusty-updates/main amd64 Packages
386: Hit http://security.ubuntu.com trusty-security/multiverse amd64 Packages
387: Hit http://archive.ubuntu.com trusty-updates/restricted amd64 Packages
388: Hit http://archive.ubuntu.com trusty-updates/universe amd64 Packages
389: Hit http://archive.ubuntu.com trusty-updates/multiverse amd64 Packages
390: Hit http://archive.ubuntu.com trusty-backports/main amd64 Packages
391: Hit http://archive.ubuntu.com trusty-backports/restricted amd64 Packages
392: Hit http://archive.ubuntu.com trusty-backports/universe amd64 Packages
393: Hit http://archive.ubuntu.com trusty-backports/multiverse amd64 Packages
394: Hit http://archive.ubuntu.com trusty Release
395: Hit http://archive.ubuntu.com trusty/main amd64 Packages
396: Hit http://archive.ubuntu.com trusty/restricted amd64 Packages
397: Hit http://archive.ubuntu.com trusty/universe amd64 Packages
398: Hit http://archive.ubuntu.com trusty/multiverse amd64 Packages
399: Reading package lists...
400: dib-run-parts Sun Oct  2 04:18:12 UTC 2016 99-apt-get-update completed
401: dib-run-parts Sun Oct  2 04:18:12 UTC 2016 Running /tmp/in_target.d/pre-install.d/99-package-uninstalls
402: + set -eu
403: + set -o pipefail
404: ++ basename /usr/local/bin/package-uninstalls
405: + SCRIPTNAME=package-uninstalls
406: ++ getopt -o hd: -n package-uninstalls -- -d /tmp/in_target.d/pre-install.d
407: + TEMP=' -d '\''/tmp/in_target.d/pre-install.d'\'' --'
408: + '[' 0 '!=' 0 ']'
409: + eval set -- ' -d '\''/tmp/in_target.d/pre-install.d'\'' --'
410: ++ set -- -d /tmp/in_target.d/pre-install.d --
411: + WORKDIR=
412: + true
413: + case "$1" in
414: + WORKDIR=/tmp/in_target.d/pre-install.d
415: + shift 2
416: + true
417: + case "$1" in
418: + shift
419: + break
420: + '[' -z /tmp/in_target.d/pre-install.d ']'
421: + PACKAGES=
422: ++ find /tmp/in_target.d/pre-install.d -maxdepth 1 -name 'package-installs-*'
423: + install-packages -e
424: Not running install-packages remove with empty packages list
425: Nothing to uninstall
426: dib-run-parts Sun Oct  2 04:18:12 UTC 2016 99-package-uninstalls completed
427: dib-run-parts Sun Oct  2 04:18:12 UTC 2016 ----------------------- PROFILING -----------------------
428: dib-run-parts Sun Oct  2 04:18:12 UTC 2016
429: dib-run-parts Sun Oct  2 04:18:12 UTC 2016 Target: pre-install.d
430: dib-run-parts Sun Oct  2 04:18:12 UTC 2016
431: dib-run-parts Sun Oct  2 04:18:12 UTC 2016 Script                                     Seconds
432: dib-run-parts Sun Oct  2 04:18:12 UTC 2016 ---------------------------------------  ----------
433: dib-run-parts Sun Oct  2 04:18:12 UTC 2016
434: dib-run-parts Sun Oct  2 04:18:12 UTC 2016 00-disable-apt-recommends                     0.003
435: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
436: dib-run-parts Sun Oct  2 04:18:12 UTC 2016 00-remove-apt-xapian-index                    1.812
437: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
438: dib-run-parts Sun Oct  2 04:18:12 UTC 2016 00-remove-grub                                0.018
439: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
440: dib-run-parts Sun Oct  2 04:18:12 UTC 2016 01-dib-python                                 0.003
441: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
442: dib-run-parts Sun Oct  2 04:18:12 UTC 2016 01-install-bin                                0.004
443: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
444: dib-run-parts Sun Oct  2 04:18:12 UTC 2016 01-set-ubuntu-mirror                          0.002
445: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
446: dib-run-parts Sun Oct  2 04:18:12 UTC 2016 02-add-apt-keys                               0.002
447: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
448: dib-run-parts Sun Oct  2 04:18:12 UTC 2016 02-package-installs                           0.029
449: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
450: dib-run-parts Sun Oct  2 04:18:12 UTC 2016 03-baseline-tools                            74.288
451: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
452: dib-run-parts Sun Oct  2 04:18:12 UTC 2016 04-dib-init-system                            0.007
453: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
454: dib-run-parts Sun Oct  2 04:18:12 UTC 2016 99-apt-get-update                             7.819
455: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
456: dib-run-parts Sun Oct  2 04:18:12 UTC 2016 99-package-uninstalls                         0.070
457: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
458: dib-run-parts Sun Oct  2 04:18:12 UTC 2016
459: dib-run-parts Sun Oct  2 04:18:12 UTC 2016 --------------------- END PROFILING ---------------------
460: dib-run-parts Sun Oct  2 04:18:12 UTC 2016 Running /tmp/in_target.d/install.d/00-baseline-environment
461: Reading package lists...
462: Building dependency tree...
463: Reading state information...
464: The following packages were automatically installed and are no longer required:
465:   libfreetype6 os-prober
466: Use 'apt-get autoremove' to remove them.
467: The following NEW packages will be installed:
468:   open-iscsi
469: perl: warning: Setting locale failed.
470: perl: warning: Please check that your locale settings:
471: 	LANGUAGE = "en_US",
472: 	LC_ALL = (unset),
473: 	LC_TIME = "zh_CN.UTF-8",
474: 	LC_MONETARY = "zh_CN.UTF-8",
475: 	LC_CTYPE = "en_US.UTF-8",
476: 	LC_ADDRESS = "zh_CN.UTF-8",
477: 	LC_TELEPHONE = "zh_CN.UTF-8",
478: 	LC_NAME = "zh_CN.UTF-8",
479: 	LC_MEASUREMENT = "zh_CN.UTF-8",
480: 	LC_IDENTIFICATION = "zh_CN.UTF-8",
481: 	LC_NUMERIC = "zh_CN.UTF-8",
482: 	LC_PAPER = "zh_CN.UTF-8",
483: 	LANG = "C"
484:     are supported and installed on your system.
485: perl: warning: Falling back to the standard locale ("C").
486: locale: Cannot set LC_ALL to default locale: No such file or directory
487: 0 upgraded, 1 newly installed, 0 to remove and 0 not upgraded.
488: Need to get 0 B/268 kB of archives.
489: After this operation, 2221 kB of additional disk space will be used.
490: Selecting previously unselected package open-iscsi.
491: (Reading database ... 24956 files and directories currently installed.)
492: Preparing to unpack .../open-iscsi_2.0.873-3ubuntu9_amd64.deb ...
493: Unpacking open-iscsi (2.0.873-3ubuntu9) ...
494: Processing triggers for man-db (2.6.7.1-1ubuntu1) ...
495: Processing triggers for ureadahead (0.100.0-16) ...
496: Setting up open-iscsi (2.0.873-3ubuntu9) ...
497: Processing triggers for ureadahead (0.100.0-16) ...
498: dib-run-parts Sun Oct  2 04:18:13 UTC 2016 00-baseline-environment completed
499: dib-run-parts Sun Oct  2 04:18:13 UTC 2016 Running /tmp/in_target.d/install.d/00-up-to-date
500: Reading package lists...
501: Building dependency tree...
502: Reading state information...
503: The following packages were automatically installed and are no longer required:
504:   libfreetype6 os-prober
505: Use 'apt-get autoremove' to remove them.
506: 0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
507: dib-run-parts Sun Oct  2 04:18:14 UTC 2016 00-up-to-date completed
508: dib-run-parts Sun Oct  2 04:18:14 UTC 2016 Running /tmp/in_target.d/install.d/01-package-installs
509: + set -eu
510: + set -o pipefail
511: ++ basename /usr/local/bin/package-installs
512: + SCRIPTNAME=package-installs
513: ++ getopt -o hd: -n package-installs -- -d /tmp/in_target.d/install.d
514: + TEMP=' -d '\''/tmp/in_target.d/install.d'\'' --'
515: + '[' 0 '!=' 0 ']'
516: + eval set -- ' -d '\''/tmp/in_target.d/install.d'\'' --'
517: ++ set -- -d /tmp/in_target.d/install.d --
518: + WORKDIR=
519: + true
520: + case "$1" in
521: + WORKDIR=/tmp/in_target.d/install.d
522: + shift 2
523: + true
524: + case "$1" in
525: + shift
526: + break
527: + '[' -z /tmp/in_target.d/install.d ']'
528: + PACKAGES=
529: ++ find /tmp/in_target.d/install.d -maxdepth 1 -name 'package-installs-*'
530: + '[' -n '' ']'
531: perl: warning: Setting locale failed.
532: perl: warning: Please check that your locale settings:
533: 	LANGUAGE = "en_US",
534: 	LC_ALL = (unset),
535: 	LC_TIME = "zh_CN.UTF-8",
536: 	LC_MONETARY = "zh_CN.UTF-8",
537: 	LC_CTYPE = "en_US.UTF-8",
538: 	LC_ADDRESS = "zh_CN.UTF-8",
539: 	LC_TELEPHONE = "zh_CN.UTF-8",
540: 	LC_NAME = "zh_CN.UTF-8",
541: 	LC_MEASUREMENT = "zh_CN.UTF-8",
542: 	LC_IDENTIFICATION = "zh_CN.UTF-8",
543: 	LC_NUMERIC = "zh_CN.UTF-8",
544: 	LC_PAPER = "zh_CN.UTF-8",
545: 	LANG = "C"
546:     are supported and installed on your system.
547: perl: warning: Falling back to the standard locale ("C").
548: locale: Cannot set LC_ALL to default locale: No such file or directory
549: locale: Cannot set LC_ALL to default locale: No such file or directory
550: Done.
551: Running depmod.
552: update-initramfs: deferring update (hook will be called later)
553: Examining /etc/kernel/postinst.d.
554: run-parts: executing /etc/kernel/postinst.d/apt-auto-removal 3.13.0-96-generic /boot/vmlinuz-3.13.0-96-generic
555: run-parts: executing /etc/kernel/postinst.d/initramfs-tools 3.13.0-96-generic /boot/vmlinuz-3.13.0-96-generic
556: update-initramfs: Generating /boot/initrd.img-3.13.0-96-generic
557: run-parts: executing /etc/kernel/postinst.d/update-notifier 3.13.0-96-generic /boot/vmlinuz-3.13.0-96-generic
558: run-parts: executing /etc/kernel/postinst.d/apt-auto-removal 3.13.0-96-generic /boot/vmlinuz-3.13.0-96-generic
559: run-parts: executing /etc/kernel/postinst.d/dkms 3.13.0-96-generic /boot/vmlinuz-3.13.0-96-generic
560: run-parts: executing /etc/kernel/postinst.d/initramfs-tools 3.13.0-96-generic /boot/vmlinuz-3.13.0-96-generic
561: update-initramfs: Generating /boot/initrd.img-3.13.0-96-generic
562: run-parts: executing /etc/kernel/postinst.d/update-notifier 3.13.0-96-generic /boot/vmlinuz-3.13.0-96-generic
563: installing ccache_package from base
564: installing linux-image-generic from ubuntu
565: installing dkms from dkms
566: dib-run-parts Sun Oct  2 04:18:51 UTC 2016 01-package-installs completed
567: dib-run-parts Sun Oct  2 04:18:51 UTC 2016 Running /tmp/in_target.d/install.d/05-set-cloud-init-sources
568: dib-run-parts Sun Oct  2 04:18:51 UTC 2016 05-set-cloud-init-sources completed
569: dib-run-parts Sun Oct  2 04:18:51 UTC 2016 Running /tmp/in_target.d/install.d/10-cloud-init
570: dib-run-parts Sun Oct  2 04:18:51 UTC 2016 10-cloud-init completed
571: dib-run-parts Sun Oct  2 04:18:51 UTC 2016 Running /tmp/in_target.d/install.d/20-install-init-scripts
572: + set -eu
573: + set -o pipefail
574: ++ dirname /tmp/in_target.d/install.d/20-install-init-scripts
575: + scripts_dir=/tmp/in_target.d/install.d/../init-scripts/upstart/
576: + '[' -d /tmp/in_target.d/install.d/../init-scripts/upstart/ ']'
577: dib-run-parts Sun Oct  2 04:18:51 UTC 2016 20-install-init-scripts completed
578: dib-run-parts Sun Oct  2 04:18:51 UTC 2016 Running /tmp/in_target.d/install.d/50-store-build-settings
579: dib-run-parts Sun Oct  2 04:18:51 UTC 2016 50-store-build-settings completed
580: dib-run-parts Sun Oct  2 04:18:51 UTC 2016 Running /tmp/in_target.d/install.d/80-disable-rfc3041
581: dib-run-parts Sun Oct  2 04:18:51 UTC 2016 80-disable-rfc3041 completed
582: dib-run-parts Sun Oct  2 04:18:51 UTC 2016 Running /tmp/in_target.d/install.d/99-autoremove
583: + set -eu
584: + set -o pipefail
585: + apt-get -y autoremove
586: Reading package lists...
587: Building dependency tree...
588: Reading state information...
589: The following packages will be REMOVED:
590:   libfreetype6 os-prober
591: perl: warning: Setting locale failed.
592: perl: warning: Please check that your locale settings:
593: 	LANGUAGE = "en_US",
594: 	LC_ALL = (unset),
595: 	LC_TIME = "zh_CN.UTF-8",
596: 	LC_MONETARY = "zh_CN.UTF-8",
597: 	LC_CTYPE = "en_US.UTF-8",
598: 	LC_ADDRESS = "zh_CN.UTF-8",
599: 	LC_TELEPHONE = "zh_CN.UTF-8",
600: 	LC_NAME = "zh_CN.UTF-8",
601: 	LC_MEASUREMENT = "zh_CN.UTF-8",
602: 	LC_IDENTIFICATION = "zh_CN.UTF-8",
603: 	LC_NUMERIC = "zh_CN.UTF-8",
604: 	LC_PAPER = "zh_CN.UTF-8",
605: 	LANG = "C"
606:     are supported and installed on your system.
607: perl: warning: Falling back to the standard locale ("C").
608: locale: Cannot set LC_ALL to default locale: No such file or directory
609: 0 upgraded, 0 newly installed, 2 to remove and 0 not upgraded.
610: After this operation, 1063 kB disk space will be freed.
611: (Reading database ... 31518 files and directories currently installed.)
612: Removing libfreetype6:amd64 (2.5.2-1ubuntu2.5) ...
613: Removing os-prober (1.63ubuntu1.1) ...
614: Processing triggers for libc-bin (2.19-0ubuntu6.9) ...
615: dib-run-parts Sun Oct  2 04:18:52 UTC 2016 99-autoremove completed
616: dib-run-parts Sun Oct  2 04:18:52 UTC 2016 Running /tmp/in_target.d/install.d/99-package-uninstalls
617: + set -eu
618: + set -o pipefail
619: ++ basename /usr/local/bin/package-uninstalls
620: + SCRIPTNAME=package-uninstalls
621: ++ getopt -o hd: -n package-uninstalls -- -d /tmp/in_target.d/install.d
622: + TEMP=' -d '\''/tmp/in_target.d/install.d'\'' --'
623: + '[' 0 '!=' 0 ']'
624: + eval set -- ' -d '\''/tmp/in_target.d/install.d'\'' --'
625: ++ set -- -d /tmp/in_target.d/install.d --
626: + WORKDIR=
627: + true
628: + case "$1" in
629: + WORKDIR=/tmp/in_target.d/install.d
630: + shift 2
631: + true
632: + case "$1" in
633: + shift
634: + break
635: + '[' -z /tmp/in_target.d/install.d ']'
636: + PACKAGES=
637: ++ find /tmp/in_target.d/install.d -maxdepth 1 -name 'package-installs-*'
638: + install-packages -e
639: Not running install-packages remove with empty packages list
640: Nothing to uninstall
641: dib-run-parts Sun Oct  2 04:18:52 UTC 2016 99-package-uninstalls completed
642: dib-run-parts Sun Oct  2 04:18:52 UTC 2016 ----------------------- PROFILING -----------------------
643: dib-run-parts Sun Oct  2 04:18:52 UTC 2016
644: dib-run-parts Sun Oct  2 04:18:52 UTC 2016 Target: install.d
645: dib-run-parts Sun Oct  2 04:18:52 UTC 2016
646: dib-run-parts Sun Oct  2 04:18:52 UTC 2016 Script                                     Seconds
647: dib-run-parts Sun Oct  2 04:18:52 UTC 2016 ---------------------------------------  ----------
648: dib-run-parts Sun Oct  2 04:18:52 UTC 2016
649: dib-run-parts Sun Oct  2 04:18:52 UTC 2016 00-baseline-environment                       0.759
650: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
651: dib-run-parts Sun Oct  2 04:18:52 UTC 2016 00-up-to-date                                 0.520
652: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
653: dib-run-parts Sun Oct  2 04:18:52 UTC 2016 01-package-installs                          37.203
654: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
655: dib-run-parts Sun Oct  2 04:18:52 UTC 2016 05-set-cloud-init-sources                     0.042
656: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
657: dib-run-parts Sun Oct  2 04:18:52 UTC 2016 10-cloud-init                                 0.003
658: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
659: dib-run-parts Sun Oct  2 04:18:52 UTC 2016 20-install-init-scripts                       0.003
660: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
661: dib-run-parts Sun Oct  2 04:18:52 UTC 2016 50-store-build-settings                       0.004
662: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
663: dib-run-parts Sun Oct  2 04:18:52 UTC 2016 80-disable-rfc3041                            0.003
664: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
665: dib-run-parts Sun Oct  2 04:18:52 UTC 2016 99-autoremove                                 0.585
666: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
667: dib-run-parts Sun Oct  2 04:18:52 UTC 2016 99-package-uninstalls                         0.043
668: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
669: dib-run-parts Sun Oct  2 04:18:52 UTC 2016
670: dib-run-parts Sun Oct  2 04:18:52 UTC 2016 --------------------- END PROFILING ---------------------
671: dib-run-parts Sun Oct  2 04:18:52 UTC 2016 Running /tmp/in_target.d/post-install.d/00-package-installs
672: + set -eu
673: + set -o pipefail
674: ++ basename /usr/local/bin/package-installs
675: + SCRIPTNAME=package-installs
676: ++ getopt -o hd: -n package-installs -- -d /tmp/in_target.d/post-install.d
677: + TEMP=' -d '\''/tmp/in_target.d/post-install.d'\'' --'
678: + '[' 0 '!=' 0 ']'
679: + eval set -- ' -d '\''/tmp/in_target.d/post-install.d'\'' --'
680: ++ set -- -d /tmp/in_target.d/post-install.d --
681: + WORKDIR=
682: + true
683: + case "$1" in
684: + WORKDIR=/tmp/in_target.d/post-install.d
685: + shift 2
686: + true
687: + case "$1" in
688: + shift
689: + break
690: + '[' -z /tmp/in_target.d/post-install.d ']'
691: + PACKAGES=
692: ++ find /tmp/in_target.d/post-install.d -maxdepth 1 -name 'package-installs-*'
693: + '[' -n '' ']'
694: Nothing to install
695: dib-run-parts Sun Oct  2 04:18:52 UTC 2016 00-package-installs completed
696: dib-run-parts Sun Oct  2 04:18:52 UTC 2016 Running /tmp/in_target.d/post-install.d/10-enable-init-scripts
697: dib-run-parts Sun Oct  2 04:18:52 UTC 2016 10-enable-init-scripts completed
698: dib-run-parts Sun Oct  2 04:18:52 UTC 2016 Running /tmp/in_target.d/post-install.d/95-package-uninstalls
699: + set -eu
700: + set -o pipefail
701: ++ basename /usr/local/bin/package-uninstalls
702: + SCRIPTNAME=package-uninstalls
703: ++ getopt -o hd: -n package-uninstalls -- -d /tmp/in_target.d/post-install.d
704: + TEMP=' -d '\''/tmp/in_target.d/post-install.d'\'' --'
705: + '[' 0 '!=' 0 ']'
706: + eval set -- ' -d '\''/tmp/in_target.d/post-install.d'\'' --'
707: ++ set -- -d /tmp/in_target.d/post-install.d --
708: + WORKDIR=
709: + true
710: + case "$1" in
711: + WORKDIR=/tmp/in_target.d/post-install.d
712: + shift 2
713: + true
714: + case "$1" in
715: + shift
716: + break
717: + '[' -z /tmp/in_target.d/post-install.d ']'
718: + PACKAGES=
719: ++ find /tmp/in_target.d/post-install.d -maxdepth 1 -name 'package-installs-*'
720: + install-packages -e
721: Not running install-packages remove with empty packages list
722: Nothing to uninstall
723: dib-run-parts Sun Oct  2 04:18:52 UTC 2016 95-package-uninstalls completed
724: dib-run-parts Sun Oct  2 04:18:52 UTC 2016 Running /tmp/in_target.d/post-install.d/97-dkms
725: ls: cannot access /usr/src/linux-headers-*-*-*: No such file or directory
726: ls: cannot access /usr/src/kernels/*: No such file or directory
727: Warning: No kernel versions found for DKMS
728: dib-run-parts Sun Oct  2 04:18:52 UTC 2016 97-dkms completed
729: dib-run-parts Sun Oct  2 04:18:52 UTC 2016 ----------------------- PROFILING -----------------------
730: dib-run-parts Sun Oct  2 04:18:52 UTC 2016
731: dib-run-parts Sun Oct  2 04:18:52 UTC 2016 Target: post-install.d
732: dib-run-parts Sun Oct  2 04:18:52 UTC 2016
733: dib-run-parts Sun Oct  2 04:18:52 UTC 2016 Script                                     Seconds
734: dib-run-parts Sun Oct  2 04:18:52 UTC 2016 ---------------------------------------  ----------
735: dib-run-parts Sun Oct  2 04:18:52 UTC 2016
736: dib-run-parts Sun Oct  2 04:18:52 UTC 2016 00-package-installs                           0.039
737: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
738: dib-run-parts Sun Oct  2 04:18:52 UTC 2016 10-enable-init-scripts                        0.004
739: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
740: dib-run-parts Sun Oct  2 04:18:52 UTC 2016 95-package-uninstalls                         0.041
741: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
742: dib-run-parts Sun Oct  2 04:18:52 UTC 2016 97-dkms                                       0.053
743: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
744: dib-run-parts Sun Oct  2 04:18:52 UTC 2016
745: dib-run-parts Sun Oct  2 04:18:52 UTC 2016 --------------------- END PROFILING ---------------------
746: Unmount /tmp/dib_build.Y0FGIa3a/mnt/var/cache/apt/archives
747: Unmount /tmp/dib_build.Y0FGIa3a/mnt/tmp/ccache
748: Unmount /tmp/dib_build.Y0FGIa3a/mnt/sys
749: Unmount /tmp/dib_build.Y0FGIa3a/mnt/proc
750: Unmount /tmp/dib_build.Y0FGIa3a/mnt/dev/pts
751: Unmount /tmp/dib_build.Y0FGIa3a/mnt/dev
752: Calculating image size (this may take a minute)...
753: dib-run-parts 2016年 10月 02日 星期日 12:18:53 CST Running /tmp/dib_build.Y0FGIa3a/hooks/block-device.d/10-partition
754: IMAGE_BLOCK_DEVICE=/dev/loop0p1
755: dib-run-parts 2016年 10月 02日 星期日 12:18:53 CST 10-partition completed
756: dib-run-parts 2016年 10月 02日 星期日 12:18:53 CST ----------------------- PROFILING -----------------------
757: dib-run-parts 2016年 10月 02日 星期日 12:18:53 CST
758: dib-run-parts 2016年 10月 02日 星期日 12:18:53 CST Target: block-device.d
759: dib-run-parts 2016年 10月 02日 星期日 12:18:53 CST
760: dib-run-parts 2016年 10月 02日 星期日 12:18:53 CST Script                                     Seconds
761: dib-run-parts 2016年 10月 02日 星期日 12:18:53 CST ---------------------------------------  ----------
762: dib-run-parts 2016年 10月 02日 星期日 12:18:53 CST
763: dib-run-parts Sun Oct  2 12:18:53 CST 2016 10-partition                                  0.280
764: dib-run-parts 2016年 10月 02日 星期日 12:18:53 CST
765: dib-run-parts 2016年 10月 02日 星期日 12:18:53 CST --------------------- END PROFILING ---------------------
766: mke2fs 1.42.13 (17-May-2015)
767: Discarding device blocks:   4096/416512             done
768: Creating filesystem with 416512 4k blocks and 416624 inodes
769: Filesystem UUID: bcc5852b-ff9c-4f2d-bd62-ebc207473f66
770: Superblock backups stored on blocks:
771: 	32768, 98304, 163840, 229376, 294912
772:
773: Allocating group tables:  0/13     done
774: Writing inode tables:  0/13     done
775: Creating journal (16384 blocks): done
776: Writing superblocks and filesystem accounting information:  0/13     done
777:
778: tune2fs 1.42.13 (17-May-2015)
779: dib-run-parts Sun Oct  2 04:18:57 UTC 2016 Running /tmp/in_target.d/finalise.d/50-bootloader
780: + set -eu
781: + set -o pipefail
782: + '[' -n /dev/loop0p1 ']'
783: + PART_DEV=/dev/loop0p1
784: + [[ amd64 =~ ppc ]]
785: ++ echo /dev/loop0p1
786: ++ sed -e s#p1##
787: ++ sed -e s#mapper/##
788: + BOOT_DEV=/dev/loop0
789: + DIB_EXTLINUX=0
790: + '[' 0 '!=' 0 ']'
791: + install_grub2
792: + '[' -f /tmp/grub/install ']'
793: + [[ amd64 =~ ppc ]]
794: + install-packages -m bootloader grub-pc
795: Reading package lists...
796: Building dependency tree...
797: Reading state information...
798: The following extra packages will be installed:
799:   grub-common grub-gfxpayload-lists grub-pc-bin grub2-common libfreetype6
800: Suggested packages:
801:   multiboot-doc grub-emu xorriso desktop-base
802: Recommended packages:
803:   os-prober
804: The following NEW packages will be installed:
805:   grub-common grub-gfxpayload-lists grub-pc grub-pc-bin grub2-common
806:   libfreetype6
807: 0 upgraded, 6 newly installed, 0 to remove and 0 not upgraded.
808: Need to get 3543 kB of archives.
809: After this operation, 17.3 MB of additional disk space will be used.
810: Get:1 http://archive.ubuntu.com/ubuntu/ trusty-updates/main libfreetype6 amd64 2.5.2-1ubuntu2.5 [304 kB]
811: Get:2 http://archive.ubuntu.com/ubuntu/ trusty-updates/main grub-common amd64 2.02~beta2-9ubuntu1.12 [1681 kB]
812: Get:3 http://archive.ubuntu.com/ubuntu/ trusty-updates/main grub2-common amd64 2.02~beta2-9ubuntu1.12 [501 kB]
813: Get:4 http://archive.ubuntu.com/ubuntu/ trusty-updates/main grub-pc-bin amd64 2.02~beta2-9ubuntu1.12 [880 kB]
814: Get:5 http://archive.ubuntu.com/ubuntu/ trusty-updates/main grub-pc amd64 2.02~beta2-9ubuntu1.12 [173 kB]
815: Get:6 http://archive.ubuntu.com/ubuntu/ trusty/main grub-gfxpayload-lists amd64 0.6 [3506 B]
816: perl: warning: Setting locale failed.
817: perl: warning: Please check that your locale settings:
818: 	LANGUAGE = "en_US",
819: 	LC_ALL = (unset),
820: 	LC_TIME = "zh_CN.UTF-8",
821: 	LC_MONETARY = "zh_CN.UTF-8",
822: 	LC_CTYPE = "en_US.UTF-8",
823: 	LC_ADDRESS = "zh_CN.UTF-8",
824: 	LC_TELEPHONE = "zh_CN.UTF-8",
825: 	LC_NAME = "zh_CN.UTF-8",
826: 	LC_MEASUREMENT = "zh_CN.UTF-8",
827: 	LC_IDENTIFICATION = "zh_CN.UTF-8",
828: 	LC_NUMERIC = "zh_CN.UTF-8",
829: 	LC_PAPER = "zh_CN.UTF-8",
830: 	LANG = "C"
831:     are supported and installed on your system.
832: perl: warning: Falling back to the standard locale ("C").
833: locale: Cannot set LC_ALL to default locale: No such file or directory
834: Preconfiguring packages ...
835: Fetched 3543 kB in 3min 10s (18.5 kB/s)
836: Selecting previously unselected package libfreetype6:amd64.
837: (Reading database ... 31469 files and directories currently installed.)
838: Preparing to unpack .../libfreetype6_2.5.2-1ubuntu2.5_amd64.deb ...
839: Unpacking libfreetype6:amd64 (2.5.2-1ubuntu2.5) ...
840: Selecting previously unselected package grub-common.
841: Preparing to unpack .../grub-common_2.02~beta2-9ubuntu1.12_amd64.deb ...
842: Unpacking grub-common (2.02~beta2-9ubuntu1.12) ...
843: Selecting previously unselected package grub2-common.
844: Preparing to unpack .../grub2-common_2.02~beta2-9ubuntu1.12_amd64.deb ...
845: Unpacking grub2-common (2.02~beta2-9ubuntu1.12) ...
846: Selecting previously unselected package grub-pc-bin.
847: Preparing to unpack .../grub-pc-bin_2.02~beta2-9ubuntu1.12_amd64.deb ...
848: Unpacking grub-pc-bin (2.02~beta2-9ubuntu1.12) ...
849: Selecting previously unselected package grub-pc.
850: Preparing to unpack .../grub-pc_2.02~beta2-9ubuntu1.12_amd64.deb ...
851: Unpacking grub-pc (2.02~beta2-9ubuntu1.12) ...
852: Selecting previously unselected package grub-gfxpayload-lists.
853: Preparing to unpack .../grub-gfxpayload-lists_0.6_amd64.deb ...
854: Unpacking grub-gfxpayload-lists (0.6) ...
855: Processing triggers for ureadahead (0.100.0-16) ...
856: Processing triggers for man-db (2.6.7.1-1ubuntu1) ...
857: Processing triggers for install-info (5.2.0.dfsg.1-2) ...
858: Setting up libfreetype6:amd64 (2.5.2-1ubuntu2.5) ...
859: Setting up grub-common (2.02~beta2-9ubuntu1.12) ...
860: runlevel:/var/run/utmp: No such file or directory
861: invoke-rc.d: policy-rc.d denied execution of start.
862: Processing triggers for ureadahead (0.100.0-16) ...
863: Setting up grub2-common (2.02~beta2-9ubuntu1.12) ...
864: Setting up grub-pc-bin (2.02~beta2-9ubuntu1.12) ...
865: Setting up grub-gfxpayload-lists (0.6) ...
866: Setting up grub-pc (2.02~beta2-9ubuntu1.12) ...
867: locale: Cannot set LC_ALL to default locale: No such file or directory
868:
869: Creating config file /etc/default/grub with new version
870: Generating grub configuration file ...
871: Found linux image: /boot/vmlinuz-3.13.0-96-generic
872: Found initrd image: /boot/initrd.img-3.13.0-96-generic
873: done
874: Processing triggers for libc-bin (2.19-0ubuntu6.9) ...
875: ++ which grub-install
876: + GRUBNAME=/usr/sbin/grub-install
877: + '[' -z /usr/sbin/grub-install ']'
878: + '[' -z /usr/sbin/grub-install ']'
879: ++ /usr/sbin/grub-install --version
880: ++ grep 0.97
881: ++ wc -l
882: + '[' 0 -ne 0 ']'
883: + echo 'Installing GRUB2...'
884: Installing GRUB2...
885: + GRUB_OPTS=--force
886: + [[ ! --force == *--target* ]]
887: ++ /usr/sbin/grub-install --version
888: + [[ /usr/sbin/grub-install (GRUB) 2.02~beta2-9ubuntu1.12 =~  2\. ]]
889: + '[' -d /sys/firmware/efi ']'
890: + [[ amd64 =~ ppc ]]
891: + /usr/sbin/grub-install '--modules=biosdisk part_msdos' --force /dev/loop0
892: Installing for i386-pc platform.
893: Installation finished. No error reported.
894: + '[' -d /boot/grub2 ']'
895: + '[' -d /boot/grub ']'
896: + GRUB_CFG=/boot/grub/grub.cfg
897: + echo 'GRUB_TERMINAL="serial console"'
898: + echo GRUB_GFXPAYLOAD_LINUX=text
899: + echo 'GRUB_CMDLINE_LINUX_DEFAULT="console=tty0 console=ttyS0,115200 no_timer_check"'
900: + echo 'GRUB_SERIAL_COMMAND="serial --speed=115200 --unit=0 --word=8 --parity=no --stop=1"'
901: + which grub2-mkconfig
902: + GRUB_MKCONFIG='grub-mkconfig -o /boot/grub/grub.cfg'
903: + DISTRO_NAME=ubuntu
904: + case $DISTRO_NAME in
905: + sed -i -e 's/\(^GRUB_CMDLINE_LINUX.*\)"$/\1 nofb nomodeset vga=normal"/' /etc/default/grub
906: + GRUB_MKCONFIG=update-grub
907: + PROBER_DISABLED=
908: + grep -qe '^\s*GRUB_DISABLE_OS_PROBER=true' /etc/default/grub
909: + PROBER_DISABLED=true
910: + echo GRUB_DISABLE_OS_PROBER=true
911: + update-grub
912: Generating grub configuration file ...
913: Found linux image: /boot/vmlinuz-3.13.0-96-generic
914: Found initrd image: /boot/initrd.img-3.13.0-96-generic
915: done
916: + '[' -n true ']'
917: + sed -i '$d' /etc/default/grub
918: + DIB_RELEASE=trusty
919: + '[' trusty = precise ']'
920: + '[' trusty = wheezy ']'
921: + sed -i s%/dev/loop0p1%LABEL=cloudimg-rootfs% /boot/grub/grub.cfg
922: + sed -i 's%search --no-floppy --fs-uuid --set=root .*$%search --no-floppy --set=root --label cloudimg-rootfs%' /boot/grub/grub.cfg
923: + sed -i 's%root=UUID=[A-Za-z0-9\-]*%root=LABEL=cloudimg-rootfs%' /boot/grub/grub.cfg
924: + '[' ubuntu = fedora ']'
925: + '[' -d /sys/firmware/efi ']'
926: dib-run-parts Sun Oct  2 04:22:12 UTC 2016 50-bootloader completed
927: dib-run-parts Sun Oct  2 04:22:12 UTC 2016 Running /tmp/in_target.d/finalise.d/50-remove-bogus-udev-links
928: + set -eu
929: + set -o pipefail
930: + '[' ubuntu = opensuse ']'
931: dib-run-parts Sun Oct  2 04:22:12 UTC 2016 50-remove-bogus-udev-links completed
932: dib-run-parts Sun Oct  2 04:22:12 UTC 2016 Running /tmp/in_target.d/finalise.d/99-clean-up-cache
933: dib-run-parts Sun Oct  2 04:22:12 UTC 2016 99-clean-up-cache completed
934: dib-run-parts Sun Oct  2 04:22:12 UTC 2016 Running /tmp/in_target.d/finalise.d/99-write-dpkg-manifest
935: + set -eu
936: + set -o pipefail
937: ++ basename image
938: + DPKG_MANIFEST_NAME=dib-manifest-dpkg-image
939: + echo '{"packages": ['
940: + format='{"package": "${binary:Package}","arch": "${Architecture}","version": "${Version}","status": "${db:Status-Abbrev}"},'
941: + tee -a /etc/dib-manifests/dib-manifest-dpkg-image
942: + dpkg-query --show '--showformat={"package": "${binary:Package}","arch": "${Architecture}","version": "${Version}","status": "${db:Status-Abbrev}"},'
943: {"package": "accountsservice","arch": "amd64","version": "0.6.35-0ubuntu7.2","status": "ii "},{"package": "acpid","arch": "amd64","version": "1:2.0.21-1ubuntu2","status": "ii "},{"package": "adduser","arch": "all","version": "3.113+nmu3ubuntu3","status": "ii "},{"package": "apparmor","arch": "amd64","version": "2.8.95~2430-0ubuntu5.3","status": "ii "},{"package": "apport","arch": "all","version": "2.14.1-0ubuntu3.21","status": "ii "},{"package": "apport-symptoms","arch": "all","version": "0.20","status": "ii "},{"package": "apt","arch": "amd64","version": "1.0.1ubuntu2.14","status": "ii "},{"package": "apt-transport-https","arch": "amd64","version": "1.0.1ubuntu2.14","status": "ii "},{"package": "apt-utils","arch": "amd64","version": "1.0.1ubuntu2.14","status": "ii "},{"package": "apt-xapian-index","arch": "all","version": "0.45ubuntu4","status": "rc "},{"package": "aptitude","arch": "amd64","version": "0.6.8.2-1ubuntu4","status": "ii "},{"package": "aptitude-common","arch": "all","version": "0.6.8.2-1ubuntu4","status": "ii "},{"package": "at","arch": "amd64","version": "3.1.14-1ubuntu1","status": "ii "},{"package": "base-files","arch": "amd64","version": "7.2ubuntu5.5","status": "ii "},{"package": "base-passwd","arch": "amd64","version": "3.5.33","status": "ii "},{"package": "bash","arch": "amd64","version": "4.3-7ubuntu1.5","status": "ii "},{"package": "bash-completion","arch": "all","version": "1:2.1-4ubuntu0.2","status": "ii "},{"package": "bc","arch": "amd64","version": "1.06.95-8ubuntu1","status": "ii "},{"package": "bind9-host","arch": "amd64","version": "1:9.9.5.dfsg-3ubuntu0.9","status": "ii "},{"package": "binutils","arch": "amd64","version": "2.24-5ubuntu14.1","status": "ii "},{"package": "bsdmainutils","arch": "amd64","version": "9.0.5ubuntu1","status": "ii "},{"package": "bsdutils","arch": "amd64","version": "1:2.20.1-5.1ubuntu20.7","status": "ii "},{"package": "busybox-initramfs","arch": "amd64","version": "1:1.21.0-1ubuntu1","status": "ii "},{"package": "busybox-static","arch": "amd64","version": "1:1.21.0-1ubuntu1","status": "ii "},{"package": "byobu","arch": "all","version": "5.77-0ubuntu1.2","status": "ii "},{"package": "bzip2","arch": "amd64","version": "1.0.6-5","status": "ii "},{"package": "ca-certificates","arch": "all","version": "20160104ubuntu0.14.04.1","status": "ii "},{"package": "ccache","arch": "amd64","version": "3.1.9-1","status": "ii "},{"package": "cloud-guest-utils","arch": "all","version": "0.27-0ubuntu9.2","status": "ii "},{"package": "cloud-init","arch": "all","version": "0.7.5-0ubuntu1.20","status": "ii "},{"package": "command-not-found","arch": "all","version": "0.3ubuntu12","status": "ii "},{"package": "command-not-found-data","arch": "amd64","version": "0.3ubuntu12","status": "ii "},{"package": "console-setup","arch": "all","version": "1.70ubuntu8","status": "ii "},{"package": "coreutils","arch": "amd64","version": "8.21-1ubuntu5.4","status": "ii "},{"package": "cpio","arch": "amd64","version": "2.11+dfsg-1ubuntu1.2","status": "ii "},{"package": "cpp","arch": "amd64","version": "4:4.8.2-1ubuntu6","status": "ii "},{"package": "cpp-4.8","arch": "amd64","version": "4.8.4-2ubuntu1~14.04.3","status": "ii "},{"package": "crda","arch": "amd64","version": "1.1.2-1ubuntu2","status": "ii "},{"package": "cron","arch": "amd64","version": "3.0pl1-124ubuntu2","status": "ii "},{"package": "cryptsetup","arch": "amd64","version": "2:1.6.1-1ubuntu1","status": "ii "},{"package": "cryptsetup-bin","arch": "amd64","version": "2:1.6.1-1ubuntu1","status": "ii "},{"package": "curl","arch": "amd64","version": "7.35.0-1ubuntu2.9","status": "ii "},{"package": "dash","arch": "amd64","version": "0.5.7-4ubuntu1","status": "ii "},{"package": "dbus","arch": "amd64","version": "1.6.18-0ubuntu4.3","status": "ii "},{"package": "debconf","arch": "all","version": "1.5.51ubuntu2","status": "ii "},{"package": "debconf-i18n","arch": "all","version": "1.5.51ubuntu2","status": "ii "},{"package": "debianutils","arch": "amd64","version": "4.4","status": "ii "},{"package": "dh-python","arch": "all","version": "1.20140128-1ubuntu8.2","status": "ii "},{"package": "diffutils","arch": "amd64","version": "1:3.3-1","status": "ii "},{"package": "dkms","arch": "all","version": "2.2.0.3-1.1ubuntu5.14.04.8","status": "ii "},{"package": "dmidecode","arch": "amd64","version": "2.12-2","status": "ii "},{"package": "dmsetup","arch": "amd64","version": "2:1.02.77-6ubuntu2","status": "ii "},{"package": "dnsutils","arch": "amd64","version": "1:9.9.5.dfsg-3ubuntu0.9","status": "ii "},{"package": "dosfstools","arch": "amd64","version": "3.0.26-1ubuntu0.1","status": "ii "},{"package": "dpkg","arch": "amd64","version": "1.17.5ubuntu5.7","status": "ii "},{"package": "e2fslibs:amd64","arch": "amd64","version": "1.42.9-3ubuntu1.3","status": "ii "},{"package": "e2fsprogs","arch": "amd64","version": "1.42.9-3ubuntu1.3","status": "ii "},{"package": "eatmydata","arch": "amd64","version": "26-2","status": "ii "},{"package": "ed","arch": "amd64","version": "1.9-2","status": "ii "},{"package": "eject","arch": "amd64","version": "2.1.5+deb1+cvs20081104-13.1","status": "ii "},{"package": "ethtool","arch": "amd64","version": "1:3.13-1","status": "ii "},{"package": "file","arch": "amd64","version": "1:5.14-2ubuntu3.3","status": "ii "},{"package": "findutils","arch": "amd64","version": "4.4.2-7","status": "ii "},{"package": "fonts-ubuntu-font-family-console","arch": "all","version": "0.80-0ubuntu6","status": "ii "},{"package": "friendly-recovery","arch": "all","version": "0.2.25","status": "ii "},{"package": "ftp","arch": "amd64","version": "0.17-28","status": "ii "},{"package": "fuse","arch": "amd64","version": "2.9.2-4ubuntu4.14.04.1","status": "ii "},{"package": "gawk","arch": "amd64","version": "1:4.0.1+dfsg-2.1ubuntu2","status": "ii "},{"package": "gcc","arch": "amd64","version": "4:4.8.2-1ubuntu6","status": "ii "},{"package": "gcc-4.8","arch": "amd64","version": "4.8.4-2ubuntu1~14.04.3","status": "ii "},{"package": "gcc-4.8-base:amd64","arch": "amd64","version": "4.8.4-2ubuntu1~14.04.3","status": "ii "},{"package": "gcc-4.9-base:amd64","arch": "amd64","version": "4.9.3-0ubuntu4","status": "ii "},{"package": "gdisk","arch": "amd64","version": "0.8.8-1ubuntu0.1","status": "ii "},{"package": "geoip-database","arch": "all","version": "20140313-1","status": "ii "},{"package": "gettext-base","arch": "amd64","version": "0.18.3.1-1ubuntu3","status": "ii "},{"package": "gir1.2-glib-2.0","arch": "amd64","version": "1.40.0-1ubuntu0.2","status": "ii "},{"package": "gnupg","arch": "amd64","version": "1.4.16-1ubuntu2.4","status": "ii "},{"package": "gpgv","arch": "amd64","version": "1.4.16-1ubuntu2.4","status": "ii "},{"package": "grep","arch": "amd64","version": "2.16-1","status": "ii "},{"package": "groff-base","arch": "amd64","version": "1.22.2-5","status": "ii "},{"package": "grub-common","arch": "amd64","version": "2.02~beta2-9ubuntu1.12","status": "ii "},{"package": "grub-gfxpayload-lists","arch": "amd64","version": "0.6","status": "ii "},{"package": "grub-pc","arch": "amd64","version": "2.02~beta2-9ubuntu1.12","status": "ii "},{"package": "grub-pc-bin","arch": "amd64","version": "2.02~beta2-9ubuntu1.12","status": "ii "},{"package": "grub2-common","arch": "amd64","version": "2.02~beta2-9ubuntu1.12","status": "ii "},{"package": "gzip","arch": "amd64","version": "1.6-3ubuntu1","status": "ii "},{"package": "hdparm","arch": "amd64","version": "9.43-1ubuntu3","status": "ii "},{"package": "hostname","arch": "amd64","version": "3.15ubuntu1","status": "ii "},{"package": "ifupdown","arch": "amd64","version": "0.7.47.2ubuntu4.4","status": "ii "},{"package": "info","arch": "amd64","version": "5.2.0.dfsg.1-2","status": "ii "},{"package": "init-system-helpers","arch": "all","version": "1.14","status": "ii "},{"package": "initramfs-tools","arch": "all","version": "0.103ubuntu4.4","status": "ii "},{"package": "initramfs-tools-bin","arch": "amd64","version": "0.103ubuntu4.4","status": "ii "},{"package": "initscripts","arch": "amd64","version": "2.88dsf-41ubuntu6.3","status": "ii "},{"package": "insserv","arch": "amd64","version": "1.14.0-5ubuntu2","status": "ii "},{"package": "install-info","arch": "amd64","version": "5.2.0.dfsg.1-2","status": "ii "},{"package": "iproute2","arch": "amd64","version": "3.12.0-2ubuntu1","status": "ii "},{"package": "iptables","arch": "amd64","version": "1.4.21-1ubuntu1","status": "ii "},{"package": "iputils-ping","arch": "amd64","version": "3:20121221-4ubuntu1.1","status": "ii "},{"package": "iputils-tracepath","arch": "amd64","version": "3:20121221-4ubuntu1.1","status": "ii "},{"package": "irqbalance","arch": "amd64","version": "1.0.6-2ubuntu0.14.04.4","status": "ii "},{"package": "isc-dhcp-client","arch": "amd64","version": "4.2.4-7ubuntu12.7","status": "ii "},{"package": "isc-dhcp-common","arch": "amd64","version": "4.2.4-7ubuntu12.7","status": "ii "},{"package": "iso-codes","arch": "all","version": "3.52-1","status": "ii "},{"package": "kbd","arch": "amd64","version": "1.15.5-1ubuntu1","status": "ii "},{"package": "keyboard-configuration","arch": "all","version": "1.70ubuntu8","status": "ii "},{"package": "klibc-utils","arch": "amd64","version": "2.0.3-0ubuntu1.14.04.1","status": "ii "},{"package": "kmod","arch": "amd64","version": "15-0ubuntu6","status": "ii "},{"package": "krb5-locales","arch": "all","version": "1.12+dfsg-2ubuntu5.2","status": "ii "},{"package": "landscape-client","arch": "amd64","version": "14.12-0ubuntu0.14.04","status": "ii "},{"package": "landscape-common","arch": "amd64","version": "14.12-0ubuntu0.14.04","status": "ii "},{"package": "language-selector-common","arch": "all","version": "0.129.3","status": "ii "},{"package": "laptop-detect","arch": "amd64","version": "0.13.7ubuntu2","status": "ii "},{"package": "less","arch": "amd64","version": "458-2","status": "ii "},{"package": "libaccountsservice0:amd64","arch": "amd64","version": "0.6.35-0ubuntu7.2","status": "ii "},{"package": "libacl1:amd64","arch": "amd64","version": "2.2.52-1","status": "ii "},{"package": "libapparmor-perl","arch": "amd64","version": "2.8.95~2430-0ubuntu5.3","status": "ii "},{"package": "libapparmor1:amd64","arch": "amd64","version": "2.8.95~2430-0ubuntu5.3","status": "ii "},{"package": "libapt-inst1.5:amd64","arch": "amd64","version": "1.0.1ubuntu2.14","status": "ii "},{"package": "libapt-pkg4.12:amd64","arch": "amd64","version": "1.0.1ubuntu2.14","status": "ii "},{"package": "libarchive-extract-perl","arch": "all","version": "0.70-1","status": "ii "},{"package": "libasan0:amd64","arch": "amd64","version": "4.8.4-2ubuntu1~14.04.3","status": "ii "},{"package": "libasn1-8-heimdal:amd64","arch": "amd64","version": "1.6~git20131207+dfsg-1ubuntu1.1","status": "ii "},{"package": "libasprintf0c2:amd64","arch": "amd64","version": "0.18.3.1-1ubuntu3","status": "ii "},{"package": "libatomic1:amd64","arch": "amd64","version": "4.8.4-2ubuntu1~14.04.3","status": "ii "},{"package": "libattr1:amd64","arch": "amd64","version": "1:2.4.47-1ubuntu1","status": "ii "},{"package": "libaudit-common","arch": "all","version": "1:2.3.2-2ubuntu1","status": "ii "},{"package": "libaudit1:amd64","arch": "amd64","version": "1:2.3.2-2ubuntu1","status": "ii "},{"package": "libbind9-90","arch": "amd64","version": "1:9.9.5.dfsg-3ubuntu0.9","status": "ii "},{"package": "libblkid1:amd64","arch": "amd64","version": "2.20.1-5.1ubuntu20.7","status": "ii "},{"package": "libboost-iostreams1.54.0:amd64","arch": "amd64","version": "1.54.0-4ubuntu3.1","status": "ii "},{"package": "libbsd0:amd64","arch": "amd64","version": "0.6.0-2ubuntu1","status": "ii "},{"package": "libbz2-1.0:amd64","arch": "amd64","version": "1.0.6-5","status": "ii "},{"package": "libc-bin","arch": "amd64","version": "2.19-0ubuntu6.9","status": "ii "},{"package": "libc6:amd64","arch": "amd64","version": "2.19-0ubuntu6.9","status": "ii "},{"package": "libcap-ng0","arch": "amd64","version": "0.7.3-1ubuntu2","status": "ii "},{"package": "libcap2:amd64","arch": "amd64","version": "1:2.24-0ubuntu2","status": "ii "},{"package": "libcap2-bin","arch": "amd64","version": "1:2.24-0ubuntu2","status": "ii "},{"package": "libcgmanager0:amd64","arch": "amd64","version": "0.24-0ubuntu7.5","status": "ii "},{"package": "libck-connector0:amd64","arch": "amd64","version": "0.4.5-3.1ubuntu2","status": "ii "},{"package": "libclass-accessor-perl","arch": "all","version": "0.34-1","status": "ii "},{"package": "libcloog-isl4:amd64","arch": "amd64","version": "0.18.2-1","status": "ii "},{"package": "libcomerr2:amd64","arch": "amd64","version": "1.42.9-3ubuntu1.3","status": "ii "},{"package": "libcryptsetup4","arch": "amd64","version": "2:1.6.1-1ubuntu1","status": "ii "},{"package": "libcurl3:amd64","arch": "amd64","version": "7.35.0-1ubuntu2.9","status": "ii "},{"package": "libcurl3-gnutls:amd64","arch": "amd64","version": "7.35.0-1ubuntu2.9","status": "ii "},{"package": "libcwidget3","arch": "amd64","version": "0.5.16-3.5ubuntu1","status": "ii "},{"package": "libdb5.3:amd64","arch": "amd64","version": "5.3.28-3ubuntu3","status": "ii "},{"package": "libdbus-1-3:amd64","arch": "amd64","version": "1.6.18-0ubuntu4.3","status": "ii "},{"package": "libdbus-glib-1-2:amd64","arch": "amd64","version": "0.100.2-1","status": "ii "},{"package": "libdebconfclient0:amd64","arch": "amd64","version": "0.187ubuntu1","status": "ii "},{"package": "libdevmapper1.02.1:amd64","arch": "amd64","version": "2:1.02.77-6ubuntu2","status": "ii "},{"package": "libdns100","arch": "amd64","version": "1:9.9.5.dfsg-3ubuntu0.9","status": "ii "},{"package": "libdrm2:amd64","arch": "amd64","version": "2.4.67-1ubuntu0.14.04.1","status": "ii "},{"package": "libdumbnet1","arch": "amd64","version": "1.12-4build1","status": "ii "},{"package": "libedit2:amd64","arch": "amd64","version": "3.1-20130712-2","status": "ii "},{"package": "libelf1:amd64","arch": "amd64","version": "0.158-0ubuntu5.2","status": "ii "},{"package": "libept1.4.12:amd64","arch": "amd64","version": "1.0.12","status": "ii "},{"package": "libestr0","arch": "amd64","version": "0.1.9-0ubuntu2","status": "ii "},{"package": "libevent-2.0-5:amd64","arch": "amd64","version": "2.0.21-stable-1ubuntu1.14.04.1","status": "ii "},{"package": "libexpat1:amd64","arch": "amd64","version": "2.1.0-4ubuntu1.3","status": "ii "},{"package": "libffi6:amd64","arch": "amd64","version": "3.1~rc1+r3.0.13-12ubuntu0.1","status": "ii "},{"package": "libfreetype6:amd64","arch": "amd64","version": "2.5.2-1ubuntu2.5","status": "ii "},{"package": "libfribidi0:amd64","arch": "amd64","version": "0.19.6-1","status": "ii "},{"package": "libfuse2:amd64","arch": "amd64","version": "2.9.2-4ubuntu4.14.04.1","status": "ii "},{"package": "libgc1c2:amd64","arch": "amd64","version": "1:7.2d-5ubuntu2","status": "ii "},{"package": "libgcc-4.8-dev:amd64","arch": "amd64","version": "4.8.4-2ubuntu1~14.04.3","status": "ii "},{"package": "libgcc1:amd64","arch": "amd64","version": "1:4.9.3-0ubuntu4","status": "ii "},{"package": "libgck-1-0:amd64","arch": "amd64","version": "3.10.1-1","status": "ii "},{"package": "libgcr-3-common","arch": "all","version": "3.10.1-1","status": "ii "},{"package": "libgcr-base-3-1:amd64","arch": "amd64","version": "3.10.1-1","status": "ii "},{"package": "libgcrypt11:amd64","arch": "amd64","version": "1.5.3-2ubuntu4.4","status": "ii "},{"package": "libgdbm3:amd64","arch": "amd64","version": "1.8.3-12build1","status": "ii "},{"package": "libgeoip1:amd64","arch": "amd64","version": "1.6.0-1","status": "ii "},{"package": "libgirepository-1.0-1","arch": "amd64","version": "1.40.0-1ubuntu0.2","status": "ii "},{"package": "libglib2.0-0:amd64","arch": "amd64","version": "2.40.2-0ubuntu1","status": "ii "},{"package": "libglib2.0-data","arch": "all","version": "2.40.2-0ubuntu1","status": "ii "},{"package": "libgmp10:amd64","arch": "amd64","version": "2:5.1.3+dfsg-1ubuntu1","status": "ii "},{"package": "libgnutls-openssl27:amd64","arch": "amd64","version": "2.12.23-12ubuntu2.5","status": "ii "},{"package": "libgnutls26:amd64","arch": "amd64","version": "2.12.23-12ubuntu2.5","status": "ii "},{"package": "libgomp1:amd64","arch": "amd64","version": "4.8.4-2ubuntu1~14.04.3","status": "ii "},{"package": "libgpg-error0:amd64","arch": "amd64","version": "1.12-0.2ubuntu1","status": "ii "},{"package": "libgpm2:amd64","arch": "amd64","version": "1.20.4-6.1","status": "ii "},{"package": "libgssapi-krb5-2:amd64","arch": "amd64","version": "1.12+dfsg-2ubuntu5.2","status": "ii "},{"package": "libgssapi3-heimdal:amd64","arch": "amd64","version": "1.6~git20131207+dfsg-1ubuntu1.1","status": "ii "},{"package": "libhcrypto4-heimdal:amd64","arch": "amd64","version": "1.6~git20131207+dfsg-1ubuntu1.1","status": "ii "},{"package": "libheimbase1-heimdal:amd64","arch": "amd64","version": "1.6~git20131207+dfsg-1ubuntu1.1","status": "ii "},{"package": "libheimntlm0-heimdal:amd64","arch": "amd64","version": "1.6~git20131207+dfsg-1ubuntu1.1","status": "ii "},{"package": "libhx509-5-heimdal:amd64","arch": "amd64","version": "1.6~git20131207+dfsg-1ubuntu1.1","status": "ii "},{"package": "libicu52:amd64","arch": "amd64","version": "52.1-3ubuntu0.4","status": "ii "},{"package": "libidn11:amd64","arch": "amd64","version": "1.28-1ubuntu2.1","status": "ii "},{"package": "libio-string-perl","arch": "all","version": "1.08-3","status": "ii "},{"package": "libisc95","arch": "amd64","version": "1:9.9.5.dfsg-3ubuntu0.9","status": "ii "},{"package": "libisccc90","arch": "amd64","version": "1:9.9.5.dfsg-3ubuntu0.9","status": "ii "},{"package": "libisccfg90","arch": "amd64","version": "1:9.9.5.dfsg-3ubuntu0.9","status": "ii "},{"package": "libisl10:amd64","arch": "amd64","version": "0.12.2-1","status": "ii "},{"package": "libitm1:amd64","arch": "amd64","version": "4.8.4-2ubuntu1~14.04.3","status": "ii "},{"package": "libjson-c2:amd64","arch": "amd64","version": "0.11-3ubuntu1.2","status": "ii "},{"package": "libjson0:amd64","arch": "amd64","version": "0.11-3ubuntu1.2","status": "ii "},{"package": "libk5crypto3:amd64","arch": "amd64","version": "1.12+dfsg-2ubuntu5.2","status": "ii "},{"package": "libkeyutils1:amd64","arch": "amd64","version": "1.5.6-1","status": "ii "},{"package": "libklibc","arch": "amd64","version": "2.0.3-0ubuntu1.14.04.1","status": "ii "},{"package": "libkmod2:amd64","arch": "amd64","version": "15-0ubuntu6","status": "ii "},{"package": "libkrb5-26-heimdal:amd64","arch": "amd64","version": "1.6~git20131207+dfsg-1ubuntu1.1","status": "ii "},{"package": "libkrb5-3:amd64","arch": "amd64","version": "1.12+dfsg-2ubuntu5.2","status": "ii "},{"package": "libkrb5support0:amd64","arch": "amd64","version": "1.12+dfsg-2ubuntu5.2","status": "ii "},{"package": "libldap-2.4-2:amd64","arch": "amd64","version": "2.4.31-1+nmu2ubuntu8.3","status": "ii "},{"package": "liblocale-gettext-perl","arch": "amd64","version": "1.05-7build3","status": "ii "},{"package": "liblockfile-bin","arch": "amd64","version": "1.09-6ubuntu1","status": "ii "},{"package": "liblockfile1:amd64","arch": "amd64","version": "1.09-6ubuntu1","status": "ii "},{"package": "liblog-message-simple-perl","arch": "all","version": "0.10-1","status": "ii "},{"package": "liblwres90","arch": "amd64","version": "1:9.9.5.dfsg-3ubuntu0.9","status": "ii "},{"package": "liblzma5:amd64","arch": "amd64","version": "5.1.1alpha+20120614-2ubuntu2","status": "ii "},{"package": "libmagic1:amd64","arch": "amd64","version": "1:5.14-2ubuntu3.3","status": "ii "},{"package": "libmodule-pluggable-perl","arch": "all","version": "5.1-1","status": "ii "},{"package": "libmount1:amd64","arch": "amd64","version": "2.20.1-5.1ubuntu20.7","status": "ii "},{"package": "libmpc3:amd64","arch": "amd64","version": "1.0.1-1ubuntu1","status": "ii "},{"package": "libmpdec2:amd64","arch": "amd64","version": "2.4.0-6","status": "ii "},{"package": "libmpfr4:amd64","arch": "amd64","version": "3.1.2-1","status": "ii "},{"package": "libncurses5:amd64","arch": "amd64","version": "5.9+20140118-1ubuntu1","status": "ii "},{"package": "libncursesw5:amd64","arch": "amd64","version": "5.9+20140118-1ubuntu1","status": "ii "},{"package": "libnewt0.52:amd64","arch": "amd64","version": "0.52.15-2ubuntu5","status": "ii "},{"package": "libnfnetlink0:amd64","arch": "amd64","version": "1.0.1-2","status": "ii "},{"package": "libnih-dbus1:amd64","arch": "amd64","version": "1.0.3-4ubuntu25","status": "ii "},{"package": "libnih1:amd64","arch": "amd64","version": "1.0.3-4ubuntu25","status": "ii "},{"package": "libnl-3-200:amd64","arch": "amd64","version": "3.2.21-1ubuntu3","status": "ii "},{"package": "libnl-genl-3-200:amd64","arch": "amd64","version": "3.2.21-1ubuntu3","status": "ii "},{"package": "libnuma1:amd64","arch": "amd64","version": "2.0.9~rc5-1ubuntu3.14.04.2","status": "ii "},{"package": "libp11-kit0:amd64","arch": "amd64","version": "0.20.2-2ubuntu2","status": "ii "},{"package": "libpam-cap:amd64","arch": "amd64","version": "1:2.24-0ubuntu2","status": "ii "},{"package": "libpam-modules:amd64","arch": "amd64","version": "1.1.8-1ubuntu2.2","status": "ii "},{"package": "libpam-modules-bin","arch": "amd64","version": "1.1.8-1ubuntu2.2","status": "ii "},{"package": "libpam-runtime","arch": "all","version": "1.1.8-1ubuntu2.2","status": "ii "},{"package": "libpam-systemd:amd64","arch": "amd64","version": "204-5ubuntu20.19","status": "ii "},{"package": "libpam0g:amd64","arch": "amd64","version": "1.1.8-1ubuntu2.2","status": "ii "},{"package": "libparse-debianchangelog-perl","arch": "all","version": "1.2.0-1ubuntu1","status": "ii "},{"package": "libparted0debian1:amd64","arch": "amd64","version": "2.3-19ubuntu1.14.04.1","status": "ii "},{"package": "libpcap0.8:amd64","arch": "amd64","version": "1.5.3-2","status": "ii "},{"package": "libpci3:amd64","arch": "amd64","version": "1:3.2.1-1ubuntu5.1","status": "ii "},{"package": "libpcre3:amd64","arch": "amd64","version": "1:8.31-2ubuntu2.3","status": "ii "},{"package": "libpipeline1:amd64","arch": "amd64","version": "1.3.0-1","status": "ii "},{"package": "libplymouth2:amd64","arch": "amd64","version": "0.8.8-0ubuntu17.1","status": "ii "},{"package": "libpng12-0:amd64","arch": "amd64","version": "1.2.50-1ubuntu2.14.04.2","status": "ii "},{"package": "libpod-latex-perl","arch": "all","version": "0.61-1","status": "ii "},{"package": "libpolkit-agent-1-0:amd64","arch": "amd64","version": "0.105-4ubuntu3.14.04.1","status": "ii "},{"package": "libpolkit-backend-1-0:amd64","arch": "amd64","version": "0.105-4ubuntu3.14.04.1","status": "ii "},{"package": "libpolkit-gobject-1-0:amd64","arch": "amd64","version": "0.105-4ubuntu3.14.04.1","status": "ii "},{"package": "libpopt0:amd64","arch": "amd64","version": "1.16-8ubuntu1","status": "ii "},{"package": "libprocps3:amd64","arch": "amd64","version": "1:3.3.9-1ubuntu2.2","status": "ii "},{"package": "libpython-stdlib:amd64","arch": "amd64","version": "2.7.5-5ubuntu3","status": "ii "},{"package": "libpython2.7:amd64","arch": "amd64","version": "2.7.6-8ubuntu0.2","status": "ii "},{"package": "libpython2.7-minimal:amd64","arch": "amd64","version": "2.7.6-8ubuntu0.2","status": "ii "},{"package": "libpython2.7-stdlib:amd64","arch": "amd64","version": "2.7.6-8ubuntu0.2","status": "ii "},{"package": "libpython3-stdlib:amd64","arch": "amd64","version": "3.4.0-0ubuntu2","status": "ii "},{"package": "libpython3.4-minimal:amd64","arch": "amd64","version": "3.4.3-1ubuntu1~14.04.4","status": "ii "},{"package": "libpython3.4-stdlib:amd64","arch": "amd64","version": "3.4.3-1ubuntu1~14.04.4","status": "ii "},{"package": "libquadmath0:amd64","arch": "amd64","version": "4.8.4-2ubuntu1~14.04.3","status": "ii "},{"package": "libreadline6:amd64","arch": "amd64","version": "6.3-4ubuntu2","status": "ii "},{"package": "libroken18-heimdal:amd64","arch": "amd64","version": "1.6~git20131207+dfsg-1ubuntu1.1","status": "ii "},{"package": "librtmp0:amd64","arch": "amd64","version": "2.4+20121230.gitdf6c518-1","status": "ii "},{"package": "libsasl2-2:amd64","arch": "amd64","version": "2.1.25.dfsg1-17build1","status": "ii "},{"package": "libsasl2-modules:amd64","arch": "amd64","version": "2.1.25.dfsg1-17build1","status": "ii "},{"package": "libsasl2-modules-db:amd64","arch": "amd64","version": "2.1.25.dfsg1-17build1","status": "ii "},{"package": "libselinux1:amd64","arch": "amd64","version": "2.2.2-1ubuntu0.1","status": "ii "},{"package": "libsemanage-common","arch": "all","version": "2.2-1","status": "ii "},{"package": "libsemanage1:amd64","arch": "amd64","version": "2.2-1","status": "ii "},{"package": "libsepol1:amd64","arch": "amd64","version": "2.2-1ubuntu0.1","status": "ii "},{"package": "libsigc++-2.0-0c2a:amd64","arch": "amd64","version": "2.2.10-0.2ubuntu2","status": "ii "},{"package": "libsigsegv2:amd64","arch": "amd64","version": "2.10-2","status": "ii "},{"package": "libslang2:amd64","arch": "amd64","version": "2.2.4-15ubuntu1","status": "ii "},{"package": "libsqlite3-0:amd64","arch": "amd64","version": "3.8.2-1ubuntu2.1","status": "ii "},{"package": "libss2:amd64","arch": "amd64","version": "1.42.9-3ubuntu1.3","status": "ii "},{"package": "libssl1.0.0:amd64","arch": "amd64","version": "1.0.1f-1ubuntu2.21","status": "ii "},{"package": "libstdc++6:amd64","arch": "amd64","version": "4.8.4-2ubuntu1~14.04.3","status": "ii "},{"package": "libsub-name-perl","arch": "amd64","version": "0.05-1build4","status": "ii "},{"package": "libsystemd-daemon0:amd64","arch": "amd64","version": "204-5ubuntu20.19","status": "ii "},{"package": "libsystemd-login0:amd64","arch": "amd64","version": "204-5ubuntu20.19","status": "ii "},{"package": "libtasn1-6:amd64","arch": "amd64","version": "3.4-3ubuntu0.4","status": "ii "},{"package": "libterm-ui-perl","arch": "all","version": "0.42-1","status": "ii "},{"package": "libtext-charwidth-perl","arch": "amd64","version": "0.04-7build3","status": "ii "},{"package": "libtext-iconv-perl","arch": "amd64","version": "1.7-5build2","status": "ii "},{"package": "libtext-soundex-perl","arch": "amd64","version": "3.4-1build1","status": "ii "},{"package": "libtext-wrapi18n-perl","arch": "all","version": "0.06-7","status": "ii "},{"package": "libtimedate-perl","arch": "all","version": "2.3000-1","status": "ii "},{"package": "libtinfo5:amd64","arch": "amd64","version": "5.9+20140118-1ubuntu1","status": "ii "},{"package": "libtsan0:amd64","arch": "amd64","version": "4.8.4-2ubuntu1~14.04.3","status": "ii "},{"package": "libudev1:amd64","arch": "amd64","version": "204-5ubuntu20.19","status": "ii "},{"package": "libusb-0.1-4:amd64","arch": "amd64","version": "2:0.1.12-23.3ubuntu1","status": "ii "},{"package": "libusb-1.0-0:amd64","arch": "amd64","version": "2:1.0.17-1ubuntu2","status": "ii "},{"package": "libustr-1.0-1:amd64","arch": "amd64","version": "1.0.4-3ubuntu2","status": "ii "},{"package": "libuuid1:amd64","arch": "amd64","version": "2.20.1-5.1ubuntu20.7","status": "ii "},{"package": "libwind0-heimdal:amd64","arch": "amd64","version": "1.6~git20131207+dfsg-1ubuntu1.1","status": "ii "},{"package": "libwrap0:amd64","arch": "amd64","version": "7.6.q-25","status": "ii "},{"package": "libx11-6:amd64","arch": "amd64","version": "2:1.6.2-1ubuntu2","status": "ii "},{"package": "libx11-data","arch": "all","version": "2:1.6.2-1ubuntu2","status": "ii "},{"package": "libxapian22","arch": "amd64","version": "1.2.16-2ubuntu1","status": "ii "},{"package": "libxau6:amd64","arch": "amd64","version": "1:1.0.8-1","status": "ii "},{"package": "libxcb1:amd64","arch": "amd64","version": "1.10-2ubuntu1","status": "ii "},{"package": "libxdmcp6:amd64","arch": "amd64","version": "1:1.1.1-1","status": "ii "},{"package": "libxext6:amd64","arch": "amd64","version": "2:1.3.2-1ubuntu0.0.14.04.1","status": "ii "},{"package": "libxml2:amd64","arch": "amd64","version": "2.9.1+dfsg1-3ubuntu4.8","status": "ii "},{"package": "libxmuu1:amd64","arch": "amd64","version": "2:1.1.1-1","status": "ii "},{"package": "libxtables10","arch": "amd64","version": "1.4.21-1ubuntu1","status": "ii "},{"package": "libyaml-0-2:amd64","arch": "amd64","version": "0.1.4-3ubuntu3.1","status": "ii "},{"package": "linux-firmware","arch": "all","version": "1.127.22","status": "ii "},{"package": "linux-image-3.13.0-96-generic","arch": "amd64","version": "3.13.0-96.143","status": "ii "},{"package": "linux-image-extra-3.13.0-96-generic","arch": "amd64","version": "3.13.0-96.143","status": "ii "},{"package": "linux-image-generic","arch": "amd64","version": "3.13.0.96.104","status": "ii "},{"package": "locales","arch": "all","version": "2.13+git20120306-12.1","status": "ii "},{"package": "lockfile-progs","arch": "amd64","version": "0.1.17","status": "ii "},{"package": "login","arch": "amd64","version": "1:4.1.5.1-1ubuntu9.2","status": "ii "},{"package": "logrotate","arch": "amd64","version": "3.8.7-1ubuntu1","status": "ii "},{"package": "lsb-base","arch": "all","version": "4.1+Debian11ubuntu6.2","status": "ii "},{"package": "lsb-release","arch": "all","version": "4.1+Debian11ubuntu6.2","status": "ii "},{"package": "lshw","arch": "amd64","version": "02.16-2ubuntu1.3","status": "ii "},{"package": "lsof","arch": "amd64","version": "4.86+dfsg-1ubuntu2","status": "ii "},{"package": "ltrace","arch": "amd64","version": "0.7.3-4ubuntu5.1","status": "ii "},{"package": "make","arch": "amd64","version": "3.81-8.2ubuntu3","status": "ii "},{"package": "makedev","arch": "all","version": "2.3.1-93ubuntu1","status": "ii "},{"package": "man-db","arch": "amd64","version": "2.6.7.1-1ubuntu1","status": "ii "},{"package": "manpages","arch": "all","version": "3.54-1ubuntu1","status": "ii "},{"package": "mawk","arch": "amd64","version": "1.3.3-17ubuntu2","status": "ii "},{"package": "mime-support","arch": "all","version": "3.54ubuntu1.1","status": "ii "},{"package": "mlocate","arch": "amd64","version": "0.26-1ubuntu1","status": "ii "},{"package": "module-init-tools","arch": "all","version": "15-0ubuntu6","status": "ii "},{"package": "mount","arch": "amd64","version": "2.20.1-5.1ubuntu20.7","status": "ii "},{"package": "mountall","arch": "amd64","version": "2.53","status": "ii "},{"package": "mtr-tiny","arch": "amd64","version": "0.85-2","status": "ii "},{"package": "multiarch-support","arch": "amd64","version": "2.19-0ubuntu6.9","status": "ii "},{"package": "nano","arch": "amd64","version": "2.2.6-1ubuntu1","status": "ii "},{"package": "ncurses-base","arch": "all","version": "5.9+20140118-1ubuntu1","status": "ii "},{"package": "ncurses-bin","arch": "amd64","version": "5.9+20140118-1ubuntu1","status": "ii "},{"package": "ncurses-term","arch": "all","version": "5.9+20140118-1ubuntu1","status": "ii "},{"package": "net-tools","arch": "amd64","version": "1.60-25ubuntu2.1","status": "ii "},{"package": "netbase","arch": "all","version": "5.2","status": "ii "},{"package": "netcat-openbsd","arch": "amd64","version": "1.105-7ubuntu1","status": "ii "},{"package": "ntfs-3g","arch": "amd64","version": "1:2013.1.13AR.1-2ubuntu2","status": "ii "},{"package": "ntpdate","arch": "amd64","version": "1:4.2.6.p5+dfsg-3ubuntu2.14.04.8","status": "ii "},{"package": "open-iscsi","arch": "amd64","version": "2.0.873-3ubuntu9","status": "ii "},{"package": "open-vm-tools","arch": "amd64","version": "2:9.4.0-1280544-5ubuntu6.2","status": "ii "},{"package": "openssh-client","arch": "amd64","version": "1:6.6p1-2ubuntu2.8","status": "ii "},{"package": "openssh-server","arch": "amd64","version": "1:6.6p1-2ubuntu2.8","status": "ii "},{"package": "openssh-sftp-server","arch": "amd64","version": "1:6.6p1-2ubuntu2.8","status": "ii "},{"package": "openssl","arch": "amd64","version": "1.0.1f-1ubuntu2.21","status": "ii "},{"package": "overlayroot","arch": "all","version": "0.25ubuntu1.14.04.1","status": "ii "},{"package": "parted","arch": "amd64","version": "2.3-19ubuntu1.14.04.1","status": "ii "},{"package": "passwd","arch": "amd64","version": "1:4.1.5.1-1ubuntu9.2","status": "ii "},{"package": "patch","arch": "amd64","version": "2.7.1-4ubuntu2.3","status": "ii "},{"package": "pciutils","arch": "amd64","version": "1:3.2.1-1ubuntu5.1","status": "ii "},{"package": "perl","arch": "amd64","version": "5.18.2-2ubuntu1.1","status": "ii "},{"package": "perl-base","arch": "amd64","version": "5.18.2-2ubuntu1.1","status": "ii "},{"package": "perl-modules","arch": "all","version": "5.18.2-2ubuntu1.1","status": "ii "},{"package": "plymouth","arch": "amd64","version": "0.8.8-0ubuntu17.1","status": "ii "},{"package": "plymouth-theme-ubuntu-text","arch": "amd64","version": "0.8.8-0ubuntu17.1","status": "ii "},{"package": "policykit-1","arch": "amd64","version": "0.105-4ubuntu3.14.04.1","status": "ii "},{"package": "pollinate","arch": "all","version": "4.21-0ubuntu1~14.04","status": "ii "},{"package": "popularity-contest","arch": "all","version": "1.57ubuntu1","status": "ii "},{"package": "powermgmt-base","arch": "amd64","version": "1.31build1","status": "ii "},{"package": "ppp","arch": "amd64","version": "2.4.5-5.1ubuntu2.2","status": "ii "},{"package": "pppconfig","arch": "all","version": "2.3.19ubuntu1","status": "ii "},{"package": "pppoeconf","arch": "all","version": "1.20ubuntu1","status": "ii "},{"package": "procps","arch": "amd64","version": "1:3.3.9-1ubuntu2.2","status": "ii "},{"package": "psmisc","arch": "amd64","version": "22.20-1ubuntu2","status": "ii "},{"package": "python","arch": "amd64","version": "2.7.5-5ubuntu3","status": "ii "},{"package": "python-apt","arch": "amd64","version": "0.9.3.5ubuntu2","status": "ii "},{"package": "python-apt-common","arch": "all","version": "0.9.3.5ubuntu2","status": "ii "},{"package": "python-chardet","arch": "all","version": "2.0.1-2build2","status": "ii "},{"package": "python-cheetah","arch": "amd64","version": "2.4.4-3.fakesyncbuild1","status": "ii "},{"package": "python-configobj","arch": "all","version": "4.7.2+ds-5build1","status": "ii "},{"package": "python-debian","arch": "all","version": "0.1.21+nmu2ubuntu2","status": "ii "},{"package": "python-gdbm","arch": "amd64","version": "2.7.5-1ubuntu1","status": "ii "},{"package": "python-json-pointer","arch": "all","version": "1.0-2build1","status": "ii "},{"package": "python-jsonpatch","arch": "all","version": "1.3-4","status": "ii "},{"package": "python-minimal","arch": "amd64","version": "2.7.5-5ubuntu3","status": "ii "},{"package": "python-oauth","arch": "all","version": "1.0.1-3build2","status": "ii "},{"package": "python-openssl","arch": "amd64","version": "0.13-2ubuntu6","status": "ii "},{"package": "python-pam","arch": "amd64","version": "0.4.2-13.1ubuntu3","status": "ii "},{"package": "python-pkg-resources","arch": "all","version": "3.3-1ubuntu2","status": "ii "},{"package": "python-prettytable","arch": "all","version": "0.7.2-2ubuntu2","status": "ii "},{"package": "python-pycurl","arch": "amd64","version": "7.19.3-0ubuntu3","status": "ii "},{"package": "python-requests","arch": "all","version": "2.2.1-1ubuntu0.3","status": "ii "},{"package": "python-serial","arch": "all","version": "2.6-1build1","status": "ii "},{"package": "python-six","arch": "all","version": "1.5.2-1ubuntu1","status": "ii "},{"package": "python-twisted-bin","arch": "amd64","version": "13.2.0-1ubuntu1","status": "ii "},{"package": "python-twisted-core","arch": "all","version": "13.2.0-1ubuntu1","status": "ii "},{"package": "python-twisted-names","arch": "all","version": "13.2.0-1ubuntu1","status": "ii "},{"package": "python-twisted-web","arch": "all","version": "13.2.0-1ubuntu1","status": "ii "},{"package": "python-urllib3","arch": "all","version": "1.7.1-1ubuntu4","status": "ii "},{"package": "python-xapian","arch": "amd64","version": "1.2.16-2ubuntu1","status": "ii "},{"package": "python-yaml","arch": "amd64","version": "3.10-4ubuntu0.1","status": "ii "},{"package": "python-zope.interface","arch": "amd64","version": "4.0.5-1ubuntu4","status": "ii "},{"package": "python2.7","arch": "amd64","version": "2.7.6-8ubuntu0.2","status": "ii "},{"package": "python2.7-minimal","arch": "amd64","version": "2.7.6-8ubuntu0.2","status": "ii "},{"package": "python3","arch": "amd64","version": "3.4.0-0ubuntu2","status": "ii "},{"package": "python3-apport","arch": "all","version": "2.14.1-0ubuntu3.21","status": "ii "},{"package": "python3-apt","arch": "amd64","version": "0.9.3.5ubuntu2","status": "ii "},{"package": "python3-commandnotfound","arch": "all","version": "0.3ubuntu12","status": "ii "},{"package": "python3-dbus","arch": "amd64","version": "1.2.0-2build2","status": "ii "},{"package": "python3-distupgrade","arch": "all","version": "1:0.220.8","status": "ii "},{"package": "python3-gdbm:amd64","arch": "amd64","version": "3.4.3-1~14.04.2","status": "ii "},{"package": "python3-gi","arch": "amd64","version": "3.12.0-1ubuntu1","status": "ii "},{"package": "python3-minimal","arch": "amd64","version": "3.4.0-0ubuntu2","status": "ii "},{"package": "python3-newt","arch": "amd64","version": "0.52.15-2ubuntu5","status": "ii "},{"package": "python3-problem-report","arch": "all","version": "2.14.1-0ubuntu3.21","status": "ii "},{"package": "python3-pycurl","arch": "amd64","version": "7.19.3-0ubuntu3","status": "ii "},{"package": "python3-software-properties","arch": "all","version": "0.92.37.7","status": "ii "},{"package": "python3-update-manager","arch": "all","version": "1:0.196.21","status": "ii "},{"package": "python3.4","arch": "amd64","version": "3.4.3-1ubuntu1~14.04.4","status": "ii "},{"package": "python3.4-minimal","arch": "amd64","version": "3.4.3-1ubuntu1~14.04.4","status": "ii "},{"package": "readline-common","arch": "all","version": "6.3-4ubuntu2","status": "ii "},{"package": "resolvconf","arch": "all","version": "1.69ubuntu1.1","status": "ii "},{"package": "rsync","arch": "amd64","version": "3.1.0-2ubuntu0.2","status": "ii "},{"package": "rsyslog","arch": "amd64","version": "7.4.4-1ubuntu2.6","status": "ii "},{"package": "run-one","arch": "all","version": "1.17-0ubuntu1","status": "ii "},{"package": "screen","arch": "amd64","version": "4.1.0~20120320gitdb59704-9","status": "ii "},{"package": "sed","arch": "amd64","version": "4.2.2-4ubuntu1","status": "ii "},{"package": "sensible-utils","arch": "all","version": "0.0.9","status": "ii "},{"package": "sgml-base","arch": "all","version": "1.26+nmu4ubuntu1","status": "ii "},{"package": "shared-mime-info","arch": "amd64","version": "1.2-0ubuntu3","status": "ii "},{"package": "software-properties-common","arch": "all","version": "0.92.37.7","status": "ii "},{"package": "ssh-import-id","arch": "all","version": "3.21-0ubuntu1","status": "ii "},{"package": "strace","arch": "amd64","version": "4.8-1ubuntu5","status": "ii "},{"package": "sudo","arch": "amd64","version": "1.8.9p5-1ubuntu1.2","status": "ii "},{"package": "systemd-services","arch": "amd64","version": "204-5ubuntu20.19","status": "ii "},{"package": "systemd-shim","arch": "amd64","version": "6-2bzr1","status": "ii "},{"package": "sysv-rc","arch": "all","version": "2.88dsf-41ubuntu6.3","status": "ii "},{"package": "sysvinit-utils","arch": "amd64","version": "2.88dsf-41ubuntu6.3","status": "ii "},{"package": "tar","arch": "amd64","version": "1.27.1-1","status": "ii "},{"package": "tasksel","arch": "all","version": "2.88ubuntu15","status": "ii "},{"package": "tasksel-data","arch": "all","version": "2.88ubuntu15","status": "ii "},{"package": "tcpd","arch": "amd64","version": "7.6.q-25","status": "ii "},{"package": "tcpdump","arch": "amd64","version": "4.5.1-2ubuntu1.2","status": "ii "},{"package": "telnet","arch": "amd64","version": "0.17-36build2","status": "ii "},{"package": "time","arch": "amd64","version": "1.7-24","status": "ii "},{"package": "tmux","arch": "amd64","version": "1.8-5","status": "ii "},{"package": "tzdata","arch": "all","version": "2016f-0ubuntu0.14.04","status": "ii "},{"package": "ubuntu-keyring","arch": "all","version": "2012.05.19","status": "ii "},{"package": "ubuntu-minimal","arch": "amd64","version": "1.325","status": "ii "},{"package": "ubuntu-release-upgrader-core","arch": "all","version": "1:0.220.8","status": "ii "},{"package": "ubuntu-standard","arch": "amd64","version": "1.325","status": "ii "},{"package": "ucf","arch": "all","version": "3.0027+nmu1","status": "ii "},{"package": "udev","arch": "amd64","version": "204-5ubuntu20.19","status": "ii "},{"package": "ufw","arch": "all","version": "0.34~rc-0ubuntu2","status": "ii "},{"package": "unattended-upgrades","arch": "all","version": "0.82.1ubuntu2.4","status": "ii "},{"package": "update-manager-core","arch": "all","version": "1:0.196.21","status": "ii "},{"package": "update-notifier-common","arch": "all","version": "0.154.1ubuntu2","status": "ii "},{"package": "upstart","arch": "amd64","version": "1.12.1-0ubuntu4.2","status": "ii "},{"package": "ureadahead","arch": "amd64","version": "0.100.0-16","status": "ii "},{"package": "usbutils","arch": "amd64","version": "1:007-2ubuntu1.1","status": "ii "},{"package": "util-linux","arch": "amd64","version": "2.20.1-5.1ubuntu20.7","status": "ii "},{"package": "uuid-runtime","arch": "amd64","version": "2.20.1-5.1ubuntu20.7","status": "ii "},{"package": "vim","arch": "amd64","version": "2:7.4.052-1ubuntu3","status": "ii "},{"package": "vim-common","arch": "amd64","version": "2:7.4.052-1ubuntu3","status": "ii "},{"package": "vim-runtime","arch": "all","version": "2:7.4.052-1ubuntu3","status": "ii "},{"package": "vim-tiny","arch": "amd64","version": "2:7.4.052-1ubuntu3","status": "ii "},{"package": "w3m","arch": "amd64","version": "0.5.3-15","status": "ii "},{"package": "wget","arch": "amd64","version": "1.15-1ubuntu1.14.04.2","status": "ii "},{"package": "whiptail","arch": "amd64","version": "0.52.15-2ubuntu5","status": "ii "},{"package": "wireless-regdb","arch": "all","version": "2013.02.13-1ubuntu1","status": "ii "},{"package": "xauth","arch": "amd64","version": "1:1.0.7-1ubuntu1","status": "ii "},{"package": "xkb-data","arch": "all","version": "2.10.1-1ubuntu1","status": "ii "},{"package": "xml-core","arch": "all","version": "0.13+nmu2","status": "ii "},{"package": "xz-utils","arch": "amd64","version": "5.1.1alpha+20120614-2ubuntu2","status": "ii "},{"package": "zerofree","arch": "amd64","version": "1.0.2-1ubuntu1","status": "ii "},{"package": "zlib1g:amd64","arch": "amd64","version": "1:1.2.8.dfsg-1ubuntu1","status": "ii "},+ sed -i -e 's/,$/\n]}/g' -e 's/\(},\)/    \1\n/g' /etc/dib-manifests/dib-manifest-dpkg-image
944: dib-run-parts Sun Oct  2 04:22:12 UTC 2016 99-write-dpkg-manifest completed
945: dib-run-parts Sun Oct  2 04:22:12 UTC 2016 ----------------------- PROFILING -----------------------
946: dib-run-parts Sun Oct  2 04:22:12 UTC 2016
947: dib-run-parts Sun Oct  2 04:22:12 UTC 2016 Target: finalise.d
948: dib-run-parts Sun Oct  2 04:22:12 UTC 2016
949: dib-run-parts Sun Oct  2 04:22:12 UTC 2016 Script                                     Seconds
950: dib-run-parts Sun Oct  2 04:22:12 UTC 2016 ---------------------------------------  ----------
951: dib-run-parts Sun Oct  2 04:22:12 UTC 2016
952: dib-run-parts Sun Oct  2 04:22:12 UTC 2016 50-bootloader                               195.060
953: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
954: dib-run-parts Sun Oct  2 04:22:12 UTC 2016 50-remove-bogus-udev-links                    0.003
955: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
956: dib-run-parts Sun Oct  2 04:22:12 UTC 2016 99-clean-up-cache                             0.021
957: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
958: dib-run-parts Sun Oct  2 04:22:12 UTC 2016 99-write-dpkg-manifest                        0.018
959: /usr/local/bin/dib-run-parts: line 132: warning: setlocale: LC_NUMERIC: cannot change locale (zh_CN.UTF-8)
960: dib-run-parts Sun Oct  2 04:22:12 UTC 2016
961: dib-run-parts Sun Oct  2 04:22:12 UTC 2016 --------------------- END PROFILING ---------------------
962: dib-run-parts 2016年 10月 02日 星期日 12:22:12 CST Running /tmp/dib_build.Y0FGIa3a/hooks/cleanup.d/01-ccache
963: dib-run-parts 2016年 10月 02日 星期日 12:22:12 CST 01-ccache completed
964: dib-run-parts 2016年 10月 02日 星期日 12:22:12 CST Running /tmp/dib_build.Y0FGIa3a/hooks/cleanup.d/01-copy-manifests-dir
965: + /tmp/dib_build.Y0FGIa3a/hooks/cleanup.d/01-copy-manifests-dir:main:21            :   set -eu
966: + /tmp/dib_build.Y0FGIa3a/hooks/cleanup.d/01-copy-manifests-dir:main:22            :   set -o pipefail
967: + /tmp/dib_build.Y0FGIa3a/hooks/cleanup.d/01-copy-manifests-dir:main:24            :   '[' -d /tmp/dib_build.Y0FGIa3a/mnt//etc/dib-manifests ']'
968: + /tmp/dib_build.Y0FGIa3a/hooks/cleanup.d/01-copy-manifests-dir:main:26            :   '[' -e /tmp/dib_build.Y0FGIa3a/mnt/etc/dib_arguments ']'
969: + /tmp/dib_build.Y0FGIa3a/hooks/cleanup.d/01-copy-manifests-dir:main:27            :   sudo mv /tmp/dib_build.Y0FGIa3a/mnt/etc/dib_arguments /tmp/dib_build.Y0FGIa3a/mnt//etc/dib-manifests
970: + /tmp/dib_build.Y0FGIa3a/hooks/cleanup.d/01-copy-manifests-dir:main:29            :   '[' -e /tmp/dib_build.Y0FGIa3a/mnt/etc/dib_environment ']'
971: + /tmp/dib_build.Y0FGIa3a/hooks/cleanup.d/01-copy-manifests-dir:main:30            :   sudo mv /tmp/dib_build.Y0FGIa3a/mnt/etc/dib_environment /tmp/dib_build.Y0FGIa3a/mnt//etc/dib-manifests
972: + /tmp/dib_build.Y0FGIa3a/hooks/cleanup.d/01-copy-manifests-dir:main:32            :   mkdir -p image.d/
973: + /tmp/dib_build.Y0FGIa3a/hooks/cleanup.d/01-copy-manifests-dir:main:33            :   cp --no-preserve=ownership -rv /tmp/dib_build.Y0FGIa3a/mnt//etc/dib-manifests image.d/
974: '/tmp/dib_build.Y0FGIa3a/mnt//etc/dib-manifests' -> 'image.d/dib-manifests'
975: '/tmp/dib_build.Y0FGIa3a/mnt//etc/dib-manifests/dib_environment' -> 'image.d/dib-manifests/dib_environment'
976: '/tmp/dib_build.Y0FGIa3a/mnt//etc/dib-manifests/dib_arguments' -> 'image.d/dib-manifests/dib_arguments'
977: '/tmp/dib_build.Y0FGIa3a/mnt//etc/dib-manifests/dib-manifest-dpkg-image' -> 'image.d/dib-manifests/dib-manifest-dpkg-image'
978: dib-run-parts 2016年 10月 02日 星期日 12:22:12 CST 01-copy-manifests-dir completed
979: dib-run-parts 2016年 10月 02日 星期日 12:22:12 CST Running /tmp/dib_build.Y0FGIa3a/hooks/cleanup.d/40-unblock-daemons
980: dib-run-parts 2016年 10月 02日 星期日 12:22:12 CST 40-unblock-daemons completed
981: dib-run-parts 2016年 10月 02日 星期日 12:22:12 CST Running /tmp/dib_build.Y0FGIa3a/hooks/cleanup.d/50-remove-img-build-proxy
982: dib-run-parts 2016年 10月 02日 星期日 12:22:12 CST 50-remove-img-build-proxy completed
983: dib-run-parts 2016年 10月 02日 星期日 12:22:12 CST Running /tmp/dib_build.Y0FGIa3a/hooks/cleanup.d/51-bootloader
984: + /tmp/dib_build.Y0FGIa3a/hooks/cleanup.d/51-bootloader:main:23                    :   set -eu
985: + /tmp/dib_build.Y0FGIa3a/hooks/cleanup.d/51-bootloader:main:24                    :   set -o pipefail
986: + /tmp/dib_build.Y0FGIa3a/hooks/cleanup.d/51-bootloader:main:26                    :   '[' -n /tmp/dib_build.Y0FGIa3a/mnt ']'
987: + /tmp/dib_build.Y0FGIa3a/hooks/cleanup.d/51-bootloader:main:28                    :   source /home/xion/gitRepo/openstack/env/bin/../share/diskimage-builder/lib/img-functions
988: + /tmp/dib_build.Y0FGIa3a/hooks/cleanup.d/51-bootloader:main:30                    :   '[' -d /tmp/dib_build.Y0FGIa3a/mnt/boot/extlinux ']'
989: + /tmp/dib_build.Y0FGIa3a/hooks/cleanup.d/51-bootloader:main:32                    :   '[' -d /tmp/dib_build.Y0FGIa3a/mnt/boot/syslinux ']'
990: + /tmp/dib_build.Y0FGIa3a/hooks/cleanup.d/51-bootloader:main:35                    :   exit 0
991: dib-run-parts 2016年 10月 02日 星期日 12:22:12 CST 51-bootloader completed
992: dib-run-parts 2016年 10月 02日 星期日 12:22:12 CST Running /tmp/dib_build.Y0FGIa3a/hooks/cleanup.d/60-untrim-dpkg
993: dib-run-parts 2016年 10月 02日 星期日 12:22:12 CST 60-untrim-dpkg completed
994: dib-run-parts 2016年 10月 02日 星期日 12:22:12 CST Running /tmp/dib_build.Y0FGIa3a/hooks/cleanup.d/99-tidy-logs
995: + /tmp/dib_build.Y0FGIa3a/hooks/cleanup.d/99-tidy-logs:main:22                     :   set -eu
996: + /tmp/dib_build.Y0FGIa3a/hooks/cleanup.d/99-tidy-logs:main:23                     :   set -o pipefail
997: + /tmp/dib_build.Y0FGIa3a/hooks/cleanup.d/99-tidy-logs:main:26                     :   sudo find /tmp/dib_build.Y0FGIa3a/mnt/var/log -type f -exec cp /dev/null '{}' ';'
998: + /tmp/dib_build.Y0FGIa3a/hooks/cleanup.d/99-tidy-logs:main:29                     :   sudo find /tmp/dib_build.Y0FGIa3a/mnt/root -name '*.log' -type f -delete
999: dib-run-parts 2016年 10月 02日 星期日 12:22:12 CST 99-tidy-logs completed
1000: dib-run-parts 2016年 10月 02日 星期日 12:22:12 CST ----------------------- PROFILING -----------------------
1001: dib-run-parts 2016年 10月 02日 星期日 12:22:12 CST
1002: dib-run-parts 2016年 10月 02日 星期日 12:22:12 CST Target: cleanup.d
1003: dib-run-parts 2016年 10月 02日 星期日 12:22:12 CST
1004: dib-run-parts 2016年 10月 02日 星期日 12:22:12 CST Script                                     Seconds
1005: dib-run-parts 2016年 10月 02日 星期日 12:22:12 CST ---------------------------------------  ----------
1006: dib-run-parts 2016年 10月 02日 星期日 12:22:12 CST
1007: dib-run-parts Sun Oct  2 12:22:12 CST 2016 01-ccache                                     0.008
1008: dib-run-parts Sun Oct  2 12:22:12 CST 2016 01-copy-manifests-dir                         0.068
1009: dib-run-parts Sun Oct  2 12:22:12 CST 2016 40-unblock-daemons                            0.041
1010: dib-run-parts Sun Oct  2 12:22:12 CST 2016 50-remove-img-build-proxy                     0.008
1011: dib-run-parts Sun Oct  2 12:22:12 CST 2016 51-bootloader                                 0.016
1012: dib-run-parts Sun Oct  2 12:22:12 CST 2016 60-untrim-dpkg                                0.012
1013: dib-run-parts Sun Oct  2 12:22:12 CST 2016 99-tidy-logs                                  0.029
1014: dib-run-parts 2016年 10月 02日 星期日 12:22:12 CST
1015: dib-run-parts 2016年 10月 02日 星期日 12:22:12 CST --------------------- END PROFILING ---------------------
1016: Unmount /tmp/dib_build.Y0FGIa3a/mnt/sys
1017: Unmount /tmp/dib_build.Y0FGIa3a/mnt/proc
1018: Unmount /tmp/dib_build.Y0FGIa3a/mnt/dev/pts
1019: Unmount /tmp/dib_build.Y0FGIa3a/mnt/dev
1020: Unmount /tmp/dib_build.Y0FGIa3a/mnt
1021: /dev/loop0: [0081]:3 (/tmp/dib_image.BvPrfATI/image.raw)
1022: Converting image using qemu-img convert
1023: Image file image.qcow2 created...
```
