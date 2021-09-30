f = open("4.txt", "r")
passports = [i.strip() for i in f.read().split("\n\n")]

#Part 1
def checkValid(passports):
	valid = 0
	totalFields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}
	for passport in passports:
		passport = ' '.join(passport.split("\n"))
		fields = passport.split(" ")
		categories = [i.split(":")[0] for i in fields]
		if len(categories) == 8 or len(categories) == 7 and "cid" not in categories:
			valid += 1
	return valid

#Part 2
def checkValid2(passports):
	valid = 0
	for passport in passports:
		passport = ' '.join(passport.split("\n"))
		fields = passport.split(" ")
		categories = [i.split(":")[0] for i in fields]
		if len(categories) == 8 or len(categories) == 7 and "cid" not in categories:
			if checkPassport(fields):
				valid += 1
	return valid

def checkPassport(fields):
	eyes = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
	for field in fields:
		cat, value = field.split(":")
		if cat == "byr":
			try:
				year = int(value)
				if year < 1920 or year > 2002:
					return False
			except:
				return False
		if cat == "iyr":
			try:
				year = int(value)
				if year < 2010 or year > 2020:
					return False
			except:
				return False
		if cat == "eyr":
			try:
				year = int(value)
				if year < 2020 or year > 2030:
					return False
			except:
				return False
		if cat == "hgt":
			num, label = value[:-2], value[-2:]
			try:
				num = int(num)
			except:
				return False
			if label == "in":
				if num < 59 or num > 76:
					return False
			elif label == "cm":
				if num < 150 or num > 193:
					return False
			else:
				return False
		if cat == "hcl":
			if value[0] != "#":
				return False
			if not value[1:].isalnum():
				return False
		if cat == "ecl":
			if value not in eyes:
				return False
		if cat == "pid":
			if not (len(value) == 9 and value.isnumeric()):
				return False

	return True


print(checkValid(passports))
print(checkValid2(passports))