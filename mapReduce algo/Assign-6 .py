
# coding: utf-8

# In[1]:


from pyspark import SparkConf, SparkContext
sc = SparkContext(conf=SparkConf().setAppName("MyApp").setMaster("local"))

import re

def parse_article(line):
    try:
        article_id, text = unicode(line.rstrip()).split('\t', 1)
        text = re.sub("^\W+|\W+$", "", text, flags=re.UNICODE)
        words = re.split("\W*\s+\W*", text, flags=re.UNICODE)
        return words
    except ValueError as e:
        return []

wiki = sc.textFile("/data/wiki/en_articles_part/articles-part", 16).map(parse_article)
result = wiki.take(1)[0]


# In[2]:


for word in result[:50]:
    print word


# In[5]:


sc.parallelize([1,2,3,4,5])


# In[2]:


get_ipython().run_cell_magic('bash', '', 'sc.parallelize([1,2,3,4,5])')


# In[6]:


from pyspark import SparkConf, SparkContext
sc = SparkContext(conf=SparkConf().setAppName("MyApp").setMaster("local"))
sc.parallelize([1,2,3,4,5])


# In[8]:


b = sc.parallelize([1,2,3,4,5])


# In[11]:


b


# In[13]:


b.getNumPartitions()


# In[14]:


a = b.map(lambda x:2*x)


# In[15]:


a


# In[16]:


a.collect()


# In[17]:


from __future__ import print_function
a = b.map(lambda x:(print(x),2*x))


# In[18]:


a.collect()


# In[43]:


b = sc.parallelize([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
a = b.map(lambda x: 9 * x )


# In[44]:


a


# In[45]:


a.collect()


# In[48]:


books_data = sc.textFile("books.json")


# In[69]:


books_data


# In[50]:


dna_data = sc.textFile("dna.json")


# In[51]:


dna_data.collect()


# In[53]:


friends_data = sc.textFile("friends.json")


# In[54]:


friends_data.collect()


# In[60]:


join_data = sc.textFile("join.json")
matrix_data = sc.textFile("matrix.json")
friend_count_data = sc.textFile("friend_count.json")
inverted_index_data = sc.textFile("inverted_index.json")
multiply_data = sc.textFile("multiply.json")
unique_trims_data = sc.textFile("unique_trims.json")
records_data = sc.textFile("records.json")


# In[63]:


join_data.collect()


# In[62]:


matrix_data.collect()


# In[64]:


friend_count_data.collect()


# In[65]:


inverted_index_data.collect()


# In[66]:


multiply_data.collect()


# In[67]:


unique_trims_data.collect()


# In[68]:


records_data.collect()

