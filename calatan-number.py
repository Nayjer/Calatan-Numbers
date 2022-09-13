"""
Can calculate Calatan Numbers on two different ways (with faculty and with sums)
& writes the explicit sums with values in a txt-file
See for proof https://medium.com/@Nayjer/gau%C3%9Fsche-summenformel-anders-betrachtet-af57d48d8e8e
"""


def numerator(x):
    num = 1
    for i in range(2, x + 1):
        num *= (x + i)
    return num


def denominator(x):
    den = 1
    for i in range(1, x):
        den *= i
    return den


def G(x):
    return numerator(x) / denominator(x)


"""
----------------------------------------------------------------
"""


def iterator_string(s, n=1):
    n -= 1
    number_strings = s.split("+")
    s = ""
    for number_string in number_strings:
        for i in range(1, int(number_string)+1):
            s += (str(i) + " + ")
    for i in range(3):
        s = s[:-1:]
    if n == 1:
        return s
    else:
        return iterator_string(s, n)


def calculate_string(x):
    string = ""
    for i in range(1, x+1):
        string += str(i) + " + "
    for i in range(3):
        string = string[:-1:]
    return iterator_string(string, x)


data = open("values.txt", "w")
for i in range(2, 6):
    value = calculate_string(i)
    data.write(value+ " = " + str(eval(value)) + " \n")
data.close()
