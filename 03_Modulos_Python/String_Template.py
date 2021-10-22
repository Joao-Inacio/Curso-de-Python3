"""
    String - Template
"""
from string import Template
from datetime import datetime
from dados_email import *

from email import policy
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

with open('template.html', 'r', encoding='utf-8') as html:
    template = Template(html.read())
    hoje = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='João', data=hoje)

msg = MIMEMultipart(policy=policy.default)

msg['from'] = 'João Inácio'
msg['to'] = 'joaoinacio206@gmail.com'
msg['subject'] = 'Deu certo!!!'

corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

with open('FeG.jpg', 'rb') as img:
    img = MIMEImage(img.read())
    msg.attach(img)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(my_email, my_semha)
    smtp.send_message(msg)
    print('E-mail enviado com sucesso')


