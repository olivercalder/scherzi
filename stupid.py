import sys

def sort_string(string):
    charlist = []
    for char in string:
        charlist.append(char)
    charlist.sort()
    sortedString = ''
    for c in charlist:
        sortedString = sortedString + c
    return sortedString

def main():
    sentence = []
    for i in range(1, len(sys.argv)):
        sentence.append(sys.argv[i])
    for j in range(len(sentence)):
        sentence[j] = sort_string(sentence[j])
    sentence.sort()
    print()
    for word in sentence:
        print('{} '.format(word), end='')
    print('\n')

main()
