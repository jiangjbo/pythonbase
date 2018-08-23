#!/usr/bin/python2
#_*_encoding:utf-8_*_

import json
import requests

ip = "172.16.106.99"
vuln_type = 1

url = "http://172.16.106.99:8080/enterprise/security/vulnerability/import"
token = dict(TOKEN='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHQiOjE1MDY1MjIzMDc0ODIsInVpZCI6IkZJS1ZJWlMzMDAwNyIsImN0IjoxNTA2NDkzNTA3NDgyLCJsbiI6ImFkbWluIiwic2FkbSI6dHJ1ZSwiY2lwIjoiMTcyLjE2LjEwMi43MyIsInJuIjoi6LaF57qn566h55CG5ZGYIiwiaWF0IjoxNTA2NDkzNTA3NDgyfQ.uyBK2BENufulF6rnh2J0WqhTwPbd5T9jGgvPIPUcj5s')

def main():
    f = open("data.json")
    vuln = json.load(f, encoding="UTF-8")
    for rec in vuln:
        params = {}
        params["ip"] = ip
        params["type"] = vuln_type
        params["category"] = rec["category"]
        params["name"] = rec["name"]
        params["score"] = rec["score"]
        params["level"] = rec["level"]
        if "occurs" in rec:
            params["occurs"] = rec["occurs"]
        
        if "description" in rec:
            params["description"] = rec["description"]
        
        params["solution"] = rec["solution"]

        if "publish_time" in rec:
            params["publish_time"] = rec["publish_time"]
        
        if "cncve_list" in rec:
            params["cncve_list"] = rec["cncve_list"]

        if "cnnvd_list" in rec:
            params["cnnvd_list"] = rec["cnnvd_list"]
        
        if "cnvd_list" in rec:
            params["cnvd_list"] = rec["cnvd_list"]
        
        if "cve_list" in rec:
            params["cve_list"] = rec["cve_list"]
        
        r = requests.post(url, cookies=token, json=params)
        print r.status_code

if __name__ == "__main__":
    main()
