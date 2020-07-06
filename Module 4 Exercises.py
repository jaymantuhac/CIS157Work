#Chapter 9 Exercise 9
def is_palindrome(string):
    reverse = string[::-1]
    return string == reverse

print(is_palindrome('racecar'))
print(is_palindrome('hello'))

#Chapter 9 Exercise 18
def find(astring, achar): #NOTE: Function modified from section 9.17 of the book
    """
    Find and return the index of achar in astring.
    Return None if achar does not occur in astring.
    """
    ix = 0
    found = False
    while ix < len(astring) and not found:
        if astring[ix] == achar:
            found = True
        else:
            ix = ix + 1
    if found:
        return ix
    else:
        return None

def message_encryptor(string, mapping):
    message = string.lower()
    lock = 'abcdefghijklmnopqrstuvwxyz'
    encryption = mapping.lower()
    index = 0
    encrypted = ''
    for character in message:
        if character not in lock: #Case when character is not a letter
            encrypted += character #append a space to the new string
        else:
            mapping_index = find(lock, character) #Pull index of letter from the key
            mapped_letter =  encryption[mapping_index] #Pull letter from encryption
            encrypted += mapped_letter #Append letter onto the final string
    return encrypted

key = 'QWERTYUIOPASDFGHJKLZXCVBNM'
print(message_encryptor('cat', key))
print(message_encryptor("But it's okay because this is a seaplane", key)) #Animal Crossing reference :D

#Chapter 10 Exercise 6
def sum_of_squares(xs):
    total = 0
    for num in xs:
        total += (num ** 2)
    return total

print(sum_of_squares([2, 3, 4]))
print(sum_of_squares([1,2,3,4,5,6,7,8,9,10]))

#Chapter 10 Exercise 11
def sumUntilEven(xs):
    total = 0
    for number in xs:
        if number % 2 == 0:
            break
        else:
            total += number
    return total

print(sumUntilEven([1,2,3,4,5]))
print(sumUntilEven([1,3,5,7,9]))
print(sumUntilEven([2,4,6,7,9]))
