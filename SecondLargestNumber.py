def SecondLargest(mylist):
    if len(mylist)<2:
        print("NOT ENOUGH ELEMENTS!")
    else:
        first=max(mylist[0],mylist[1])
        second =min((mylist[0],mylist[1]))
        for i in range(2,len(mylist)):
             if mylist[i]> first:
                second=first
                first=mylist[i]
             elif mylist[i]>second & mylist[i]!=first :
                second=mylist[i]
        print("THE SECOND LARGEST SALARY IS:  ",+second)

##salary=[1000] ###TEST IF THE LIST HAS ENOUGH ELEMENTS
salary=[1000, 4000, 2000,5000]
SecondLargest(salary)