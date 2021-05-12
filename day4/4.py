f = open("4.txt", "r")
passports = f.read().split("\n\n")

#Part 1
def checkValid(passports):
	valid = 0
	required = {"iyr", "byr", "eyr", "hgt", "hcl", "ecl", "pid"}
	for passport in passports:
		add = True
		for r in required:
			if r not in passport:
				add = False 
		if add:
			valid += 1
	return valid 

print(checkValid(passports))

#Part 2
def checkValid2(passports):
	valid = 0 
	required = {"iyr", "byr", "eyr", "hgt", "hcl", "ecl", "pid"}
	eyes = {"brn", "amb", "blu", "gry", "grn", "hzl", "oth"}
	chars = "abcdef0123456789"
	for passport in passports:
		add = True 
		for r in required:
			if r not in passport:
				add = False 
			else:
				field = passport.split(r+":")[1].split(" ")[0].strip().split("\n")[0]
				if r == "byr":
					try:
						field = int(field)
						if field < 1920 or field > 2002:
							add = False
					except:
						add = False
				if r == "iyr":
					try:
						field = int(field)
						if field < 2010 or field > 2020:
							add = False
					except:
						add = False
				if r == "eyr":
					try:
						field  = int(field)
						if field < 2020 or field > 2030:
							add = False
					except:
						add = False
				if r == "hgt":
					try:
						num = int(field[:-2])
					except:
						add = False
						break
					if field[-2:] == "cm":
						if num < 150 or num > 193:
							add = False
					elif field[-2:] == "in":
						if num < 59 or num > 76:
							add = False
					else:
						add = False
				if r == "hcl":
					num, field = field[0], field[1:]
					if num != "#" or len(field)!=6:
						add = False 
					for i in field:
						if i not in chars:
							add = False
				if r == "ecl":
					if field not in eyes:
						add = False
				if r == "pid":
					if len(field)!=9:
						add = False 
					try:
						field = int(field)
					except:
						add = False
		if add:
			valid += 1
	return valid

print(checkValid2(passports))