
import csv
import sys
import datetime
import json
import ast
import os
from os import listdir
import os.path
from os import listdir
from os.path import isfile, join
import os
from distutils.dir_util import copy_tree
from shutil import copytree, copy2
import random
import json
import operator
import os
import http.client
import time
import gzip
from io import BytesIO
import json
from threading import Thread
import threading
from time import sleep
import http.client
import gzip
from io import BytesIO
import json
import random

conn = ''
headersDynamic = []
import _thread
import datetime
from multiprocessing import Process, Lock, Manager, Value
import collections
from difflib import SequenceMatcher
import _thread
import itertools
from itertools import islice
import multiprocessing
import gc
from io import StringIO
from multiprocessing import Pool
import glob
from os import listdir
from os.path import isfile, join

import shutil, os
import re


def get_column(row, service):
    if service == 'Circ':
        # if is_mod_file == True:  # mod
        #     scooterIdIndex = row.index('idScooter')
        #     batteryIndex = row.index('PowerPercentInt')
        #     latitudeIndex = row.index('location_latitude')
        #     longitudeIndex = row.index('location_longitude')
        #
        # else:
        scooterIdIndex = row.index('id')  # no mod
        batteryIndex = row.index('battery_level')
        latitudeIndex = row.index('location_latitude')
        longitudeIndex = row.index('location_longitude')


    elif service == 'Bird':
        scooterIdIndex = row.index('id')
        batteryIndex = row.index('battery_level')
        latitudeIndex = row.index('location_latitude')
        longitudeIndex = row.index('location_longitude')
    elif service == 'Jump':
        scooterIdIndex = row.index('0_assetId')
        batteryIndex = row.index('0_vehicle_battery_low')
        latitudeIndex = row.index('0_location_latitude')
        longitudeIndex = row.index('0_location_longitude')
    elif service == 'Lime':
        scooterIdIndex = row.index('id')
        batteryIndex = row.index('attributes_battery_level')
        latitudeIndex = row.index('attributes_latitude')
        longitudeIndex = row.index('attributes_longitude')
    elif service == 'LyftScooter':
        scooterIdIndex = row.index('rideable_name')
        batteryIndex = row.index('battery_status_percent')
        latitudeIndex = row.index('location_lat')
        longitudeIndex = row.index('location_lng')
    elif service == 'Movo':
        scooterIdIndex = row.index('id')
        batteryIndex = row.index('battery_percentage')
        latitudeIndex = row.index('latitude')
        longitudeIndex = row.index('longitude')
    elif service == 'Scoot':
        scooterIdIndex = row.index('id')
        batteryIndex = row.index('batt_pct_smoothed')
        latitudeIndex = row.index('latitude')
        longitudeIndex = row.index('longitude')
    elif service == 'Skip':
        scooterIdIndex = row.index('ID')
        batteryIndex = row.index('rideablePercentage')
        latitudeIndex = row.index('location_lat')
        longitudeIndex = row.index('location_lon')
    elif service == 'Spin':
        scooterIdIndex = row.index('last4')  # no id
        batteryIndex = row.index('batt_percentage')
        latitudeIndex = row.index('lat')
        longitudeIndex = row.index('lng')
    elif service == 'Tier':
        scooterIdIndex = row.index('id')
        batteryIndex = row.index('batteryLevel')
        latitudeIndex = row.index('lat')
        longitudeIndex = row.index('lng')

    elif service == 'Voi':

        scooterIdIndex = row.index('id')
        batteryIndex = row.index('battery')
        latitudeIndex = row.index('location_0')
        longitudeIndex = row.index('location_1')


    elif service == 'Wind':
        scooterIdIndex = row.index('boardId')
        batteryIndex = row.index('isInOperatingHours')  # no battery
        latitudeIndex = row.index('latitude')
        longitudeIndex = row.index('longitude')
    return scooterIdIndex, batteryIndex, latitudeIndex, longitudeIndex


# services = ['Bird', 'Circ', 'Jump', 'Lime', 'LyftScooter', 'Movo', 'Scoot', 'Skip', 'Spin', 'Tier', 'Voi', 'Wind']
citys = ['DC', 'Detroit', 'Lisbon', 'Madrid', 'MexicoCity', 'Paris', 'SanFrancisco', 'TelAviv', 'Zurich' ]
# city='Zurich'
# service = 'Tier2019-10-30'
dpath = 'E:/P1'

#full_path = os.path.realpath(__file__)
#dpath, realfilename = os.path.split(full_path)
#city='Detroit'

for city in citys:

    dataFilesPath = dpath + '/' + city
    onlyfiles = [f for f in listdir(dataFilesPath) if isfile(join(dataFilesPath, f))]

    service_city_date2num_of_scotter_in_use = {}
    service_city_date2all_scotter = {}
    for file in onlyfiles:
        try:
            date = re.findall("\d{4}-\d{2}-\d{2}", file)[0]
            service = re.findall("\D{4}", file)[0]
        except IndexError:
            date = re.findall("\d{4}-\d{2}", file)[0]
            service = re.findall("\D{4}", file)[0]
        txtFile = dataFilesPath + '/'+file
        date2num_of_scotter_in_use = {}

        if '.txt' in txtFile and 'lock' not in txtFile:
            f = open(txtFile, 'r',encoding='utf-8', errors='ignore')#encoding='utf-8', errors='ignore'

            dataDictionary = f.read()
            f.close()
            print('Reading File: ', txtFile)
            #reader = csv.reader(StringIO(dataDictionary))

            dataDictionary = json.loads(dataDictionary)
            scooterIDS = list(dataDictionary.keys())

            for id in scooterIDS:
                # lastLocations = -1
                # timeStamps = list(dataDictionary[id].keys())
                # timeStamps.sort()

                for epoch in dataDictionary[id]:
                    Latitude = dataDictionary[id][epoch][1]
                    Longitude = dataDictionary[id][epoch][2]
                    Timestamp = dataDictionary[id][epoch][0]
                    Battery = dataDictionary[id][epoch][3]

            print(len(scooterIDS))

           
