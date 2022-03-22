import pandas as pd

path_txt = '/path/to/txt'

file1 = open(path_txt, 'r') 
lines = file1.readlines()
dicts = list()
for i, line in enumerate(lines):
    if i < 2:
        continue
    parts = line.split(') ')[1].split(' ')
    parts.pop(-1)
    dict_tmp = dict()
    dict_tmp['D_A'] = float(parts[1])
    dict_tmp['G_A'] = float(parts[3])
    dict_tmp['cycle_A'] = float(parts[5])
    dict_tmp['idt_A'] = float(parts[7])
    dict_tmp['D_B'] = float(parts[9])
    dict_tmp['G_B'] = float(parts[11])
    dict_tmp['cycle_B'] = float(parts[13])
    dict_tmp['idt_B'] = float(parts[15])
    dicts.append(dict_tmp)
df = pd.DataFrame(dicts)
