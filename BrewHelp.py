# -*- coding: utf-8 -*-
import sys
import time

import jsonpath
import requests
import json
import socket

timeout = 20
socket.setdefaulttimeout(timeout)

g_proxies = {
    # "http": "127.0.0.1:1080",
}
http_client = requests.Session()


def brew_get_dlink(url):
    headers = {
        "authorization": "Bearer QQ==",
        "accept": "application/vnd.oci.image.index.v1+json"
    }
    response = http_client.get(url, headers=headers, proxies=g_proxies, timeout=300, allow_redirects=False)
    if response.status_code == 307:
        return response.headers.get('location')
    return response.text


def brew_find(app_name):
    print('正在处理 %s' % app_name)
    url = "https://formulae.brew.sh/api/formula/%s.json" % (app_name.lower())
    headers = {
        "authorization": "Bearer QQ==",
        "accept": "application/vnd.oci.image.index.v1+json"
    }
    response = http_client.get(url, headers=headers, proxies=g_proxies, timeout=300)
    if response.status_code == 404:
        print("无 %s 的搜索内容" % app_name)
        return
    if response.status_code != 200:
        print(response.text)
        return
    json_obj = json.loads(response.text)
    depends = jsonpath.jsonpath(json_obj, "$..dependencies")
    if depends is not False and len(depends) > 1:
        print("依赖项目 %s" % str(' '.join(depends[0])))
    res_list = jsonpath.jsonpath(json_obj, "$..files")
    if res_list is False or len(res_list) < 1:
        print("无下载地址数据")
        return
    stable_version = ''
    stables = jsonpath.jsonpath(json_obj, "$..stable")
    if stables is not False:
        stable_version = stables[0]
    for list_dict in res_list:
        for key in list_dict:
            d_link = brew_get_dlink(list_dict[key]['url'])
            print("%s_%s_%s.tar.gz  %s" % (app_name, stable_version, key, d_link))
    history = jsonpath.jsonpath(json_obj, "$..versioned_formulae")
    if history is not False and len(history) > 0:
        print("历史版本大全 %s" % ' '.join(history[0]))

if __name__ == '__main__':
    print('python info %s' % sys.version)
    print('brew 下载地址解析 20220310')
    start_time = int(time.time())

    # brew_find('mtr')
    # brew_find('go')
    # brew_find('go@1.16')
    input_key = input('请输入想要解析（如：mtr）：')
    brew_find(input_key)

    end_time = int(time.time())
    print('用时' + str(end_time - start_time) + '秒')
