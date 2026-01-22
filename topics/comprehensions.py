sample_articles = [
    {
        "title": "Python logra nuevo éxito",
        "source": {"name": "TechNews"},
        "description": "Gran noticia",
        "category": "Tecnología",
    },
    {
        "title": "Mercado en crisis",
        "source": {"name": "Finance"},
        "description": "Análisis completo",
        "category": "Economía",
    },
    {
        "title": "Nueva tecnología",
        "source": {"name": "TechNews"},
        "description": "Innovación",
        "category": "Tecnología",
    },
    {
        "title": "Deportes hoy",
        "source": {"name": "Sports"},
        "description": "Resultados",
        "category": "Deportes",
    },
    {
        "title": "Política actual",
        "source": {"name": "News"},
        "description": "Actualidad",
        "category": "Política",
    },
    {
        "title": "Ciencia avanza",
        "source": {"name": "Science"},
        "description": "Descubrimientos",
        "category": "Ciencia",
    },
]

# Comprehensions nos permite convertir un ciclo for de varias niveles en una sola linea de codigo
# Extrae titulos usando FOR

def extract_titles_for(articles):
    titles = []
    for article in articles:
        titles.append(article['title'])
    return titles

# Extraer titulos con Comprehensions

def extract_titles(articles):
    '''[Expression for elemento in iterable]'''
    return [article['title'] for article in articles]


# Extraer titulo y descripcion con Comprehensions

def extract_title_and_description(articles):
    return { article['title'] : article['description'] for article in articles}
    

# Reto: Agregar if en cada funcion, crear una lista sin que se repitan de todas las fuentes con set() primero for y luengo comprehensions.

def extract_source_for(articles):
    source = set()
    for article in articles:
        if article.get('source') and article.get('source').get('name'):
            source.add(article.get('source').get('name'))
    return source

def extract_sources(articles):
    return {
        article.get('source').get('name')
        for article in articles
        if article.get('source') and article.get('source').get('name')
    }

# Categorizar todas las noticias deacuerdo a la categoria para tener una lista de las noticias que hacen match con esta categoria

def categorizar_for(articles):
    sources = extract_sources(articles)
    results = {}
    for source in sources:
        if source not in results:
            results[source] = []
        for article in articles:
            if source == article.get('source').get('name'):
                results[source].append(article)
    return results


def categorizar(articles):
    sources = extract_sources(articles)
    return {
        source: [
            article
            for article in articles
            if source == article.get('source').get('name')
        ]
        for source in sources
    }


# print(f'Con For titles: {extract_titles_for(sample_articles)}') 
# print(f'Con Comprehension titles: {extract_titles(sample_articles)}') 
# print(f'Titulo y descripcion con Comprenhesions: {extract_title_and_description(sample_articles)}')
# print(f'Fuentes con for: {extract_source_for(sample_articles)}')
# print(f'Fuente con comprehensions: {extract_sources(sample_articles)}')
# print(f'Catogorias: {categorizar_for(sample_articles)}')
print(f'Categorizacion:{categorizar_for(sample_articles)}')
print(f'Categorizacion Comprehensions: {categorizar(sample_articles)}')
