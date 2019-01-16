
  

def get_input_description():
    while True:
        data_input = raw_input("Please Enter a file name: \n") 
        try:
            return open(data_input)
        except:
            print ("Enter a valid file!")
            continue

    
def get_data_list(file_object, column_number):
    stock_data = []
    for lines in file_object:
        if not lines.startswith('Date'):
            different_lines=lines.split(',')
            stock_data.append((different_lines[0], float(different_lines[column_number])))
    return stock_data


def average_data(stock_data):
    mydictionary={}
    for lines in stock_data:
        date,data =lines
        month = date[:7]
        current = mydictionary.get (month,(0,0)) 
        new = (current[0] + 1, current[1] + data)
        mydictionary[month]= new
    averagelist = []
    for month,t in mydictionary.items():
        average = t[1]/t[0]
        averagelist.append((average, month))
    averagelist=sorted(averagelist)
    print ("Lowest 5 for column:")
    for i in averagelist[0:6]:
        print("Date: %s, Value:%s" %(i[1],i[0]))
    print("")
    print("Highest 6 for column:")
    for i in averagelist[-6:][::-1]:
            print("Date: %s, Value: %s" %(i[1],i[0]))

    
def main():
    input_file = get_input_description()
    column = int(raw_input("What column would you like to search for?\n"))
    stock_data = get_data_list(input_file,column)
    average_data(stock_data)    

main()