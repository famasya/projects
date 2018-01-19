from scipy.misc import imread
import numpy as np
from pprint import pprint
from PIL import Image
from random import randint
from operator import itemgetter

c = []
colors = {}
def transform(tuples):
	t = []
	for i in xrange(0,len(tuples[0])):
		row = []
		for j in xrange(0,len(tuples)):
			row.append(tuples[j][i])
		t.append({'t':row,'c':i})
		c.append(i)
	return t

def color():
	return [randint(0,255),randint(0,255),randint(0,255)]

def cluster(tuples,k):
	dist_space = []
	c_len = len(tuples)
	members = []
	l = 0
	for i in xrange(0,c_len):
		members.append(0)

	print "Calculating distance..."
	for i,x in enumerate(tuples):
		for j,y in enumerate(tuples):
			if(i<j):
				a = np.asarray(x['t'])
				b = np.asarray(y['t'])
				dist = np.linalg.norm(a-b)
				dist_space.append([i,j,dist])
				l += 1
	sort = sorted(dist_space,key=itemgetter(2))

	print "Clustering..."
	for idx,row in enumerate(sort):
		i = row[0]
		j = row[1]
		if(members[i] > members[j]):
			tuples[j]['c'] = tuples[i]['c']
			c[j] = c[i]
			members[i] += 1
		else:
			c[i] = c[j]
			tuples[i]['c'] = tuples[j]['c']
			members[j] += 1
		if(len(set(c)) == k):
			for index in set(c):
				colors[index] = color()
			return tuples

def main():
	images = ["images/gb1.GIF","images/gb2.GIF","images/gb3.GIF","images/gb4.GIF","images/gb5.GIF","images/gb7.GIF"]
	fspace = []
	for i,image in enumerate(images):
		feature = imread(image).flatten()
		fspace.append(feature.tolist())

	tuples = transform(fspace)
	clustered = cluster(tuples,5)
	w, h = 32, 32
	data = np.zeros((h,w,3), dtype=np.uint8)
	# pprint(clustered)
	print "Generating image..."
	for x in xrange(0,32):
		for y in xrange(0,32):
			idx = x*32+y
			data[x,y] = colors[clustered[idx]['c']]
	img = Image.fromarray(data, 'RGB')
	img.save('result.png')
	img.show()

if __name__ == '__main__':
	main()
