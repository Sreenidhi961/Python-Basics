sentence=input("Enter sentence")
count={}
for ch in sentence:
    if ch!=" ":
        if ch in count:
            count[ch]=count[ch]+1
        else:
            count[ch]=1
print(count)
