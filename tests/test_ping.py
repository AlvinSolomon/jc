import os
import unittest
import json
import jc.parsers.ping

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


class MyTests(unittest.TestCase):

    def setUp(self):
        # input

        # centos
        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/centos-7.7/ping-ip-O.out'), 'r', encoding='utf-8') as f:
            self.centos_7_7_ping_ip_O = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/centos-7.7/ping-ip-O-D.out'), 'r', encoding='utf-8') as f:
            self.centos_7_7_ping_ip_O_D = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/centos-7.7/ping-hostname-O.out'), 'r', encoding='utf-8') as f:
            self.centos_7_7_ping_hostname_O = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/centos-7.7/ping-hostname-O-p.out'), 'r', encoding='utf-8') as f:
            self.centos_7_7_ping_hostname_O_p = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/centos-7.7/ping-hostname-O-D-p-s.out'), 'r', encoding='utf-8') as f:
            self.centos_7_7_ping_hostname_O_D_p_s = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/centos-7.7/ping6-ip-O-p.out'), 'r', encoding='utf-8') as f:
            self.centos_7_7_ping6_ip_O_p = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/centos-7.7/ping6-ip-O-D-p.out'), 'r', encoding='utf-8') as f:
            self.centos_7_7_ping6_ip_O_D_p = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/centos-7.7/ping6-hostname-O-p.out'), 'r', encoding='utf-8') as f:
            self.centos_7_7_ping6_hostname_O_p = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/centos-7.7/ping6-hostname-O-D-p-s.out'), 'r', encoding='utf-8') as f:
            self.centos_7_7_ping6_hostname_O_D_p_s = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/centos-7.7/ping-ip-dup.out'), 'r', encoding='utf-8') as f:
            self.centos_7_7_ping_ip_dup = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/centos-7.7/ping6-ip-dup.out'), 'r', encoding='utf-8') as f:
            self.centos_7_7_ping6_ip_dup = f.read()

        # ubuntu
        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/ubuntu-18.04/ping-ip-O.out'), 'r', encoding='utf-8') as f:
            self.ubuntu_18_4_ping_ip_O = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/ubuntu-18.04/ping-ip-O-D.out'), 'r', encoding='utf-8') as f:
            self.ubuntu_18_4_ping_ip_O_D = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/ubuntu-18.04/ping-hostname-O.out'), 'r', encoding='utf-8') as f:
            self.ubuntu_18_4_ping_hostname_O = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/ubuntu-18.04/ping-hostname-O-p.out'), 'r', encoding='utf-8') as f:
            self.ubuntu_18_4_ping_hostname_O_p = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/ubuntu-18.04/ping-hostname-O-D-p-s.out'), 'r', encoding='utf-8') as f:
            self.ubuntu_18_4_ping_hostname_O_D_p_s = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/ubuntu-18.04/ping6-ip-O-p.out'), 'r', encoding='utf-8') as f:
            self.ubuntu_18_4_ping6_ip_O_p = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/ubuntu-18.04/ping6-ip-O-D-p.out'), 'r', encoding='utf-8') as f:
            self.ubuntu_18_4_ping6_ip_O_D_p = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/ubuntu-18.04/ping6-hostname-O-p.out'), 'r', encoding='utf-8') as f:
            self.ubuntu_18_4_ping6_hostname_O_p = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/ubuntu-18.04/ping6-hostname-O-D-p-s.out'), 'r', encoding='utf-8') as f:
            self.ubuntu_18_4_ping6_hostname_O_D_p_s = f.read()

        # fedora
        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/fedora32/ping-ip-O.out'), 'r', encoding='utf-8') as f:
            self.fedora32_ping_ip_O = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/fedora32/ping-ip-O-D.out'), 'r', encoding='utf-8') as f:
            self.fedora32_ping_ip_O_D = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/fedora32/ping-hostname-O.out'), 'r', encoding='utf-8') as f:
            self.fedora32_ping_hostname_O = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/fedora32/ping-hostname-O-p.out'), 'r', encoding='utf-8') as f:
            self.fedora32_ping_hostname_O_p = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/fedora32/ping-hostname-O-D-p-s.out'), 'r', encoding='utf-8') as f:
            self.fedora32_ping_hostname_O_D_p_s = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/fedora32/ping6-ip-O-p.out'), 'r', encoding='utf-8') as f:
            self.fedora32_ping6_ip_O_p = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/fedora32/ping6-ip-O-D-p.out'), 'r', encoding='utf-8') as f:
            self.fedora32_ping6_ip_O_D_p = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/fedora32/ping6-hostname-O-p.out'), 'r', encoding='utf-8') as f:
            self.fedora32_ping6_hostname_O_p = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/fedora32/ping6-hostname-O-D-p-s.out'), 'r', encoding='utf-8') as f:
            self.fedora32_ping6_hostname_O_D_p_s = f.read()

        # freebsd
        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/freebsd12/ping-hostname-p.out'), 'r', encoding='utf-8') as f:
            self.freebsd12_ping_hostname_p = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/freebsd12/ping-hostname-s.out'), 'r', encoding='utf-8') as f:
            self.freebsd12_ping_hostname_s = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/freebsd12/ping-hostname.out'), 'r', encoding='utf-8') as f:
            self.freebsd12_ping_hostname = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/freebsd12/ping-ip-p.out'), 'r', encoding='utf-8') as f:
            self.freebsd12_ping_ip_p = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/freebsd12/ping-ip-s.out'), 'r', encoding='utf-8') as f:
            self.freebsd12_ping_ip_s = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/freebsd12/ping-ip.out'), 'r', encoding='utf-8') as f:
            self.freebsd12_ping_ip = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/freebsd12/ping6-hostname-p.out'), 'r', encoding='utf-8') as f:
            self.freebsd12_ping6_hostname_p = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/freebsd12/ping6-hostname-s.out'), 'r', encoding='utf-8') as f:
            self.freebsd12_ping6_hostname_s = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/freebsd12/ping6-hostname.out'), 'r', encoding='utf-8') as f:
            self.freebsd12_ping6_hostname = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/freebsd12/ping6-ip-p.out'), 'r', encoding='utf-8') as f:
            self.freebsd12_ping6_ip_p = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/freebsd12/ping6-ip-s.out'), 'r', encoding='utf-8') as f:
            self.freebsd12_ping6_ip_s = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/freebsd12/ping6-ip.out'), 'r', encoding='utf-8') as f:
            self.freebsd12_ping6_ip = f.read()

        # osx
        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/osx-10.14.6/ping-hostname-p.out'), 'r', encoding='utf-8') as f:
            self.osx_10_14_6_ping_hostname_p = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/osx-10.14.6/ping-hostname-s.out'), 'r', encoding='utf-8') as f:
            self.osx_10_14_6_ping_hostname_s = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/osx-10.14.6/ping-hostname.out'), 'r', encoding='utf-8') as f:
            self.osx_10_14_6_ping_hostname = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/osx-10.14.6/ping-ip-p.out'), 'r', encoding='utf-8') as f:
            self.osx_10_14_6_ping_ip_p = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/osx-10.14.6/ping-ip-s.out'), 'r', encoding='utf-8') as f:
            self.osx_10_14_6_ping_ip_s = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/osx-10.14.6/ping-ip.out'), 'r', encoding='utf-8') as f:
            self.osx_10_14_6_ping_ip = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/osx-10.14.6/ping6-hostname-p.out'), 'r', encoding='utf-8') as f:
            self.osx_10_14_6_ping6_hostname_p = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/osx-10.14.6/ping6-hostname-s.out'), 'r', encoding='utf-8') as f:
            self.osx_10_14_6_ping6_hostname_s = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/osx-10.14.6/ping6-hostname.out'), 'r', encoding='utf-8') as f:
            self.osx_10_14_6_ping6_hostname = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/osx-10.14.6/ping6-ip-p.out'), 'r', encoding='utf-8') as f:
            self.osx_10_14_6_ping6_ip_p = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/osx-10.14.6/ping6-ip-s.out'), 'r', encoding='utf-8') as f:
            self.osx_10_14_6_ping6_ip_s = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/osx-10.14.6/ping6-ip.out'), 'r', encoding='utf-8') as f:
            self.osx_10_14_6_ping6_ip = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/osx-10.14.6/ping-ip-dup.out'), 'r', encoding='utf-8') as f:
            self.osx_10_14_6_ping_ip_dup = f.read()

        # output

        # centos
        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/centos-7.7/ping-ip-O.json'), 'r', encoding='utf-8') as f:
            self.centos_7_7_ping_ip_O_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/centos-7.7/ping-ip-O-D.json'), 'r', encoding='utf-8') as f:
            self.centos_7_7_ping_ip_O_D_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/centos-7.7/ping-hostname-O.json'), 'r', encoding='utf-8') as f:
            self.centos_7_7_ping_hostname_O_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/centos-7.7/ping-hostname-O-p.json'), 'r', encoding='utf-8') as f:
            self.centos_7_7_ping_hostname_O_p_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/centos-7.7/ping-hostname-O-D-p-s.json'), 'r', encoding='utf-8') as f:
            self.centos_7_7_ping_hostname_O_D_p_s_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/centos-7.7/ping6-ip-O-p.json'), 'r', encoding='utf-8') as f:
            self.centos_7_7_ping6_ip_O_p_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/centos-7.7/ping6-ip-O-D-p.json'), 'r', encoding='utf-8') as f:
            self.centos_7_7_ping6_ip_O_D_p_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/centos-7.7/ping6-hostname-O-p.json'), 'r', encoding='utf-8') as f:
            self.centos_7_7_ping6_hostname_O_p_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/centos-7.7/ping6-hostname-O-D-p-s.json'), 'r', encoding='utf-8') as f:
            self.centos_7_7_ping6_hostname_O_D_p_s_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/centos-7.7/ping-ip-dup.json'), 'r', encoding='utf-8') as f:
            self.centos_7_7_ping_ip_dup_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/centos-7.7/ping6-ip-dup.json'), 'r', encoding='utf-8') as f:
            self.centos_7_7_ping6_ip_dup_json = json.loads(f.read())

        # ubunutu
        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/ubuntu-18.04/ping-ip-O.json'), 'r', encoding='utf-8') as f:
            self.ubuntu_18_4_ping_ip_O_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/ubuntu-18.04/ping-ip-O-D.json'), 'r', encoding='utf-8') as f:
            self.ubuntu_18_4_ping_ip_O_D_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/ubuntu-18.04/ping-hostname-O.json'), 'r', encoding='utf-8') as f:
            self.ubuntu_18_4_ping_hostname_O_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/ubuntu-18.04/ping-hostname-O-p.json'), 'r', encoding='utf-8') as f:
            self.ubuntu_18_4_ping_hostname_O_p_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/ubuntu-18.04/ping-hostname-O-D-p-s.json'), 'r', encoding='utf-8') as f:
            self.ubuntu_18_4_ping_hostname_O_D_p_s_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/ubuntu-18.04/ping6-ip-O-p.json'), 'r', encoding='utf-8') as f:
            self.ubuntu_18_4_ping6_ip_O_p_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/ubuntu-18.04/ping6-ip-O-D-p.json'), 'r', encoding='utf-8') as f:
            self.ubuntu_18_4_ping6_ip_O_D_p_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/ubuntu-18.04/ping6-hostname-O-p.json'), 'r', encoding='utf-8') as f:
            self.ubuntu_18_4_ping6_hostname_O_p_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/ubuntu-18.04/ping6-hostname-O-D-p-s.json'), 'r', encoding='utf-8') as f:
            self.ubuntu_18_4_ping6_hostname_O_D_p_s_json = json.loads(f.read())

        # fedora
        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/fedora32/ping-ip-O.json'), 'r', encoding='utf-8') as f:
            self.fedora32_ping_ip_O_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/fedora32/ping-ip-O-D.json'), 'r', encoding='utf-8') as f:
            self.fedora32_ping_ip_O_D_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/fedora32/ping-hostname-O.json'), 'r', encoding='utf-8') as f:
            self.fedora32_ping_hostname_O_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/fedora32/ping-hostname-O-p.json'), 'r', encoding='utf-8') as f:
            self.fedora32_ping_hostname_O_p_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/fedora32/ping-hostname-O-D-p-s.json'), 'r', encoding='utf-8') as f:
            self.fedora32_ping_hostname_O_D_p_s_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/fedora32/ping6-ip-O-p.json'), 'r', encoding='utf-8') as f:
            self.fedora32_ping6_ip_O_p_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/fedora32/ping6-ip-O-D-p.json'), 'r', encoding='utf-8') as f:
            self.fedora32_ping6_ip_O_D_p_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/fedora32/ping6-hostname-O-p.json'), 'r', encoding='utf-8') as f:
            self.fedora32_ping6_hostname_O_p_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/fedora32/ping6-hostname-O-D-p-s.json'), 'r', encoding='utf-8') as f:
            self.fedora32_ping6_hostname_O_D_p_s_json = json.loads(f.read())

        # freebsd
        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/freebsd12/ping-hostname-p.json'), 'r', encoding='utf-8') as f:
            self.freebsd12_ping_hostname_p_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/freebsd12/ping-hostname-s.json'), 'r', encoding='utf-8') as f:
            self.freebsd12_ping_hostname_s_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/freebsd12/ping-hostname.json'), 'r', encoding='utf-8') as f:
            self.freebsd12_ping_hostname_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/freebsd12/ping-ip-p.json'), 'r', encoding='utf-8') as f:
            self.freebsd12_ping_ip_p_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/freebsd12/ping-ip-s.json'), 'r', encoding='utf-8') as f:
            self.freebsd12_ping_ip_s_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/freebsd12/ping-ip.json'), 'r', encoding='utf-8') as f:
            self.freebsd12_ping_ip_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/freebsd12/ping6-hostname-p.json'), 'r', encoding='utf-8') as f:
            self.freebsd12_ping6_hostname_p_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/freebsd12/ping6-hostname-s.json'), 'r', encoding='utf-8') as f:
            self.freebsd12_ping6_hostname_s_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/freebsd12/ping6-hostname.json'), 'r', encoding='utf-8') as f:
            self.freebsd12_ping6_hostname_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/freebsd12/ping6-ip-p.json'), 'r', encoding='utf-8') as f:
            self.freebsd12_ping6_ip_p_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/freebsd12/ping6-ip-s.json'), 'r', encoding='utf-8') as f:
            self.freebsd12_ping6_ip_s_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/freebsd12/ping6-ip.json'), 'r', encoding='utf-8') as f:
            self.freebsd12_ping6_ip_json = json.loads(f.read())

        # osx:
        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/osx-10.14.6/ping-hostname-p.json'), 'r', encoding='utf-8') as f:
            self.osx_10_14_6_ping_hostname_p_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/osx-10.14.6/ping-hostname-s.json'), 'r', encoding='utf-8') as f:
            self.osx_10_14_6_ping_hostname_s_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/osx-10.14.6/ping-hostname.json'), 'r', encoding='utf-8') as f:
            self.osx_10_14_6_ping_hostname_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/osx-10.14.6/ping-ip-p.json'), 'r', encoding='utf-8') as f:
            self.osx_10_14_6_ping_ip_p_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/osx-10.14.6/ping-ip-s.json'), 'r', encoding='utf-8') as f:
            self.osx_10_14_6_ping_ip_s_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/osx-10.14.6/ping-ip.json'), 'r', encoding='utf-8') as f:
            self.osx_10_14_6_ping_ip_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/osx-10.14.6/ping6-hostname-p.json'), 'r', encoding='utf-8') as f:
            self.osx_10_14_6_ping6_hostname_p_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/osx-10.14.6/ping6-hostname-s.json'), 'r', encoding='utf-8') as f:
            self.osx_10_14_6_ping6_hostname_s_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/osx-10.14.6/ping6-hostname.json'), 'r', encoding='utf-8') as f:
            self.osx_10_14_6_ping6_hostname_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/osx-10.14.6/ping6-ip-p.json'), 'r', encoding='utf-8') as f:
            self.osx_10_14_6_ping6_ip_p_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/osx-10.14.6/ping6-ip-s.json'), 'r', encoding='utf-8') as f:
            self.osx_10_14_6_ping6_ip_s_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/osx-10.14.6/ping6-ip.json'), 'r', encoding='utf-8') as f:
            self.osx_10_14_6_ping6_ip_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/osx-10.14.6/ping-ip-dup.json'), 'r', encoding='utf-8') as f:
            self.osx_10_14_6_ping_ip_dup_json = json.loads(f.read())

    def test_ping_nodata(self):
        """
        Test 'ping' with no data
        """
        self.assertEqual(jc.parsers.ping.parse('', quiet=True), {})

    def test_ping_ip_O_centos_7_7(self):
        """
        Test 'ping <ip> -O' on Centos 7.7
        """
        self.assertEqual(jc.parsers.ping.parse(self.centos_7_7_ping_ip_O, quiet=True), self.centos_7_7_ping_ip_O_json)

    def test_ping_ip_O_D_centos_7_7(self):
        """
        Test 'ping <ip> -O -D' on Centos 7.7
        """
        self.assertEqual(jc.parsers.ping.parse(self.centos_7_7_ping_ip_O_D, quiet=True), self.centos_7_7_ping_ip_O_D_json)

    def test_ping_hostname_O_centos_7_7(self):
        """
        Test 'ping <hostname> -O' on Centos 7.7
        """
        self.assertEqual(jc.parsers.ping.parse(self.centos_7_7_ping_hostname_O, quiet=True), self.centos_7_7_ping_hostname_O_json)

    def test_ping_hostname_O_p_centos_7_7(self):
        """
        Test 'ping <hostname> -O -p' on Centos 7.7
        """
        self.assertEqual(jc.parsers.ping.parse(self.centos_7_7_ping_hostname_O_p, quiet=True), self.centos_7_7_ping_hostname_O_p_json)

    def test_ping_hostname_O_D_p_s_centos_7_7(self):
        """
        Test 'ping <hostname> -O -D -p -s' on Centos 7.7
        """
        self.assertEqual(jc.parsers.ping.parse(self.centos_7_7_ping_hostname_O_D_p_s, quiet=True), self.centos_7_7_ping_hostname_O_D_p_s_json)

    def test_ping6_ip_O_p_centos_7_7(self):
        """
        Test 'ping6 <ip> -O -p' on Centos 7.7
        """
        self.assertEqual(jc.parsers.ping.parse(self.centos_7_7_ping6_ip_O_p, quiet=True), self.centos_7_7_ping6_ip_O_p_json)

    def test_ping6_ip_O_D_p_centos_7_7(self):
        """
        Test 'ping6 <ip> -O -D -p' on Centos 7.7
        """
        self.assertEqual(jc.parsers.ping.parse(self.centos_7_7_ping6_ip_O_D_p, quiet=True), self.centos_7_7_ping6_ip_O_D_p_json)

    def test_ping6_hostname_O_p_centos_7_7(self):
        """
        Test 'ping6 <hostname> -O -p' on Centos 7.7
        """
        self.assertEqual(jc.parsers.ping.parse(self.centos_7_7_ping6_hostname_O_p, quiet=True), self.centos_7_7_ping6_hostname_O_p_json)

    def test_ping6_hostname_O_D_p_s_centos_7_7(self):
        """
        Test 'ping6 <hostname> -O -D -p -s' on Centos 7.7
        """
        self.assertEqual(jc.parsers.ping.parse(self.centos_7_7_ping6_hostname_O_D_p_s, quiet=True), self.centos_7_7_ping6_hostname_O_D_p_s_json)

    def test_ping_ip_dup_centos_7_7(self):
        """
        Test 'ping <ip>' to broadcast IP to get duplicate replies on Centos 7.7
        """
        self.assertEqual(jc.parsers.ping.parse(self.centos_7_7_ping_ip_dup, quiet=True), self.centos_7_7_ping_ip_dup_json)

    def test_ping6_ip_dup_centos_7_7(self):
        """
        Test 'ping6 <ip>' to broadcast IP to get duplicate replies on Centos 7.7
        """
        self.assertEqual(jc.parsers.ping.parse(self.centos_7_7_ping6_ip_dup, quiet=True), self.centos_7_7_ping6_ip_dup_json)

    def test_ping_ip_O_ubuntu_18_4(self):
        """
        Test 'ping <ip> -O' on Ubuntu 18.4
        """
        self.assertEqual(jc.parsers.ping.parse(self.ubuntu_18_4_ping_ip_O, quiet=True), self.ubuntu_18_4_ping_ip_O_json)

    def test_ping_ip_O_D_ubuntu_18_4(self):
        """
        Test 'ping <ip> -O -D' on Ubuntu 18.4
        """
        self.assertEqual(jc.parsers.ping.parse(self.ubuntu_18_4_ping_ip_O_D, quiet=True), self.ubuntu_18_4_ping_ip_O_D_json)

    def test_ping_hostname_O_ubuntu_18_4(self):
        """
        Test 'ping <hostname> -O' on Ubuntu 18.4
        """
        self.assertEqual(jc.parsers.ping.parse(self.ubuntu_18_4_ping_hostname_O, quiet=True), self.ubuntu_18_4_ping_hostname_O_json)

    def test_ping_hostname_O_p_ubuntu_18_4(self):
        """
        Test 'ping <hostname> -O -p' on Ubuntu 18.4
        """
        self.assertEqual(jc.parsers.ping.parse(self.ubuntu_18_4_ping_hostname_O_p, quiet=True), self.ubuntu_18_4_ping_hostname_O_p_json)

    def test_ping_hostname_O_D_p_s_ubuntu_18_4(self):
        """
        Test 'ping <hostname> -O -D -p -s' on Ubuntu 18.4
        """
        self.assertEqual(jc.parsers.ping.parse(self.ubuntu_18_4_ping_hostname_O_D_p_s, quiet=True), self.ubuntu_18_4_ping_hostname_O_D_p_s_json)

    def test_ping6_ip_O_p_ubuntu_18_4(self):
        """
        Test 'ping6 <ip> -O -p' on Ubuntu 18.4
        """
        self.assertEqual(jc.parsers.ping.parse(self.ubuntu_18_4_ping6_ip_O_p, quiet=True), self.ubuntu_18_4_ping6_ip_O_p_json)

    def test_ping6_ip_O_D_p_ubuntu_18_4(self):
        """
        Test 'ping6 <ip> -O -D -p' on Ubuntu 18.4
        """
        self.assertEqual(jc.parsers.ping.parse(self.ubuntu_18_4_ping6_ip_O_D_p, quiet=True), self.ubuntu_18_4_ping6_ip_O_D_p_json)

    def test_ping6_hostname_O_p_ubuntu_18_4(self):
        """
        Test 'ping6 <hostname> -O -p' on Ubuntu 18.4
        """
        self.assertEqual(jc.parsers.ping.parse(self.ubuntu_18_4_ping6_hostname_O_p, quiet=True), self.ubuntu_18_4_ping6_hostname_O_p_json)

    def test_ping6_hostname_O_D_p_s_ubuntu_18_4(self):
        """
        Test 'ping6 <hostname> -O -D -p -s' on Ubuntu 18.4
        """
        self.assertEqual(jc.parsers.ping.parse(self.ubuntu_18_4_ping6_hostname_O_D_p_s, quiet=True), self.ubuntu_18_4_ping6_hostname_O_D_p_s_json)

    def test_ping_ip_O_fedora32(self):
        """
        Test 'ping <ip> -O' on fedora32
        """
        self.assertEqual(jc.parsers.ping.parse(self.fedora32_ping_ip_O, quiet=True), self.fedora32_ping_ip_O_json)

    def test_ping_ip_O_D_fedora32(self):
        """
        Test 'ping <ip> -O -D' on fedora32
        """
        self.assertEqual(jc.parsers.ping.parse(self.fedora32_ping_ip_O_D, quiet=True), self.fedora32_ping_ip_O_D_json)

    def test_ping_hostname_O_fedora32(self):
        """
        Test 'ping <hostname> -O' on fedora32
        """
        self.assertEqual(jc.parsers.ping.parse(self.fedora32_ping_hostname_O, quiet=True), self.fedora32_ping_hostname_O_json)

    def test_ping_hostname_O_p_fedora32(self):
        """
        Test 'ping <hostname> -O -p' on fedora32
        """
        self.assertEqual(jc.parsers.ping.parse(self.fedora32_ping_hostname_O_p, quiet=True), self.fedora32_ping_hostname_O_p_json)

    def test_ping_hostname_O_D_p_s_fedora32(self):
        """
        Test 'ping <hostname> -O -D -p -s' on fedora32
        """
        self.assertEqual(jc.parsers.ping.parse(self.fedora32_ping_hostname_O_D_p_s, quiet=True), self.fedora32_ping_hostname_O_D_p_s_json)

    def test_ping6_ip_O_p_fedora32(self):
        """
        Test 'ping6 <ip> -O -p' on fedora32
        """
        self.assertEqual(jc.parsers.ping.parse(self.fedora32_ping6_ip_O_p, quiet=True), self.fedora32_ping6_ip_O_p_json)

    def test_ping6_ip_O_D_p_fedora32(self):
        """
        Test 'ping6 <ip> -O -D -p' on fedora32
        """
        self.assertEqual(jc.parsers.ping.parse(self.fedora32_ping6_ip_O_D_p, quiet=True), self.fedora32_ping6_ip_O_D_p_json)

    def test_ping6_hostname_O_p_fedora32(self):
        """
        Test 'ping6 <hostname> -O -p' on fedora32
        """
        self.assertEqual(jc.parsers.ping.parse(self.fedora32_ping6_hostname_O_p, quiet=True), self.fedora32_ping6_hostname_O_p_json)

    def test_ping6_hostname_O_D_p_s_fedora32(self):
        """
        Test 'ping6 <hostname> -O -D -p -s' on fedora32
        """
        self.assertEqual(jc.parsers.ping.parse(self.fedora32_ping6_hostname_O_D_p_s, quiet=True), self.fedora32_ping6_hostname_O_D_p_s_json)

    def test_ping_hostname_p_freebsd12(self):
        """
        Test 'ping <hostname> -p' on freebsd12
        """
        self.assertEqual(jc.parsers.ping.parse(self.freebsd12_ping_hostname_p, quiet=True), self.freebsd12_ping_hostname_p_json)

    def test_ping_hostname_s_freebsd12(self):
        """
        Test 'ping <hostname> -s' on freebsd12
        """
        self.assertEqual(jc.parsers.ping.parse(self.freebsd12_ping_hostname_s, quiet=True), self.freebsd12_ping_hostname_s_json)

    def test_ping_ping_hostname_freebsd12(self):
        """
        Test 'ping <hostname>' on freebsd12
        """
        self.assertEqual(jc.parsers.ping.parse(self.freebsd12_ping_hostname, quiet=True), self.freebsd12_ping_hostname_json)

    def test_ping_ip_p_freebsd12(self):
        """
        Test 'ping <ip> -p' on freebsd12
        """
        self.assertEqual(jc.parsers.ping.parse(self.freebsd12_ping_ip_p, quiet=True), self.freebsd12_ping_ip_p_json)

    def test_ping_ip_s_freebsd12(self):
        """
        Test 'ping <ip> -s' on freebsd12
        """
        self.assertEqual(jc.parsers.ping.parse(self.freebsd12_ping_ip_s, quiet=True), self.freebsd12_ping_ip_s_json)

    def test_ping_ip_freebsd12(self):
        """
        Test 'ping6 <ip>' on freebsd127
        """
        self.assertEqual(jc.parsers.ping.parse(self.freebsd12_ping_ip, quiet=True), self.freebsd12_ping_ip_json)

    def test_ping6_hostname_p_freebsd12(self):
        """
        Test 'ping6 <hostname> -p' on freebsd12
        """
        self.assertEqual(jc.parsers.ping.parse(self.freebsd12_ping6_hostname_p, quiet=True), self.freebsd12_ping6_hostname_p_json)

    def test_ping6_hostname_s_freebsd12(self):
        """
        Test 'ping6 <hostname> -s' on freebsd12
        """
        self.assertEqual(jc.parsers.ping.parse(self.freebsd12_ping6_hostname_s, quiet=True), self.freebsd12_ping6_hostname_s_json)

    def test_ping6_hostname_freebsd12(self):
        """
        Test 'ping6 <hostname>' on freebsd12
        """
        self.assertEqual(jc.parsers.ping.parse(self.freebsd12_ping6_hostname, quiet=True), self.freebsd12_ping6_hostname_json)

    def test_ping6_ip_p_freebsd12(self):
        """
        Test 'ping6 <ip> -p' on freebsd12
        """
        self.assertEqual(jc.parsers.ping.parse(self.freebsd12_ping6_ip_p, quiet=True), self.freebsd12_ping6_ip_p_json)

    def test_ping6_ip_s_freebsd12(self):
        """
        Test 'ping6 <ip> -s' on freebsd12
        """
        self.assertEqual(jc.parsers.ping.parse(self.freebsd12_ping6_ip_s, quiet=True), self.freebsd12_ping6_ip_s_json)

    def test_ping6_ip_freebsd12(self):
        """
        Test 'ping6 <ip>' on freebsd12
        """
        self.assertEqual(jc.parsers.ping.parse(self.freebsd12_ping6_ip, quiet=True), self.freebsd12_ping6_ip_json)

    def test_ping_hostname_p_osx_10_14_6(self):
        """
        Test 'ping <hostname> -p' on osx 10.14.6
        """
        self.assertEqual(jc.parsers.ping.parse(self.osx_10_14_6_ping_hostname_p, quiet=True), self.osx_10_14_6_ping_hostname_p_json)

    def test_ping_hostname_s_osx_10_14_6(self):
        """
        Test 'ping <hostname> -s' on osx 10.14.6
        """
        self.assertEqual(jc.parsers.ping.parse(self.osx_10_14_6_ping_hostname_s, quiet=True), self.osx_10_14_6_ping_hostname_s_json)

    def test_ping_ping_hostname_osx_10_14_6(self):
        """
        Test 'ping <hostname>' on osx 10.14.6
        """
        self.assertEqual(jc.parsers.ping.parse(self.osx_10_14_6_ping_hostname, quiet=True), self.osx_10_14_6_ping_hostname_json)

    def test_ping_ip_p_osx_10_14_6(self):
        """
        Test 'ping <ip> -p' on osx 10.14.6
        """
        self.assertEqual(jc.parsers.ping.parse(self.osx_10_14_6_ping_ip_p, quiet=True), self.osx_10_14_6_ping_ip_p_json)

    def test_ping_ip_s_osx_10_14_6(self):
        """
        Test 'ping <ip> -s' on osx 10.14.6
        """
        self.assertEqual(jc.parsers.ping.parse(self.osx_10_14_6_ping_ip_s, quiet=True), self.osx_10_14_6_ping_ip_s_json)

    def test_ping_ip_osx_10_14_6(self):
        """
        Test 'ping6 <ip>' on osx 10.14.6
        """
        self.assertEqual(jc.parsers.ping.parse(self.osx_10_14_6_ping_ip, quiet=True), self.osx_10_14_6_ping_ip_json)

    def test_ping6_hostname_p_osx_10_14_6(self):
        """
        Test 'ping6 <hostname> -p' on osx 10.14.6
        """
        self.assertEqual(jc.parsers.ping.parse(self.osx_10_14_6_ping6_hostname_p, quiet=True), self.osx_10_14_6_ping6_hostname_p_json)

    def test_ping6_hostname_s_osx_10_14_6(self):
        """
        Test 'ping6 <hostname> -s' on osx 10.14.6
        """
        self.assertEqual(jc.parsers.ping.parse(self.osx_10_14_6_ping6_hostname_s, quiet=True), self.osx_10_14_6_ping6_hostname_s_json)

    def test_ping6_hostname_osx_10_14_6(self):
        """
        Test 'ping6 <hostname>' on osx 10.14.6
        """
        self.assertEqual(jc.parsers.ping.parse(self.osx_10_14_6_ping6_hostname, quiet=True), self.osx_10_14_6_ping6_hostname_json)

    def test_ping6_ip_p_osx_10_14_6(self):
        """
        Test 'ping6 <ip> -p' on osx 10.14.6
        """
        self.assertEqual(jc.parsers.ping.parse(self.osx_10_14_6_ping6_ip_p, quiet=True), self.osx_10_14_6_ping6_ip_p_json)

    def test_ping6_ip_s_osx_10_14_6(self):
        """
        Test 'ping6 <ip> -s' on osx 10.14.6
        """
        self.assertEqual(jc.parsers.ping.parse(self.osx_10_14_6_ping6_ip_s, quiet=True), self.osx_10_14_6_ping6_ip_s_json)

    def test_ping6_ip_osx_10_14_6(self):
        """
        Test 'ping6 <ip>' on osx 10.14.6
        """
        self.assertEqual(jc.parsers.ping.parse(self.osx_10_14_6_ping6_ip, quiet=True), self.osx_10_14_6_ping6_ip_json)

    def test_ping_ip_dup_osx_10_14_6(self):
        """
        Test 'ping <ip>' to broadcast IP to get duplicate replies on osx 10.14.6
        """
        self.assertEqual(jc.parsers.ping.parse(self.osx_10_14_6_ping_ip_dup, quiet=True), self.osx_10_14_6_ping_ip_dup_json)


if __name__ == '__main__':
    unittest.main()
