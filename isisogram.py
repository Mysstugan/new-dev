def is_isogram(string):
    mystr = string.lower()
    letter_list = []
    for letter in mystr:
        if letter.isalpha():
            if letter in letter_list:
                return False
            letter_list.append(letter)
    return True


print(is_isogram("Hhej"))

#bättre lösning

'''
def is_isogram(string):
    string = string.lower()
    for letter in string:
        if string.count(letter) > 1: return False
    return True
                '''


#bästa lösningen

'''
    def is_isogram(string):
    return len(string) == len(set(string.lower()))
                                                    '''
