#functions and variables.


name = str(input("Enter your name: "))
career = str(input("Enter your career: "))

#remove white space from string
name = name.strip()

#capitalize name
name = name.capitalize()

#capitalize and strip at the same time.
location = input("Enter address: ").strip().title()

print("Hello", name)
print("I am a proud", career)
print(location)
