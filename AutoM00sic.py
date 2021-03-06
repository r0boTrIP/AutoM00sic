#!/usr/bin/env python3
import string 
import sys
import argparse
import os
import configparser
import youtube_dl 
import datetime
from bs4 import BeautifulSoup as bss 

ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})
ydl_opts = {}
listfile = configparser.ConfigParser()
dl_path = os.path.dirname(__file__)


def set_download_path(path: str) -> str:
    print("changing downloads path to", str(path))

def create_artists(artist: str, website: str, platform: str) -> str:
    print("adding", str(artist), "@", str(website))     
    listfile.read('resources/list.txt')
    if listfile.has_section(str(artist)) == True: 
        listfile.set(str(artist), str(platform), str(website))
        with open('resources/list.txt', 'w') as listdata:
            listfile.write(listdata)
        listdata.close()
    else:
        listfile.add_section(str(artist))
        listfile[str(artist)][str(platform)] = str(website)
        with open('resources/list.txt', 'w') as listdata:
            listfile.write(listdata)
        listdata.close()

#interfaces with list file, sends values to scraper functions & determines correct scraper
def update_tunes(datetime: str) -> str:
    print("looking for updates!")
    listfile.read('resources/list.txt')
    for each_section in listfile.sections():
        for (each_key, each_val) in listfile.items(each_section):
            print("checking out", str(each_val))
            webscrape(each_val)

#does the actual scraping & determines url. eventually make faster by comparing complete.txt before crawling 
def webscrape(site: str) -> str:
    for sites in site: 

#handles ydl downloads
def download_tunes():
	print("downloading!")
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		for link in ydl_opts:
			if ydl_opts not in ('resources/complete.txt'):
				 ydl.download([''])
				 with open('resources/complete.txt', 'w') as complete:
					 listfile.write(complete)
					 complete.close()
					 print('downloaded', complete)

def remove_artist(artist: str) -> str:
    print("removing",  str(artist))
    listfile.read('resources.list.txt')
    listfile.remove_section(str(artist))

def list_artists():
    listfile.read('resources/list.txt')
    sections = listfile.sections()
    for section in sections:
        if listfile.has_section(section):
            print(f'Found {section}')

#configuring argparse stuff

parser = argparse.ArgumentParser()
subparser= parser.add_subparsers(dest='command')

setup = subparser.add_parser('setup', help='add download path. default is is AutoM00sic dir')
setup.add_argument('--path', type=str, required=True)

add = subparser.add_parser('add', help='add artist and site')
add.add_argument('--artist', type=str, required=True)
add.add_argument('--website', type=str, required=True)
add.add_argument('--platform', type=str, required=True)

update = subparser.add_parser('update', help='update from list. use date yyyy-mm-dd if you want to start searching from a certain date. Will download everything otherwise.')
update.add_argument('--datetime', type=str, required=False)

download = subparser.add_parser('download', help='download t00ns')

listn = subparser.add_parser('list', help='list t00ns')

remove = subparser.add_parser('remove', help='remove artist and site from list') 
remove.add_argument('--artist', type=str, required=True)

if len(sys.argv) <= 1:
    sys.argv.append('--help')

args = parser.parse_args()

#calling functions with input from argparse

if args.command == 'add':
    create_artists(args.artist, args.website, args.platform)

if args.command == 'setup':
    set_download_path(args.path)

if args.command == 'remove':
    remove_artist(args.artist)

if args.command == 'update':
    update_tunes(args.datetime)

if args.command == 'download':
    download_tunes()

if args.command == 'list':
    list_artists()
