u=int(input("Enter units consumed:"))
if u<=100:
    b=u*2.50
elif u<=200:
    b=(100*2.50)+((u-100)*4.00)
elif u<=300:
    b=(100*2.50)+(100*4.00)+((u-200)*6.00)
else:
    b=(100*2.50)+(100*4.00)+(100*6.00)+((u-300)*8.00)
print("Bill before discount=",b)
if b>1500:
    d=b*0.05
else:
    d=0
net_b=b-d
if net_b<200:
    net_b=200
print("Units Consumed:",u)
print("Bill Before Discount:",b)
print("Discount:",d)
print("Net Bill:",net_b)
