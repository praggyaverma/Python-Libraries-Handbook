# Requests is a simple HTTP library. It allows to send HTTP requests easily.
# ALWAYS use requests package with a website you are allowed to scrap from, some websites do not allow scraping

import requests
# to install run `$ python -m pip install requests`

res = requests.get("website-url")

text = res.text #stores html code in one single string

status = res.status_code #indicates status of webpage: 200 is OK, 404 is Not Found
