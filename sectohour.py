seconds=int(input("Enter seconds:"))
hours=seconds//3600
minutes=(seconds%3600)//60
remaining_sec=seconds%60
print(f"Hours:{hours} Minutes:{minutes} Seconds:{remaining_sec}")
