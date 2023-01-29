from openpyxl import Workbook
import openpyxl
import pathlib
import time
from whoisapi import *
import json
import os

ips = open("WhoisD/ips.txt")
contador = 0
lista_ips = []
ips_error = []
lista_excel = []

for i in ips:
    lista_ips.append(i.strip("\n"))

client = Client(api_key='at_XHWPMISEcbQ8ZmqYpk3SJBb8GDB9Q')
direccion = "Whois"

for i in range(0,len(lista_ips)):
    try:
        raw_data = client.raw_data(lista_ips[i])
        json_obj = json.loads(raw_data)
        whois_jason = json_obj["WhoisRecord"]
        domain_name = whois_jason["domainName"]
        path_absolute = pathlib.Path().absolute()
        registrar_name = whois_jason["registrarName"]

        if "contactEmail" not in whois_jason:
            contact_email = "N/A"
        else:
            contact_email = whois_jason["contactEmail"]
        
        registry_data = whois_jason["registryData"]

        if "createDate" not in registry_data:
            created_date = "N/A"
        else:
            created_date = registry_data["createDate"]

        if "registrant" not in registry_data:
            country = "N/A"
        elif "country" not in registry_data["registrant"]:
            country = "N/A"
        else:
            country = registry_data["registrant"]["country"]

        

        if whois_jason["registrarName"]:
            with open(os.path.join(direccion, domain_name+".json"), 'w') as file:
                json.dump(whois_jason, file)
            lista_excel.append(
                [
                    str(path_absolute)+direccion+"\\"+str(domain_name)+".json",
                    domain_name,
                    registrar_name,
                    contact_email,
                    created_date,
                    country
                ]
            )

    except Exception as e:
        print("something went wrong...", e )
        ips_error.append(lista_ips[i])

    time.sleep(1)

wb = openpyxl.load_workbook("WhoisD/whois.xlsx")
doc = wb.active

for i in lista_excel:
    doc.append((i))
wb.save("WhoisD/whois.xlsx")

with open("WhoisD/fails.xlsx", "a") as file:
    for i in ips_error:
        file.write(i+"\n")
