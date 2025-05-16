my_dict = {}
n = int(input("Enter number of students you want to register: "))

for i in range(n):
    key = input(f"Enter name of student {i+1}: ")
    value = input(f"Enter the marks obtained by '{key}': ")
    my_dict[key] = value

print("Your dictionary:", my_dict)

def find(key):
    if key in my_dict:
        print(f"Marks obtained by '{key}' are: {my_dict[key]}")
    else:
        print(f"'{key}' is not registered.")


find_key = input("Enter the name of the student to find their marks: ")
find(find_key)
