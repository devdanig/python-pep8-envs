# *args 
# *Args argumentos dinamicos

def newsapi_client(api_key, query, timeout=30, retries=3):
    return f'News API: {query} con timeout: {timeout}'

def guardian_client(api_key, section, from_date, timeout=30, retries=3):
    return f'Guardian {section} desde {from_date} con timeout de {timeout}'

def ejemplo_args(api_key, *args):
    print(f'API KEY: {api_key}')
    print(f'args: {args}')
    print(f'Type: {type(args)}')

ejemplo_args('API_KEY_VALUE', 'Este', 'Parametro', 'Aca')
ejemplo_args('API_KEY_VALUE', 'Hola', 'Mundo')

# **kwargs: van a ser nombrados, vamos a poder utlitizar el nombre de la variable como fue enviada para poder utilizarla dentro de la funcion

def ejemplo_kwargs(**kwargs):
    print(f'Tipo: {type(kwargs)}')
    print(f'Kawargs: {kwargs}')

ejemplo_kwargs(api_key='DEMO', query='Noticias de Python', timeout=30, retries=3)
ejemplo_kwargs(api_key='DEMO_GUARDIAN', section='Sports', from_date='2020-10-10', timeout=30, retries=3)

def fetch_news(api_name, *args, **kwargs):
    pass