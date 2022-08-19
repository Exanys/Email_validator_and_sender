from checker import Checker
from sendEmails import Mail

START = 50
def run():

    # scrapper
    # checker = Checker('All_contacts.xlsx', 'result_krasotky.xlsx', ['Jméno', 'Email', 'Číslo'], 'Email')
    # data = checker.get_data()
    # checker.validate(data)
    # checker.save()

    # production
    # mailer = Checker('result_krasotky.xlsx', '', ['Email'], 'Email')
    # emails = mailer.get_data()['Email']
    # mail = Mail()
    # mail = mail.send(emails[START:START + 20], 'Nový portál pro erotickou inzerci zdarma')
    # print(mail)

    # for test emails
    mail = Mail()
    mail = mail.send(['testovaci226@gmail.com'], 'Nový portál pro erotickou inzerci zdarma')
    print(mail)



if __name__ == '__main__':
    run()
