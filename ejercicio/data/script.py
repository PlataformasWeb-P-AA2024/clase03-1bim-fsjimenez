# import csv

# with open('Listado-Instituciones-Educativas-distribuidas-por-zona-distrito-y-circuito.csv', newline='') as csvfile:

#     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

#     for row in spamreader:

#         print(', '.join(row))



# # proceso 
# #
# # acceder al archivo
# archivo = open('Listado-Instituciones-Educativas-distribuidas-por-zona-distrito-y-circuito.csv', "r")

# # obtener las líneas del archivo
# lineas = archivo.readlines()

# # lineas es ina lista de cadenas
# # se imprime las siguientes posiciones
# print(lineas[0])
# print(lineas[1])

# # en línea tomo el valor de lineas[1]
# linea = lineas[1]
# # a línea que es una cadena, la separo mediante la función
# # de Python split
# # Recuerdo que el separador de la cadena es un "|"

# linea = linea.split("|")

# # imprimo la nueva línea; que ahora es una lista
# print(linea)

# archivo.close()


# Abre el archivo CSV en modo lectura
with open('Listado-Instituciones-Educativas-distribuidas-por-zona-distrito-y-circuito.csv', "r") as archivo_csv:
    # Lee las líneas del archivo CSV
    lineas = archivo_csv.readlines()
    
    # Itera sobre las líneas del archivo CSV
    for i, linea in enumerate(lineas[1:], start=1):  # Ignora la primera línea que es el encabezado
        # Separa los campos de la línea
        campos = linea.strip().split("|")
        
        # Crea un nuevo archivo HTML para esta línea
        with open(f'output_{i}.html', 'w') as archivo_html:
            # Escribe los datos como texto con títulos en el archivo HTML
            archivo_html.write('<h1>Información de la Institución Educativa</h1>\n')
            archivo_html.write('<p><strong>Código AMIE:</strong> ' + campos[0] + '</p>\n')
            archivo_html.write('<p><strong>Nombre de la Institución Educativa:</strong> ' + campos[1] + '</p>\n')
            archivo_html.write('<p><strong>Provincia:</strong> ' + campos[2] + '</p>\n')
            archivo_html.write('<p><strong>Cantón:</strong> ' + campos[3] + '</p>\n')
            archivo_html.write('<p><strong>Parroquia:</strong> ' + campos[4] + '</p>\n')
            archivo_html.write('<p><strong>Zona Administrativa:</strong> ' + campos[5] + '</p>\n')
            archivo_html.write('<p><strong>Código de Distrito:</strong> ' + campos[6] + '</p>\n')
            archivo_html.write('<p><strong>Sostenimiento:</strong> ' + campos[7] + '</p>\n')
            archivo_html.write('<p><strong>Régimen Escolar:</strong> ' + campos[8] + '</p>\n')
            archivo_html.write('<p><strong>Modalidad:</strong> ' + campos[9] + '</p>\n')
            archivo_html.write('<p><strong>Jornada:</strong> ' + campos[10] + '</p>\n')
            archivo_html.write('<p><strong>Nivel:</strong> ' + campos[11] + '</p>\n')
            archivo_html.write('<p><strong>Etnia:</strong> ' + campos[12] + '</p>\n')
            archivo_html.write('<p><strong>Número de estudiantes:</strong> ' + campos[13] + '</p>\n')
            archivo_html.write('<p><strong>Número de docentes:</strong> ' + campos[14] + '</p>\n')
            archivo_html.write('<p><strong>Estado:</strong> ' + campos[15] + '</p>\n')
