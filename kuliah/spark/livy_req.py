import pprint, requests, json, textwrap

proxies = {
  "http": None,
  "https": None,
}

host = 'http://10.252.108.77:8998'
data = {'kind': 'spark'}
headers = {'Content-Type': 'application/json'}
data = {
  'code': textwrap.dedent("""
    import random
    NUM_SAMPLES = 100000
    def sample(p):
      x, y = random.random(), random.random()
      return 1 if x*x + y*y < 1 else 0

    count = sc.parallelize(xrange(0, NUM_SAMPLES)).map(sample).reduce(lambda a, b: a + b)
    print "Pi is roughly %f" % (4.0 * count / NUM_SAMPLES)
    """)
}

r = requests.post(host + '/sessions', data=json.dumps(data), headers=headers, proxies=proxies)
print r.headers
# session_url = host + r.headers['location']
# statements_url = session_url + '/statements'

# r = requests.post(statements_url, data=json.dumps(data), headers=headers)
# pprint.pprint(r.json())