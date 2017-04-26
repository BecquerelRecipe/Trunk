import re

def ingredients_parser(stringToSearch):
# Lets use a regular expression to match a date string. Ignore
# the output since we are just testing if the regex matches.
    regexQuantity = r"[0-9]+ g"
    regexProduct = r"oeuf|beurre|sucre|amandes|feve"
    ##stringToSearch = "I want 500g cauliflower and 100g chocolate"
    if (re.search(regexProduct, stringToSearch) and re.search(regexQuantity, stringToSearch)):
        matchProduct = re.findall(regexProduct, stringToSearch)
        matchQuantity = re.findall(regexQuantity, stringToSearch)
        stringsBeforeProducts = re.split(regexProduct, stringToSearch)
        productQuantity = []
        print(matchProduct)
        print(matchQuantity)
        print(stringsBeforeProducts)
        for i in range(0, len(matchProduct)):
            resultSearch = re.search(regexQuantity, stringsBeforeProducts[i])
            if (resultSearch):
                productQuantity.append(resultSearch.group(0))
            else:
                productQuantity.append('')
        print(productQuantity)
    else:
        # If re.search() does not match, then None is returned
        print("The regex pattern does not match. :(")

