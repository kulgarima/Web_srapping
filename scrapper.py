import bs4
from bs4 import BeautifulSoup

IGNORABLE_TAGS=['script']
KEY_TAGS = ["h1"]

response = {}
links = {}

def isKeyTag(tag):
	if tag.name in KEY_TAGS:
		return True
	elif tag.name == 'div':
		if tag.has_attr('class') and 'headerBig' in tag['class']:
			return True
	return False

def isValueTag(tag):
	if isinstance(tag,bs4.element.NavigableString):
		return True
	elif tag.name =='a':
		return True
	return False

def scrubValues(text):
	restricted_char=['\n','\0']
	scrubbedText=""
	if text == None:
		return scrubbedText
	for i in text:
		if i not in restricted_char:
			scrubbedText+=i
	return scrubbedText.strip()

def scrubKey(text):
	scrubbedText=""
	if text == None:
		return scrubbedText
	for i in text:
		if ord(i)>=32 and ord(i)<=126:
			scrubbedText+=i
	return scrubbedText.strip()

def populate_json(tag):
	if isValueTag(tag):
		last_heading = None
		for heading in response.keys():
			last_heading = heading
		if last_heading != None:
			text=""
			if tag.name=='a' and tag.has_attr('href'):
				url=tag['href']
				if url.startswith('http')==False:
					return
				caption = ""
				for child in tag.children:
					if isValueTag(child):
						caption = scrubValues(child.string)
				links[last_heading].append((caption,url))
			else:
				text=scrubValues(tag.string)
			if len(text)>0:
				response[last_heading]+= (text+' ')
		return
	elif isKeyTag(tag):
		reponse_key=scrubKey(tag.string)
		if len(reponse_key)!=0:
			response[reponse_key]= ""
			links[reponse_key] = []
		return
	elif tag.name in IGNORABLE_TAGS:
		return
	for child in tag.children:
		populate_json(child)

def getUrls():
	return links
def scrap(html):
	response.clear()
	links.clear()
	html=BeautifulSoup(html, 'html5lib')
	populate_json(html.find())
	return response
