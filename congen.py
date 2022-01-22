ff=open("contacts.txt","w")
fp=open("Date.txt","r")
while True:
        line = fp.readline()
        con = ' '.join(line.split())
        if con and con.isdigit():
            number=int(con)
            ff.write(str("91"+str(number)+"\n"))
            print(number)
        if not line:
            break