"""
python program to detect an armstrong number.An armstrong number is that number
whose sum of its own digit each raised to the power of number of digits
Example -:  153 (1^3 + 5^3 + 3^3 = 153) or 407 or 370
"""

num = input("Enter your number : ")
list = []
list.extend(num)

list2=[]
for n in list:
    n1 = int(n)**3
    list2.append(n1)

total=0
for n in range(len(list2)):
    total = total+list2[n]

if str(total) == num : print(f"yes {num} is an armstrong number")
else : print(f"No {num} is not an armstrong number")


