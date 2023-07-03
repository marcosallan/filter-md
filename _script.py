final_file = open('_final.txt', 'w+')
final_list = list()
file_01 = open('_apoiadores_01.txt', 'r')
file_02 = open('_apoiadores_02.txt', 'r')
file_03 = open('_apoiadores_03.txt', 'r')
file_04 = open('_militancia_go.txt', 'r')
file_05 = open('_tropa_do_joao.txt', 'r')
files_list = [file_01, file_02, file_03, file_04, file_05]
# del lists, conversao num proibidos, add nums, criar function

for file in files_list:
    for i in file:
        aux = i[i.index('-') + 1:len(i)].strip()
        if aux in final_list:
            continue
        final_list.append(aux)

for i, item in enumerate(final_list):
    final_file.write(f'{i + 1} - {item}\n')

files_list.append(final_file)
for file in files_list:
    file.close()
