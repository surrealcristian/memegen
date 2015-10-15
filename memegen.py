#!/usr/bin/env python3

import json
import requests
import urllib.request

__author__ = 'Cristian Cabrera'
__version__ = '0.0.1'
__license__ = 'MIT'

__all__ = [
    'BaseCreator',
    'MemeGeneratorCreator',
    'ImgFlipCreator',
]

MEME_GENERATOR_USERNAME = 'YOUR_USERNAME'
MEME_GENERATOR_PASSWORD = 'YOUR_PASSWORD'

IMG_FLIP_USERNAME = 'YOUR_USERNAME'
IMG_FLIP_PASSWORD = 'YOUR_PASSWORD'


# ========
# Creators
# ========

class BaseCreator:
    """Base class for creators"""
    def get_keys(self):
        keys = list(self.memes.keys())
        keys.sort()
        return keys


class MemeGeneratorCreator(BaseCreator):
    """Create memes using memegenerator.net API"""
    def __init__(self):
        super().__init__()
        self._username = MEME_GENERATOR_USERNAME
        self._password = MEME_GENERATOR_PASSWORD
        self.memes = {
            'doge': {'generator_id': 2452817, 'image_id': 9861901},
            'trollface': {'generator_id': 68, 'image_id': 269},
            'yao-ming': {'generator_id': 6715, 'image_id': 1123673},
            'y-u-no': {'generator_id': 2, 'image_id': 1123673},
            'neil-degrasse': {'generator_id': 1474060, 'image_id': 6090424},
            'scumbag-steve': {'generator_id': 142, 'image_id': 366130},
            'okay-guy': {'generator_id': 417, 'image_id': 172405},
            'good-guy-greg': {'generator_id': 534, 'image_id': 699717},
            'ancient-aliens': {'generator_id': 1323, 'image_id': 627067},
            'bad-luck-brian': {'generator_id': 740857, 'image_id': 3459374},
            'philosoraptor': {'generator_id': 17, 'image_id': 984},
            'really-high-guy': {'generator_id': 934293, 'image_id': 4168627},
            'the-most-interesting-man-in-the-world': {'generator_id': 74,
                                                      'image_id': 2485},
            'omg-rage-guy': {'generator_id': 1197, 'image_id': 552601},
            'xzibit-yo-dawg': {'generator_id': 12773, 'image_id': 1137321},
            'grumpy-cat': {'generator_id': 1771888, 'image_id': 6541210},
            'archaic-rap': {'generator_id': 50, 'image_id': 42},
            'i-know-that-feel-bro': {'generator_id': 1203367,
                                     'image_id': 5092856},
            'socially-awkward-penguin': {'generator_id': 29, 'image_id': 983},
            'fap': {'generator_id': 332427, 'image_id': 2030114},
            'futurama-fry-not-sure-if': {'generator_id': 305,
                                         'image_id': 84688},
            'one-does-not-simply': {'generator_id': 689854,
                                    'image_id': 3291562},
            'insanity-wolf': {'generator_id': 45, 'image_id': 20},
            'courage-wolf': {'generator_id': 303, 'image_id': 24},
            'genius': {'generator_id': 967125, 'image_id': 4298821},
            'sweet-jesus': {'generator_id': 35564, 'image_id': 1226208},
            'conspiracy-keanu': {'generator_id': 318374, 'image_id': 1986282},
            'prepare-your-anus': {'generator_id': 4374050,
                                  'image_id': 12823183},
        }

    def create(self, meme, top, bottom):
        """Creates the meme"""
        url = 'http://version1.api.memegenerator.net/Instance_Create'
        params = {
            'username': self._username,
            'password': self._password,
            'languageCode': 'en',
            'generatorID': self.memes[meme]['generator_id'],
            'imageID': self.memes[meme]['image_id'],
            'text0': top,
            'text1': bottom,
        }
        try:
            res = requests.get(url, params)
        except Exception as e:
            raise Exception('Error requesting the service.')
        try:
            dict_res = json.loads(res.text)
        except:
            msg = 'Unexpected response format: (%s)' % res.text
            raise Exception(msg)
        if not dict_res['success']:
            msg = 'Unexpected response: (%s)' % res.text
            raise Exception(msg)
        print(dict_res['data']['url'])


