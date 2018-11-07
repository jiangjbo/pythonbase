#!/usr/bin/env python
# coding:utf-8
import json
import os
import time
import wmi_client_wrapper as wmi
import codecs
import sys
import errno
import logging
from logging.handlers import TimedRotatingFileHandler
reload(sys)
sys.setdefaultencoding('utf8')

try:
    os.makedirs("./logs")
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

log_file = "./logs/monitor.log"
logger = logging.getLogger('monitor')
formatter = logging.Formatter(fmt='%(asctime)s%(levelname)-8s%(threadName)-10s: %(message)s',
                              datefmt="%Y-%m-%d %H:%M:%S ")
handler = TimedRotatingFileHandler(log_file, when="D",
                                   interval=1,
                                   backupCount=30)
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel("INFO")


class EventLog(object):
    def __init__(self, host, username, password, wql, dstDir):
        self.host = host
        self.username = username
        self.password = password
        self.wql = wql
        self.dstDir = dstDir
        self.wmic = wmi.WmiClientWrapper(username=username, password=password, host=host)

    def write_event_log(self, last_number, current_number):
        if str(self.wql).upper().find("WHERE") > 0:
            results = self.wmic.query("%s and RecordNumber > %d and RecordNumber <= %d" % (self.wql, last_number, current_number))
        else:
            results = self.wmic.query("%s where RecordNumber > %d and RecordNumber <= %d" % (self.wql, last_number, current_number))
        current_time_str = str(int(round(time.time() * 1000)))
        dst_path = self.dstDir + "/" + "wmi_windows-" + current_time_str + ".log"
        count = 0
        ct = results.count()
        with codecs.open(dst_path, "w", encoding="UTF-8") as file:
            for row in results:
                text = json.dumps(row, ensure_ascii=False)
                file.write(text + "\n")
                if ++count / 1000 == 0:
                    file.flush()
                if count == ct:
                    ct = json.loads(text)["RecordNumber"]
        file.close()
        return ct

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
    number = config["recordNumber"]
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    event_log = EventLog(host, username, password, wql, dst_dir)
    while True:
        current_number = event_log.write_event_log(number, interval)
        number = number + current_number
        time.sleep(interval)

if __name__ == "__main__":
    main()
