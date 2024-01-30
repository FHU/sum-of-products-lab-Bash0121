#REMOVE PASS AND FIX THE FUNCTION
def sum_of_products(list1, list2):
        list3=[]
        list1 = [int(item) for item in list1]
        list2 = [int(item) for item in list2]
        for num3 in range(list1):
              for num4 in range(list2):
                    list3.append(num3*num4)
                    return list3


if __name__ == '__main__':
   #REMOVE PASS AND YOUR CODE GOES HERE
   list1=list[input()]
   list2=list[input()]
   sum_of_products(list1, list2)
   print (sum(sum_of_products))
