def number_to_words(n):
    if n < 20:
        return ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"][n]
    elif n < 100:
        return ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"][n//10] + ("" if n % 10 == 0 else "-" + number_to_words(n % 10))
    elif n < 1000:
        return number_to_words(n//100) + " hundred" + ("" if n % 100 == 0 else " and " + number_to_words(n % 100))
    else:
        return "one thousand"


print("The total number of letters used:", sum([len(number_to_words(
    i).replace(" ", "").replace("-", "")) for i in range(1, 1001)]))
