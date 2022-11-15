
# | [2235](https://leetcode.com/problems/add-two-integers/description/) | [Add Two Integers](/LeetCode/Easy/2235.%20Add%20Two%20Integers/) | [Python](/LeetCode/Easy/2235.%20Add%20Two%20Integers/2235.%20Add%20Two%20Integers.py) | [Facebook](/Facebook/), [Google](/Google/), [Amazon](/Amazon/), [Apple](/Apple/)| Math |  |
# | [2235](https://leetcode.com/problems/add-two-integers/description/) | [Add Two Integers](/LeetCode/Easy/2235.%20Add%20Two%20Integers/) | Hard | [Python](/LeetCode/Easy/2235.%20Add%20Two%20Integers/2235.%20Add%20Two%20Integers.py) | Math |  |

#######################################
#######################################
hardest = 'Easy' #  Medium, Hard
title = '1662. Check If Two String Arrays are Equivalent'
companies = [2, 3] ## '1. Amazon', '2. Apple', '3. Facebook', '4. Google', '5. Microsoft'
url = 'https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/'
topic = ['Array', 'String']
related = ''
#######################################
#######################################
hashmap = {1 : '[Amazon](/Amazon/)', 2 : '[Apple](/Apple/)', 3 : '[Facebook](/Facebook/)', 4 : '[Google](/Google/)', 5 : '[Microsoft](/Microsoft/)'}

title = title.strip()
titleNum = title.split('.')[0]
titleWords = title.split('.')[1].strip()
titlepath = '%20'.join([titleNum + '.'] + titleWords.split(' '))

path1 = '/LeetCode/' + hardest + '/' + titlepath + '/'
path2 = path1 + titlepath + '.py'

sec1 = '| [' + titleNum + ']' + '(' + url + ') '
sec2 = ' [' + titleWords + ']' + '(' + path1 + ') '
sec3 = ' ' + hardest + ' '
sec4 = ' [Python]' + '(' + path2 + ') '
sec5Array = [hashmap[x] for x in companies]
sec5 = ' ' + (', ').join(sec5Array) + ' '
sec6 = ' ' + (', ').join(topic) + ' '
sec7 = ' ' + related + ' |'

overallReadme = '|'.join([sec1, sec2, sec4, sec5, sec6, sec7])
companyReadme = '|'.join([sec1, sec2, sec3, sec4, sec6, sec7])

import os

os.mkdir('LeetCode/' + hardest + '/' + title + '/')
with open('LeetCode/' + hardest + '/' + title + '/' + title + '.py', 'w') as f:
    f.write('# ' + hardest)

def prepend_line(file_name, insertline):
    """ Insert given string as a new line at the beginning of a file """
    # define name of temporary dummy file
    dummy_file = file_name + '.bak'
    # open original file in read mode and dummy file in write mode
    with open(file_name, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        # Read lines from original file one by one and append them to the dummy file
        prev = ''
        insertNum = int(titleNum)
        flag = True
        prev = ''
        for line in read_obj:
            if line[0] == '|' and line[2] == '[' and flag:
                curNum = int(line[3:8].split(']')[0])
                if insertNum < curNum:
                    write_obj.write(insertline + '\n')
                    flag = False
            elif flag and prev and prev[0] == '|' and prev[2] == '[':
                write_obj.write(insertline + '\n')
                flag = False
            prev = line
            write_obj.write(line)
    # remove original file
    os.remove(file_name)
    # Rename dummy file as the original file
    os.rename(dummy_file, file_name)

prepend_line('LeetCode/' + hardest + '/README.md', overallReadme)
# LeetCode/Easy/README.md
hashmap2 = {1 : 'Amazon/', 2 : 'Apple/', 3 : 'Facebook/', 4 : 'Google/', 5 : 'Microsoft/'}
for company in companies:
    comName = hashmap2[company]
    tempPath = comName + 'README.md'
    # Amazon/README.md
    prepend_line(tempPath, companyReadme)

