#!/usr/bin/env python
# encoding: utf-8

import json
import dicttoxml
from third_part import pyMoeFou
import argparse
import sys

MF = pyMoeFou.MoeFou()

def JsonToXml(J):
    d = json.loads(J)

    return dicttoxml.dicttoxml(d)

def GetMusics(name):
    musicDict = {}
    num = 1
    for music in MF.GetMusicByName(name):
        musicDict[str(num)] = [music.id, music.title]
        num += 1

    return musicDict

def GetSongs(musicID):
    songDict = {}
    music = MF.GetMusicByID(musicID)
    num = 1
    for song in MF.GetSongByMusic(music):
        songDict[str(num)] = [song.id, song.title]
        num += 1

    return songDict

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

    args = parser.parse_args()

    try:
        rlt = ''
        if args.music:
            rlt = dicttoxml.dicttoxml(GetMusics(args.music))
        elif args.song:
            rlt = dicttoxml.dicttoxml(GetSongs(int(args.song)))
        elif args.url:
            rlt = GetUrl(int(args.url))
        else:
            exit(-1)

        with open("OUT.txt", "wb") as fp:
            fp.write(rlt)
    except Exception as e:
        print(e.message)

