f=open('bank.txt','a')
banks_list = ["Kotak\n", "HDFC\n", "RBL\n", "SBI\n", "Bank of Baroda\n"] 
for i in range(len(banks_list)):
    f.write(banks_list[i])
    i+=1
f.close()