#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from trackfilter.cli import split_artist_track as f


class Test(unittest.TestCase):

    def test_split_artist_track(self):
        self.assertEqual(f("Artist - Track"), [["Artist"], "Track"])
        self.assertEqual(f("Artist - Track | something"), [["Artist"], "Track"])
        self.assertEqual(f("Artist   -   Track"), [["Artist"], "Track"])
        self.assertEqual(f("Artist -- Track"), [["Artist"], "Track"])
        self.assertEqual(f("Artist – Track"), [["Artist"], "Track"])
        self.assertEqual(f("Art-ist - Track"), [["Art-ist"], "Track"])
        self.assertEqual(f("Artist - Tr-ack"), [["Artist"], "Tr-ack"])
        self.assertEqual(f("Artist - Track - Something"), [["Artist"], "Track - Something"])
        self.assertEqual(f("Artist-Track"), [["Artist"], "Track"])
        self.assertEqual(f("Artist & Track"), None)
        self.assertEqual(f(None), None)
        self.assertEqual(f(""), None)
        self.assertEqual(f("Artist - Track [LABEL001]"), [["Artist"], "Track"])
        self.assertEqual(f("Artist - Track [LABEL001] album"), [["Artist"], "Track"])
        self.assertEqual(f("[LABEL001] Artist - Track"), [["Artist"], "Track"])
        self.assertEqual(f("Artist [LABEL001] - Track"), [["Artist"], "Track"])
        self.assertEqual(f("Artist - Track (official)"), [["Artist"], "Track"])
        self.assertEqual(f("Artist - Track.mp3"), [["Artist"], "Track"])
        self.assertEqual(f("Artist1 & Artist2 - Track"), [["Artist1", "Artist2"], "Track"])
        self.assertEqual(f("Art&ist - Track"), [["Art&ist"], "Track"])
        self.assertEqual(f("Artist1 vs. Artist2- Track"), [["Artist1", "Artist2"], "Track"])
        self.assertEqual(f("Artist1 - Track feat. Artist2"), [["Artist1", "Artist2"], "Track"])
        self.assertEqual(f("A1. Artist - Track"), [["Artist"], "Track"])
        self.assertEqual(f("AA. Artist - Track"), [["Artist"], "Track"])
        self.assertEqual(f("AB. Artist - Track"), [["Artist"], "Track"])
        self.assertEqual(f("BA. Artist - Track"), [["Artist"], "Track"])
        self.assertEqual(f("BB. Artist - Track"), [["Artist"], "Track"])
        self.assertEqual(f("D1. Artist - Track"), [["Artist"], "Track"])
        self.assertEqual(f("A1. Artist - Track"), [["Artist"], "Track"])
        self.assertEqual(f("A. Artist - Track"), [["Artist"], "Track"])
        self.assertEqual(f("AA. Artist - Track"), [["Artist"], "Track"])
        self.assertEqual(f("AA1. Artist - Track"), [["Artist"], "Track"])
        self.assertEqual(f("1A. Artist - Track"), [["1A. Artist"], "Track"])
        self.assertEqual(f("1. Artist - Track"), [["Artist"], "Track"])
        self.assertEqual(f("01. Artist - Track"), [["Artist"], "Track"])
        self.assertEqual(f("99. Artist - Track"), [["Artist"], "Track"])
        self.assertEqual(f("100. Artist - Track"), [["100. Artist"], "Track"])
        self.assertEqual(f("Artist - Track (A1)"), [["Artist"], "Track"])
        self.assertEqual(f("PREMIERE: Artist - Track"), [["Artist"], "Track"])
        self.assertEqual(f("Premiere: Artist - Track"), [["Artist"], "Track"])
        self.assertEqual(f("Premiere : Artist - Track"), [["Artist"], "Track"])
        self.assertEqual(f("Artist - Track (1999)"), [["Artist"], "Track"])
        self.assertEqual(f("Artist - Track (Techno 1990)"), [["Artist"], "Track"])
        self.assertEqual(f("Artist - Track (Techno 123)"), [["Artist"], "Track (Techno 123)"])
        self.assertEqual(f("Artist - Track ( unreleased 1990 )"), [["Artist"], "Track"])
        self.assertEqual(f("  Premiere : Artist - Track"), [["Artist"], "Track"])
        self.assertEqual(f("   Premiere : Artist - Track"), [["Artist"], "Track"])
        self.assertEqual(f("Artist ► Track"), [["Artist"], "Track"])
        self.assertEqual(f("Artist ► Track [genre] album"), [["Artist"], "Track"])
        self.assertEqual(f("Artist - Track ᴴᴰ"), [["Artist"], "Track"])
        self.assertEqual(f("[PREMIERE] B2. Artist - Track [OATH001]"), [["Artist"], "Track"])
        self.assertEqual(f("Artist - Track // Label"), [["Artist"], "Track"])
        self.assertEqual(f("Artist - Track ///Label"), [["Artist"], "Track"])
        self.assertEqual(f("Artist - Track (Official Video) | Some label"), [["Artist"], "Track"])
        self.assertEqual(f("Artist - Track (Official audio)"), [["Artist"], "Track"])
        self.assertEqual(f("Artist \"Track\" something"), [["Artist"], "Track"])
        self.assertEqual(f("Artist - Track (From \"foo\")"), [["Artist"], "Track (From \"foo\")"])
        self.assertEqual(f("Artist - Track (Subtítulos en español) ||Lyrics||"), [["Artist"], "Track"])
        self.assertEqual(f("Artist - Track (french subtitles)"), [["Artist"], "Track"])
        self.assertEqual(f("Artist - Track (something archives)"), [["Artist"], "Track"])
        self.assertEqual(f("Artist - Track - foo archives"), [["Artist"], "Track"])
        self.assertEqual(f("Artist - Track #HashTag"), [["Artist"], "Track"])
        self.assertEqual(f("INCOMING : Artist - Track #HashTag"), [["Artist"], "Track"])
        self.assertEqual(f("Artist - Track (CAT001)"), [["Artist"], "Track"])
        self.assertEqual(f("Artist - Track (Artist remix) (CAT001)"), [["Artist"], "Track (Artist remix)"])
        self.assertEqual(f("Artist - Track (Artist remix)(CAT001)"), [["Artist"], "Track (Artist remix)"])
        self.assertEqual(f("Artist - Track (Artist remix)(1998)"), [["Artist"], "Track (Artist remix)"])
        self.assertEqual(f("Artist - Track (Artist remix) (1998)"), [["Artist"], "Track (Artist remix)"])
        self.assertEqual(f("Artist - Track (Artist remix) 1998"), [["Artist"], "Track (Artist remix)"])
        self.assertEqual(f("Artist - Track (Artist remix) (Something else)"), [["Artist"], "Track (Artist remix)"])
        self.assertEqual(f("Artist - Track (Artist remix)(Something else) (again)"), [["Artist"], "Track (Artist remix)"])
