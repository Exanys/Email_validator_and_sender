from checker import Checker


def run():
    checker = Checker('All_contacts.xlsx', 'result_krasotky.xlsx', ['Jméno', 'Email', 'Číslo'], 'Email')
    data = checker.get_data()
    checker.validate(data)
    checker.save()


if __name__ == '__main__':
    run()
