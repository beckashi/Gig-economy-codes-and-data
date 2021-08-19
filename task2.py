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

citys = ['Detroit']
dpath = 'E:/P1'

list1=[]
i=0
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

            dataDictionary = json.loads(dataDictionary)
            scooterIDS = list(dataDictionary.keys())

            list1.append(len(scooterIDS))
            s = sum(list1)
            #print(list1)
            print(s)
