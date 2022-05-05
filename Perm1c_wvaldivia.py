web = {'https://ucsp.edu.pe/cs111/index.html':                                            
"""
<html>
<body>
<h1>Algoritmo CS111</h1>
<p>
Aqui encontraremos más información al respecto:
<ul>
<li> <a href="https://ucsp.edu.pe/cs111/pseudocodigo.html">Pseudocódigo</a>
<li> <a href="https://ucsp.edu.pe/cs111/implementacion.html">Implementación del algoritmo</a>
<li> <a href="https://ucsp.edu.pe/cs111/python.html">Documentación de Python</a>
</ul>
Podemos revisar comentarios adicional al respecto: 
<a href="https://ucsp.edu.pe/cs111/guido.html">Guido van Rossum</a> 
y <a href="https://ucsp.edu.pe/cs111/peter.html">Peter Norvig</a>.
</body>
</html>
""",'https://ucsp.edu.pe/cs111/peter.html':                                                
"""<html>
<body>
<h1>Peter Norvig</h1>
<p>
Peter Norvig es un científico estadounidense, investigador en ciencias de la computación. Actualmente 
es director de investigación de la empresa Google. Ha publicado unos cincuenta artículos científicos 
sobre informática, en particular en el campo de la inteligencia artificial, el procesamiento automático 
del lenguaje natural , la recuperación de información y el diseño de software.
Con muchos años de expiencia en el lenguaje <a href="https://ucsp.edu.pe/cs111/python.html">Python</a>, 
creado por <a href="https://ucsp.edu.pe/cs111/guido.html">Guido van Rossum</a>.
</body>
</html>
""",
   'https://ucsp.edu.pe/cs111/guido.html': """<html>                                        
<body>
<h1>Guido van Rossum</h1>
<p>
El es el creador de 
<a href="https://ucsp.edu.pe/cs111/python.html">Python</a>
</body>
</html>
""",
   'https://ucsp.edu.pe/cs111/python.html': """<html>                                       
<body>
<h1>
Lenguaje de Programación Python
</h1>
<p>
<ol>
<li> Python 2.
<li> Python 3.
</ol>
</body>
</html>
""",
   'https://ucsp.edu.pe/cs111/implementacion.html': """<html>                               
<body>
<h1>
La Implementación del algoritmo
</h1>
<p>
<ol>
<li> En el siguiente link <a href="https://ucsp.edu.pe/cs111/guido.html">Guido van Rossum</a>.
<li> Cree las variables de manera correcta, siguiendo los estandares.
</ol>
</body>
</html>
""",
   'https://ucsp.edu.pe/cs111/pseudocodigo.html': """<html>                                 
<body>
<h1>
Pseudocódigo
</h1>
<p>
<ol>
<li> "https://ucsp.edu.pe/cs111/implementacion.html".
<li> "https://ucsp.edu.pe/cs111/pseudocodigo.html".
<li> "https://ucsp.edu.pe/cs111/pseudocodigo.html".
<li> "https://ucsp.edu.pe/cs111/pseudocodigo.html".
<li> "https://ucsp.edu.pe/cs111/pseudocodigo.html".
<li> "https://ucsp.edu.pe/cs111/pseudocodigo.html".
<li> "https://ucsp.edu.pe/cs111/pseudocodigo.html".
<li> "https://ucsp.edu.pe/cs111/pseudocodigo.html".
<li> "https://ucsp.edu.pe/cs111/pseudocodigo.html".
</ol>
</body>
</html>
"""}

# Implementamos el codigo para extraer las URL de las paginas web 
diccionario = {}
for i,j in web.items():
   lista = []
   texto = j
   texto = texto.splitlines()
   for k in range(len(texto)):
      a = texto[k]
      if (a.find("https://") != -1) and (a.find(".html") != -1):
         posicion1 = a.find("https://")
         posicion2 = a.find(".html")
         posicion2 +=5
         url =  a[posicion1:posicion2]
         lista.append(url)

   diccionario[i] = lista


# Mostramos el diccionario con las URL de las paginas web 
#for i,j in diccionario.items():
#   print(i)
#   print(j)
#   print("\n")


# Creamos un diccionario, para verificar los valores entrantes y salientes de las URL
diccionario2 = {
   "https://ucsp.edu.pe/cs111/python.html": 3,
   "https://ucsp.edu.pe/cs111/guido.html": 1.5,
   "https://ucsp.edu.pe/cs111/implementacion.html": 1,
   "https://ucsp.edu.pe/cs111/pseudocodigo.html": 0.666,
   "https://ucsp.edu.pe/cs111/peter.html":0.333,
   "https://ucsp.edu.pe/cs111/implementacion.html": 1
}

# Imprimimos el ranking de las paginas web y su puntaje

print(diccionario2)




   





