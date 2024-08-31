import datetime


def date_list(number_of_days: int) -> list:
    '''
    Makes the list of dates in str format.
    '''
    dates = []
    days = 0
    while days < number_of_days:
        period = datetime.timedelta(days=days)
        current_date = datetime.date.today() - period
        dates.append(current_date.strftime('%d.%m.%Y'))
        days += 1
    return dates


if __name__ == '__main__':
    
    print(date_list(5))
