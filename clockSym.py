# File: clockSym.py
# This program calculates all times when the minute and hour hands of an analog clock are symmetrical about the center axis

def main():
    m = 0
    h = 0
    s = 0
    def printTime(a, b, c):
        print(int(a / 3600), int((b % 43200) / 720), int((c % 43200) / 720))
    for n in range(43200):      # I chose to use 43200 because the hour hand assumes 43200 discrete positions as it moves about the clock face one time
        h = h + 1           # Each second, the hour hand moves 1/43200th of the circumference, while the second hand moves 720/43200ths (1/60th),
        s = s + 720         # and the minute hand moves 12/43200ths (1/3600th)
        m = m + 12
        mtemp = 43200 - (m % 43200)
        if h % 12 < 6:
            hround = (int(h / 12)) * 12
        elif h % 12 >= 6:
            hround = (int(h / 12) + 1) * 12
        if hround == mtemp:
            printTime(h, m, s)
main()
