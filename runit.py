from Webshare import Webshare
from pprint import PrettyPrinter




pp = PrettyPrinter(indent=4) 
ws = Webshare("6UenksRC","HoGwDPdovOrJ")
result = ws.getURL("https://www.exporters.sg/member_profile.asp?co_id=143380", True)
print(result.text)
print(80*"*")
print(result.status_code)


# pp = PrettyPrinter(indent=4) 
# ws = Webshare("6UenksRC","HoGwDPdovOrJ")
# result = ws.getURL("https://ipv4.webshare.io/", True)
# print(result.text)

# pp = PrettyPrinter(indent=4) 
# ws = Webshare("6UenksRC","HoGwDPdovOrJ")
# my_url_list = ["https://ipv4.webshare.io/"
# 		,"http://ip4.me"
# 		,"https://api.ipify.org/"
# 		,"https://whatismyipaddress.com/"]
# ws.thread_getURL(my_url_list, threadCount = 20)
# pp.pprint(ws.RESULT_LIST)
