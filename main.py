import feedparser#Faz as requisições dos arquivos fedd
import envioEmail
import time

#Função para pegar as noticas e fazer um dict com as partes desejadas
def filtragemNoticias(urls,palavrasChaves):
    noticias=[]
    #Loop para todas as URL passadas
    for url in urls:
        feeds = feedparser.parse(url)#Pega todo os textos das URL
        for feed in feeds.entries:
            titulo = feed.get('title', '')#Faz uma verificação se tem 'title' no feed
            for palavrasChave in palavrasChaves:
                if palavrasChave.lower() in titulo.lower():#Faz os comparativos das palavras com o 'title', convertendo em minusculo
                    noticia={#salva tudo em um dict
                    'title':feed.title,
                    'description':feed.get('description', 'Não tem descrição'),
                    'published':feed.get('published', 'Não tem data'),
                    'link':feed.link }
                    noticias.append(noticia)#salva na lista, uma lista de discionario
                    break#Para nao verificar a mesma noticia, evitando duplucidade
    return noticias

#Sites de interesse 
urls = [
    'https://agfeed.com.br/feed/',
    'https://revistaagrocampo.com.br/feed/',
    'https://afnews.com.br/feed/',
    'https://www.noticiasagricolas.com.br/conteudo.rss'
]

#Palavras de interesse
palavrasChaves=[
    'Fertilizantes',
    'Fertilizante',
    'Insumos',
    'Insumos Agrícolas',
    'Quebec',
    'Sysco',
    'Riff',
    'Simanto',
    'Kelpak',
    'Go Humate',
    'Tarssus',
    'Polly',
    'Galga',
    'Karrega',
    'Monico',
    'Manzin',
    'Moncuz',
    'Skymobil',
    'Maggo',
    'Defensivo',
    'Defensivo agrícola',
    'Herbicida',
    'Insumos',
    'Inseticida',
    'Fungicida',
    'defensivos',
]

noticiasAntigas=filtragemNoticias(urls,palavrasChaves)
status=envioEmail.enviar(noticiasAntigas)#Envia para a função do email
print(status)

while True:
    noticiasNova=filtragemNoticias(urls,palavrasChaves)#Faz uma nova requisição 
    if noticiasAntigas != noticiasNova: #Compara para ver se ouve alguma mudança
        status=envioEmail.enviar(noticiasNova)#Caso sim envia um novo email
        print(status)
        noticiasAntigas=noticiasNova
    time.sleep(1800)#Espera 30 min para fazer uma nova verificação 
