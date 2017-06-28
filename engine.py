import pandas as pd
import time
import redis
from flask import current_app
from sklearn.feature_extraction.text import TfidVectorizer
from sklearn.metrics.pairwise import linear_kernel

def info(message):
	current_app.logger.info(message)

class ContenEngine(object):
	SIMILAR_KEY = "p:smlr:%s"

	def __init__(self):
		self._r = redis.StrictRedis.from_url(current_app.config['REDIS_URL'])

	def train(self, data_source):
		start = time.time()
		ds = pd.read_csv(data_source)
		info("Training data ingested in %s seconds." %(time.time() - start))

		# flush stale training data from redis
		self._r.flushdb()

		start = time.time()
		self._train(ds)
		info("Engine trained in %s seconds" %(time.time() - start))

	def _train(self, ds):
		#params 
		# analyzer : Whether the feature should be made of word or character n-grams
		# ngram_range : The lower and upper boundary of the range of n-values for different
		# 				n-grams to be extracted. 
		# 				All values of n such that min_n <= n <= max_n will be used.
		# min_df :	When building the vocabulary ignore terms that have a document 
		# 			frequency strictly lower than the given threshold. 
		tf = TfidVectorizer(analyzer = 'word', ngram_range=(1,3), min_df=0, stop_words='english')
		
		# fit_transform	:	Learn vocabulary and idf, return term-document matrix.	
		tfidf_matrix = tf.fit_transform(ds['description'])	

		cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)

		for idx, row in ds.iterrows():
			similar_inidices = cosine_similarities[idx].argsort()[:-100:-1]
			similar_items = [(cosine_similarities[idx][i]) for i in similar_inidices]


			flattend = sum(similar_items[1:], ())
			self._r.zadd(self.SIMILAR_KEY % row['id'], *flattend)


	def predict(self, item_id, num):
#		  param item_id: string
#       param num: number of similar items to return
#       return: A list of lists like: [["19", 0.2203], ["494", 0.1693], ...]. The first item in each sub-list is
#       the item ID and the second is the similarity score. Sorted by similarity score, descending.
		return  self._r.zrange(self.SIMILAR_KEY % item_id, 0, num-1, withscores = True, desc = True)


content_enigine = ContenEngine()