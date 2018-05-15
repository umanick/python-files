from sys import argv
op_filename = "out.py"
if len(argv) > 1 :
    op_filename = argv[1]
out_file = open(op_filename, "w")
with open("/Users/upen/Documents/github/pfiles/script.txt", "r") as ins:
    array = []
    dotab = False
    for readline in ins:
        readline = readline.lstrip().rstrip()
        #print readline
        #print len(readline)
        #print readline.find(' ')
        if readline.find(' ') > 0:
            line = readline[readline.index(' ')+1:len(readline)]
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