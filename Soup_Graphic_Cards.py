from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

try:
	my_url = "https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=graphic+cards&ignorear=0&N=-1&isNodeId=1"
	parse = True
except:
	print("Link Broken: The link has been changed.")
	parse = False


if parse:
	# donloading the html website
	uClient = uReq(my_url)

	# reading the file into a variable
	page_html = uClient.read()
	uClient.close()

	# parsing the file into a variable
	page_soup = soup(page_html, "html.parser")

	# finding the division that holds all unstructured data of graphic cards
	containers = page_soup.findAll("div", {"class":"item-container"})

	# print on console how many items where found
	print("There were {} items found.".format(len(containers)))

	# extracting and exporting product brand, title, price, shipping, rating, and rating sample size
	filename = "graphic_cards.csv"
	f = open(filename, "w")
	headers = "brand, product_name, price, shipping, rating, rating_size\n"
	f.write(headers)

	def write_formatter(variable_list=[]):
		""" prepares all values to be written in csv format"""

		""" I want to go over every variable in the list of variables and append its value into a list that will be joined with commas"""
		write_this = []
		
		for content in variable_list:
			write_this.append(str(content))

		# finish the sentence
		write_this.append('\n')
		write_this = ','.join(write_this)

		#print(write_this)
		return write_this


	for container in containers:

		# brand and title
		brand = container.div.div.a.img['title'].replace(',', '').replace('Inc.', '')
		title = container.findAll("a", {"class":"item-title"})[0].text.replace(',', '')

		try: # dollars
			dollars = container.findAll("li", {"class":"price-current"})[0].strong.text
		except:
			dollars = None

		try: # cents
			cents = container.findAll("li", {"class":"price-current"})[0].sup.text
		except:
			cents = None

		# price
		if dollars != None and cents != None:
			price = (dollars + cents).replace(',', '')
		elif cents:
			price = cents.replace(',', '')
		elif dollars:
			price = dollars.replace(',', '')
		else:
			price = None

		shipping = container.findAll("li", {"class":"price-ship"})[0].text.strip()
		shipping = shipping[:shipping.find("Sh")].replace('$', '').replace('Free', '0.00')

		# rating
		try:
			rating = int(container.findAll("a", {"class":"item-rating"})[0].i['class'][1].replace('rating-', ''))
			rating_size = int(container.findAll("a", {"class":"item-rating"})[0].i.next_sibling.text.strip("()"))
		except:
			rating = None
			rating_size = None

		print(brand, price, dollars, cents, shipping, rating, rating_size)

		row = write_formatter([brand, title, price, shipping, rating, rating_size])

		f.write(row)

	f.close()