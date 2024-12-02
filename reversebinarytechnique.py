import math

n = int(input())

def binCon(n):
    bin_num = 0
    pow = 1
    while n>0:
        rem = n%2
        bin_num = bin_num + rem * pow
        n = n//2
        pow *= 10
    reversal(bin_num)

def conBin(n):
    dec_num = 0
    i = 0
    while n>0:
        temp = n%10
        dec_num = dec_num + temp * math.pow(2,i)
        n = n//10
        i+=1
    print(int(dec_num))

def reversal(n):
    line = str(n)[::-1]
    conBin(int(line))

binCon(n)