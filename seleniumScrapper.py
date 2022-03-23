from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
import scrapper
import userStory
import json

DRIVER_PATH='/Users/anananim/Desktop/Garima/chromedriver'

email = 'cognitivesearch@pl.abb.com'
password='7puDukeDrAswEta4'

AVERAGE_PAGE_LOADING_TIME=10

EMAILFIELD = (By.ID, "i0116")
PASSWORDFIELD = (By.ID, "i0118")
NEXTBUTTON = (By.ID, "idSIButton9")


LOGIN_URL = 'https://login.microsoftonline.com/'

browser = webdriver.Chrome(DRIVER_PATH)
browser.get(LOGIN_URL)

# wait for email field and enter email
WebDriverWait(browser, AVERAGE_PAGE_LOADING_TIME).until(EC.element_to_be_clickable(EMAILFIELD)).send_keys(email)

# Click Next
WebDriverWait(browser, AVERAGE_PAGE_LOADING_TIME).until(EC.element_to_be_clickable(NEXTBUTTON)).click()

# wait for password field and enter password
WebDriverWait(browser, AVERAGE_PAGE_LOADING_TIME).until(EC.element_to_be_clickable(PASSWORDFIELD)).send_keys(password)

# Click Login - same id?
WebDriverWait(browser, AVERAGE_PAGE_LOADING_TIME).until(EC.element_to_be_clickable(NEXTBUTTON)).click()


##############################################
# From here normal scrapping old code starts #
##############################################


json_output = []

countryStories = userStory.getCountryStories()



for country in countryStories:
	country_json = {}
	stories = []
	for story_url in countryStories[country]:
		browser.get(story_url)
		HTML_RESPONSE = browser.page_source
		response=scrapper.scrap(HTML_RESPONSE)
		hyperLinks = scrapper.getUrls()
		counter = 1
		for keys in response:
			val={}
			val['Id'] = counter
			val['key'] = keys
			val['value'] = response[keys]
			val['urls'] = []
			for entry in hyperLinks[keys]:
				urlMap = {}
				urlMap['caption'],urlMap['url']=entry[0],entry[1]
				val['urls'].append(urlMap)
			stories.append(val)
			counter+=1

	country_json['country'] = country
	country_json['story'] = stories

	json_output.append(country_json)

browser.quit()

JSON_FILE = open('indexResponse.txt','w')
JSON_FILE.write(json.dumps(json_output))