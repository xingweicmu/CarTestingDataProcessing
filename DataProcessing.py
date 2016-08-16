def check_current(current):
	# Currently to check if the car is running, we simply check if 
	# any of 12th and 12th value in current_line is not 0. More accurate
	# calculation or constraints could be added here later on.
	if current == '0':
		return False
	return int(current.split(',')[11]) != 0 or int(current.split(',')[12]) != 0


def check_prev(pre_line):
	if prev_line == '0':
		return False
	return int(prev_line.split(',')[11]) == 0 and int(prev_line.split(',')[12]) == 0


with open("./8.28/8.28/0828.txt") as f:

	count = 0
	prev_line = '0'
	current_line = '0'
	file_to_write = open("./result/0", "a+")

	for line in f:
		# Skip Time
		if line.startswith('"'):
			continue

		# Prepare Data 
		next_line = line

		# Count the starting and open file to get ready to write.
		# The car is starting if and only if
		# 12th and 13th value in prev_line are both 0 (check_prev returns true)
		# and any of 12th and 13th value in current_line is not 0 (check_current return true)
		if check_prev(prev_line) and check_current(current_line):
			count = count + 1
			# Open the file
			file_to_write = open("./result/"+str(count), "a+")
			print "open file "+ str(count)

		# Check if the car is running
		# The car is running if any of 12th and 12th value in current_line is not 0 (check_current return true)
		if check_current(current_line):
			# Write 12, 13 and 18 to file
			file_to_write.write(current_line.split(',')[11] + ' ' + current_line.split(',')[12] + ' ' + current_line.split(',')[17] + "\n")

		# Get ready for reading next line
		prev_line = current_line
		current_line = next_line

	# handle last next_line
	if int(next_line.split(',')[12]) != 0:
		file_to_write.write(current_line.split(',')[11] + ' ' + current_line.split(',')[12] + ' ' + current_line.split(',')[17] + "\n")



