# -*- coding: utf-8 -*-

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
import statistics
import shutil, os
import re

# services = ['Bird', 'Circ', 'Jump', 'Lime', 'LyftScooter', 'Movo', 'Scoot', 'Skip', 'Spin', 'Tier', 'Voi', 'Wind']
# citys = ['DC', 'Detroit', 'Lisbon', 'Madrid', 'MexicoCity', 'Paris', 'SanFrancisco', 'TelAviv', 'Zurich' ]
citys=['Brussels']
# service = 'Tier2019-10-30'
dpath = 'E:/P3'
# full_path = os.path.realpath(__file__)
# dpath, realfilename = os.path.split(full_path)
sumtime = 0

coordinatesDict = {}
for city in citys:

    dataFilesPath = dpath + '/' + city
    onlyfiles = [f for f in listdir(dataFilesPath) if isfile(join(dataFilesPath, f))]

    service_city_date2num_of_scotter_in_use = {}
    service_city_date2all_scotter = {}
    for file in onlyfiles:
        trips = 0
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
            scootersDict = json.loads(dataDictionary)  # json to python
            # scootersDict = list(dataDictionary.keys())   # return keys of datadict to list
            tripsDictionary = []
            for id in scootersDict:
                currentlocation = (0,0)
                previousEpoch = 0
                previousBattery = 0
                for epoch in scootersDict[id]:
                    # location = (latitude,longitude)
                    latitute = float(scootersDict[id][epoch][1])
                    longitude = float(scootersDict[id][epoch][2])
                    location = (latitute, longitude)
                    if currentlocation == (0, 0):
                        currentlocation = location
                        previousEpoch = int(epoch)
                        previousBattery = float(scootersDict[id][epoch][3])
                    else:
                        if location != currentlocation:
                            # distance
                            distance = (currentlocation[0] - location[0], currentlocation[1] - location[1])
                            # trip total time = epoch - previousEpoch
                            epoch1 = epoch[:10]
                            previousEpoch1 = previousEpoch[:10]
                            epoch1 = int(epoch1)  # str to int
                            previousEpoch1 = int(previousEpoch1)
                            #print(epoch1, previousEpoch1)
                            try:
                                epoch2 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(epoch1))  # MS to time
                                previousEpoch2 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(previousEpoch1))
                                #print(epoch2, previousEpoch2)

                                d1 = datetime.datetime.strptime(epoch2, '%Y-%m-%d %H:%M:%S')  # use time to subtract
                                d2 = datetime.datetime.strptime(previousEpoch2, '%Y-%m-%d %H:%M:%S')
                                delta = d1 - d2
                                time = delta.total_seconds()  # per seconds
                                #print(time)
                            except:
                                pass

                            # distance between location and currentlocation
                            # time difference between epoch, previousEpoch
                            # difference between batteries previousBattery & scootersDict[id][epoch][5]
                            if time < 5*3600 and (previousBattery - float(scootersDict[id][epoch][3])) < 0:

                                dictElement = dict()
                                dictElement['source'] = currentlocation
                                dictElement['destination'] = location
                                # trip total time
                                dictElement['totaltime'] = time

                                # distance
                                dictElement['distance'] = distance
                                # day time of the trip
                                dictElement['daytime'] = time/(24*3600)
                                # scooter company(services)
                                dictElement['company'] = service
                                # scooter id
                                dictElement['scooterid'] = id # MS

                                tripsDictionary.append(dictElement)
                                print(tripsDictionary)

                                # averagetripdistance =
                                f.close()
                    currentlocation = location
                    previousEpoch = epoch
                    previousBattery = float(scootersDict[id][epoch][3])











