#!/usr/bin/env python
# -*- coding: utf-8 -*-

from trackfilter.cli import split_artist_track as f


def test_split_artist_track():
    assert f("Artist - Track") == ["Artist", "Track"]
    assert f("Artist   -   Track") == ["Artist", "Track"]
    assert f("Artist -- Track") == ["Artist", "Track"]
    assert f("Artist – Track") == ["Artist", "Track"]
    assert f("Art-ist - Track") == ["Art-ist", "Track"]
    assert f("Artist - Tr-ack") == ["Artist", "Tr-ack"]
    assert f("Artist - Track - Something") == ["Artist", "Track - Something"]
    assert f("Artist & Track") is None
    assert f(None) is None
    assert f("") is None
    assert f("Artist - Track [LABEL001]") == ["Artist", "Track"]
    assert f("[LABEL001] Artist - Track") == ["Artist", "Track"]
    assert f("Artist - Track (official)") == ["Artist", "Track"]
    assert f("Artist - Track.mp3") == ["Artist", "Track"]
    assert f("Artist & Artist - Track") == ["Artist Artist", "Track"]
    assert f("Artist&Artist - Track") == ["Artist&Artist", "Track"]
    assert f("Artist vs. Artist- Track") == ["Artist Artist", "Track"]
    assert f("A1. Artist - Track") == ["Artist", "Track"]
    assert f("AA. Artist - Track") == ["Artist", "Track"]
    assert f("AB. Artist - Track") == ["Artist", "Track"]
    assert f("BA. Artist - Track") == ["Artist", "Track"]
    assert f("BB. Artist - Track") == ["Artist", "Track"]
    assert f("D1. Artist - Track") == ["Artist", "Track"]
    assert f("A1. Artist - Track") == ["Artist", "Track"]
    assert f("A. Artist - Track") == ["Artist", "Track"]
    assert f("AA. Artist - Track") == ["Artist", "Track"]
    assert f("AA1. Artist - Track") == ["Artist", "Track"]
    assert f("1. Artist - Track") == ["Artist", "Track"]
    assert f("01. Artist - Track") == ["Artist", "Track"]
    assert f("99. Artist - Track") == ["Artist", "Track"]
    assert f("PREMIERE: Artist - Track") == ["Artist", "Track"]
    assert f("Premiere: Artist - Track") == ["Artist", "Track"]
    assert f("Artist - Track (1999)") == ["Artist", "Track"]
    assert f("Artist - Track (Techno 1990)") == ["Artist", "Track"]
    assert f("Artist - Track (Remix123)") == ["Artist", "Track (Remix123)"]
    assert f("Artist - Track (Techno 123)") == ["Artist", "Track (Techno 123)"]
