stock=50
reorder_level=10
while stock>0:
    sold = int(input("Enter units sold today (-1 to stop:"))
    if sold == -1:
         print("Exiting inventory system.")
         break
        stock-=sold
        if stock<0:
            stock=0

    print("Remaining stock:{stock}")
    if 0<stock<=reorder_level:
        print("Recordered level. Stock is low")
    if stock == 0:
        print("Out of Stock")
        
             
