# variables
name = "Mukesh"
age = 40
is_project_manager = True
salary= 3500000
skills = ["Python","AI", "Azure"]

# Print Variables

print(name, age,is_project_manager,salary)
print(type(name))
print(type(age))
print(type(is_project_manager))
print(type(salary))
print(type(skills))

x= 10
if x>5:
    print("X is greater")
else:
    print("X is smaller")

for i in range(x-5):
    print (i)

reviews = ["This is great!", "I hate it", "Average product"]  
for review in reviews:  
    if "great" in review or "good" in review:  
        print(f"Positive: {review}")  
    else:  
        print(f"Negative: {review}") 