

i = 0
k = 0
j = 0

def get_spaces(a):
    n = a.index('<')
    #print('длина пробела', len(a[0:n]))
    return '  ' * len(a[0:n])


def get_tags(a):
    global i
    global j
    global k
    n = a.index('<')
    m = a.index('>')
    tags = ['td', 'tr', 'dd']
    #print ('ВАША СТРОКА', a)
    #print('Новая строка', a[n+1: m])
    if (str(a[n + 1:m]) in tags) and (len(a[0:n+1]) == 2 or len(a[0:n+1]) == 1):
        if a[n + 1:m] in 'td':
            tags += 'td' + str(i)
            i += 1
            #print('i=',i)
            #print(tags)
            return a[n + 1:m] + str(i) + ':'
        if a[n + 1:m] in 'tr':
            k += 1
            #print('k=',k)
            tags += 'tr' + str(k)
            #print(tags)
            return a[n + 1:m] + str(k) + ':'
        if a[n + 1:m] in 'dd':
            j += 1
            tags += 'dd' + str(j)
            #print(tags)

            return a[n + 1:m] + str(j) + ':'
    else:
        return a[n + 1:m] + ':'


def get_value(a):
    n = a.index('<')
    m = a.index('>')
    if a[m+1::] == '' and a[n + 1:m] == 'i':
        return "''"
    return a[m+1::]


def correct(a):
    if "</" not in a:
        return True


def reading():
    test = open('test.txt', 'w')
    with open('xml.txt', 'r') as xml:
        cnt = 0
        for line in xml:
            spaceline = line
            line = line.strip()
            #print(line)
            cnt += 1
            #print(cnt)
            if correct(line):
                test.write(get_spaces(spaceline) + get_tags(line) + ' ' + get_value(line) + '\n')
            else:
                continue
    test.close()


reading()


import xml_parser

with open('xml.txt', 'r', encoding='utf-8') as in_, \
      open('test2.txt', 'w+', encoding='utf-8') as out:
    a = xml_parser.parse(in_)
    xml_parser.to_yaml(a, out)
