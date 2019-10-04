# File: roundCheat.py
# This program uses iterated round commands to round floats less than #.5 up to the next integer

def main():
    n = float(input("Enter a number of any length of the form n.4444[...]44m where m >=5 and [n, m] = R: "))
    l = string.length(n)
    print()
    for i in range(l, n, -1):
        print(i)
        round(n, i)
        print(n)
main()
