#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import print_function
from collections import namedtuple

Disk = namedtuple('Disk', 'major_nurnber minor_number device_name'
                            ' read_count read_merged_count read_sections'
                            ' time_spent_reading write_count write_merged_count'
                            ' write_sections time_spent_write io_requests'
                            ' time_spent_doing_io weighted_time_spent_doing_io')
def get_disk_info(device):
    with open('/proc/diskstats') as f:
        for line in f:
            print(line)
            if line.split()[2] == device:
                return Disk(*(line.split()))
    raise RuntimeError("device ({0}) not found !".format(device))

def main():
    disk_info = get_disk_info('vdc')
    print(disk_info)

if __name__ == '__main__':
    main()