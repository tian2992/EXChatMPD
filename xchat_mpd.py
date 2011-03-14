#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2011 Sebastian Oliva <tian2992@gmail.com>
#Permission to use, copy, modify, and/or distribute this software for any
#purpose with or without fee is hereby granted, provided that the above
#copyright notice and this permission notice appear in all copies.

#THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
#WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
#MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
#ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
#WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
#ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
#OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

import os
import xchat
import mpd

__module_name__ = "MPD Status"
__module_version__ = "0.3"
__module_description__ = "MPD Current playing song"


def send_status():
  try:
    current_song = client.currentsong()
  except:
    current_song = {}
  if current_song == {}:
    status = "silence"
  else:
    try:
      status = current_song["title"] + " - " + current_song["artist"]
      if "album" in current_song:
        status = status +  " (" + current_song["album"] + ")"
    except:
      status = "a song with missing tags"
  xchat.command("me is listening to %s" % (status))

def command_pause():
  client.pause()

def command_set_volume(argString):
  volume = int(argString)
  client.setvol(volume)

def EXChatMPD(word, word_eol, userdata):
  client = mpd.MPDClient()
  try:
    client.connect("localhost",6600) #TODO: parametrize
    if (word_eol[0]=="mpd"):
      send_status()
    else: #it's not status
      
    client.disconnect()
  except: #fail to connect
    print("connection failed")
  return xchat.EAT_ALL
  
xchat.hook_command("mpd", EXChatMPD, help="/mpd command or just /mpd for current playing song")
