"""inputvalid.py
The validating inputed values.
"""

import re

message_latin = 'Only Latin letters are allowed in this field!'
message_cyrillic = 'No cyrillic letters are allowed in this field!'


def cyrillic_presence_test(string, message=message_latin):
    """No cyrillic letters please."""
    result = re.findall("[а-яА-Я]", string)
    if not bool(result):
        pass
    else:
        print(f'Error: {message}')
        string = input('Repeat input: ')
        string = cyrillic_presence_test(string, message)  # Recursion.
    return string


def remove_tabs(string):
    """Code to remove tabulation."""
    if '\t' in string:
        print('Warning: Inputted Tabs characters were removed!')
    return string.replace('\t', '')


def check_letters(string):
    """Checking for absence of letters in given string.
    Return "True" if string has no letters.
    """
    string = cyrillic_presence_test(string)
    string = remove_tabs(string)
    result = True  # Initializing result variable.
    for i in string:
        if i.isalpha():  # If string has letter:
            result = False
    return result


def remove_cyrillic_and_tabs(string, message=message_latin):
    """Function checks for the presence of Cyrillic
    and removes tabs.
    """
    string = cyrillic_presence_test(string, message)
    string = remove_tabs(string)
    return string


def test_cyr_tabs_whitespaces(string, message=message_latin):
    """Function checks for the presence of Cyrillic
    and removes tabs.
    """
    string = cyrillic_presence_test(string, message)
    string = remove_tabs(string)
    string = remove_whitespaces(string)
    return string


def remove_whitespaces(string):
    """Code to remove whitespaces."""
    if ' ' in string:
        print('Warning: Inputted whitespaces were removed!')
    return string.replace(' ', '')


def remove_tabs_and_whitespaces(string):
    """Code to remove tabulation and whitespaces."""
    string = remove_tabs(string)
    string = remove_whitespaces(string)
    return string


def str_valid_to_upper(string):
    """ String validation.
    Capital letters only. No numbers.
    string - parameter (Input string to validation).
    """
    string = cyrillic_presence_test(string, message_cyrillic)
    string = remove_tabs(string)
    modified_string = remove_whitespaces(string)
    # if string.isalpha():
    if modified_string.isalpha():    
        pass
    else:
        print('Error: Only Latin letters are allowed in this field!')
        string = input('Repeat input: ')
        string = cyrillic_presence_test(string, message_cyrillic)
        string = remove_tabs(string)
        string = str_valid_to_upper(string)  # Recursion.
    string = string.upper()
    return string


def valid_decimal(number, sign_control='0'):  # Now sign control is "off".
    """ "number" validation function.
    Checks what decimal digits are allowed for "number".
    number - parameter (Input string to validation).
    number -> <class 'str'>
    sign_control -> parameter (what decimal digits 
    are allowed for "number").
    sign_control = 0 -> Sign control is "off",
    Only decimal digits >= 0 are allowed;
                 = 1 -> 
    Only decimal digits > 0 are allowed.
    """
    sign_control = str(sign_control)
    number = cyrillic_presence_test(number, message_cyrillic)
    number = remove_tabs_and_whitespaces(number)
    # The ability to leave the field empty.
    i = 'y'
    if number in ['']:
        i = input('Do you really want to leave this field empty (y/n): ')
        if i in ['y', 'Y', '', 'yes', 'YES', 'Yes']:
            pass
        else:
            number = input('Repeat input of your decimal number: ')
            number = valid_decimal(number, sign_control)  # Recursion.
    else: pass
    # The end of such ability.
    if number.isdecimal() or number in ['']:  # Decimal validation.
        pass
    else:
        print('Error: Only decimal digits are allowed in this field!')
        number = input('Repeat input: ')
        number = valid_decimal(number, sign_control)  # Recursion.
    # Sign control block.
    if sign_control in ['1'] and number not in ['']:
        if number not in ['0']:  # Only decimal digits > 0 are allowed.
            pass
        else:
            print('Error: Only decimal digits > 0 are allowed \
in this field!')
            number = input('Repeat input: ')
            number = valid_decimal(number, sign_control)  # Recursion.
    else: pass
    # The END of sign control block.
    return number  # <class 'str'>.


