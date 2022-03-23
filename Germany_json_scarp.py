#!/usr/bin/env python
# coding: utf-8

# In[8]:


#p = "New.txt"
#a = open(p, "r")
#print(a.read())


# In[ ]:


#LOGIN_URL = "https://google.com"
#HTML_RESPONSE=requests.get(URL_TO_SCRAP)


# In[31]:


import json
import requests
import bs4
from bs4 import BeautifulSoup


# In[32]:


FILE_PATH_FROM_THIS_SCRIPT = "Page name - 38.html"

HTMLFileToBeOpened = open(FILE_PATH_FROM_THIS_SCRIPT, "r",encoding='utf-8')
contents = HTMLFileToBeOpened.read()

HTML_RESPONSE = BeautifulSoup(contents, 'html5lib')

html_body = HTML_RESPONSE.find('body')


# In[33]:



key_tags = ["h1"]
text_tags=["div","p","span","td"]

response={}


# In[34]:


def scrubText(text):
	scrubbedText=""
	for i in text:
		if ord(i)>=32 and ord(i)<=126:
			scrubbedText+=i
	return scrubbedText

def populate_json(tag):
	if isinstance(tag,bs4.element.NavigableString):
		last_heading=None
		for heading in response.keys():
			last_heading = heading
		if last_heading != None:
			text = tag.string
			if len(text)>0:
				response[last_heading]+= tag.string
		return
	
	for child in tag.children:
		if tag.name in key_tags:
			reponse_key=scrubText(tag.text)
			if len(reponse_key)!=0:
				response[reponse_key]=""
			continue
		populate_json(child)


# In[35]:


populate_json(html_body)
print(json.dumps(response))


# In[ ]:




