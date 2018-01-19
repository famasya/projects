import sys

current_word = None
word = None
current_count = 1

for line in sys.stdin:
	line = line.strip()
	word, count = line.split('\t', 1)

	try:
		count = int(count)
	except ValueError:
		continue
	if current_word == word:
		current_count += 1
	else:
		if(current_word):
			print '%s\t%s' % (current_word, current_count)
		current_count = count
		current_word = word
if(current_word == word):
	print '%s\t%s' % (current_word, current_count)
