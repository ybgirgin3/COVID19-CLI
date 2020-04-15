# !/usr/bin/python3
# Filename connectionControl.py
import os
import colorama
from colorama import Style, Fore
import requests as req


def chknet():
    colorama.init()
    url = 'https://www.google.com/'
    timeout = 5

    resp = req.get(url, timeout=timeout)
    print(Fore.GREEN + f'{resp.status_code}')
    print(Style.RESET_ALL)
    return True

# end file
# print(chknet())