class ImgFlipCreator(BaseCreator):
    """Create memes using imgflip.com API"""
    def __init__(self):
        super().__init__()
        self._username = IMG_FLIP_USERNAME
        self._password = IMG_FLIP_PASSWORD
        self.memes = {
            'doge': {'template_id': 8072285},
            'trollface': {'template_id': 73863},
            'yao-ming': {'template_id': 6411349},
            'y-u-no': {'template_id': 61527},
            'neil-degrasse': {'template_id': 109017},
            'scumbag-steve': {'template_id': 61522},
            'okay-guy': {'template_id': 994292},
            'good-guy-greg': {'template_id': 61521},
            'ancient-aliens': {'template_id': 101470},
            'bad-luck-brian': {'template_id': 61585},
            'philosoraptor': {'template_id': 61516},
            'really-high-guy': {'template_id': 101440},
            'the-most-interesting-man-in-the-world': {'template_id': 61532},
            'omg-rage-guy': {'template_id': 127181},
            'xzibit-yo-dawg': {'template_id': 101716},
            'grumpy-cat': {'template_id': 405658},
            'archaic-rap': {'template_id': 23669271},
            'i-know-that-feel-bro': {'template_id': 5471748},
            'socially-awkward-penguin': {'template_id': 61524},
            'fap': {'template_id': 5135625},
            'futurama-fry-not-sure-if': {'template_id': 61520},
            'one-does-not-simply': {'template_id': 61579},
            'insanity-wolf': {'template_id': 61518},
            'courage-wolf': {'template_id': 61517},
            'genius': {'template_id': 14738977},
            'sweet-jesus': {'template_id': 3515702},
            'conspiracy-keanu': {'template_id': 61583},
            'prepare-your-anus': {'template_id': 22405170},
            'too-damn-high': {'template_id': 61580},
        }

    def create(self, meme, top, bottom):
        url = 'https://api.imgflip.com/caption_image'
        params = {
            'template_id': self.memes[meme]['template_id'],
            'username': self._username,
            'password': self._password,
            'text0': top,
            'text1': bottom,
        }
        try:
            res = requests.post(url, params)
        except Exception as e:
            raise Exception('Error requesting the service.')
        try:
            dict_res = json.loads(res.text)
        except:
            msg = 'Unexpected response format: (%s)' % res.text
            raise Exception(msg)
        if not dict_res['success']:
            msg = 'Unexpected response: (%s)' % res.text
            raise Exception(msg)
        print(dict_res['data']['url'])


# =================
# Utility functions
# =================

def _parse_args():
    """Parse command line arguments."""
    import argparse
    parser = argparse.ArgumentParser(description='Meme generator')
    arg = parser.add_argument
    arg('-l', '--list', action='store_true',
        help='lists available memes for the service')
    arg('meme', nargs='?')
    arg('top', nargs='?')
    arg('bottom', nargs='?')
    arg('-s', '--service', choices=['imgflip', 'memegenerator'],
        default='imgflip', help='defaults to imgflip')
    args = parser.parse_args()
    return parser, args


if __name__ == '__main__':
    parser, args = _parse_args()

    if args.service == 'imgflip':
        creator = ImgFlipCreator()
    elif args.service == 'memegenerator':
        creator = MemeGeneratorCreator()

    if args.list:
        for k in creator.get_keys():
            print(k)
    elif args.meme:
        if not args.meme in creator.get_keys():
            parser.error('Unknown meme: (%s)' % args.meme)
        elif not args.top and not args.bottom:
            parser.print_help()
        else:
            meme = args.meme
            top = args.top if args.top else ''
            bottom = args.bottom if args.bottom else ''
            try:
                creator.create(meme, top, bottom)
            except Exception as e:
                parser.error(str(e))
    else:
        parser.print_help()
