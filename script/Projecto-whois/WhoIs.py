#instalamos pip install whois-api
from whoisapi import *
import json
#aqui abro el txt de las ips
ips = open("whois\IIPPs.txt")
iips = [] #variable para colocar las ips en una lista

#ciclo donde colocaremos las ips en la variable de la lista
for i in ips:
    #The . append() method takes an object as an argument and adds it to the end of an existing list.
    iips.append(i.strip("\n"))

print(iips) # Muestra la lista de txt

#Parte para el uso de la api whois
client = Client(api_key='at_XHWPMISEcbQ8ZmqYpk3SJBb8GDB9Q')

params = RequestParameters(ignore_raw_texts=1, da=2)

whois = client.data(iips, params)
#print(whois.domain_availability_raw)

# Also you can modify default values of parameters:
client.parameters.output_format = 'json'
json_ip = client.raw_data(iips)

###################################################################################
with open('whois\ip.json', 'w') as fp:
    json.dump(json_ip, fp)

with open('whois\ip.json', 'r') as fp:
    data = json.load(fp)
print(data)
#print(type(data))