import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import formataddr
import requests

# SERVER = 'smtp.gmail.com'
# SERVER = 'etu03.vas-server.cz'
SERVER = 'krasotky.com'
PAGE = 'https://krasotky.com'
# PAGE = 'http://127.0.0.1:8000'

PORT = 587
# PORT = 465

load_dotenv()


class Mail:

    def __init__(self):
        self.port = PORT
        self.smtp_server_domain_name = SERVER
        self.sender_mail = os.getenv('EMAIL_KRASOTKY')
        self.username = os.getenv('EMAIL_KRASOTKY')
        self.password = os.getenv('PASSWORD_KRASOTKY')
        # self.sender_mail = os.getenv('EMAIL_MY')
        # self.password = os.getenv('PASSWORD_MY')

    def send(self, emails: list, subject: str, start: int = 0):
        print(f'Connecting to {self.smtp_server_domain_name}: {self.port}')
        service = smtplib.SMTP(self.smtp_server_domain_name, self.port)
        print('Connected')
        service.starttls()
        service.login(self.username, self.password)
        print('Logged in')
        mail = MIMEMultipart('alternative')
        mail['Subject'] = subject
        mail['From'] = "{} <{}>".format(Header('Tým Krasotky.com').encode(), self.sender_mail)
        mail['Reply-to'] = self.sender_mail
        text_template = """
                   Dobrý den, vážení,

jsme nová online platforma www.krasotky.com, díky které budete na internetu lépe viditelní pro Vaše potenciální zákazníky v oblasti erotických služeb.

Nejdůležitější informace je, že jsme zcela zdarma, nemáme žádné skryté poplatky, příplatky apod. Váš profil můžete kdykoliv sami online upravit nebo smazat. Nemáte žádné závazky.

Před pár dny jsme se spustili, ale naší ambicí je být jedničkou v našem sektoru, budeme na tom tvrdě a vytrvale pracovat. Služby pro naše uživatele chceme poskytovat slušně, stylově a s pokročilými funkcemi online vyhledávání, které všem ušetří čas a jednoduše propojí účastníky webu. Velkou výhodou pro Vás je, že přes portál budou vyhledávat služby i movití cizinci, kteří nemají přehled o službách.
 
Pokud budete mít zájem, založení Vašeho profilu zabere chvilku, probíhá plně samoobslužně online přes jednoduchý registrační formulář ZDE.
 
V případě, že byste měli jakýkoliv dotaz nebo podnět ke zlepšení, můžete nás kontaktovat na info@krasotky.com. Budeme rádi, pokud nás vyzkoušíte. Nemáte co ztratit a jen získáte. Nyní máte šanci být mezi úplně prvními uživateli, kteří budou z tohoto prvenství profitovat.

S pozdravem,
tým Krasotky.com
info@krasotky.com
www.krasotky.com
                   """
        html_template = """
        <html>
        <head></head>
        <body>
                   <div id="editbody1">
                    <div style="font-size: 10pt; font-family: Verdana,Geneva,sans-serif;">
                        <div id="v1editbody1">
                            <div style="font-size: 10pt; font-family: Verdana,Geneva,sans-serif;">
                                <div id="v1v1editbody1">
                                    <div style="font-size: 10pt; font-family: Verdana,Geneva,sans-serif;">
                                        <div id="v1v1v1editbody1">
                                            <div style="font-size: 10pt; font-family: Verdana,Geneva,sans-serif;">
                                                <div id="v1v1v1v1editbody1">
                                                    <div style="font-size: 10pt; font-family: Verdana,Geneva,sans-serif;">
                                                        <div id="v1v1v1v1v1editbody1">
                                                            <div style="font-size: 10pt; font-family: Verdana,Geneva,sans-serif;">
                                                                <div id="v1v1v1v1v1v1editbody1">
                                                                    <div style="font-size: 10pt; font-family: Verdana,Geneva,sans-serif;">
                                                                        <div id="v1v1v1v1v1v1v1editbody1">
                                                                            <div style="font-size: 10pt; font-family: Verdana,Geneva,sans-serif;">
                                                                                <div id="v1v1v1v1v1v1v1v1editbody1">
                                                                                    <div style="font-size: 10pt; font-family: Verdana,Geneva,sans-serif;">
                                                                                        <div id="v1v1v1v1v1v1v1v1v1editbody1">
                                                                                            <div style="font-size: 10pt; font-family: Verdana,Geneva,sans-serif;">
                                                                                                <div id="v1v1v1v1v1v1v1v1v1v1editbody1">
                                                                                                    <div style="font-size: 10pt; font-family: Verdana,Geneva,sans-serif;">
                                                                                                        <div id="v1v1v1v1v1v1v1v1v1v1v1editbody1">
                                                                                                            <div style="font-size: 10pt; font-family: Verdana,Geneva,sans-serif;">
                                                                                                                <div id="v1v1v1v1v1v1v1v1v1v1v1v1editbody1">
                                                                                                                    <div style="font-size: 10pt; font-family: Verdana,Geneva,sans-serif;">
                                                                                                                        <div id="v1v1v1v1v1v1v1v1v1v1v1v1v1editbody1">
                                                                                                                            <div style="font-size: 10pt; font-family: Verdana,Geneva,sans-serif;">
                                                                                                                                <div id="v1v1v1v1v1v1v1v1v1v1v1v1v1v1editbody1">
                                                                                                                                    <div style="font-size: 10pt; font-family: Verdana,Geneva,sans-serif;">
                                                                                                                                        <div id="v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1editbody1">
                                                                                                                                            <div style="font-size: 10pt; font-family: Verdana,Geneva,sans-serif;">
                                                                                                                                                <div id="v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1editbody1">
                                                                                                                                                    <div style="font-size: 10pt; font-family: Verdana,Geneva,sans-serif;">
                                                                                                                                                        <div id="v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1editbody1">
                                                                                                                                                            <div style="font-size: 10pt; font-family: Verdana,Geneva,sans-serif;">
                                                                                                                                                                <div id="v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1editbody1">
                                                                                                                                                                    <div style="font-size: 10pt; font-family: Verdana,Geneva,sans-serif;">
                                                                                                                                                                        <div id="v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1editbody1">
                                                                                                                                                                            <div style="font-size: 10pt; font-family: Verdana,Geneva,sans-serif;">
                                                                                                                                                                                <div id="v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1editbody1">
                                                                                                                                                                                    <div style="font-size: 10pt; font-family: Verdana,Geneva,sans-serif;">
                                                                                                                                                                                        <div id="v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1editbody1">
                                                                                                                                                                                            <div style="font-size: 10pt; font-family: Verdana,Geneva,sans-serif;">
                                                                                                                                                                                                <div id="v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1editbody1">
                                                                                                                                                                                                    <div style="font-size: 10pt; font-family: Verdana,Geneva,sans-serif;">
                                                                                                                                                                                                        <div id="v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1editbody1">
                                                                                                                                                                                                            <div style="font-size: 10pt; font-family: Verdana,Geneva,sans-serif;">
                                                                                                                                                                                                                <div id="v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1editbody1">
                                                                                                                                                                                                                    <div style="font-size: 10pt; font-family: Verdana,Geneva,sans-serif;">
                                                                                                                                                                                                                        <div id="v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1editbody1">
                                                                                                                                                                                                                            <div style="font-size: 10pt; font-family: Verdana,Geneva,sans-serif;">
                                                                                                                                                                                                                                <div id="v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1editbody1">
                                                                                                                                                                                                                                    <div style="font-size: 10pt; font-family: Verdana,Geneva,sans-serif;">
                                                                                                                                                                                                                                        <div id="v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1editbody1">
                                                                                                                                                                                                                                            <div style="font-size: 10pt; font-family: Verdana,Geneva,sans-serif;">
                                                                                                                                                                                                                                                <div id="v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1editbody1">
                                                                                                                                                                                                                                                    <div style="font-size: 10pt; font-family: Verdana,Geneva,sans-serif;">
                                                                                                                                                                                                                                                        <div id="v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1editbody1">
                                                                                                                                                                                                                                                            <div style="font-size: 10pt; font-family: Verdana,Geneva,sans-serif;">
                                                                                                                                                                                                                                                                <div id="v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1editbody1">
                                                                                                                                                                                                                                                                    <div style="font-size: 10pt; font-family: Verdana,Geneva,sans-serif;">
                                                                                                                                                                                                                                                                        <div class="v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1pre"
                                                                                                                                                                                                                                                                             style="margin: 0; padding: 0; font-family: monospace;">
                                                                                                                                                                                                                                                                            <span style="font-family: verdana, geneva, sans-serif;">Dobr&yacute; den, v&aacute;žen&iacute;,</span><br/><br/><span
                                                                                                                                                                                                                                                                                style="font-family: verdana, geneva, sans-serif;">jsme nov&aacute; online platforma <a
                                                                                                                                                                                                                                                                                href="{page}/from_email_home?email={email}"
                                                                                                                                                                                                                                                                                target="_blank"
                                                                                                                                                                                                                                                                                rel="noopener noreferrer">www.krasotky.com</a>, d&iacute;ky kter&eacute; budete na internetu l&eacute;pe viditeln&iacute; pro Va&scaron;e potenci&aacute;ln&iacute; z&aacute;kazn&iacute;ky v oblasti erotick&yacute;ch služeb.</span>
                                                                                                                                                                                                                                                                            <div>
                                                                                                                                                                                                                                                                                <br/>
                                                                                                                                                                                                                                                                                <div>
                                                                                                                                                                                                                                                                                    <span style="font-family: verdana, geneva, sans-serif;"><strong>Nejdůležitěj&scaron;&iacute; informace je, že jsme zcela zdarma, nem&aacute;me ž&aacute;dn&eacute; skryt&eacute; poplatky, př&iacute;platky apod. V&aacute;&scaron; profil můžete kdykoliv sami online upravit nebo smazat. Nem&aacute;te ž&aacute;dn&eacute; z&aacute;vazky.</strong></span>
                                                                                                                                                                                                                                                                                </div>
                                                                                                                                                                                                                                                                                <div>
                                                                                                                                                                                                                                                                                    <br/><span
                                                                                                                                                                                                                                                                                        style="font-family: verdana, geneva, sans-serif;">Před p&aacute;r dny jsme se spustili, ale na&scaron;&iacute; ambic&iacute; je b&yacute;t jedničkou v na&scaron;em sektoru, budeme na tom tvrdě a vytrvale pracovat. Služby pro na&scaron;e uživatele chceme poskytovat slu&scaron;ně, stylově a s pokročil&yacute;mi funkcemi online vyhled&aacute;v&aacute;n&iacute;, kter&eacute; v&scaron;em u&scaron;etř&iacute; čas a jednodu&scaron;e propoj&iacute; &uacute;častn&iacute;ky webu. Velkou v&yacute;hodou pro V&aacute;s je, že přes port&aacute;l budou vyhled&aacute;vat služby i movit&iacute; cizinci, kteř&iacute; nemaj&iacute; přehled o služb&aacute;ch.</span>
                                                                                                                                                                                                                                                                                </div>
                                                                                                                                                                                                                                                                                <div>
                                                                                                                                                                                                                                                                                    &nbsp;
                                                                                                                                                                                                                                                                                </div>
                                                                                                                                                                                                                                                                                <div>
                                                                                                                                                                                                                                                                                    <span style="font-family: verdana, geneva, sans-serif;"><strong>Pokud budete m&iacute;t z&aacute;jem, založen&iacute; Va&scaron;eho profilu zabere chvilku, prob&iacute;h&aacute; plně samoobslužně online přes jednoduch&yacute; registračn&iacute; formul&aacute;ř <a
                                                                                                                                                                                                                                                                                            href="{page}/from_email_registrace?email={email}"
                                                                                                                                                                                                                                                                                            target="_blank"
                                                                                                                                                                                                                                                                                            rel="noopener noreferrer">ZDE</a>.</strong></span>
                                                                                                                                                                                                                                                                                </div>
                                                                                                                                                                                                                                                                                <div>
                                                                                                                                                                                                                                                                                    &nbsp;
                                                                                                                                                                                                                                                                                </div>
                                                                                                                                                                                                                                                                                <div>
                                                                                                                                                                                                                                                                                    <span style="font-family: verdana, geneva, sans-serif;">V př&iacute;padě, že byste měli jak&yacute;koliv dotaz nebo podnět ke zlep&scaron;en&iacute;, můžete n&aacute;s kontaktovat na <a
                                                                                                                                                                                                                                                                                            href="mailto:info@krasotky.com"
                                                                                                                                                                                                                                                                                            rel="noreferrer">info@krasotky.com</a>. Budeme r&aacute;di, pokud n&aacute;s vyzkou&scaron;&iacute;te. Nem&aacute;te co ztratit a jen z&iacute;sk&aacute;te. Nyn&iacute; m&aacute;te &scaron;anci b&yacute;t mezi &uacute;plně prvn&iacute;mi uživateli, kteř&iacute; budou z tohoto prvenstv&iacute; profitovat.</span>
                                                                                                                                                                                                                                                                                </div>
                                                                                                                                                                                                                                                                                <div>
                                                                                                                                                                                                                                                                                    <br/><span
                                                                                                                                                                                                                                                                                        style="font-family: verdana, geneva, sans-serif;">S pozdravem,</span>
                                                                                                                                                                                                                                                                                </div>
                                                                                                                                                                                                                                                                                <div>
                                                                                                                                                                                                                                                                                    <span style="font-family: verdana, geneva, sans-serif;">t&yacute;m <a
                                                                                                                                                                                                                                                                                            href="{page}/from_email_home?email={email}"
                                                                                                                                                                                                                                                                                            target="_blank"
                                                                                                                                                                                                                                                                                            rel="noopener noreferrer">Krasotky.com</a></span>
                                                                                                                                                                                                                                                                                </div>
                                                                                                                                                                                                                                                                                <div>
                                                                                                                                                                                                                                                                                    <a href="#v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1v1NOP"><span
                                                                                                                                                                                                                                                                                            style="font-family: verdana, geneva, sans-serif;">info@krasotky.com</span></a>
                                                                                                                                                                                                                                                                                </div>
                                                                                                                                                                                                                                                                                <div>
                                                                                                                                                                                                                                                                                    <span style="font-family: verdana, geneva, sans-serif;"><a
                                                                                                                                                                                                                                                                                            href="{page}/from_email_home?email={email}"
                                                                                                                                                                                                                                                                                            target="_blank"
                                                                                                                                                                                                                                                                                            rel="noopener noreferrer">www.krasotky.com</a></span>
                                                                                                                                                                                                                                                                                </div>
                                                                                                                                                                                                                                                                            </div>
                                                                                                                                                                                                                                                                        </div>
                                                                                                                                                                                                                                                                    </div>
                                                                                                                                                                                                                                                                </div>
                                                                                                                                                                                                                                                            </div>
                                                                                                                                                                                                                                                        </div>
                                                                                                                                                                                                                                                    </div>
                                                                                                                                                                                                                                                </div>
                                                                                                                                                                                                                                            </div>
                                                                                                                                                                                                                                        </div>
                                                                                                                                                                                                                                    </div>
                                                                                                                                                                                                                                </div>
                                                                                                                                                                                                                            </div>
                                                                                                                                                                                                                        </div>
                                                                                                                                                                                                                    </div>
                                                                                                                                                                                                                </div>
                                                                                                                                                                                                            </div>
                                                                                                                                                                                                        </div>
                                                                                                                                                                                                    </div>
                                                                                                                                                                                                </div>
                                                                                                                                                                                            </div>
                                                                                                                                                                                        </div>
                                                                                                                                                                                    </div>
                                                                                                                                                                                </div>
                                                                                                                                                                            </div>
                                                                                                                                                                        </div>
                                                                                                                                                                    </div>
                                                                                                                                                                </div>
                                                                                                                                                            </div>
                                                                                                                                                        </div>
                                                                                                                                                    </div>
                                                                                                                                                </div>
                                                                                                                                            </div>
                                                                                                                                        </div>
                                                                                                                                    </div>
                                                                                                                                </div>
                                                                                                                            </div>
                                                                                                                        </div>
                                                                                                                    </div>
                                                                                                                </div>
                                                                                                            </div>
                                                                                                        </div>
                                                                                                    </div>
                                                                                                </div>
                                                                                            </div>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                                   <img src="{page}/api/email_read?email={email}" alt="Krasotky.com" width="1" height="1" style="display:none;" />

                </body>
                </html>
                   """
        html_content = MIMEText(html_template, 'html', _charset='UTF-8')
        text_content = MIMEText(text_template, 'plain', _charset='UTF-8')
        # mail.attach(text_content)
        # mail.attach(html_content)

        # service.sendmail(self.sender_mail, emails, mail.as_string())
        # result = service.sendmail(self.sender_mail, emails, f"Subject: {subject}\n{content}")
        for email in emails:
            html_content = MIMEText(html_template.format(page=PAGE, email=email), 'html', _charset='UTF-8')
            text_content = MIMEText(text_template, 'plain', _charset='UTF-8')
            mail.attach(text_content)
            mail.attach(html_content)
            mail['To'] = email
            print(email)
            result = service.sendmail(self.sender_mail, email, mail.as_string())
            r = requests.get(f'{PAGE}/api/email_sent?email={email}')
            # print(r)

        service.quit()
        return f'Sent {len(emails)} emails'
