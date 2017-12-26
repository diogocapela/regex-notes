import re

# ---> Option 1

# Compile regex pattern
myRegexOne = re.compile('\d\d\d-\d\d\d-\d\d\d\d')

# Search haystack string
mOne = myRegexOne.search('My phone number is 426-172-0023 , please call me later.')

# Print if pattern was found
if mOne is not None:
    print(mOne.group())

# ---> Option 2

# Compile regex pattern and search haystack string
mTwo = re.search('\d\d\d-\d\d\d-\d\d\d\d', 'My phone number is 426-172-0023 , please call me later.')

# Print if pattern was found
if mTwo is not None:
    print(mTwo.group())