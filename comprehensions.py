# Las comprehensions son una forma concisa de crear listas, diccionarios o conjuntos a partir de iterables. Permiten escribir código más limpio y legible. Aquí veremos algunos ejemplos.

# Primero creo una lista de diccionarios que simula ser un conjunto de artículos de noticias listas para procesar:

sample_articles = [
    {
        "title": "Python logra grandes avances en IA",
        "source": {"name": "Tech News"},
        "description": "Python se ha convertido en el lenguaje de programación más popular para el desarrollo de inteligencia artificial, gracias a su simplicidad y la gran cantidad de bibliotecas disponibles.",
        "category": "Tecnología",
    },
    {
        "title": "Mercado de criptomonedas en auge",
        "source": {"name": "Finances"},
        "description": "El mercado de criptomonedas ha experimentado un crecimiento significativo en los últimos meses, impulsado por el interés de inversores y empresas tecnológicas.",
        "category": "Finanzas",
    },
    {
        "title": "Se descubre nueva tecnología de baterías",
        "source": {"name": "Econoticias"},
        "description": "Se ha descubierto una nueva tecnología de baterías que promete ser más eficiente y duradera que las actuales.",
        "category": "Tecnología",
    },
    {
        "title": "Deportes hoy: se complica el escándalo de la AFA",
        "source": {"name": "Deportes Hoy"},
        "description": "El escándalo de la AFA se complica con nuevas revelaciones que ponen en duda la integridad de varios directivos.",
        "category": "Deportes",
    },
    {
        "title": "Las nuevas medidas de política internacional",
        "source": {"name": "El foro"},
        "description": "Las nuevas medidas de política internacional buscan mejorar la cooperación entre países en temas de seguridad y desarrollo sostenible.",
        "category": "Política",
    },
    {
        "title": "La ciencia avanza en una cura para el Alzheimer",
        "source": {"name": "Muy interesante"},
        "description": "Un equipo de científicos ha desarrollado una nueva terapia experimental que muestra prometedoros resultados en el tratamiento del Alzheimer.",
        "category": "Ciencia",
    },
]

# Ahora vamos a definir algunas funciones, convencionales y aplicando comprehensions, para comparar y procesar esta lista de artículos.


def extract_titles_with_for(articles):
    """
    Función para extraer los títulos de los artículos utilizando un for normal.
    """
    titles = []
    for article in articles:
        titles.append(article["title"])
    return titles


def extract_titles(articles):
    """
    Función para extraer los títulos de los artículos utilizando una list comprehension.
    """
    return [article["title"] for article in articles]
    # Esta última línea es equivalente a la función anterior pero escrita de forma más concisa y legible. Compacta en una sola línea la iteración, la creación de la lista y el retorno de la misma.


print("Títulos extraídos con for:")
print(extract_titles_with_for(sample_articles))
print("\nTítulos extraídos con list comprehension:")
print(extract_titles(sample_articles))
# Ambas funciones devolverán el mismo resultado.

# ¿Qué pasa si queremos extraer solo los títulos de los artículos que pertenecen a la categoría "Tecnología"? Podemos usar una list comprehension con una condición:


def extract_technology_titles(articles):
    """
    Función para extraer los títulos de los artículos de la categoría "Tecnología" utilizando una list comprehension con condición.
    """
    return [
        article["title"] for article in articles if article["category"] == "Tecnología"
    ]


# Entonces para resumir la sintaxis de una list comprehension:
# [expresión for item in iterable if condición]
# Primero lo que se busca de cada uno de los elementos de la estructura iterable, luego la iteración, aclarando cuál es el iterable, y finalmente, de ser necesario, una condición a seguir. Todo dentro de corchetes, pues queremos obtener una lista.

print("\nTítulos de artículos de la categoría 'Tecnología':")
print(extract_technology_titles(sample_articles))

