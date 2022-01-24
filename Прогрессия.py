a = int(input("Член прогрессии "))
d = int(input("Номер члена прогрессии "))
n = int(input("Разность "))
N=n
while n>0:
    print("a"+str(N-n+a)+" = "+str(a))
    a=+d
    n-=1
