from trackfilter.cli import split_artist_and_track_name


def test_split_artist_and_track_name():
    assert split_artist_and_track_name("Artist - Track") == ["Artist", "Track"]
