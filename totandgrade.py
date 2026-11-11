sub1=int(input("Enter marks:"))
sub2=int(input("Enter marks:"))
sub3=int(input("Enter marks:"))
total_marks=sub1+sub2+sub3
total=(sub1+sub2+sub3)/3
print(f"Total marks:{total}")
if 90<=total<=100:
    print("Grade O")
elif 81<=total<=89:
    print("Grade A+")
elif 71<=total<=80:
    print("Grade A")
elif 61<=total<=70:
    print("Grade B+")
elif 51<=total<=60:
    print("Grade B")
elif 41<=total<=50:
    print("Grade c+")
elif 35<=total<=40:
    print("Pass")
else:
    print("Fail")
    
