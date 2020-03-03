import os
import os.path
import re

all_dic = os.listdir()

print(all_dic)

nah = 0
for f in all_dic:
    nah += 1

kek=0
blankTXT = ''
for f in all_dic:
    kek+=1
    #print(all_dic[1])
    #print(kek)
    textfiles = open(all_dic[kek], 'r', encoding='utf-8')
    for line in textfiles:
        if not line.strip(): continue
        x = re.sub(r'^((?!p id\=).)*$', r'', line)
        x = re.sub(r'(<).*?(>)', r'', x)
        x = re.sub('&quot;', r'', x)
        x = re.sub('&nbsp;', r'', x)
        x = re.sub(r'✴.*', r'', x)
        x = re.sub(r'(    )(.*?)', r'', x)
        x = re.sub(r'^(?:[\t ]*(?:\r?\n|\r))+', r'', x)

        blankTXT += x
    
    blankTXT += "\n"
    

    f=open('outputBook.txt', 'w', encoding='utf-8')
    f.write(blankTXT)
    f.close()
textfiles.close()
    #print(kek)

