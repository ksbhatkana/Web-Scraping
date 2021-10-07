import re
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url) #Opening HTML page in program
html = page.read().decode("utf-8")

pattern = "<title.*?>.*?</title.*?>" #Regular Expression
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title) # Remove HTML tags

print(title)
