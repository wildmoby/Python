input_filename = raw_input("Enter input file: ")
output_filename = raw_input("Enter output file: ")

count = 0
total = 0

input_filehandle = open(input_filename)
output_filehandle = open(output_filename, 'w')

for line in input_filehandle:
    if line.startswith('X-DSPAM-Confidence: '):
        spacePos = line.find(" ")
        total += float(line[spacePos::1])
        count += 1
        output_filehandle.write(line)
print "Average spam confidence: ", (total / count)

output_filehandle.close()