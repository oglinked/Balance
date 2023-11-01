"""inputvalid.py
The validating inputed values.
"""

import re
from cidvalid import cid_validation

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
        print('Warning: Tabs characters were removed!')
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
    """The Function checks for the presence of Cyrillic and 
    removes tabs and whitespaces.
    """
    string = cyrillic_presence_test(string, message)
    string = remove_tabs(string)
    string = remove_whitespaces(string)
    return string


def remove_whitespaces(string):
    """Code to remove whitespaces."""
    if ' ' in string:
        print('Warning: Whitespaces were removed!')
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
    string = remove_cyrillic_and_tabs(string, message_cyrillic)
    modified_string = remove_whitespaces(string)
    # if string.isalpha():
    if modified_string.isalpha():
        pass
    else:
        print('Error: Only Latin letters are allowed in this field!')
        string = input('Repeat input: ')
        string = remove_cyrillic_and_tabs(string, message_cyrillic)
        string = str_valid_to_upper(string)  # Recursion.
    string = string.upper()
    return string


def valid_decimal(number, sign_control='0'):  # Now sign control is "off".
    """ "number" validation function.
    Checks what decimal digits are allowed for "number".
        number - parameter (Input string to validation).
        number - <class 'str'>
        sign_control -> parameter (what decimal digits 
                        are allowed for "number").
        sign_control = 0 -> Sign control is "off",
                            Only decimal digits >= 0 are allowed;
        sign_control = 1 -> Only decimal digits > 0 are allowed.
    """
    sign_control = str(sign_control)
    number = test_cyr_tabs_whitespaces(number, message_cyrillic)
    # The ability to leave the field empty.
    i = 'y'
    if number in ['']:
        i = input('Do you really want to leave this field empty (y/n): ')
        if i in ['y', 'Y', '', 'yes', 'YES', 'Yes']:
            pass
        else:
            number = input('Repeat input of your decimal number: ')
            number = valid_decimal(number, sign_control)  # Recursion.
    else:
        pass
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
    else:
        pass
    # The END of sign control block.
    return number  # <class 'str'>.


def isfloat(number):
    """Python Program to Check If a String Is a Number (Float)."""
    number = test_cyr_tabs_whitespaces(number, message_cyrillic)
    try:
        float(number)
        return True
    except ValueError:
        return False


def empty_field_denied(string, sign_control):
    """This function denied empty field input."""
    if string in ['']:
        print('Error: It\'s denied to leave this field empty.')
        string = input('Repeat Input: ')
        string = amount_checking(string, sign_control)  # !!
    else:
        pass
    return str(string)


def amount_checking(string, sign_control='1'):
    """    """
    string = empty_field_denied(string, sign_control)
    string = valid_number(string, sign_control)
    string = empty_field_denied(string, sign_control)
    return str(string)


def cid_checking(name, string, sign_control='0'):
    """CID validation function. It's new approach."""
    string = empty_cid_denied(name, string, sign_control)
    # string = valid_decimal(string, sign_control)  # Only decimal digitds.
    string = cid_validation(string)  # Latin letters and decimal digits only.
    string = empty_cid_denied(name, string, sign_control)
    return str(string)


def empty_cid_denied(name, string, sign_control):
    """This function denied empty field input.
    For CID only.
    """
    if string in ['']:
        print('Error: It\'s denied to leave this field empty.')
        string = input(f'Repeat "{name}" Input: ')
        string = cid_checking(name, string, sign_control)  # !!
    else:
        pass
    return str(string)


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
    # Clearing the Input:
    number = str(number)
    sign_control = str(sign_control)
    number = test_cyr_tabs_whitespaces(number, message_cyrillic)
    if '_' in number:
        number = input('Error: "_" sign is not allowed! \
Repeat input: ')
        number = valid_number(number, sign_control)  # Recursion.
    else:
        pass

    # The ability to leave the field empty.
    i = 'y'
    if number in ['']:
        i = input('Do you really want to leave this field empty (y/n): ')
        if i in ['y', 'Y', '', 'yes', 'YES', 'Yes']:
            pass
        else:
            number = input('Repeat input of your number: ')
            number = valid_number(number, sign_control)  # Recursion.
    else:
        pass
    # The end of such ability.

    if number.isdecimal() or number in ['']:  # Decimal validation.
        pass
    elif isfloat(number) or number in ['']:  # Float validation.
        pass
    else:
        print('Error: Only decimal digits (and one dot for \
<class \'float\'> are allowed in this field!')
        number = input('Repeat input: ')
        number = valid_number(number, sign_control)  # Recursion.

    # Sign control block.
    if sign_control in ['1'] and number not in ['']:
        number = float(number)  # str --> float
        if number > 0:
            pass  # Only numbers > 0 are allowed.
        else:
            print('Error: Only numbers > 0 are allowed \
in this field!')
            number = input('Repeat input: ')
            number = valid_number(number, sign_control)  # Recursion.
    elif sign_control in ['2'] and number not in ['']:
        number = float(number)  # str --> float
        if number >= 0:
            pass  # Only numbers >= 0 are allowed.
        else:
            print('Error: Only numbers >= 0 are allowed \
in this field!')
            number = input('Repeat input: ')
            number = valid_number(number, sign_control)  # Recursion.
    else:
        pass
    # The END of sign control block.

    number = dash_signs_removing(number)  # No '-' in number allowed.
    return str(number)


def dash_signs_removing(string):
    """Code to remove dash signs."""
    string = str(string)
    if '-' in string:
        print('Warning: Dash "-" sign(s) was(were) removed!')
    else:
        pass
    return string.replace('-', '')


def yes_or_no(string):
    """Only "y","Y" or "n","N" are allowed."""
    string = test_cyr_tabs_whitespaces(string, message_cyrillic)
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
    currency = test_cyr_tabs_whitespaces(currency, message_cyrillic)
    if len(currency) < 1:  # Minimum 1 character should be present.
        print('Error: Too few characters were inputted!')
        currency = input('Repeat Input: ')
        currency = currency_validation(currency)  # Recursion.
    else:
        pass
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
    amount = remove_cyrillic_and_tabs(amount, message_cyrillic)
    if len(amount) < 1:  # Minimum 1 character should be present.
        print('Error: Too few characters were inputted.')
        amount = input('Repeat Input: ')
        amount = amount_validation(amount, sign_control)  # Recursion.
    amount = valid_number(amount, sign_control)
    return amount


def exit_test(i):
    """Exit or continue validation test."""
    i = test_cyr_tabs_whitespaces(i, message_cyrillic)
    if i in ['q', '']:
        pass
    else:
        print('Error: only "q" or "ENTER" are allowed!')
        i = input('Press "q" to exit, or "ENTER" to continue): ')
        i = exit_test(i)  # Recursion.
    return i


def one_or_zero(string):
    """Only "1" or "0" are valid values to input parameter."""
    string = test_cyr_tabs_whitespaces(string, message_cyrillic)
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
    number = test_cyr_tabs_whitespaces(number, message_cyrillic)

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
        else:
            pass
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
    field = test_cyr_tabs_whitespaces(field, message_cyrillic)
    if field == '':
        field = force_empty_field(field)
    else:
        field = valid_decimal(field, 0)
    return field


def force_empty_field(field):  # ???
    """Empty (or ...) field's value."""
    result = False
    result = input('Do you really want to leave this field empty (y/n)?: ')
    result = remove_cyrillic_and_tabs(result, message_cyrillic)
    if result in ['y', 'Y', '']:
        field = ''
    else:
        field = valid_decimal(field, 0)  # Go to
    return field
