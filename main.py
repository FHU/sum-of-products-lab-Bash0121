#REMOVE PASS AND FIX THE FUNCTION
def sum_of_products(list1, list2):
        list5=[]

        if len(list1)==len(list2):
            list3=[eval(i) for i in list1]
            list4=[eval(i) for i in list2]
            for num3 in range(len(list3)):
                  for num4 in range(len(list4)):
                        list5.append(num3*num4)
                        
                        return list5
        else:
             return 'error'   
        
if __name__ == '__main__':
   #REMOVE PASS AND YOUR CODE GOES HERE
   list1=[]
   list2=[]
   input1=input()
   input2=input()
   for i in input1:
      list1.append(i)
   for i in input2:
      list2.append(i)
sum_of_products(list1, list2)
print(sum_of_products)
