from check_begin_end import check_opening

list_of_words = []
idx = -1
with open("ok.txt", 'r') as file:
    for line_number, line in enumerate(file, start=1):
        words = line.split()
        for word in words:
            if word.lower() in ['begin', 'end']:
                idx += 1
                temp = {
                    "lno": line_number,
                    "word": word,
                    "index": idx
                }
                list_of_words.append(temp)

only_words = [l["word"] for l in list_of_words]
"---call the function---"
c = check_opening()
result = c.check_and_update(list_of_words, "ok.txt")

with open("ok.txt", 'r') as file:
    lines = file.readlines()
    for item in result:
        beg_end_tup = (item["begin_lno"], item["end_lno"])
        new_begin = f"{lines[beg_end_tup[0]-1]}{item['number']}"
        new_end = f"{lines[beg_end_tup[1]-1]}{item['number']}"

        lines[beg_end_tup[0]-1] = lines[beg_end_tup[0]-1].replace(lines[beg_end_tup[0]-1], new_begin)
        lines[beg_end_tup[1]-1] = lines[beg_end_tup[1]-1].replace(lines[beg_end_tup[1]-1], new_end)

with open("result.txt", 'w') as file:
    file.writelines(lines)

print("DONE")