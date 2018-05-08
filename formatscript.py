out_file = open("out.py", "w")
with open("script.txt", "r") as ins:
    array = []
    dotab = False
    for string in ins:
        string = string.lstrip().rstrip()
        if len(string) > 2:
            line = string[string.index(' ')+1:len(string)]
            iselse = line.startswith('elif') | line.startswith('else')
            if dotab and not iselse:
                out_file.write('\t')
            out_file.write(line)
            out_file.write('\n')
            if line.endswith(':'):
                dotab = True
        else: 
            dotab = False
            out_file.write('\n')
out_file.close()