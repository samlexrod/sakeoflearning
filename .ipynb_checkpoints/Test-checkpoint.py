

# spliting text delimited with commas
text = "spam, eggs, ham, bacon"
menu = text.split(',')

spam_aside = text.split(',', 1)
print(spam_aside)

bacon_aside = text.rsplit(',', 1)
print(bacon_aside)