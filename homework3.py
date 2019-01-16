hours = int(input('How many hours did you work? '))
rate = int(input('What is your hourly rate? '))

if hours <= 40 :
    print ("pay = " +str(hours * rate))
elif hours > 40 :
    print ("overtime pay = " +str(rate * 1.5 * (hours - 40) + (40 * rate)))
