from os import path
import re


def open_graphical():
    with open('graphical.txt', 'r', encoding='utf-8') as f:
        graphical = f.read()

    graphical_lists = graphical.split('\n')
    return graphical_lists



def is_file(txt):
    dir_path = r'/usr/lib/systemd/system/'
    file_path = dir_path + txt
    if path.isfile(file_path):
        return file_path
    else:
        False

def look_for_expross(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        txt = f.read()
        txt_lists = txt.split('\n')
        for txt_list in txt_lists:
            if 'Description' in txt_list:
                prog = re.compile('=(.*)')
                result = prog.match(txt_list)
                return txt_list



def start():
    with open('graphicalcomplass', 'w', encoding='utf-8') as f:
        table = str.maketrans('● ├─│└', '      ')
        graphical_lists = open_graphical()
        for graphical in graphical_lists:
            if 'target' in graphical:
                graphical = graphical + '\n'
                f.write(graphical)
                continue
            grap = graphical.translate(table)
            grap = grap.strip()
            # print(grap)
            file_path = is_file(grap)
            if file_path:
                txt_list = look_for_expross(file_path)
                graphical = graphical + '   ####    '  + txt_list + '\n'
                f.write(graphical)




if __name__ == '__main__':
    # file_path = is_file('zram.service')
    # look_for_expross(file_path)
    # str = 'Description=Service enabling compressing RAM with zRam'● ├─
    # prog = re.compile('=(.*)')
    # result = prog.match(str)
    # print(result[0])
    start()