def find_first_digit(line, digits):
    minind=len(line)
    firstdigit=""
    for digit in "123456789":
        ind=line.find(digit)
        if ind>=0 and ind<minind:
            minind=ind
            firstdigit=int(digit)
    for text, digit in digits.items():
        ind=line.find(text)
        if ind>=0 and ind<minind:
            minind=ind
            firstdigit=digit
    return firstdigit
    
res=0
fname="day1_input.txt"
digits_to_num={"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
digits_to_num_rev={key[::-1]: val for key, val in digits_to_num.items()}
with open(fname) as inputfile:
    for line in inputfile:
        line=line.strip()
        res+=10*find_first_digit(line, digits_to_num)+find_first_digit(line[::-1], digits_to_num_rev)
print(res)