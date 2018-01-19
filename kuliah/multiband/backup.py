from scipy.misc import imread
import numpy as np
from pprint import pprint
import signal
import sys

def transform(tuples):
	t = []
	for i in xrange(0,len(tuples[0])):
		row = []
		for j in xrange(0,len(tuples)):
			row.append(tuples[j][i])
		t.append({'t':row,'c':i})
	return t

def cluster(tuples,k):
	merged = [0,0]
	class_length = len(tuples)
	members = []
	done = []
	for i in xrange(0,class_length):
		members.append(0)

	while(class_length > k):
		minval = 999999
		for i,x in enumerate(tuples):
			for j,y in enumerate(tuples):
				if((i > j) and (x['c'] != y['c']) and (i not in done) and (j not in done)):
					a = np.asarray(x['t'])
					b = np.asarray(y['t'])
					dist = np.linalg.norm(a-b)
					if(dist < minval):
						minval = dist
						merged = [i,j]
		if(members[merged[0]] > members[merged[1]]):
			tuples[merged[1]] = tuples[merged[0]]
		else:
			tuples[merged[0]] = tuples[merged[1]]
		done.append(merged[0])
		done.append(merged[1])
		class_length -= 1
		print class_length, merged[0], 'gabung dengan', merged[1], tuples[merged[0]]['c'], tuples[merged[1]]['c']
	return tuples

def main():
	images = ["images/gb1.GIF","images/gb2.GIF","images/gb3.GIF","images/gb4.GIF","images/gb5.GIF","images/gb7.GIF"]
	# images = ["images/gb1.GIF","images/gb2.GIF","images/gb3.GIF"]
	# images = ["images/gb1.GIF"]
	fspace = []
	for i,image in enumerate(images):
		feature = imread(image).flatten()
		fspace.append(feature.tolist())

	tuples = transform(fspace)
	clustered = cluster(tuples,5)
	pprint(clustered)

if __name__ == '__main__':
	main()
