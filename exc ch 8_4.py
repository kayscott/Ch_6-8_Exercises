fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    words = line.split()
    for word in words: 
        t = word.split()
        lst.append(t)
        print lst