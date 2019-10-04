#   File: deposits.py
#   By: Oliver Calder, 1 January 2019

'''
This program takes the csv file for all account activity and exports a csv file
with just deposits.
'''


import sys

def get_transactions(csv_file_name):
    transactions = []
    try:
        with open(csv_file_name) as csv_file:
            for row in csv_file:
                transactions.append(row)
        return transactions
    except FileNotFoundError:
        print('\nFile not found in current directory.\n')
        csv_file_name = input('What is the file name of the transaction log?\n(include ".csv" at the end, without quotation marks)\nFile name: ')
        transactions = get_transactions(csv_file_name)
        return transactions

def main():
    if len(sys.argv) != 2:
        print('Usage: python3', sys.argv[0], 'filename.csv')
    csv_file_name = sys.argv[1]
    transactions = get_transactions(csv_file_name)
    outfile = open(csv_file_name.split('.')[0]+'-deposits.csv', 'w')
    for item in transactions:
        if item.split(',')[1][1] == '-':
            print(item, end='', file=outfile)

main()
