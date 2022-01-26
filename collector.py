import xml.etree.ElementTree as ET
import urllib.request
from PIL import Image, ImageFilter
import requests
import os
from tqdm import tqdm
import json

f = open('./settings.json',)
settings = json.load(f)
locals().update(settings)
f.close()

directory = folder 
if not os.path.exists(directory):
    os.makedirs(directory)
globalCount = amount
blacklist = '+-blood+-gore+-bloody+-guro+'

pageIndex = 0
localCount = 1
while globalCount > 0:
    if globalCount >= 100:
        pageLimit = 100
    else:
        pageLimit = globalCount
    
    url = 'https://safebooru.org/index.php?page=dapi&s=post&q=index&tags=rating%3asafe+' + blacklist + tags + '&limit=' + str(pageLimit) + '&pid=' + str(pageIndex)
    tree = ET.parse(urllib.request.urlopen(url))
    root = tree.getroot()

    for post in tqdm(root):
        image = Image.open(requests.get(post.attrib['file_url'], stream=True).raw)
        image = image.convert("RGB") 
        image.save(directory + str(localCount) + '.jpg')
        localCount += 1
    globalCount -= pageLimit
    pageIndex += 1