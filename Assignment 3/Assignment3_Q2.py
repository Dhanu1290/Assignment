# function with parameters

def Addition(No1,No2):        # paramenter No1,No2
    return No1 + No2

def main():
    Ret1= Addition (10,5)
    print("Addition is :",Ret1)
    
def Hello():
    print("Jay Ganesh")        # no parameter
    
Hello()                         # function call
   
if __name__=="__main__":                                #1
    main()  