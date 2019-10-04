# here's an idea: This
from PIL import Image

def getRuleDict(rule):
    digits = bin(rule)[2:].zfill(8)
    ruleDict = {tuple(int(bin(i)[2:].zfill(3)[j]) for j in range(3)):int(digits[7-i]) for i in range(8)}
    return ruleDict

def genRow(ruleDict, prev):
    return [ruleDict[(prev[(i-1)%len(prev)], prev[i], prev[(i+1)%len(prev)])] for i in range(len(prev))]

def processSSV(st):
    return tuple(int(st.split(" ")[i]) for i in range(len(st.split(" "))))

def bin2dListToImage(lsts, colors):
    w, h = len(lsts[0]), len(lsts)
    im = Image.new("RGB", (w, h))
    pix = im.load()
    for x in range(w):
        for y in range(h):
            pix[x, y] = colors[lsts[y][x]]
    return im

def main():
    colors = [processSSV(input("Enter {} color as rgb values separated by spaces: ".format(i))) for i in range(2)]
    ruleDict = getRuleDict(int(input("Enter a rule number: ")))
    result = [list(processSSV(input("Enter a starting state as binary digits separated by spaces: ")))]
    for i in range(1, int(input("How many rows to compute? "))):
        result.append(genRow(ruleDict, result[i-1]))
    bin2dListToImage(result, colors).show()

main()
