#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

    You might be tempted to import things from __main__ later, but that will cause
    problems: the code will get executed twice:

    - When you run `python -mtrackfilter` python will execute
        ``__main__.py`` as a script. That means there won't be any
        ``trackfilter.__main__`` in ``sys.modules``.
    - When you import __main__ it will get executed again (as a module) because
        there's no ``trackfilter.__main__`` in ``sys.modules``.

    Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
import re

YOUTUBE_TRACK_FILTER_RULES = [
    r"^\s+|\s+$"
    r"\*+\s?\S+\s?\*+$",
    r"\[[^\]]+\]$",
    r"\([^)]*version\)$",
    r"\.(avi|wmv|mpg|mpeg|flv|mp3|flac)$",
    r"((with)?\s*lyrics?( video)?\s*)",
    r"(Official Track Stream*)",
    r"(of+icial\s*)?(music\s*)?video",  # (official)? (music)? video
    r"(of+icial\s*)?(music\s*)?audio",  # (official)? (music)? audio
    r"(ALBUM TRACK\s*)?(album track\s*)",  # (ALBUM TRACK)
    r"(COVER ART\s*)?(Cover Art\s*)",  # (Cover Art)
    r"\(\s*of+icial\s*\)",  # (official)
    r"\(\s*[0-9]{4}\s*\)",  # (1999)
    r"\(\s*(HD|HQ)\s*\)$",  # HD (HQ)
    r"(HD|HQ)\s*$",  # HD (HQ)
    r"(vid[\u00E9e]o)?\s?clip\sofficiel",  # video clip officiel
    r"of+iziel+es\s*",  # offizielles
    r"vid[\u00E9e]o\s?clip",  # video clip
    r"\sclip",  # clip
    r"full\s*album",  # Full Album
    r"\(?live.*?\)?$",  # live
    r"\|.*$",  # | something
    r"\(+\s*\)+",  # Leftovers after e.g. (official video)
    r"\(.*[0-9]{1,2}\/[0-9]{1,2}\/[0-9]{2,4}.*\)",  # (*01/01/1999*)
    # r"^[/,:;~-\s"]+",  # trim starting white chars and dash
    # r"[/,:;~-\s"!]+$"  # trim trailing white chars and dash
]


SEPARATORS = [
    ' -- ', '--', ' ~ ', ' - ', ' – ', ' — ',
    ' // ', '-', '–', '—', ':', '|', '///', '/'
]


def find_separator(title):
    if title is None or len(title) == 0:
        return
    for sep in SEPARATORS:
        try:
            index = title.index(sep)
            return {
                'index': index,
                'length': len(sep)
            }
        except ValueError:
            continue


def split_artist_track(title):
    if title:
        title = filter_with_filter_rules(title)
        separator = find_separator(title)
        if separator:
            i = separator['index']
            length = separator['length']
            artist = title[0:i]
            track = title[i+length:]
            return strip([artist, track])
    return None


def strip(words):
    return list(map(str.strip, words))


def filter_with_filter_rules(text):
    for regex in YOUTUBE_TRACK_FILTER_RULES:
        text = re.sub(regex, "", text)
    return text
