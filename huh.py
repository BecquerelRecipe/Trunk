import re

# Lets use a regular expression to match a date string. Ignore
# the output since we are just testing if the regex matches.
regexQuantity = r"[0-9]+g"
regexProduct = r"cauliflower"
stringToSearch = "I want 500g cauliflower"
if (re.search(regexProduct, stringToSearch) and re.search(regexQuantity, stringToSearch)):
    # Indeed, the expression "([a-zA-Z]+) (\d+)" matches the date string

    # If we want, we can use the MatchObject's start() and end() methods
    # to retrieve where the pattern matches in the input string, and the
    # group() method to get all the matches and captured groups.
    matchProduct = re.search(regexProduct, stringToSearch)
    matchQuantity = re.search(regexQuantity, stringToSearch)
    print("Match of product at index %s, %s" % (matchProduct.start(), matchProduct.end()))
    print("Match of quantity at index %s, %s" % (matchQuantity.start(), matchQuantity.end()))

    # The groups contain the matched values.  In particular:
    #    match.group(0) always returns the fully matched string
    #    match.group(1) match.group(2), ... will return the capture
    #            groups in order from left to right in the input string
    #    match.group() is equivalent to match.group(0)

    # So this will print "June cauliflower"
    print("Full match product: %s" % (matchProduct.group(0)))
    print("Full match quantity: %s" % (matchQuantity.group(0)))

else:
    # If re.search() does not match, then None is returned
    print
    "The regex pattern does not match. :("
