import re

volume_title_pattern = re.compile(r'第[0-9零一二三四五六七八九十百千万两]+卷')
volume_section_title_pattern = re.compile(r'第[0-9零一二三四五六七八九十百千万两]+卷.*第[零一二三四五六七八九十百千万]+章.*')
section_title_pattern = re.compile(r'第[0-9零一二三四五六七八九十百千万两]+章[ ].*')

current_volume = ''
counter = 0
# Load and read a txt file from .data/input/剑来.txt
with open('.data/input/剑来.txt', 'r', encoding='utf-8') as input_file:
    for line in input_file:
        line_text = line.strip()
        if (volume_section_title_pattern.match(line_text)):
            counter += 1
            print(str(counter) + ' ' + line_text)
        # elif volume_title_pattern.match(line_text):
        #     current_volume = line_text
        #     print(current_volume)
        elif section_title_pattern.match(line_text):
            # print(current_volume + ' ' + line_text)
            counter += 1
            print(str(counter) + ' ' + line_text)
        else:
            continue
        
