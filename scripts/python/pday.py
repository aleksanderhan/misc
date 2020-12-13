from datetime import date, timedelta, datetime


formats = {
	'yyyy-mm-dd' : '%Y-%m-%d',
	'dd-mm-yyyy' : '%d-%m-%Y',
	'mm-dd-yyyy' : '%m-%d-%Y'
}


def isPalindrome(dateStr):
	dateStr = dateStr.replace('-', '')
	return dateStr == dateStr[::-1]


def dayGenerator(startDate):
	d = startDate
	dt = timedelta(days=1)
	while True:
		yield d
		d = d + dt


def findNextPalDate(day):
	while True:
		_date = next(day)

		palDateFormat = []
		for fk, fv in formats.items():
			dateStr = datetime.strftime(_date, fv)
			if isPalindrome(dateStr):
				palDateFormat.append(fk)

		if len(palDateFormat) > 0:
			break

	return _date, palDateFormat


def main():
	startDate = date.today()

	i = 0
	while (i := i + 1) <= 10:
		palDate, palDateFormat = findNextPalDate(dayGenerator(startDate))
		print(f"{palDate} (yyyy-mm-dd) is a palindrome date on the format(s): {', '.join(palDateFormat)}")
		startDate = palDate + timedelta(days=1)


if __name__ == '__main__':
	main()