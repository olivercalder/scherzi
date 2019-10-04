import sys

def round_down_to_election(year):
    return (year // 4 * 4)

def round_up_to_election(year):
    return (year + (4 - year%4)

def calc_year(birth):
#    return (round_down_to_election(birth + 18) + 4)
    return (birth + 21 - ((birth + 21) % 4))

def test_cases():
    for y in range(1996, 2005):
        print('Birth: {}  Vote: {}'.format(y,calc_year(y)))

def main():
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            year = int(sys.argv[i])
            print('Birth: {}  Vote: {}'.format(year,calc_year(year)))
    else:
        test_cases()

main()
