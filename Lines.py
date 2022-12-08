filename="code.txt"
linescount=0
with  open(filename,'r') as files:
    for i in files:
        linescount=linescount+1

print()
print(linescount)