# Si quisiéramos obtener un diccionario o un conjunto, usaríamos llaves {} o paréntesis () respectivamente, y la sintaxis de la expresión cambiaría ligeramente para adaptarse a la estructura que queremos crear.


# Ejemplo con diccionarios:
def extract_article_summaries(articles):
    """
    Función para extraer un diccionario con el título y la descripción de cada artículo.
    """
    return {article["title"]: article["description"] for article in articles}


# Aquí lo que cambia es que en lugar de corchetes estamos utilizando llaves, propias de los diccionarios; y además estamos definiendo la expresión como clave: valor, donde la clave es el título del artículo y el valor es su descripción.

print("\nDiccionario con títulos y descripciones de los artículos:")
print(extract_article_summaries(sample_articles))

# En el caso de los sets, que suelen ser menos utilizados, la sintaxis sería similar a la de las listas pero con paréntesis, y se obtendría un conjunto de elementos únicos. Podría utilizarse, por ejemplo, para obtener un conjunto de las fuentes de las noticias sin que estas se repitan.


def get_sources_with_for(articles):
    """
    Función para obtener un conjunto de las fuentes de las noticias utilizando un for normal.
    """
    sources = set()
    for article in articles:
        if article.get("source") and article["source"].get("name"):
            sources.add(article["source"]["name"])
    return sources


# Ahora vamos a hacer lo mismo pero con una set comprehension:
def get_sources(articles):
    """
    Función para obtener un conjunto de las fuentes de las noticias utilizando una set comprehension.
    """
    return {
        article["source"]["name"]
        for article in articles
        if article.get("source") and article["source"].get("name")
    }


# En este caso, la expresión es simplemente el nombre de la fuente, y el resultado será un conjunto de nombres de fuentes sin duplicados. En este caso también se usan llaves, pero la expresión es diferente a la del diccionario. En el diccionario se define una relación clave-valor, mientras que en el set solo se define un valor único para cada elemento del conjunto.

print("\nConjunto de fuentes de las noticias:")
print(get_sources(sample_articles))

# Ahora veremos un ejemplo de anidación de bucles utilizando comprehensions. Supongamos que queremos obtener un diccionario que agrupe las noticias según su fuente.


def articles_by_source_with_for(articles):
    """
    Función para agrupar los artículos por su fuente utilizando un for anidado normal.
    """
    sources = get_sources(sample_articles)
    results = {}

    for source in sources:
        if source not in results:
            results[source] = []  # Inicializamos la lista para cada fuente
        for article in articles:
            if article.get("source") and article["source"].get("name") == source:
                results[source].append(article["title"])
                # Esto es, si el artículo tiene una fuente y el nombre de la fuente coincide con la fuente que estamos procesando, entonces agregamos ese artículo a la lista correspondiente en el diccionario de resultados.
    return results

print("\nArtículos agrupados por fuente utilizando for anidado:")
print(articles_by_source_with_for(sample_articles))
# Notese que aquí estamos utilizando cuatro lineas con sus respectivas estructuras e indentaciones para lograr el resultado.

# Ahora vamos a hacer lo mismo pero con una dict comprehension anidada:
def articles_by_source(articles):
    """
    Función para agrupar los artículos por su fuente utilizando una dict comprehension anidada.
    """
    return {
        source: [
            article["title"]
            for article in articles
            if article.get("source") and article["source"].get("name") == source
        ]
        for source in get_sources(sample_articles)
    }
#Aquí directamente retornamos un diccionario, donde la clave es cada una de las fuentes obtenidas por la iteración de la línea 171, y el valor contiene también una comprehension, de tipo lista que itera integrando todos los títulos al valor de cada fuente, siguiendo la misma condición aplicada en la función anterior.
#Como vemos, cuando el comprehension tiene varias secciones, es visualmente mejor separar la sentencia en varias lineas, como en este ejemplo en el que el comprehension anidado comprende las lineas 167 a 169. 

print("\nArtículos agrupados por fuente utilizando comprehension anidada:")
print(articles_by_source(sample_articles))