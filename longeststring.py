def longest(s1, s2):
    return ''.join(sorted((set(s1+s2))))

#Sets are distinct values
#''.join -- concatenate to string with 'join'

print(longest("aasdfasdflkj", "asdfjgreitr"))