import requests
url=input("Enter The URL (Without http) : ")
file=open("list.txt")
content=file.read()
subdomain=content.splitlines()
for i in subdomain:
	sub_url=f"http://{i}.{url}"
	try:
		requests.get(sub_url)
		print("FOUND ",sub_url," ------> ",requests.get(sub_url).status_code)
	except:
		pass
	

