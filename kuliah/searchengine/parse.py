from __future__ import division
import re
import json
from pprint import pprint

def tf(term,corpus):
    splitted = corpus.split(' ')
    total = 0
    freq = 0
    for k in splitted:
        if(k == term):
            freq += 1
        total += 1
    return freq/total

def main():
    with open('source.json') as data_file:
        data = json.load(data_file)

    words = re.sub('[^0-9a-zA-Z]+',' ',data['item'][0]['content'])
    pprint(tf('untuk',words))

    # for i in data['item']:
    #     print i['title']

if __name__ == '__main__':
    main()
