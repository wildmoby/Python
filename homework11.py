grades = list()

while True:
    firstname = raw_input("First Name: ")
    if firstname == '':
        break
    lastname = raw_input("Last Name: ")
    grade = raw_input("Grade: ")
 

    my_tuple = (grade, lastname, firstname)
    grades.append(my_tuple)

grades.sort()

for grade in grades:
    print '  %-3s %-10s %-10s' % (grade [0], grade[1], grade[2])
  
