import matplotlib.pyplot as plt
days= ["Mon","Tue","Wed","Thur","Fri","Sat","Sun"]
sales=[1,2,3,4,5,6,7]
plt.bar(days,sales)

plt.xlabel("Days")
plt.ylabel("Sales")

plt.show()