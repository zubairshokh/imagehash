#!/usr/bin/env python
from __future__ import (absolute_import, division, print_function)
from PIL import Image
import six

import imagehash

def generate_phash(image_path, hashsize = 8, expose_image = False, hashfunc = imagehash.phash, freqfactor = 4):
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
    import os

    tail = os.path.basename(image_path)
    image_opened = Image.open(image_path)
    img_size = hashsize * freqfactor
    image_converted = image_opened.convert("L").resize((img_size, img_size), Image.ANTIALIAS)
    try:
        os.mkdir("priv/hashed_images")
    except FileExistsError:
        pass
    
    image_converted.save("priv/hashed_images/{0}".format(tail.decode('utf-8')), "PNG")
    return None
