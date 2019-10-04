# File: goldenRatioCalc.py
# This file estimates the Golden Ratio by averaging the ratios n/(n-1) for the first n terms of the Fibonacci sequence

def main():
  print("This program estimates the Golden Ratio using the first n terms of the Fibonacci sequence")
  n = eval(input("Enter a value for n: "))
  x = 1
  y = 1
  ratSum = 1
  for i in range(n):
    z = x + y
    x = y
    y = z
    ratyx = y / x
    ratSum = ratSum + ratyx
  goldenRatio = ratSum / n
  print("The Golden Ratio equals:", goldenRatio)

main()
