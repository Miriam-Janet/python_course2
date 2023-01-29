                                        #Crear archivo excel en Python con openpyxl

#En el código siguiente te muestro cómo crear un libro en openpyxl:
#https://j2logo.com/python/crear-archivo-excel-en-python-con-openpyxl/
#https://www.javatpoint.com/python-openpyxl
import openpyxl
import time
wb = openpyxl.Workbook()
sheet = wb.active

sheet['A1'] = 87  
sheet['A2'] = "Devansh"  
sheet['A3'] = 41.80  
sheet['A4'] = 10  
  
now = time.strftime("%x")  
sheet['A5'] = now  
  
wb.save("sample_file.xlsx")  


""" 
print(f'Hoja activa: {hoja.title}')


hoja.title = "Valores"
print(f'Hoja activa: {wb.active.title}')
"""
