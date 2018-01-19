from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer()

cv.fit_transform(
	['saya pergi ke pasar', 
	 'ani pergi ke sekolah', 
	 'mama dan papa berangkat kerja']).toarray()

cv.transform(['saya pergi']).toarray()
cv.transform(['bertamasya keliling jogja']).toarray()

print cv.get_feature_names()
