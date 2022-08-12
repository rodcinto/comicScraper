from lxml import html
import requests
from urllib import request
import os

page = requests.get('{{DIR_HERE}}')
tree = html.fromstring(page.content)
images = tree.xpath('//img[@class="chapter_img"]/@src');

rootDir = '/comicsDownloader/'
targetDir = 'sandman-presents-lucifer'
fullPath = rootDir + targetDir
os.mkdir(fullPath)

fileCount = 1

for image in images:
    fullname = fullPath + '/' + str(fileCount) + '.jpg'
    fileCount += 1
    request.urlretrieve(image, fullname)
