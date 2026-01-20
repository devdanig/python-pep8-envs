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


def extract_titles_traditional(articles):
    """Extrae solo los titulos usando un for"""
    titles = []
    for article in articles:
        if len(article['title']) > 15:
            titles.append(article['title'])
    return titles

def extract_titles(articles):
    """Extrae los titulos usando comprehension"""
    return [
        article['title'] for article in articles if len(article['title']) > 10
    ]


"""Reto devolver un diccionario de titulos y categoria"""

def extract_titles_diccionary(article_list):
    titles_category = {}
    for article in article_list:
        titles_category[article['title']] = article['category']
    return titles_category


def extract_titles_diccionary_comprehension(article_list):
    return {
        article['title'] : article['category'] for article in article_list
    }


def extract_titles_set(article_list):
    categories = set()
    for article in article_list:
        categories.add(article['category'])
    return categories

def extract_titles_set_comprehension(article_list):
    return { article['category'] for article in article_list }


print(extract_titles_traditional(sample_articles))
print("------------------------------------------")
print(extract_titles(sample_articles))
print("------------------------------------------")
print(extract_titles_diccionary(sample_articles))
print("------------------------------------------")
print(extract_titles_diccionary_comprehension(sample_articles))
print("------------------------------------------")
print(extract_titles_set(sample_articles))
print("------------------------------------------")
print(extract_titles_set_comprehension(sample_articles))