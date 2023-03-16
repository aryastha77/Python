def result (math,sci,nep,eng,comp):
    marks= math+sci+nep+eng+comp
    total=500
    percentage= (marks/total)*100
    return(percentage)
math=float(input("enter the marks of math"))
sci=float(input("enter the marks of science"))
nep=float(input("enter the marks of nepali"))
eng=float(input("enter the marks of english"))
comp=float(input("enter the marks of computer"))
Final=result (math,sci,nep,eng,comp)
print("the final result is=","%.2f"%Final,"%")

