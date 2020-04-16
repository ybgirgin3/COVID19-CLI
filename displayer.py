# !/usr/bin/python3
# -*- coding: utf8 -*-
# Filename: displayer.py

from platform import system as plt
from os import system as oss

def clean():
    if plt == 'Windows':
        oss('cls')      # for windows
    else:
        oss('clear')    # for linux and darwin


def information_return(world_new_confirmed, world_confirmed, world_new_deaths, \
                        world_death, world_new_recovered, world_total_recovered, \
                        cnt, cnt_total_cases, cnt_total_living_case, cnt_total_death,\
                        cnt_total_recovered, dayone_cases, dayone_deaths, dayone_recovered, date, lat, lon):
    # clean terminal screen before printing
    clean()
    # this will print items on shell
    return f"""
        WORLD TOTAL INFORMATION

        CONFIRMED
    New Confirmed   :   {world_new_confirmed}
    Total Confirmed :   {world_confirmed}

        DEATHS
    New Deaths      :   {world_new_deaths}
    Total Death     :   {world_death}

        RECOVERED
    New Recovered   :   {world_new_recovered}
    Total Recovered :   {world_total_recovered}




        LASTEST INFORMATION OF THE {cnt} (date: {date}) (latitude: {lat}, longtitude: {lon})

        TOTAL
    Cases           :   {cnt_total_cases}
    Active Cases    :   {cnt_total_living_case}
    Deaths          :   {cnt_total_death}
    Recovered       :   {cnt_total_recovered}

        DAYONE
    Cases           :   {dayone_cases}
    Deaths          :   {dayone_deaths}
    Recovered       :   {dayone_recovered}



    """
# end file
