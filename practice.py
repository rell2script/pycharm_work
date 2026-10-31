sum_even=0
sum_odd=0

numbers = [40, 45, 66, 70, 90]
for number in numbers:
    if number %2 == 0:
        sum_even=sum_even+number
else :
    sum_odd=sum_odd+number
print(sum_even)
print(sum_odd)




