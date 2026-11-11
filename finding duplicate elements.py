my_list=[10,20,30,10,40,50,20,30,60]
print("Original List:",my_list)
duplicates=[]
seen=[]
for item in my_list:
    if item in seen and item not in duplicates:
        duplicates.append(item)
    else:
        seen.append(item)
print("Duplicate Elements:",duplicates)
