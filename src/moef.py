#!/usr/bin/env python
# encoding: utf-8

#import json
#import dicttoxml
from third_part import pyMoeFou
import argparse
import requests
import os
#import sys

MF = pyMoeFou.MoeFou()

#def JsonToXml(J):
#    d = json.loads(J)
#
#    return dicttoxml.dicttoxml(d)

def GetMusics(name):
    musicList = []
    for music in MF.GetMusicByName(name):
        musicList.append((music.id, music.title.encode('utf-8')))

    return musicList

def GetSongs(musicID):
    songList = []
    music = MF.GetMusicByID(musicID)
    for song in MF.GetSongByMusic(music):
        songList.append((song.id, song.title.encode('utf-8')))

    return songList

def GetUrl(songID):
    song = MF.GetSongByID(songID)
    try:
        up = MF.GetUpBySong(song)[-1]
        return up.url
    except IndexError as e:
        print(e.message)
        return ''

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="MoeFou Desktop App.")
    parser.add_argument('-m', '--music', default='', help='music name for get musics.')
    parser.add_argument('-s', '--song', default='', help='music id for get songs.')
    parser.add_argument('-u', '--url', default='', help='song id for get song\'s url.')
    parser.add_argument('-l', '--loop', default='1', help='the loop times if play')

    args = parser.parse_args()

    content_length = -1
    if args.music:
        rlt = GetMusics(args.music)
    elif args.song:
        rlt = GetSongs(int(args.song))
    elif args.url:
        rlt = GetUrl(int(args.url))
        headers = requests.head(rlt.strip()).headers
        content_length = int(headers.get('content-length', -1))
    else:
        exit(-1)
    if content_length > 0:
        os.system("mplayer -loop {times} -cache {cache_length} {url}".format(
            times=int(args.loop),
            cache_length=content_length / 10,
            url=rlt)
        )
    else:
        for item in rlt:
            print("~~{iden}~~\t{title}".format(iden=item[0], title=item[1]))

    #try:
    #    rlt = ''
    #    if args.music:
    #        rlt = dicttoxml.dicttoxml(GetMusics(args.music))
    #    elif args.song:
    #        rlt = dicttoxml.dicttoxml(GetSongs(int(args.song)))
    #    elif args.url:
    #        rlt = GetUrl(int(args.url))
    #    else:
    #        exit(-1)

    #    with open("OUT.txt", "wb") as fp:
    #        fp.write(rlt)
    #except Exception as e:
    #    print(e.message)

