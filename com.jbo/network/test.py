# -*- coding: utf-8 -*-
import requests
import struct
import json

#get_url = "http://172.16.100.78:12001/nta/file/PXQSVJPFMIQBCJRA.xls?mime=application\/vnd.ms-excel&time=1529046811&tvu=574809&fid=3&md5=1843AC63A076F873002C637027D842FB"
#r = requests.get(get_url)
#print(r)

#url = "http://127.0.0.1:8080/excel/url?url=http://172.16.100.98:11001/nta/files/ETJBDGWKGYFAIOVYSZBX.xls?mime=application/vnd.ms-excel&ts=0&id=0&md5=00b05921c8a4285b0a0720620a010e26efce5000"
# url = "http://127.0.0.1:8090/excel/download"
# data = {"indexName": "event_20180621", "id": "15295836687556831"}
# response = requests.post(url, data=data)
# fout = open('C:\\Users\\16274\\Downloads\\a5.xls', 'wb')
# fout.write(response.content)
# fout.close()


url = "http://172.16.106.24:8080/enterprise/security/intelligence"
''
data = '{"allDayOfWeek":false,"dayOfWeek":[0,0,0,0,0,0,0],"startTimeStr":"","endTimeStr":"","startTime":{"hour":0,"minute":0,"second":0},"endTime":{"hour":0,"minute":0,"second":0},"contentType":"single","name":"重要服务器资产IP","typeId":"6JUS82AW1dd1","type":"ip","intelligenceType":"ip","intelligenceTypeMap":{"value":"ip","text":"IP"},"content":"127.0.0.2","groupId":"6JUS82AW1dd1"}'
headers = {
    'Cookie': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHQiOjIxMzIzODUwODc4MTksInVpZCI6IkZJS1ZJWlMzMDAwNyIsImN0IjoxNTAxNjY1MDg3ODIyLCJsbiI6ImFkbWluIiwic2FkbSI6dHJ1ZSwiY2lwIjoiMTI3LjAuMC4xIiwicm4iOiLotoXnuqfnrqHnkIblkZgiLCJpYXQiOjE1MDE2NjUwODc4MTl9.y9rtK7wG6Bo-GWgJyD_RZG8-q8pNCZagP-sHZeZ2UaI',
    'TOKEN': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHQiOjIxMzIzODUwODc4MTksInVpZCI6IkZJS1ZJWlMzMDAwNyIsImN0IjoxNTAxNjY1MDg3ODIyLCJsbiI6ImFkbWluIiwic2FkbSI6dHJ1ZSwiY2lwIjoiMTI3LjAuMC4xIiwicm4iOiLotoXnuqfnrqHnkIblkZgiLCJpYXQiOjE1MDE2NjUwODc4MTl9.y9rtK7wG6Bo-GWgJyD_RZG8-q8pNCZagP-sHZeZ2UaI'
}
response = requests.post(url, data=data)
print(response.content)