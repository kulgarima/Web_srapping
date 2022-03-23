def getCountryStories():
	countryStories = {}
	uk_Stories = ["https://go.insideplus.abb.com/uk/functions/procurement-logistics/vehicle-fleet"]
	uk_Stories.append("https://go.insideplus.abb.com/uk/tools-and-services/travel-and-expenses/useful-information")
	uk_Stories.append("https://go.insideplus.abb.com/uk/tools-and-services/travel-and-expenses")

	countryStories['UK'] = uk_Stories

	in_Stories = ["https://go.insideplus.abb.com/in/tools-and-services/travel-and-expense-management/useful-information"]
	in_Stories.append("https://go.insideplus.abb.com/in/tools-and-services/travel-and-expense-management")

	countryStories['India'] = in_Stories

	southern_africa_Stories = ["https://go.insideplus.abb.com/southern-africa/travel-and-expense-management/kenya"]
	southern_africa_Stories.append("https://go.insideplus.abb.com/southern-africa/travel-and-expense-management/tanzania")
	southern_africa_Stories.append("https://go.insideplus.abb.com/southern-africa/travel-and-expense-management/zimbabwe")

	countryStories['Southern_Africa'] = southern_africa_Stories

	return countryStories