#!/usr/bin/env python
from __future__ import (absolute_import, division, print_function)
from PIL import Image
import six

import imagehash

def generate_phash(image_path, hashsize = 8, hashfunc = imagehash.phash, freqfactor = 4):
    hash = hashfunc(Image.open(image_path), hashsize, freqfactor)
    return str(hash)

def hamming_distance(hash1, hash2):
    hash1 = imagehash.hex_to_hash(hash1)
    hash2 = imagehash.hex_to_hash(hash2)
    return str(hash1 - hash2)

def generate_ahash(image_path, hashsize = 8, hashfunc = imagehash.average_hash):
    hash = hashfunc(Image.open(image_path), hashsize)
    return str(hash)
    