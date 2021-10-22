#!/usr/bin/env python3
import scrapy 
import string 
import os
import argparse
import sys 
import configparser
import youtube-dl 

ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})
ydl_opts = {}
config = configparser.ConfigParser()

##def functionsi

def set_download_path(path: str) -> str:
    print("changing downloads path to", str(path))

def create_artists(artist: str, website: str, platform: str) -> str:
    print("adding", str(artist), "@", str(website))     
    config.read('resources/list.txt')
    if config.has_section(str(artist)) == True: 
        config.set(str(artist), str(platform), str(website))
        with open('resources/list.txt', 'w') as configfile:
            config.write(configfile)
        configfile.close()
    else:
        config.add_section(str(artist))
        config[str(artist)][str(platform)] = str(website)
        with open('resources/list.txt', 'w') as configfile:
            config.write(configfile)
        configfile.close()

def update_tunes():
    print("looking for updates!")
    

def download_tunes():
    print("downloading!")
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([''])

def remove_artist(artist: str) -> str:
    print("removing",  str(artist))
    config.read('resources.list.txt')
    config.remove_section(str(artist))

def list_artists():
    config.read('resources/list.txt')
    sections = config.sections()
    for section in sections:
        if config.has_section(section):
            print(f'Found {section}')

##configuring argparse stuff

parser = argparse.ArgumentParser()
subparser= parser.add_subparsers(dest='command')

setup = subparser.add_parser('setup', help='add download path. default is is AutoM00sic dir')
setup.add_argument('--path', type=str, required=True)

add = subparser.add_parser('add', help='add artist and site')
add.add_argument('--artist', type=str, required=True)
add.add_argument('--website', type=str, required=True)
add.add_argument('--platform', type=str, required=True)

update = subparser.add_parser('update', help='update from list')

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
    update_tunes()

if args.command == 'download':
    download_tunes()

if args.command == 'list':
    list_artists()
