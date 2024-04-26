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

# encabezados = lineas[0]
# encabezados = encabezados.split("|")
# # en línea tomo el valor de lineas[1]
# linea = lineas[1]
# # a línea que es una cadena, la separo mediante la función
# # de Python split
# # Recuerdo que el separador de la cadena es un "|"

# linea = linea.split("|")

# # imprimo la nueva línea; que ahora es una lista
# print(linea)

# archivo.close()

# pagina = """
# <!DOCTYPE html>
# <html lang="en" dir="ltr">
#   <head>
#     <meta charset="utf-8">
#     <title></title>
#   </head>
#   <body>
#   <b>%s:</b> %s  
#   </body>
# </html>
# """ % (encabezados[1], linea[1])

# print(pagina)

# archivo_generado = open("%s.html" % linea[0], "w")
# archivo_generado.writelines("%s" % pagina)
# archivo_generado.close()





# Acceder al archivo
with open('Listado-Instituciones-Educativas-distribuidas-por-zona-distrito-y-circuito.csv', "r") as archivo:
    # Obtener las líneas del archivo
    lineas = archivo.readlines()

    # Separar los encabezados
    encabezados = lineas[0].strip().split("|")

    # Iterar sobre cada línea de datos (excluyendo el encabezado)
    for linea in lineas[1:]:
        # Separar los campos de la línea
        campos = linea.strip().split("|")

        # Crear el HTML para esta línea
        pagina = """
        <!DOCTYPE html>
        <html lang="en" dir="ltr">
          <head>
            <meta charset="utf-8">
            <title></title>
          </head>
          <body>
        """
        
        # Agregar cada campo al HTML
        for encabezado, valor in zip(encabezados, campos):
            pagina += f"<b>{encabezado}:</b> {valor}<br>"
        
        # Cerrar el HTML
        pagina += """
          </body>
        </html>
        """

        # Nombre del archivo HTML
        nombre_archivo = f"{campos[0]}.html"

        # Escribir el HTML en el archivo
        with open(nombre_archivo, "w") as archivo_generado:
            archivo_generado.write(pagina)
