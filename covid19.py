#! /usr/bin/python3
# -*- coding: utf8 -*-

# Author: Yusuf Berkay Girgin
# Date: 12 April 2020, 02:29

import requests as req
from pprint import pprint
import json
import sys

# local modules
import connectionControl
import displayer



"""
expected output:

    {'Cases': 47029,
     'Country': 'Turkey',
     'CountryCode': 'TR',
     'Date': '2020-04-11T00:00:00Z',
     'Lat': '38.96',
     'Lon': '35.24',
     'Status': 'confirmed'}
    }
"""

# api = 'https://api.covid19api.com/dayone/country/turkey/status/confirmed'
# api = 'https://api.covid19api.com/country/south-africa/status/confirmed'
# api = 'https://api.covid19api.com/country'
# api = 'https://api.covid19api.com/countries'


def api_customization(BASE_API):
    api = req.get(BASE_API).text
    api = json.loads(api)
    return api




# eğer ülke ismi girilirse api değiştir
def byCountry(api, cnt):#, country):

    ##### world total information
    tot_api = 'https://api.covid19api.com/summary'
    tot_api = api_customization(tot_api)
    glob = tot_api['Global']

    # world information
    w_new_conf = glob['NewConfirmed']
    w_total_conf = glob['TotalConfirmed']
    w_new_death = glob['NewDeaths']
    w_total_death = glob['NewDeaths']
    w_new_rec = glob['NewRecovered']
    w_total_rec = glob['TotalRecovered']

    ######### total information for only specified country ########
    api = api_customization(api)

    # for newer information use last dict item of list
    focus = api[-1]

    # for countryname look for 'Country' and 'CountryCode'
    for i in focus:
        if cnt != focus['Country']:
            countryname = focus['CountryCode']

    # bu zamana kadar ki toplam hastalıklar
    cnt_total_cases = focus['Confirmed']

    # şu anki ölmemiş hasta sayısı
    cnt_total_living_case = focus['Active']
    cnt_total_death = focus['Deaths']
    cnt_total_recovered = focus['Recovered']


    # daily information
    # get lastest item information
    # get one before the lastest information
    # and get difference between 'em
    before_api = api[len(api)-2]
    dayone_cases = cnt_total_cases - before_api['Confirmed']
    dayone_deaths = cnt_total_death - before_api['Deaths']
    dayone_recovered = cnt_total_recovered - before_api['Recovered']

    ## contry location information
    lat = focus['Lat']
    lon = focus['Lon']
    date = focus['Date']


    # information_return(countryname, cases, death, recovered)
    print(displayer.information_return(w_new_conf, w_total_conf, w_new_death, w_total_death, w_new_rec, w_total_rec, \
                        cnt, cnt_total_cases, cnt_total_living_case, cnt_total_death, cnt_total_recovered, \
                        dayone_cases, dayone_deaths, dayone_recovered, date, lat, lon))





if __name__ == '__main__':
    # kullanıcıdan bileşenler al ve onlara göre gerekli olan fonksiyonlara dön

    # get country
    # cnt = input('country: ')
    cnt = sys.argv[1]

    # kullanmam gereken bu api
    arg = f'https://api.covid19api.com/live/country/{cnt}/status/confirmed'
    if connectionControl.chknet():
        byCountry(arg, cnt)
    else: os.system('python3 covid19.py')
