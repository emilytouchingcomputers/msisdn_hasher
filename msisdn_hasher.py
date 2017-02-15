#Generates a SHA2 hash table for all MSISDN's
#example output: 277939637 565e98c5ce2a20fca63194f28ef4493829cce6ea08b3118d6e6e87963f676c04
#based off of valid area codes from here: http://www.allareacodes.com/area-code-list.php?pdf=by_number
import hashlib
file = open('/Users/username/Desktop/areacodes.txt')
for line in file:
	areacode = line
	fullcode = (int(areacode) * 10000000)
	code_range = (fullcode + 9999999)
	for msisdn in range(fullcode, code_range):
		hash_object = hashlib.sha256(str(msisdn))
		print(str(msisdn) + " " + hash_object.hexdigest())