def isfloat(number):
    """Python Program to Check If a String Is a Number (Float)"""
    number = cyrillic_presence_test(number, message_cyrillic)
    number = remove_tabs_and_whitespaces(number)
    try:
        float(number)
        return True
    except ValueError:
        return False


def valid_number(number, sign_control='0'):
    """ "number" (int and float) validation function.
    Numbers only. Dots are allowed to float numbers.
    Checks what decimal digits are allowed for "number".
    number - parameter (Input string to validation).
    number --> <class 'str'>
    sign_control --> parameter (what is allowed for "number").
    sign_control = 0 --> Sign control is "off";
                 = 1 --> Only numbers > 0 are allowed;
                 = 2 --> Only numbers >= 0 are allowed.
    """
    sign_control = str(sign_control)
    number = cyrillic_presence_test(number, message_cyrillic)
    number = remove_tabs_and_whitespaces(number)
    # The ability to leave the field empty.
    i = 'y'
    if number in ['']:
        i = input('Do you really want to leave this field empty (y/n): ')
        if i in ['y', 'Y', '', 'yes', 'YES', 'Yes']:
            pass
        else:
            number = input('Repeat input of your number: ')
            number = valid_number(number, sign_control)  # Recursion.
    else: pass
    # The end of such ability.
    if number.isdecimal() or number in ['']:  # Decimal validation.
        pass
    elif isfloat(number) or number in ['']:  # Float validation.
        pass
    else:
        print('Error: Only decimal digits (and one dot for <class "float"> \
are allowed in this field!')
        number = input('Repeat input: ')
        number = valid_number(number, sign_control)  # Recursion.
    # Sign control block.
    if sign_control in ['1'] and number not in ['']:
        number = float(number)  # str --> float
        if number > 0: pass  # Only numbers > 0 are allowed.
        else:
            print('Error: Only numbers > 0 are allowed \
in this field!')
            number = input('Repeat input: ')
            number = valid_number(number, sign_control)  # Recursion.
    elif sign_control in ['2'] and number not in ['']:
        number = float(number)  # str --> float
        if number >= 0: pass  # Only numbers >= 0 are allowed.
        else:
            print('Error: Only numbers >= 0 are allowed \
in this field!')
            number = input('Repeat input: ')
            number = valid_number(number, sign_control)  # Recursion.  
    else: pass
    # The END of sign control block.
    return str(number)


def yes_or_no(string):
    """Only "y","Y" or "n","N" are allowed."""
    string = cyrillic_presence_test(string, message_cyrillic)
    string = remove_tabs_and_whitespaces(string)
    if string in ['y', 'Y']:
        string = 'Y'
    elif string in ['n', 'N']:
        string = 'N'
    else:
        print('Error: Only "Y" or "N" are allowed in this field!')
        string = input('Repeat input: ')
        string = yes_or_no(string)  # Recursion.
    return string


def currency_validation(currency):
    """Checks if the currency's input was right."""
    currency = cyrillic_presence_test(currency, message_cyrillic)
    currency = remove_tabs_and_whitespaces(currency)
    if len(currency) < 1:  # Minimum 1 character should be present.
        print('Error: Too few characters were inputted!')
        currency = input('Repeat Input: ')
        currency = currency_validation(currency)  # Recursion.
    else: pass
    currency = str_valid_to_upper(currency)  # May contain whitespaces.
    currency = remove_whitespaces(currency)  
    return currency


