from __future__ import print_function
from PIL import Image
import imagehash

filename = 'testfile.jpg'

def retrieve_example():
	import os
	if not os.path.exists(filename):
		url = 'http://lh5.googleusercontent.com/-0iu4m4njVmQ/S3YH3wwXuPI/AAAAAAAABeU/i8jX5uKGCFo/s800/Alyson_Hannigan_200512.jpg'
		import urllib2
		response = urllib2.urlopen(url)
		open(filename, 'w').write(response.read())
	return Image.open(filename)

def test_average_hash():
	img = retrieve_example()
	hash = imagehash.average_hash(img)
	print(hash)
	print("rotate slightly")
	imgrot = img.rotate(-1)
	otherhash = imagehash.average_hash(imgrot)
	print(otherhash)
	print(hash == otherhash)
	assert hash == otherhash
	assert hash - otherhash < 10
	
	print("rotate 90 degrees")
	imgrot = img.rotate(-90)
	otherhash = imagehash.average_hash(imgrot)
	print(otherhash)
	print(hash == otherhash)
	assert hash != otherhash
	assert hash - otherhash > 10

def test_average_hash_length():
	for hash_size in [8]:
		hash = imagehash.average_hash(retrieve_example(), hash_size=hash_size)
		assert hash.hash.size == hash_size**2, hash.hash.shape


