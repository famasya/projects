import urllib2,sys

# definisi url, baca parameter
url = 'http://sururimn.pe.student.pens.ac.id/pulsa.php?pulsa='+sys.argv[1]
# buka url
response = urllib2.urlopen(url)
# baca respon html
html = response.read()
# simpan ke file pulsa.dat
save = open('pulsa.dat','w')
# isi pulsa.dat dengan output html
save.write(html)
save.close()
response.close()
