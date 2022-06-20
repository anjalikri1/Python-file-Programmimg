f=open("bank.txt","w")
bank=["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
for b in bank:
    a=f.write(b+"\n")
    print(a)