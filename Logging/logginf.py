from datetime import timedelta
log = []
with open('logfile.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        s = [elem.strip() for elem in line.split(',')]
        log_in = [int(i) for i in s[1].split(':')]
        log_out = [int(i) for i in s[2].split(':')]
        delta = str(timedelta(hours=log_out[0], minutes=log_out[1]) -  timedelta(hours=log_in[0], minutes=log_in[1])).split(':')[0]
        log.append(( s[0], delta ))
with open('output.txt', 'w', encoding='UTF-8') as file:
    print(*[elem[0] for elem in filter(lambda x: int(x[1]) >= 1, log)], sep='\n', file=file)