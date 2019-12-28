#!/usr/bin/python3

__author__ = 'sxwxs'
__date__ = '2019-12-28'

import requests
import getpass
import getopt
import json
import sys
import os


host = 'gw.bupt.edu.cn'


def login(name, passwd):
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36',
        'Upgrade-Insecure-Requests':'1',
        'Connection':'keep-alive'
    }
    data = {'user':name, 'pass':passwd}#, 'line':"CUC-BRAS"}
    requests.post(f'http://{host}/login', data, headers=headers)


def logout():
    requests.get(f'http://{host}/logout')


def show_useage():
    print ('Usage: buptgw -i|-o|-w  [-c <config_file>] [-u <username>] [-p <password>]')
    print ('    -i                login')
    print ('    -o                logout')
    print ('    -w                write username and password to config file')
    print ('    -c <config_path>  config file path, optional, defualt is ~/.buptgw')
    print ('    -u <username>')
    print ('    -p <password>')


def main():
    username = ""
    password = ""
    config_path = os.path.join(os.environ['HOME'], '.butpgw')
    try:
        opts, _ = getopt.getopt(sys.argv[1:],"iocwu:p:",["config_path=","username=", "password="])
    except getopt.GetoptError as e:
        print(e)
        show_useage()
        sys.exit(2)
    flogin = 0
    flogout = 0
    fwrite_config = 0

    for opt, arg in opts:
        if opt == '-i':
            flogin = 1
        if opt == '-o':
            flogout = 1
        if opt == '-u':
            username = arg
        if opt == '-p':
            password = arg
        if opt == '-c':
            config_path = arg
        if opt == '-w':
            fwrite_config = 1
    
    if sum([flogin, flogout, fwrite_config]) != 1:
        show_useage()
        sys.exit(2)
    if flogout:
        return logout()
    if not username:
        try:
            print('using config file:', config_path)
            if fwrite_config: raise Exception() # 如果要新建配置文件则不尝试读取配置文件
            with open(config_path) as f:
                username, password = json.load(f)
        except:
            username = input("Username:")
    if not password:
        password = getpass.getpass()
    if flogin:
        return login(username, password)
    with open(config_path, 'w', encoding='utf8') as f:
        json.dump([username, password], f)