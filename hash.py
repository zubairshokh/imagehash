#!/usr/bin/env python
from __future__ import (absolute_import, division, print_function)
from PIL import Image
import six

import imagehash

def generate_phash(image_path, hashsize = 8, hashfunc = imagehash.phash, freqfactor = 4, expose_image = False):
    if expose_image:
        export_image(image_path, hashsize, freqfactor)
    
    hash = hashfunc(Image.open(image_path), hashsize, freqfactor)
    return str(hash)

def hamming_distance(hash1, hash2):
    hash1 = imagehash.hex_to_hash(hash1)
    hash2 = imagehash.hex_to_hash(hash2)
    return str(hash1 - hash2)

def generate_ahash(image_path, hashsize = 8, hashfunc = imagehash.average_hash):
    hash = hashfunc(Image.open(image_path), hashsize)
    return str(hash)
    
def export_image(image_path, hashsize, freqfactor):
    import os, sys
    name = os.path.basename(image_path)
    image = Image.open(image_path)
    img_size = hashsize * freqfactor
    image = image.convert("L").resize((img_size, img_size), Image.ANTIALIAS)
    try:
        os.mkdir("../hashed_images")
    except FileExistsError:
        pass
    
    image.save("../hashed_images/%s" % name)
    return None
