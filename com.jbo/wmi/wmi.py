#!/usr/bin/env python
# coding:utf-8
import json
import os
import time
import wmi_client_wrapper as wmi
import codecs
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class EventLog(object):
    def __init__(self, host, username, password, wql, dstDir):
        self.host = host
        self.username = username
        self.password = password
        self.wql = wql
        self.dstDir = dstDir
        self.wmic = wmi.WmiClientWrapper(username=username, password=password, host=host)

    def write_event_log(self, last_time, current_time):
        if str(self.wql).upper().find("WHERE") > 0:
            results = self.wmic.query("%s and TimeWritten > '%s.000000-000' and TimeWritten <= '%s.000000-000'" % (self.wql, last_time, current_time))
        else:
            results = self.wmic.query("%s where TimeWritten > '%s.000000-000' and TimeWritten <= '%s.000000-000'" % (self.wql, last_time, current_time))
        current_time_str = str(int(round(time.time() * 1000)))
        dst_path = self.dstDir + "/" + "wmi_windows-" + current_time_str + ".log"
        count = 0
        with codecs.open(dst_path, "w", encoding="UTF-8") as file:
            for row in results:
                text = json.dumps(row, ensure_ascii=False)
                file.write(text + "\n")
                if ++count / 1000 == 0:
                    file.flush()
        file.close()


def load_config():
    with open("config.json") as json_file:
        data = json.load(json_file)
        return data


def main():
    config = load_config()
    host = config["wmi"]["host"]
    username = config["wmi"]["username"]
    password = config["wmi"]["password"]
    wql = config["wmi"]["wql"]
    dst_dir = config["dstDir"]
    interval = config["interval"]
    start_time = config["start_time"]
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    first_current_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
    event_log = EventLog(host, username, password, wql, dst_dir)
    event_log.write_event_log(start_time, first_current_time)
    while True:
        current_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
        event_log.write_event_log(first_current_time, current_time)
        first_current_time = current_time
        time.sleep(interval)

if __name__ == "__main__":
    main()
