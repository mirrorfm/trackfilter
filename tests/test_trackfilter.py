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
    assert f("Artist - Track (official)") == ["Artist", "Track"]
    assert f("Artist - Track.mp3") == ["Artist", "Track"]
    assert f("Artist & Artist - Track") == ["Artist Artist", "Track"]
    assert f("Artist&Artist - Track") == ["Artist&Artist", "Track"]
    assert f("Artist vs. Artist - Track") == ["Artist Artist", "Track"]
