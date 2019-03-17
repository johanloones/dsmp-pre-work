# --------------
# Code starts here

# Create the lists 
class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio' ]
class_2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']

# Concatenate both the strings
new_class = (class_1 + class_2)
print (new_class)


# Append the list
new_class.append('Peter Warden')

# Print updated list
print(new_class)


# Remove the element from the list
new_class.remove('Carla Gentry')

# Print the list
print(new_class)

# Code ends here


# --------------
# Code starts here
#Task 2 - Create dictionary for Geoffery Hinton

# Create the dictionary 
courses={'Math':65, 'English':70, 'History':80,'French':70,'Science':60}

# Print all the marks
print(courses)

# Add and save all marks in total
total=sum(courses.values())

# Print total
print(total)

# Calculate percentage
percentage=total/500 *100

# Print percentage
print(percentage)

# Code ends here


# --------------
# Code starts here

#Task 3 - Create dictionary for Highest marks

# Create the dictionary 
mathematics={'Geoffrey Hinton':78, 'Andrew Ng':95, 'Sebastian Raschka':65,'Yoshua Benjio':50,'Hilary Mason':70,'Corinna Cortes':66,'Peter Warden':75}

# Calculate max value
topper=max(mathematics,key=mathematics.get)
print(topper)

# Code ends here  


# --------------
# Given string
topper = 'andrew ng'


# Code starts here

# Storing the first_name
first_name=topper.split()[0]
print(first_name)
#Storing last_name
last_name=topper.split()[1]
print(last_name)
# full_name
full_name=last_name + ' ' +first_name
print(full_name)
# certificate_name
certificate_name=full_name.upper()
print(certificate_name)
# Code ends here


