res = []
with open('test.txt') as code:    
    prev_line = ''
    for l in code:
        line = l.strip()
        if 'def ' in line and '#' not in prev_line:
            res.append(line[line.find(' ')+1:line.find('(')])
        prev_line = line
if res == []:
    res = ['Best programing team!']

print(*res, sep='\n')