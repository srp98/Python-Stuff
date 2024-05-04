import datetime


def print_header():
    print('------------------------------')
    print('       Birthday App')
    print('------------------------------')
    print()


def get_birthday():
    try:
        print('When are you born ?')
        year = int(input('Year [YYYY]: '))
        month = int(input('Month [MM]: '))
        day = int(input('Day [DD]: '))
        birthday = datetime.date(year=year, month=month, day=day)
        return birthday
    except ValueError:
        print('Check Your input values correctly!!')


def compute_days_between_days(original_date, target_date):
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)
    dt = this_year - target_date
    return dt.days


def print_birthday_info(days):
    if days < 0:
        print('You had your birthday {} days ago this year.'.format(-days))
    elif days > 0:
        print('Your birthday is in {} days'.format(days))
    else:
        print('Happy Birthday!!!')


def main():
    print_header()
    birthday = get_birthday()
    today = datetime.date.today()
    number_of_days = compute_days_between_days(birthday, today)
    print_birthday_info(number_of_days)


main()
