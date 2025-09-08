f=open("input.txt","r")
a=[]
with open("input.txt","r") as f1:
    lines = f1.readlines()
text = lines[0].strip().split()
op = lines[1].strip()
if op=="+":
    k=0
    for num in text:
        k+=int(num)
elif op=="-":
    k=int(text[0])
    for num in text[1:]:
        k-=int(num)
elif op=="*":
    k=1
    for num in text:
        k*=int(num)
with open("output.txt", "w") as output_file:
    output_file.write(str(k))