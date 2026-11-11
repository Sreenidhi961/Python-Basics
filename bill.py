item1=int(input("Enter 1st item price:"))
item2=int(input("Enter 2nd item price:"))
item3=int(input("Enter 3rd item price:"))
originalTotal=item1+item2+item3
gst=(originalTotal)*0.05
finalPrice=originalTotal+gst
print(f"Original Total Price:{originalTotal} GST:{gst} Final Price:{finalPrice}")
