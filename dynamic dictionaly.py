students={}
num_students=int(input("Enter number of students:"))
for i in range(num_students):
    print(f"\nStudent {i+1}:")
    name=input("Enter student name:")
    num_subjects=int(input("Enter student marks:"))
    marks_dict={}
    for j in range(num_subject):
        subject=input("Enter subject name{j+1} name:")
        marks=float(input("Enter Marks for{subject}:"))
        marks_dict[subject]=marks
        student[name]=marks_dict





print("\n----REPORT CARD----")
for name,subjects in students in students.items():
    print("f/n Student Name:{name}")
    total=sum(subject.values())
    average=total/len(subjets)
    if average>=90:
        grade="A+"
    elif average>=80:
        grade="A"
    elif average>=70:
        grade="B"
    elif average>=60:
        grade="C"
    elif average>=50:
        grade="D"
    else:
        grade="F"
    print("Subject and Marks:")
    for subject,marks in subject.items():
        print(f"{subject}: {marks}")
    print("Total marks"),total
    print("Average marks",round(average,2))
    print("Grade",grade)          
                     
                     
