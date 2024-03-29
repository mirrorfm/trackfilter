#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from trackfilter.cli import split_artist_track as f


class Test(unittest.TestCase):

    def test_split_artist_track(self):
        from_to = {
            "Artist - Track": [["Artist"], "Track"],
            "Artist - Track | something": [["Artist"], "Track"],
            "Artist   -   Track": [["Artist"], "Track"],
            "Artist -- Track": [["Artist"], "Track"],
            "Artist – Track": [["Artist"], "Track"],
            "Art-ist - Track": [["Art-ist"], "Track"],
            "Artist - Tr-ack": [["Artist"], "Tr-ack"],
            "Artist - Track - Something": [["Artist"], "Track - Something"],
            "Artist-Track": [["Artist"], "Track"],
            "Artist & Track": None,
            None: None,
            "": None,
            "Artist - Track [LABEL001]": [["Artist"], "Track"],
            "Artist - Track [LABEL001] album": [["Artist"], "Track"],
            "[LABEL001] Artist - Track": [["Artist"], "Track"],
            "Artist [LABEL001] - Track": [["Artist"], "Track"],
            "Artist - Track (official)": [["Artist"], "Track"],
            "Artist - Track.mp3": [["Artist"], "Track"],
            "Artist1 & Artist2 - Track": [["Artist1", "Artist2"], "Track"],
            "Art&ist - Track": [["Art&ist"], "Track"],
            "Artist1 vs. Artist2- Track": [["Artist1", "Artist2"], "Track"],
            "Artist1 - Track feat. Artist2": [["Artist1", "Artist2"], "Track"],
            "A1. Artist - Track": [["Artist"], "Track"],
            "AA. Artist - Track": [["Artist"], "Track"],
            "AB. Artist - Track": [["Artist"], "Track"],
            "BA. Artist - Track": [["Artist"], "Track"],
            "BB. Artist - Track": [["Artist"], "Track"],
            "D1. Artist - Track": [["Artist"], "Track"],
            "A. Artist - Track": [["Artist"], "Track"],
            "AA1. Artist - Track": [["Artist"], "Track"],
            "1A. Artist - Track": [["1A. Artist"], "Track"],
            "1. Artist - Track": [["Artist"], "Track"],
            "01. Artist - Track": [["Artist"], "Track"],
            "99. Artist - Track": [["Artist"], "Track"],
            "100. Artist - Track": [["100. Artist"], "Track"],
            "Artist - Track (A1)": [["Artist"], "Track"],
            "PREMIERE: Artist - Track": [["Artist"], "Track"],
            "Premiere: Artist - Track": [["Artist"], "Track"],
            "Premiere : Artist - Track": [["Artist"], "Track"],
            "  Premiere : Artist - Track": [["Artist"], "Track"],
            "   Premiere : Artist - Track": [["Artist"], "Track"],
            "[PREMIERE] B2. Artist - Track [OATH001]": [["Artist"], "Track"],
            "(1999) Artist - Track": [["Artist"], "Track"],
            "Artist - Track (1999)": [["Artist"], "Track"],
            "Artist - Track // 2020 (1994)": [["Artist"], "Track"],
            "Artist - Track // Unknown Year": [["Artist"], "Track"],
            "Artist - Track (Techno 1990)": [["Artist"], "Track"],
            "Artist - Track (Techno 123)": [["Artist"], "Track (Techno 123)"],
            "Artist - Track ( unreleased 1990 )": [["Artist"], "Track"],
            "Artist ► Track": [["Artist"], "Track"],
            "Artist ► Track [genre] album": [["Artist"], "Track"],
            "Artist - Track ᴴᴰ": [["Artist"], "Track"],
            "Artist - Track // Label": [["Artist"], "Track"],
            "Artist - Track ///Label": [["Artist"], "Track"],
            "Artist - Track (Official Video) | Some label": [["Artist"], "Track"],
            "Artist - Track (Official audio)": [["Artist"], "Track"],
            "Artist - Track (vinyl)": [["Artist"], "Track"],
            "Artist - Track (lyrics)": [["Artist"], "Track"],
            "Artist - Track |label|": [["Artist"], "Track"],
            "Artist \"Track\" something": [["Artist"], "Track"],
            "Artist - Track (From \"foo\")": [["Artist"], "Track (From \"foo\")"],
            "Artist - Track (Subtítulos en español) ||Lyrics||": [["Artist"], "Track"],
            "Artist - Track (french subtitles)": [["Artist"], "Track"],
            "Artist - Track (something archives)": [["Artist"], "Track"],
            "Artist - Track (Free Download)": [["Artist"], "Track"],
            "Artist - Track (extended)": [["Artist"], "Track"],
            "Artist - Track - foo archives": [["Artist"], "Track"],
            "Artist - Track - unlimited download": [["Artist"], "Track"],
            "Artist - Track #HashTag": [["Artist"], "Track"],
            "Artist - Track (Free Download) #HashTag": [["Artist"], "Track"],
            "INCOMING : Artist - Track #HashTag": [["Artist"], "Track"],
            "Artist - Track (CAT001)": [["Artist"], "Track"],
            "Artist - Track (Artist remix) (CAT001)": [["Artist"], "Track (Artist remix)"],
            "Artist - Track (Artist remix)(CAT001)": [["Artist"], "Track (Artist remix)"],
            "Artist - Track (Artist remix)(1998)": [["Artist"], "Track (Artist remix)"],
            "Artist - Track (Artist remix) (1998)": [["Artist"], "Track (Artist remix)"],
            "Artist - Track (Artist remix) 1998": [["Artist"], "Track (Artist remix)"],
            "Artist - Track (Artist remix) (Something else)": [["Artist"], "Track (Artist remix)"],
            "Artist - Track (Artist remix)(Something else) (again)": [["Artist"], "Track (Artist remix)"]
        }

        for fr, to in from_to.items():
            self.assertEqual(f(fr), to)
