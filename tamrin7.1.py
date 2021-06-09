import re

def counter(word, case_sensitive=False):
    with open('sample.html') as f:
        string = f.read()
        if case_sensitive == True:
            res = re.findall(fr'.*({word}).*', string)
            return len(res)
        else:
            res1 = re.findall(fr'.*({word}).*', string)
            res2 = re.findall(fr'.*({word.upper()}).*', string)
            word = word.lower()
            res3 = re.findall(fr'.*({word}).*', string)
    return len(res1)+len(res2)+len(res3)

def counter_word_html(word, tag):
    with open('sample.html') as f:
        string = f.read()

    mystr = re.findall(fr'<{tag}.*</{tag}>', string)
    res = re.findall(fr'{word}', str(mystr))
    return len(res)


print(counter('Python'))
print(counter('Python',True))