def amount_validation(amount, sign_control=0):  # Function not in use!!!
    """Amount validation function.
    amount --> parameter to validate.
    amount --> <class 'str'>
    sign_control --> parameter (what is allowed for "amount").
    sign_control = 0 --> Sign control is "off";
                 = 1 --> Only numbers > 0 are allowed;
                 = 2 --> Only numbers >= 0 are allowed.
    """
    sign_control = str(sign_control)
    amount = cyrillic_presence_test(amount, message_cyrillic)
    amount = remove_tabs(amount)
    if len(amount) < 1:  # Minimum 1 character should be present.
        print('Error: Too few characters were inputted.')
        amount = input('Repeat Input: ')
        amount = amount_validation(amount, sign_control)  # Recursion.
    amount = valid_number(amount, sign_control)
    return amount


def exit_test(i):
    """Exit or continue validation test."""
    i = cyrillic_presence_test(i, message_cyrillic)
    i = remove_tabs_and_whitespaces(i)
    if i in ['q', '']:
        pass
    else:
        print('Error: only "q" or "ENTER" are allowed!')
        i = input('Press "q" to exit, or "ENTER" to continue): ')
        i = exit_test(i)  # Recursion.
    return i


def one_or_zero(string):
    """Only "1" or "0" are valid values to input parameter."""
    string = cyrillic_presence_test(string,
                                    message_cyrillic)
    string = remove_tabs_and_whitespaces(string)
    if string in ["1", "0"]:
        pass
    else:
        print('Error: Only "1" or "0" without spaces \
are allowed in this field!')
        string = input('Repeat input: ')
        string = one_or_zero(string)  # Recursion.
    return string


def number_validation(number, max_number, min_number=1):
    """Number validation (integer 
    in interval [min_number, max_number]).
    """
    number = cyrillic_presence_test(number, message_cyrillic)
    number = remove_tabs_and_whitespaces(number)

    if number.isdigit():  # Only decimal digits.
        # Removing leading 0...0 from String "number".
        # number = number.lstrip('0')
        pass
    else:
        print(f'Error: The item number should be decimal digit \
in [{min_number}, {max_number}].')
        number = input('Repeat input: ')
        # Recursion:
        number = number_validation(number, max_number, min_number)

    number = int(number)  # <class 'str'> -> <class 'int'>
    if number in range(min_number, max_number+1):
        # Only in range [min_number, max_number].
        pass
    else:
        print(f'Error: The item number should be decimal digit \
in [{min_number}, {max_number}].')
        number = input('Repeat input: ')
        # Recursion:
        number = number_validation(number, max_number, min_number)
    return str(number)


def choose_item(item_name, item_menu, control=0):
    """Drop-down menu analog."""
    print(f'\nThe {item_name} menu Table is: \n')  # Table's title.
    for i, item in enumerate(item_menu, start=1):
        if control == 0:
            print(i, item)
        elif control == 1:
            print(i, item, end='')
        else: pass
    number = input('\nChoose and Input the ordinal number: ')
    number = number_validation(number, len(item_menu))  # Validation.
    number = int(number)
    if item_name == 'Source':
        return str(number)  # Output for 'Source'.
    else:
        return item_menu[number - 1]  # If not 'Source'.


def empty_field(field):  # ??
    """"Please repeat input": if field is empty and I press
    "Enter", make the program ask me if I really want
    to leave this field empty y/n?.
    """
    field = cyrillic_presence_test(field, message_cyrillic)
    field = remove_tabs_and_whitespaces(field)  # Remove "\t" and " ".
    if field == '':
        field = force_empty_field(field)
    else:
        field = valid_decimal(field, 0)
    return field


def force_empty_field(field):  # ???
    """Empty (or ...) field's value."""
    result = False
    result = input('Do you really want to leave this field empty (y/n)?: ')
    result = cyrillic_presence_test(result, message_cyrillic)
    result = remove_tabs(result)
    if result in ['y', 'Y', '']:
        field = ''
    else:
        field = valid_decimal(field, 0)  # Go to
    return field
