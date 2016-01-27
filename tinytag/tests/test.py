from __future__ import unicode_literals

import os

from tinytag import TinyTag


testfiles = {'vbri.mp3': {'track_total': None, 'duration': 0.5224489795918368, 'album': 'I Can Walk On Water I Can Fly', 'year': '2007', 'title': 'I Can Walk On Water I Can Fly', 'artist': 'Basshunter', 'track': '01'},
             'cbr.mp3': {'track_total': None, 'duration': 0.4963265306122449, 'album': 'I Can Walk On Water I Can Fly', 'year': '2007', 'title': 'I Can Walk On Water I Can Fly', 'artist': 'Basshunter', 'track': '01'},
             'id3v22-test.mp3': {'track_total': '11', 'duration': 0.156734693877551, 'album': 'Hymns for the Exiled', 'year': '2004', 'title': 'cosmic american', 'artist': 'Anais Mitchell', 'track': '3'},
             'silence-44-s-v1.mp3': {'track_total': None, 'duration': 3.7355102040816326, 'album': 'Quod Libet Test Data', 'year': '2004', 'title': 'Silence', 'artist': 'piman', 'track': '2'},
             'UTF16.mp3': {'duration': 0.052244897959183675, 'track_total': '11', 'track': '07', 'artist': 'The National', 'year': '2010', 'album': 'High Violet', 'title': 'Lemonworld'},
             'empty.ogg': {'track_total': None, 'duration': 3.684716553287982, 'album': None, '_max_samplenum': 162496, 'year': None, 'title': None, 'artist': None, 'track': None, '_tags_parsed': False},
             'multipagecomment.ogg': {'track_total': None, 'duration': 3.684716553287982, 'album': None, '_max_samplenum': 162496, 'year': None, 'title': None, 'artist': None, 'track': None, '_tags_parsed': False},
             'multipage-setup.ogg': {'track_total': None, 'duration': 4.128798185941043, 'album': 'Timeless', 'year': '2006', 'title': 'Burst', 'artist': 'UVERworld', 'track': '7', '_tags_parsed': False},
             'test.ogg': {'track_total': None, 'duration': 1.0, 'album': 'the boss', 'year': '2006', 'title': 'the boss', 'artist': 'james brown', 'track': '1', '_tags_parsed': False},
             'test.wav': {'duration': 1.0},
             'test3sMono.wav': {'duration': 3.0},
             'test-tagged.wav': {'duration': 1.0},

             'flac1sMono.flac': {'track_total': None, 'album': None, 'year': None, 'duration': 1.0, 'title': None, 'track': None, 'artist': None},
             'flac1.5sStereo.flac': {'track_total': None, 'album': None, 'year': None, 'duration': 1.4995238095238095, 'title': None, 'track': None, 'artist': None},
             'flac_application.flac': {'track_total': None, 'album': 'Belle and Sebastian Write About Love', 'year': '2010-10-11', 'duration': 273.64, 'title': 'I Want the World to Stop', 'track': '4/11', 'artist': 'Belle and Sebastian'},
             'no-tags.flac': {'track_total': None, 'album': None, 'year': None, 'duration': 3.684716553287982, 'title': None, 'track': None, 'artist': None},
             'variable-block.flac': {'track_total': None, 'album': 'Appleseed Original Soundtrack', 'year': '2004', 'duration': 261.68, 'title': 'DIVE FOR YOU', 'track': '01', 'artist': 'Boom Boom Satellites'},
             'wav-with-nul-byte.wav': {'album': None, 'audio_offset': 0, 'artist': None, 'track': None, 'title': None, 'track_total': None, 'audio_offest': 36, 'filesize': 410198, 'year': None, 'duration': 2, 'samplerate': 44100, 'bitrate': 1378},
             }


def get_info(testfile, expected):
    folder = os.path.join(os.path.dirname(__file__), 'samples')
    filename = os.path.join(folder, testfile)
    print(filename)
    tag = TinyTag.get(filename)
    for key, value in expected.items():
        result = getattr(tag, key)
        fmt_string = 'field "%s": got %s (%s) expected %s (%s)!'
        fmt_values = (key, repr(result), type(result), repr(value), type(value))
        assert result == value, fmt_string % fmt_values
    print(tag)
    print('')


def test_generator():
    for testfile, expected in testfiles.items():
        yield get_info, testfile, expected
