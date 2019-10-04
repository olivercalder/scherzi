import sys
import os

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 isolate_emails.py filename.csv')
        quit()
    else:
        filename = sys.argv[1]
    infile = open(filename, 'r')
    os.system('touch emails.txt')
    outfile = open('emails.txt', 'w')
    for line in infile:
        email = line.split(',')[0]
        print(email, file=outfile)
    outfile.close()

main()
