# Webshare
Python 3.x wrapper for the Webshare proxy.  Additional support for randomization of proxies & multithreading support

Sign up to your free account here: https://proxy.webshare.io/

# To collect the package:

From git version control:
git clone https://github.com/HLXCo/Webshare.git

# Basic functionality:

```python
# * -	Import our Webshare library
from Webshare import Webshare
from pprint import PrettyPrinter

# * -	Instantiate the object
pp = PrettyPrinter(indent=4) 
ws = Webshare("__Your_name_here__","__Your_password_here__")

# * -	Basic usage for a single URL
result = ws.getURL("https://ipv4.webshare.io/", True)
print(result.text)


# * -	Advanced usage with multithreading & randomization
my_url_list = ["https://ipv4.webshare.io/"
		,"http://ip4.me"
		,"https://api.ipify.org/"
		,"https://whatismyipaddress.com/"]
ws.thread_getURL(my_url_list, threadCount = 20)
pp.pprint(ws.RESULT_LIST)
```
