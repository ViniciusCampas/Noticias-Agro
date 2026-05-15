import smtplib#Conectar ao servidor de email
from email.mime.text import MIMEText#Conta o conteudo para envio de email

#Função que formata o texto em html e envia para o email desejado
def enviar(noticias):
    #Abri o HTML e o formata 
    html = '''
    <html>
    <body style='font-family: Arial; background:#f4f4f4; padding:20px;'>

    <h2 style='color:#333;'>
    Relatório das principais notícias
    </h2>
    '''

    #Adiciona as informações coletadas nas noticias
    for noticia in noticias:
        html += f'''
        <div style='
            background:white;
            padding:15px;
            margin-bottom:20px;
            border-radius:10px;
            box-shadow:0 0 5px rgba(0,0,0,0.1);
        '>

            <h3 style='color:#1a73e8;'>
                {noticia['title']}
            </h3>

            <p>
                {noticia['description']}
            </p>

            <p>
                <strong>Publicado:</strong>
                {noticia['published']}
            </p>

            <a href='{noticia['link']}'
            style='
                    display:inline-block;
                    padding:10px 15px;
                    background:#1a73e8;
                    color:white;
                    text-decoration:none;
                    border-radius:5px;
            '>
            Ler notícia
            </a>

        </div>
        '''

    #Fecha o HTML
    html += '''
    </body>
    </html>
    '''

    email=''
    senha=''

    msg=MIMEText(html,'html')

    msg['Subject'] =''
    msg['From'] = email
    msg['To'] =''


    try :
        #abri o servidor do 'gmail' para enviar os email
        with smtplib.SMTP('smtp.gmail.com',587,timeout=10) as servidor:
            servidor.starttls()
            servidor.login(email,senha)
            servidor.send_message(msg)
        return f'Email enviado com sucesso'
    except Exception as erro:
        return f'Erro ao enviar o email, erro: {erro}'
