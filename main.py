#REMOVE PASS AND FIX THE FUNCTION
def sum_of_products(list1, list2):
        int_list1=[]
        int_list2=[]
        list3=[]
        for num1 in list1:
              int_list1.append(int(list1))
        for num2 in list2:
              int_list2.append(int(list1))
        for num3 in range(int_list1):
              for num4 in range(int_list2):
                    list3.append(num3*num4)
                    return list3


if __name__ == '__main__':
   #REMOVE PASS AND YOUR CODE GOES HERE
   list1=list[input()]
   list2=list[input()]
   sum_of_products(list1, list2)
   print (sum(sum_of_products))
   