#REMOVE PASS AND FIX THE FUNCTION
#change to test push and forks
def sum_of_products(list1, list2):
   total=0
   for i in range(len(list1)):
         product=int(list1[i])*int(list2[i])
         total+=product
   return total
        
if __name__ == '__main__':
   #REMOVE PASS AND YOUR CODE GOES HERE
   list1=[]
   list2=[]
   u_input1=input()
   u_input2=input()
   list1=u_input1.split()
   list2=u_input2.split()
total=sum_of_products(list1, list2)
print(total)
