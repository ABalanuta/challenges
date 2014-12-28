import os
import sys
import sys

def fit(array, bus_length):

	pos = 0
	bucket = 0
	while pos < len(array):
		if array[pos]+bucket == bus_length:
			pos += 1
			bucket = 0
		
		elif array[pos]+bucket > bus_length:
			return False

		else:
			bucket += array[pos]
			pos += 1

	if bucket == 0:
		return True
	else:
		return False

if __name__ == "__main__":
	lines = sys.stdin.readlines()
	n = int(lines[0])
	a = map(int, lines[1].split())

	min_bus_len = 1
	max_bus_len = sum(a)

	#print min_bus_len, max_bus_len

	#array that will store the possible bus lengths
	bus_lenghts = []

	for l in range(min_bus_len, max_bus_len):

		#Exclude bus length if cannot fit the biggest group
		if max(a) > l:
			continue

		#Excludes if the groups do not fit exactly the bus
		elif not fit(a, l):
			continue

		else:
			bus_lenghts.append(l)

	bus_lenghts.append(max_bus_len)

	for l in bus_lenghts:
		print l,
