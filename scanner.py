from requests import session
from os import path
from sys import stdout
from datetime import datetime
from pathlib import Path as folder
q = session()
display_logs = True

def logs(text, s=display_logs):
	waktu = datetime.now().strftime("%H:%M:%S")
	stdout.writelines(f"[{waktu}] {text}") if(s) else None	
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
	banner()
	mydo = search(domain)
	if not mydo.startswith("error"):
		folder(real_path(f"/logs/{domain}/")).mkdir(parents=True, exist_ok=True)
		for host in mydo.split("\n"):
			myhost = host.split(",")
			files_save(f"/logs/{domain}/{domain}_host.txt", myhost[0])
			files_save(f'/logs/{domain}/{domain}_ip.txt', myhost[1])
			logs(f"{myhost[0]} > {myhost[1]}\r\n\r\n")
	else:
		logs(f"{mydo}\r\n\r\n")
		
if __name__ == "__main__":
	main(input("Host: "))
#	main("facebook.com")
