import pandas as pd
#para instalar pandas, se coloca en la terminal -> pip install pandas
from pandas import ExcelWriter

# decodigo.com

df = pd.DataFrame({'Id': [1, 3, 2, 4],
                   'Nombre': ['Juan', 'Eva', 'María', 'Pablo'],
                   'Apellido': ['Méndez', 'López', 'Tito', 'Hernández']})
df = df[['Id', 'Nombre', 'Apellido']]

writer = ExcelWriter('ejemplo.xlsx')
df.to_excel(writer, 'Hoja de datos', index=False)
writer.save()