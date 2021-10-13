def return_10():
    return 10

def add(first_number, second_number):
    sum = first_number + second_number
    return sum

def subtract(first_number, second_number):
    sum = first_number - second_number
    return sum

def multiply(first_number, second_number):
    sum = first_number * second_number
    return sum

def divide(first_number, second_number):
    sum = first_number / second_number
    return sum 

def length_of_string(test_string):
    return len(test_string)

def join_string( string_1, string_2 ):
    return string_1 + string_2

def add_string_as_number(string_1, string_2):
    return int(string_1) + int(string_2)

months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}


def number_to_full_month_name(month):
    return(months[month])


short_months = {
    1: "Jan",
    2: "Feb",
    3: "Mar",
    4: "Apr",
    5: "May",
    6: "Jun",
    7: "Jul",
    8: "Aug",
    9: "Sep",
    10: "Oct",
    11: "Nov",
    12: "Dec"
}
    
def number_to_short_month_name(short_month):
    return(short_months[short_month])
    

def test_volume_of_cube(sidelength):
    return(sidelength ** 3)

def test_reverse_string(string):
    return(string).reverse

def test_fahrenheit_to_celsius(warmth):
    return(warmth - 32 * .5556 )