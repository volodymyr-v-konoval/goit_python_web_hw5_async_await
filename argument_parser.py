import argparse

from settings import DAYS_MAX  


def check_range(value: int) -> int:
    '''
    It is a custom validator for the inputed argument.
    '''
    ivalue = int(value)
    if ivalue < 1 or ivalue > DAYS_MAX:
        raise argparse.ArgumentTypeError(
            f"{value} is an invalid value. It must be between 1 and {DAYS_MAX}."
            )
    return ivalue

def argument_parser() -> int:
    '''
    Parses the comand line input.
    '''
    parser = argparse.ArgumentParser(
        description='Number of days to see exchange.'
        )
    parser.add_argument("number_of_days", 
                        help="Number of days", 
                        type=check_range, 
                        default=1, 
                        nargs="?")
    args = vars(parser.parse_args())
    return args.get("number_of_days")

if __name__ == '__main__':
    current_number = argument_parser()
    print(current_number, type(current_number))