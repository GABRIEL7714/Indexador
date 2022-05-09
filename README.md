# Indexadorr
Este programa nos permite indexar p´aginas web, buscando la interrelaci´on
entre cada una de estas para su posterior uso en un buscador.
## Descripcion
El programa consiste en un algoritmo que permite extraer todas las URL de un documento web.py, para despues organizarlo en un diccionario donde las llaves son las URL entrantes, y los valores son las URL salientes. Posteriormente elaboramos un raking  con base a la formaula
. Links  Entrantes / Links Salientes
Finalmente mostramos el ranking con los respectivos puntajes que obtuvo cada pagina web
## Funcionamiento
 El programa muestra las paginas web indexadas:    
 .{'https://ucsp.edu.pe/cs111/index.html': {'https://ucsp.edu.pe/cs111/guido.html', 'https://ucsp.edu.pe/cs111/implementacion.html', 'https://ucsp.edu.pe/cs111/python.html', 'https://ucsp.edu.pe/cs111/peter.html', 'https://ucsp.edu.pe/cs111/pseudocodigo.html'}, 'https://ucsp.edu.pe/cs111/peter.html': {'https://ucsp.edu.pe/cs111/guido.html', 'https://ucsp.edu.pe/cs111/python.html'}, 'https://ucsp.edu.pe/cs111/guido.html':{'https://ucsp.edu.pe/cs111/python.html'}, 'https://ucsp.edu.pe/cs111/python.html':, 'https://ucsp.edu.pe/cs111/implementacion.html': {'https://ucsp.edu.pe/cs111/guido.html'},
 'https://ucsp.edu.pe/cs111/pseudocodigo.html': {'https://ucsp.edu.pe/cs111/implementacion.html', 'https://ucsp.edu.pe/cs111/pseudocodigo.html'}}
 
Muestra ademas un ranking de las paginas web:
"https://ucsp.edu.pe/cs111/python.html": 3,
   "https://ucsp.edu.pe/cs111/guido.html": 1.5,
   "https://ucsp.edu.pe/cs111/implementacion.html": 1,
   "https://ucsp.edu.pe/cs111/pseudocodigo.html": 0.666,
   "https://ucsp.edu.pe/cs111/peter.html":0.333,
   "https://ucsp.edu.pe/cs111/implementacion.html": 1
