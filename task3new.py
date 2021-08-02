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
import shapely
from shapely.geometry import asShape, Point  # manipulating geometry
from descartes import PolygonPatch
import shutil, os
import re
from shapely.geometry import Polygon
import json # reading geojson files
from collections import Counter
data = json.load(open('Brussels.geojson'))
data = data["features"]

#services = ['Bird', 'Circ', 'Jump', 'Lime', 'LyftScooter', 'Movo', 'Scoot', 'Skip', 'Spin', 'Tier', 'Voi', 'Wind']
#citys = ['DC', 'Detroit', 'Lisbon', 'Madrid', 'MexicoCity', 'Paris', 'SanFrancisco', 'TelAviv', 'Zurich' ]
citys=['Brussels']
dpath = 'E:/P1'
list1=[]
# full_path = os.path.realpath(__file__)
# dpath, realfilename = os.path.split(full_path)
#city='Detroit'

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

            dataDictionary = json.loads(dataDictionary)
            scooterIDS = list(dataDictionary.keys())
            coordinatesDict = {}

            for id in scooterIDS:
                lastlocation = -1
                timeStamps = list(dataDictionary[id].keys())
                timeStamps.sort()

                for epoch in timeStamps:
                    Latitude = float(dataDictionary[id][epoch][1])
                    # Latitude = dataDictionary[id][epoch][1]
                    Longitude = float(dataDictionary[id][epoch][2])
                    # Longitude = dataDictionary[id][epoch][2]
                    coordinatesDict[tuple((Latitude, Longitude))] = 1
                    Timestamp = dataDictionary[id][epoch][0]
                    Battery = dataDictionary[id][epoch][3]
                    currentlocation = (Latitude, Longitude)
                    if lastlocation == -1:
                        lastlocation = (Latitude, Longitude)
                    else:
                        if currentlocation != lastlocation:
                            trips += 1

            totalNH = 19
            numberOfScooterInNH = [0] * totalNH

            for coordinate in coordinatesDict.keys():
                polygonNumber = 0
                for polygon in data:
                    # coordinateTemp = Point(float(coordinate[1]), float(coordinate[0]))
                    coordinateTemp = Point(coordinate[1], coordinate[0])
                    geom = asShape(polygon["geometry"])
                    # Point(LONGITUDE, LATITUDE)

                    # x, y = geom.centroid.x, geom.centroid.y
                    # coordinate= Point((x,y))

                    if coordinateTemp.within(geom):
                        #print('Found in ', polygonNumber)
                        list1.append(polygonNumber)
                        maxlabel = max(list1, key=list1.count)

                    # print(x,y)
                    polygonNumber += 1
                    #result = Counter(list1)
            print(maxlabel)


