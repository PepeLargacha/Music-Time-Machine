"""Control the input of the user"""
from datetime import datetime


def get_year_from_user():
    year = input('To which year do you want to travel back to? (YYYY): ')
    if year.isnumeric():
        year = int(year)
        if year < 1959 or year > datetime.now().year - 10:
            print(f'Invalid year, try one between 1959 and \
                {datetime.now().year - 10}')
            return get_year_from_user()
        else:
            print('You will travel back to', year)
    else:
        print(f'Invalid year, try one between 1959 and \
            {datetime.now().year - 10}')
        return get_year_from_user()

    return year
