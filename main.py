#REMOVE PASS AND FIX THE FUNCTION
def sum_of_products(list1, list2):
     total=0
     for i in range(0, len(list2), 2):
         product=int(list1[i])*int(list2[i])
         total+=product
         return product
        
if __name__ == '__main__':
   #REMOVE PASS AND YOUR CODE GOES HERE
   list1=input()
   list2=input()
sum_of_products(list1, list2)
print(sum_of_products)
