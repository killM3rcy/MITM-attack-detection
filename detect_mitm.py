import os
import re
import arpreq
def get_gateway_ip():
	table = []
	route = os.popen("route")
	i=0
	for r in route:
		r = " ".join(re.split("\s+",r, flags=re.UNICODE))
		table.append(r)
		

	l = len(table)
	for i in range(l):
		table[i] = table[i].strip()
		table[i] = table[i].split(" ")
	    
		#print(table[i])
		#lst.split(" ")
	for i in range(l-2):
		if table[i+2][7] == "wlp2s0" and table[i+2][1] != "*":
			gateway_ip = table[i+2][1]
			gateway_ip = str(gateway_ip)
			print("gateway_ip : " + gateway_ip)
	
	gateway = arpreq.arpreq(gateway_ip)
	print("gateway : " + gateway)
	gateway = str(gateway) 
	#print(table)
	tshark(gateway, gateway_ip)


def tshark(gateway, gateway_ip):
	file = open("test3.log","w")
	tshark = os.popen("sudo tshark -i wlp2s0 arp")
	check = " is at "
	for line in tshark:
		#print(line)
		#print("HELLO")
		
		if check in line:
			file.write(line)
			line = line.split(" ")
			index = line.index("ARP")
			print(line)
			print(line[index + 2])
			print(line[index + 5])
			if line[index + 2] == gateway_ip :

				if line[index + 5] == gateway :
					continue
				else :
					print ("ARP Poisoning Detected")
					print("MITM attack by " + line[index + 5])

		
			


if __name__ == '__main__':
	get_gateway_ip()






"""	import os
import re
def get_gateway_ip():
	lst = []
	table = []
	route = os.popen("route")
	for r in route:
		lst = " ".join(re.split("\s+",r, flags=re.UNICODE))
		lst.split(" ")
		table.append(lst)
	print(table)
"""