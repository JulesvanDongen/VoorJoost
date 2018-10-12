# Suppose you want two counters: one for wins, and one for losses.
# You could then rename this file to wins, copy it, and rename the copy to losses.
# Don't forget to change the text content
# Then you can run each individual script to increment each individual text counter.

text = "Count:" # Replace this text to insert into a file

k = __file__.rfind('.')
filename = __file__[:k] + ".txt"
count = 0

try:
	file = open(filename, "r+")
except FileNotFoundError:
	file = open(filename, "w+")

try:
	# Load the text
	content = file.read()
	k = content.rfind(' ')
	count = int(content[k:])
	count += 1
	file.close()
except ValueError:
	pass

file = open(filename, "w")
file.write(text + " " + str(count))