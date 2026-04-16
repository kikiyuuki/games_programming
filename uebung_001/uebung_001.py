#region summe aller Zahlen von 432 bis 32482
sum = 0

for i in range(432, 32483):
    sum += i
print("Die Summe beträgt:", sum)
#endregion


def rechner():
    a = float(input("Geben Sie die erste Gleitkommazahl ein: "))
    b = float(input("Geben Sie die zweite Gleitkommazahl ein: "))
    if a > b:
        ratio = a / b
        return ratio
    elif b > a:
        ratio = b / a
        return ratio
    elif a == b:
        return 1
    
print("Der Quotient beträgt:", rechner())