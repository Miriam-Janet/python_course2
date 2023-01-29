# WHOIS sobre IP
# 5-11-19
# Sergio Bastian Rodriguez
# https://blog.tiraquelibras.com/?p=714

# Importamos las librerias necesarias
import sys, pprint
from ipwhois import IPWhois #pip install ipwhois 
from IPy import IP #pip install IPy

# Obtenemos el argumento indicado al ejecutar la herramienta
ip = sys.argv[1]

# Logica de la heramienta
try:
        # Confirmamos si el argumento es una direccion IP
        ipType = IP(ip)
        
        # Confirmamos si la direccion IP es publica o no
        if ipType.iptype() == 'PUBLIC':
                
                # De ser publica obtenemos los datos del whois y los mostramos
                obj = IPWhois(ip)
                results = obj.lookup_whois()
                pprint.pprint(results)
        else:
                # De no ser publica lo indicamos en un mensaje de error
                raise Exception('The IP ' + ip + ' is not public.')

except Exception as e:
        # Si el argumento no es una dirección IP valida, o no es publica, mostramos el mensaje con el error
        print('ERROR - The argument added is not correct.\n%s' % (str(e)))

finally:
        # Para finalizar mostramos la información del creador de la herramienta
        print('\n***Herramienta desarrollada por:\n Tiraquelibras.com (https://blog.tiraquelibras.com/?p=714)***')