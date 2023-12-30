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
    r"\[[^\]]+\].*",  # [whatever] something else
    r"\([^)]*version\)$",
    r"\.(avi|wmv|mpg|mpeg|flv|mp3|flac)$",
    r"((with)?\s*lyrics?( video)?\s*)",
    r"(Official Track Stream*)",
    r"(of+icial\s*)?(music\s*)?video",  # (official)? (music)? video
    r"(of+icial\s*)?(music\s*)?audio",  # (official)? (music)? audio
    r"(ALBUM TRACK\s*)?(album track\s*)",  # (ALBUM TRACK)
    r"(COVER ART\s*)?(Cover Art\s*)",  # (Cover Art)
    r"\((.*?)subt(.*?)\)",  # (subtitles espanol) https://regex101.com/r/8kVFrm/1
    r"\((.*?)archives\)",  # (something ARCHIVES)
    r"\-? (.*?) archives",  # - something ARCHIVES)
    r"\(\s*of+icial\s*\)",  # (official)
    r"\(\s*[0-9]{4}\s*\)",  # (1999)
    r"\(\s*([a-z]*\s)?\s*[0-9]{4}([a-z])?\s*([a-z]*\s?)?\)",  # (Techno 1990)
    r"\([A-Z]{1,10}[0-9]{1,4}\)",  # (CAT001) or (A1) https://regex101.com/r/JiLQST/2
    r"\(\s*([0-9]{4}\s*)?unreleased\s*([0-9]{4}\s*)?\)",  # (unreleased) https://regex101.com/r/Z5zD8l/1
    r"\(\s*(HD|HQ|ᴴᴰ)\s*\)$",  # HD (HQ)
    r"(HD|HQ|ᴴᴰ)\s*$",  # HD (HQ)
    r"(vid[\u00E9e]o)?\s?clip\sofficiel",  # video clip officiel
    r"of+iziel+es\s*",  # offizielles
    r"vid[\u00E9e]o\s?clip",  # video clip
    r"\sclip",  # clip
    r"full\s*album",  # Full Album
    r"\(?live.*?\)?$",  # live
    r"([|]|[\\\/]{2,}).*$",  # | something
    r"\s*[0-9]{4}\s*",  # Track (Artist remix) 1999 https://regex101.com/r/vFHEvY/2
    r"\(+\s*\)+",  # Leftovers after e.g. (official video)
    r"\(.*[0-9]{1,2}\/[0-9]{1,2}\/[0-9]{2,4}.*\)",  # (*01/01/1999*)
    r"#[a-z0-9]*"  # #HashTag
]


SEPARATORS = [
    ' -- ', '--', ' ~ ', ' - ', ' – ', ' — ',
    ' // ', '-', '–', '—', ':', '|', '///', '/', '►'
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


def clean_artist(artist):
    # Remove [whatever] before artist
    artist = re.sub(r"\[[^\]]+\]", "", artist)

    # Remove (1999) before Artist
    artist = re.sub(r"\(\s*[0-9]{4}\s*\)", "", artist)

    # Remove "PREMIERE: " or "INCOMING: "
    # https://regex101.com/r/nG16TF/3
    artist = re.sub(r"((PREMIERE|INCOMING)\s*:)?", "", artist.strip(), flags=re.IGNORECASE)

    # Remove vinyl track number
    # https://regex101.com/r/gHh2TB/4
    artist = re.sub(r"^((([a-zA-Z]{1,2})|([0-9]{1,2}))[1-9]?\. )?", "", artist.strip())

    # Remove indicator for multiple artists
    artist_separators = ['&', 'feat', 'feat.', 'vs', 'vs.', 'featuring']
    for s in artist_separators:
        artists = artist.split(' %s ' % s)
        if len(artists) > 1:
            return artists
    return [artist]


def artist_in_track(track):
    feat_separator = [' feat. ', ' featuring ', ' feat ', ' ft. ', ' ft ']  # order matters
    for s in feat_separator:
        parts = track.split(s)
        if len(parts) > 1:
            return parts[0].strip(), parts[1].strip()
    return track, None


def split_artist_track(title):
    if not title:
        return None

    # Strip full title
    title = title.strip()

    separator = find_separator(title)
    if separator:
        i = separator['index']
        length = separator['length']
        artist = title[0:i]
        track = filter_with_filter_rules(title[i+length:])
        artists = clean_artist(artist)

        # Handle case where another artist is part of the track
        # Artist1 - Track feat. Artist2
        track, second_artist = artist_in_track(track)
        if second_artist:
            artists.append(second_artist)
        return [strip(artists), strip([track])[0]]

    # https://regex101.com/r/FkABDG/1
    quoted_track = re.match(r"(.+?)\"([^\"]*)\"", title)
    if quoted_track:
        artist = quoted_track.group(1)
        track = quoted_track.group(2)
        return [strip([artist]), strip([track])[0]]


def strip(words):
    return list(map(str.strip, words))


def filter_with_filter_rules(text):
    for regex in YOUTUBE_TRACK_FILTER_RULES:
        text = re.sub(regex, "", text, flags=re.IGNORECASE)

    while True:
        # Track (Artist remix) (Remove this) (And this)  https://regex101.com/r/0meJko/2
        groups = re.findall(r"\(.*\)\s*(\((.*)\))", text)
        if len(groups) > 0:
            text = text.replace(groups[0][0], "")
        else:
            break

    return text
