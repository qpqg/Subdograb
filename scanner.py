from requests import session
from os import path
from pathlib import Path as folder
q = session()

def banner():
	print("Simple SubDomain Scanner\nApi from: api.hackertarget.com")
def real_path(file_name):
    return path.dirname(path.abspath(__file__)) + file_name
def search(host):
	resp = q.get(f"https://api.hackertarget.com/hostsearch/?q={host}")
	return resp.text
def files_save(myfile, text):
	with open(real_path(myfile), "+a") as files:
		files.writelines(f"{text}\n")
def main(domain):
	folder(real_path(f"/logs/{domain}/")).mkdir(parents=True, exist_ok=True)
	for host in search(domain).split("\n"):
		myhost = host.split(",")
		files_save(f"/logs/{domain}/{domain}_host.txt", myhost[0])
		files_save(f'/logs/{domain}/{domain}_ip.txt', myhost[1])
if __name__ == "__main__":
	banner()
	main(input("Host: "))
#	main("facebook.com")
