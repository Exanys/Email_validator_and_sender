import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# SERVER = 'smtp.gmail.com'
SERVER = 'etu03.vas-server.cz'
PORT = 587
load_dotenv()


class Mail:

    def __init__(self):
        self.port = PORT
        self.smtp_server_domain_name = SERVER
        self.sender_mail = os.getenv('EMAIL')
        self.password = os.getenv('PASSWORD')

    def send(self, emails, subject, content):
        service = smtplib.SMTP(self.smtp_server_domain_name, self.port)
        service.starttls()
        service.login(self.sender_mail, self.password)
        mail = MIMEMultipart('alternative')
        mail['Subject'] = 'Test'
        mail['From'] = 'Vojtěch Binar '
        mail['To'] = emails

        text_template = """
                   Zdravíme všechny milovníky psů!

                Děkujeme za to, že jsi součástí naší komunity HAFIO. Jsme tu proto, abychom ti pomohli najít parťáka na procházky a zároveň brigádu, které tě bude bavit.

            Už jsi skrz HAFIO našel pejska na hlídání? Budeme moc rádi, když nám pošleš fotky z procházky s tvým novým svěřencem. 

            Fotky můžeš posílat na email (info@hafio.cz) či instagram (@hafio.cz) společně s tvým jménem a jménem pejska, kterého jsi hlídal. Ty nejlepší fotky pak zveřejníme na našem instagramu.

                Moc děkujeme za to, že jsi s námi a budujeme společně stále větší a větší komunitu milovníků psů! Budeme také rádi za jakoukoliv tvoji zpětnou vazbu.

                Měj se krásně! HAF!

                Tým HAFIO
                   """
        html_template = """
                   <h3>Zdravíme všechny milovníky psů!</h3>

<p>Děkujeme za to, že jsi součástí naší komunity HAFIO. Jsme tu proto, abychom ti pomohli najít parťáka na procházky a zároveň brigádu, které tě bude bavit.</p>

<p>Už jsi skrz HAFIO našel pejska na hlídání? Budeme moc rádi, když nám pošleš fotky z procházky s tvým novým svěřencem.</p> 

<p>Fotky můžeš posílat na email <a href='mailto:info@hafio.cz'>(info@hafio.cz)</a> či instagram (<a href='https://instagram.com/hafio.cz'>@hafio.cz</a>) společně s tvým jménem a jménem pejska, kterého jsi hlídal. Ty nejlepší fotky pak zveřejníme na našem instagramu.</p>

<p>Moc děkujeme za to, že jsi s námi a budujeme společně stále větší a větší komunitu milovníků psů! Budeme také rádi za jakoukoliv tvoji zpětnou vazbu.</p>
<br>
<p>Měj se krásně! HAF!<br>

Tým HAFIO</p>
                   """

        html_content = MIMEText(html_template, 'html', _charset='UTF-8')
        text_content = MIMEText(text_template, 'plain', _charset='UTF-8')

        mail.attach(text_content)
        mail.attach(html_content)

        service.sendmail(self.sender_mail, emails, mail.as_string())
        # result = service.sendmail(self.sender_mail, emails, f"Subject: {subject}\n{content}")
        # for email in emails:
        #     result = service.sendmail(self.sender_mail, emails, f"Subject: {subject}\n{content}")

        service.quit()
        return 'Sent'

