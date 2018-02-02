fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    pos = line.find('0')
    num = line[pos:pos + 6]
    num1 = float(num)
    count = count + 1
    total = total + num1
    avg = total / count
print 'Average spam confidence:', avg


        