#!/usr/bin/python
import socket, sys

def perform_whois(server , query) :
    #socket connection
    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    s.connect((server , 43))

    #send data
    s.send(query + '\r\n')

    #receive reply
    msg = ''
    while len(msg) < 10000:
        chunk = s.recv(100)
        if(chunk == ''):
            break
        msg = msg + chunk

    return msg
#End

#Function to perform the whois on a domain name
def get_whois_data(domain):

    #elimina http y www
    domain = domain.replace('http://','')
    domain = domain.replace('www.','')

    #optione las extensiones , .com , .org , .edu
    ext = domain[-3:]

    #si los dominios son .com .org .net
    if(ext == 'com' or ext == 'org' or ext == 'net'):
        whois = 'whois.internic.net'
        msg = perform_whois(whois , domain)

        #Busqueda
        lines = msg.splitlines()
        for line in lines:
            if ':' in line:
                words = line.split(':')
                if  'Whois' in words[0] and 'whois.' in words[1]:
                    whois = words[1].strip()
                    break;

    #contacto whois.iana.org encontrar el servidor whois de un TLD en particular
    else:
        #romper de nuevo como , co.uk to uk
        ext = domain.split('.')[-1]
        # le dice conectate al servidor de iana        
        whois = 'whois.iana.org'
        msg = perform_whois(whois , ext)

        #Busqueda en el servidor whois
        lines = msg.splitlines()
        for line in lines:
            if ':' in line:
                words = line.split(':')
                if 'whois.' in words[1] and 'Whois Server (port 43)' in words[0]:
                    whois = words[1].strip()
                    break;

    #Nuevo contacto en el servidor con el whois
    msg = perform_whois(whois , domain)

    #Retorna la replica
    return msg
# end

# En esta linea se pasa la variable que contiene el nombre del dominio...
nombre_dominio = "www.google.com"
print (get_whois_data(nombre_dominio))

