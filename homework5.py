total = 0
count = 0
while True:
    number = raw_input("Enter a number: ")
    if number == 'done':
        print "Sum: ", total, '\n', "Count: ", count, '\n', "Average: ", (total / count)
        break
    else:
        try:
            total += float(number)
            count += 1
        except:
            print "Invalid input"
