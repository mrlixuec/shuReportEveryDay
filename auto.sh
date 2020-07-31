#!/bin/bash
python3 /usr/local/selenium/healthInput.py

#每次执行完关闭chrome的webdriver
ps -ef | grep chrome| grep -v grep | awk '{print $2}' | xargs kill -9
#python3 /usr/local/selenium/hello.py
