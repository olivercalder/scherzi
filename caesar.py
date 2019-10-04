import sys

def encrypt_conditional(letter, shift):
    i = ord(letter)
    j = i + shift
    print(letter, 'with shift of', shift, 'becomes', chr(j))
    print('Thus, we need to mod it and start back at 97.')
    if j > 122:
        k = j % 123 + 97
    encrypted_letter = chr(k)
    print(letter, 'encrypted with shift of', shift, 'becomes', encrypted_letter)
    print()

def better_encrypt(letter, shift):
    i = ord(letter) - 97
    print('Everything is easier if we put the index in terms of a=0, y=25...')
    print('Thus,', letter, 'is actually', i)
    j = i + shift
    print('That way', letter, 'with shift of', shift, 'becomes', j)
    k = j % 26
    print('Now, without an if-statement, we can ensure that', j, 'loops back to the')
    print('    beginning of the alphabet if it exceeds z, using k = j % 26.')
    l = k + 97
    encrypted_letter = chr(l)
    print('Then, we easily add back the 97 that we subtracted at the beginning.')
    print(letter, 'encrypted with shift of', shift, 'becomes', encrypted_letter)
    print()

def encrypt_letter(letter, shift):
    i = ord(letter) - 97
    j = i + shift
    k = j % 26
    l = k + 97
    encrypted_letter = chr(l)
    return(encrypted_letter)

def encrypt_message(message, shift):
    words = message.split(' ')
    encrypted_message = ''
    for word in words:
        encrypted_word = ''
        for letter in word:
            encrypted_letter = encrypt_letter(letter, shift)
            encrypted_word = encrypted_word + encrypted_letter
        encrypted_message = encrypted_message + encrypted_word + ' '
    return encrypted_message

def main():
    if len(sys.argv) == 1:
        letter = 'x'
        shift = 5
        encrypt_conditional(letter, shift)
        better_encrypt(letter, shift)
    elif len(sys.argv) == 3:
        letter = sys.argv[1]
        shift = int(sys.argv[2])
        encrypt_conditional(letter, shift)
        better_encrypt(letter, shift)
    elif len(sys.argv) > 3:
        shift = int(sys.argv[1])
        message = ''
        for i in range(2, len(sys.argv)):
            message = message + sys.argv[i] + ' '
        message.rstrip()
        encrypted_message = encrypt_message(message, shift)
        print('Original message:')
        print(message)
        print('With shift of {}:'.format(shift))
        print(encrypted_message)
    else:
        print('Usage: python3 {} letter shift'.format(sys.argv[0]))
        print('    OR')
        print('Usage: python3 {} shift words in message ... ...'.format(sys.argv[0]))
        quit()

main()

