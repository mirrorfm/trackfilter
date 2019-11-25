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


def split_artist_and_track_name(youtube_title):
    """
    Args:
        youtube_title (string): Song name

    Returns:
       array: An array of string containing the artist and track name

    Splits artist and track name.
    """
    artist_and_track = youtube_title.split("-", 1)
    return list(map(str.strip, artist_and_track))
