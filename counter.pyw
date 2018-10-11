filename = "hello.txt"
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