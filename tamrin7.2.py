import re
def capital_space(word):
    words = re.findall(r'[A-Z][^A-Z]*', word)
    res = ''
    for word in words:
        res += word + ' '
    
    return res

print(capital_space('TheFirstProgrammingBootcamp'))