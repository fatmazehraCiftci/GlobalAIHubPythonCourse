"""
Create a list and swap the second half of the list with the first half of the list and 
print this list on the screen
"""

def DivideandSwap(list):
    length=len(list)
    list1=[]
    list2=[]
    for i in range(int(length/2)):
        list1.append(list[i])
    
    remainder=length-int(length/2)
    for i in range(remainder):
        list2.append(list[i-remainder])
    
    list=list2+list1
    print(list)




list=[1,2,3,4,5,6]
DivideandSwap(list)