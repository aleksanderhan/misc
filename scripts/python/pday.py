from datetime import date, timedelta, datetime


formats = {
	'yyyy-mm-dd' : '%Y-%m-%d',
	'dd-mm-yyyy' : '%d-%m-%Y',
	'mm-dd-yyyy' : '%m-%d-%Y'
}


def isPalindrome(dateStr):
	dateStr = dateStr.replace('-', '')
	return dateStr == dateStr[::-1]


def dayGenerator():
	d = date.today()
	dt = timedelta(days=1)
	while True:
		yield d
		d = d + dt


def main():
	dg = dayGenerator()

	while True:
		day = next(dg)

		palDateFormat = []
		for fk, fv in formats.items():
			dateStr = datetime.strftime(day, fv)
			if isPalindrome(dateStr):
				palDateFormat.append(fk)

		if len(palDateFormat) > 0:
			break

	print(f'{day} (yyyy-mm-dd) is the next palindrome date from today on the format(s): {", ".join(palDateFormat)}')




if __name__ == '__main__':
	main()