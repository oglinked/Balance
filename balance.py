"""The program balance.py (version 04.08) is intermediate 
balance calculating program where xlwings library is used to 
interact with .xlsx data file.

xlwings (Open Source) is a BSD-licensed Python library that 
makes it easy to call Python from Excel and vice versa:

    Scripting: Automate/interact with Excel from Python 
    using a syntax close to VBA.

    Macros: Replace VBA macros with clean and powerful 
    Python code.

    UDFs: Write User Defined Functions (UDFs) in Python 
    (Windows only).

Numpy arrays and Pandas Series/DataFrames are fully supported. 
xlwings-powered workbooks are easy to distribute and 
work on Windows and Mac.

https://docs.xlwings.org/en/latest/index.html

To understand the primary Task and calculating algorithm 
please GOTO: 

https://github.com/oglinked/balance/blob/main/task.txt
"""

import xlwings as xw
import pandas as pd
import inputvalid as iv
import os

message_cyrillic = 'No cyrillic letters are allowed in this field!'


def choose_path(file_extension=".csv"):
    """Choosing file with dedicated extention in current directory
    and getting relative path to it.
    """
    files_number = len(list_files(file_extension))
    if files_number >= 2:
        print(f'\nThere are {files_number} {file_extension} files in \
current directory.\n')
        for i, file in enumerate(list_files(file_extension), start=1):
            print(i, '\t', file)
        k = input(f'\nInput the file ordinal number you are going \
to work with. \nPlease get the number in [1, {files_number}]: ')
        k = valid_index_input(k, files_number)  # Validation.
        # k  <class int>
        file_path = './' + list_files(file_extension)[k-1]
    elif files_number == 1:
        file_path = './' + list_files(file_extension)[0]
    else:
        input(f'\nError: No {file_extension} files in current directory! \
              \nPlease upload {file_extension} file you are going to \
work with in current directory. \nPress "ENTER" to continue: ')
        file_path = choose_path(file_extension)  # Recursion.
    return file_path


def list_files(file_extension=".csv"):
    """Returns all files with specific extension
    in current directory as a list.
    """
    list_f = []
    for file in os.listdir(r'./'):
        # Checking the files with specific extension.
        if file.endswith(file_extension):
            list_f.append(file)
    return list_f


def valid_index_input(number, max_number, min_number=1):
    """Index input validation."""
    number = iv.test_cyr_tabs_whitespaces(number, message_cyrillic)
    # Validation.
    number = iv.number_validation(number, max_number, min_number)
    number = int(number)
    return number


def cell_coordinates_validation(cell, required_letter='I'):
    """Cell's coordinates first letter validation function
    for excel.
    """
    cell = iv.test_cyr_tabs_whitespaces(cell, message_cyrillic)
    if cell[0] in [required_letter.upper(),
                   required_letter.lower()]:
        pass
    else:
        print(f'Error: First part of your input should be \
"{required_letter}".')
        cell = input('Repeat input: ')
        # Recursion:
        cell = cell_coordinates_validation(cell, required_letter)
    return cell.upper()


def balance():
    """balance.py function."""
    os.system('cls')  # Clearing the Screen.
    # The Greeting & information.
    print('\nHello Host!\nYou run version 04.08 of \
the program balance.py.')

    file_path = choose_path('.xlsx')
    print('\nFull Path to your .xlsx file is: \n'
          + os.path.abspath(file_path)
          + '\n')

    # Getting sheet name (sh_name) to work with:
    sheet_list = pd.ExcelFile(file_path).sheet_names
    sh_name = iv.choose_item('Sheets', sheet_list)
    # sh_name = 'Transfers'  # Default.

    # The getting maximum index of rows to evaluate:
    df = pd.read_excel(file_path, sheet_name=sh_name,
                       header=None)
    row_max = str(df.shape[0])

    # The getting index of row to start with:
    row_min = str(13)  # Default.

    # Interacting with Excel from xlwings:  # !!
    # wb = xw.Book()  # This will open a new workbook.
    wb = xw.Book(file_path)  # Connecting to a file that is open
    # or in the current working directory.
    sheet = wb.sheets[sh_name]  # Instantiates a sheet object.

    # The main loop:
    k = 'continue'
    while k != 'q':
        # Column I:
        # Inputing target cell's coordinates:
        cell = input('Input cell coordinates in "I" column \
to count cell\'s value: ')
        # Validation:
        cell = cell_coordinates_validation(cell, 'I')

        # Column H:
        # Getting corresponding H cell coordinates and it's value.
        h_corresponding_cell = f'H{cell[1:]}'
        h_cell_value = sheet[h_corresponding_cell].value

        # Column B:
        # Getting iterable list in "B" column.
        column = sheet[f'B{str(row_min)}: B{str(row_max)}'].value

        # Calculating target item occurrences in item_list for "B" column.
        namber_occurrences_b = column.count(h_cell_value)

        # Getting occurrences' list (index_list) in "B" column.
        item = h_cell_value
        index_list = [i+int(row_min) for i in range(len(column))
                      if column[i] == item]

        # Column D:
        d_corresponding_cell = [f'D{str(index_list[i-1])}' for i in
                                range(len(index_list))]

        # Column L:
        # Getting iterable list in "L" column.
        column = sheet[f'L{str(row_min)}: L{str(row_max)}'].value

        # Calculating target item (h_cell_value) occurrences
        # in item_list for "L" column.
        namber_occurrences_l = column.count(h_cell_value)

        # Getting occurrences' list (index_list) in "L" column.
        item = h_cell_value
        index_list = [i+int(row_min) for i in range(len(column))
                      if column[i] == item]

        # Column N:
        n_corresponding_cell = [f'N{str(index_list[i-1])}'
                                for i in range(len(index_list))]

        # Formula: =cell_befor+SUM(D)-SUM(N)
        cell_befor = cell[0]+str(int(cell[1:])-1)

        sum_d = '+'.join(d_corresponding_cell)

        sum_n = '-'.join(n_corresponding_cell)  # !! Not really sum!

        if namber_occurrences_b >= 1 and namber_occurrences_l >= 1:
            cell_formula = f'={cell_befor}+{sum_d}-{sum_n}'
        elif namber_occurrences_b >= 1 and namber_occurrences_l < 1:
            cell_formula = f'={cell_befor}+{sum_d}'
        elif namber_occurrences_b < 1 and namber_occurrences_l >= 1:
            cell_formula = f'={cell_befor}-{sum_n}'
        elif namber_occurrences_b < 1 and namber_occurrences_l < 1:
            cell_formula = f'={cell_befor}'
        print(f'Now formula in cell "{cell}" is: "{cell_formula}"')

        # Reading/writing values to/from ranges:
        sheet[cell].value = cell_formula
        print(f'"{cell}"value now is: {sheet[cell].value}')

        # The end of the main loop.
        k = input('\nWould you like to fill another cell \
in .xlsx file? \n(Press "q" to exit, or "ENTER" to continue): ')
        k = iv.exit_test(k)  # Validation.

    input('Press "ENTER" to exit balance.py: ')  # Exit.
    return


if __name__ == "__main__":
    balance()
