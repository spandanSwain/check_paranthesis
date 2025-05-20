with open("test.txt", 'r') as file:
    lines = file.readlines()

print(len(lines))
if len(lines) >= 12:
    if "thisword" in lines[11]:
        print("Found!")
        lines[11] = lines[11].replace("thisword", "ok")
        print(lines[11])

with open("test.txt", 'w') as file:
    file.writelines(lines)
