'''
File: QR_URL_Generator.py
Created by Oliver Calder, 27 November 2018

This program takes a .csv file and appends to it a new column with QR code
URLs based on the code (ie. 1a0000) of the guest.
'''

import csv

def main():
    filename = input('Please input filename (include .csv): ')
    try:
        test = open(filename, 'r')
    except:
        print('File', filename, 'not found in current directory.')
        print('\nPlease try one or more of the following:')
        print('1. Move either this program or the csv file so that they are in the same directory.')
        print('2. Export the Excel file as a .csv file and try again.')
        exit()

    outfilename = str(filename.split('.csv')[0]) + '_with_URLs.csv'
    column = input('Input the letter of the column in which the codes (ie. 1a0000) are stored: ').lower()
    c = ord(column) - ord('a')

    with open(filename,'r') as csvinput:
        with open(outfilename, 'w') as csvoutput:
            writer = csv.writer(csvoutput, lineterminator='\n')
            reader = csv.reader(csvinput)

            all = []
            row = next(reader)
            row.append('QR Code URL')
            all.append(row)

            for row in reader:
                row.append('https://api.qrserver.com/v1/create-qr-code/?size=150x150&data='+row[c])
                all.append(row)

            writer.writerows(all)

main()
