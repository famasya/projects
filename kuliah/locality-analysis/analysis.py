
def main():
	working_set = []
	working_set_depth = 4
	popped = 0
	processed = 0
	with open('http.log','r') as f:
		for log in f:
			try:
				index = working_set.index(log)
			except:
				index = -1

			if(index == -1):
				working_set.append(log)
				if len(working_set) > working_set_depth:
					del working_set[0]
					popped += 1
			else:
				del working_set[index]
				working_set.append(log)
			processed += 1

	replaced = 100.0*(float(popped)/float(processed))
	print replaced


if __name__ == '__main__':
	main()
