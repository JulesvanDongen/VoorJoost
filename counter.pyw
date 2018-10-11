# Suppose you want two counters: one for wins, and one for losses.
# You could then rename this file to wins, copy it, and rename the copy to losses.
# Then you can run each individual script to increment each individual text counter.

k = __file__.rfind('.')
filename = __file__[:k] + ".counter"
count = 0

try:
	file = open(filename, "r+")
except FileNotFoundError:
	file = open(filename, "w+")

try:
	count = int(file.read())
	count += 1
	file.close()
except ValueError:
	pass

file = open(filename, "w")
file.write(str(count))
