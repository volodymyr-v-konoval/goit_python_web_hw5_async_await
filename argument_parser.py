import argparse

from enum_of_currencies import Currencies
from settings import DAYS_MAX
    
available_currencies = []

for currency in Currencies:
    available_currencies.append(currency.name)

# print(available_currencies)

def check_range(value: str) -> int:
    '''
    It is a custom validator for the inputed argument.
    '''
    try:
        int(value)
        ivalue = int(value)
        if ivalue < 1 or ivalue > DAYS_MAX:
            raise argparse.ArgumentTypeError(
            f"{value} is an invalid value. It must be between 1 and {DAYS_MAX}."
            )
        return True
    except ValueError:
        return False
    
    return ivalue


def check_currencies(currencies_list: list) -> list:
    '''
    The function validates currencies.
    '''
    valid_currencies = []
    not_valid_currencies = []

    for currency in currencies_list:
        if any(currency.upper() == item.name for item in Currencies):
            valid_currencies.append(currency.upper())
        else:
            not_valid_currencies.append(currency)

    if not_valid_currencies:
        if len(not_valid_currencies) == 1:
            print(f"There is no currency like {not_valid_currencies} in the bank!")
        else:
            print(f"There are not currencies like {not_valid_currencies} in the bank!")
        print(f"Available currencies are {available_currencies}.")
    return valid_currencies    


def argument_parser() -> int:
    '''
    Parses the comand line input.
    '''
    parser = argparse.ArgumentParser(
        description='Number of days and currencies to see exchange.'
        )
    parser.add_argument("args",
                        nargs="*", 
                        help="Number of days and/or currencies.", 
                        )
    args = parser.parse_args()
    if args.args and check_range(args.args[0]):
        number_of_days = int(args.args[0])
        currencies = args.args[1:]
    else: 
        number_of_days = 1
        currencies = args.args
    currencies = check_currencies(currencies)
    return [number_of_days, currencies]

if __name__ == '__main__':
    bash_args = argument_parser()
    print(bash_args, type(bash_args))
    