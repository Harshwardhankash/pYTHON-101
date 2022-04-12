import math



def isDivisible2(n):
    """
    Check the divisibility of 'n' by 
    3
    py:function::
    
    Args:
      n(str):the number to check
    Returns:
      bool:'True' if 'n'is divisible by
      3
      """
      
    
    

    a=str(n)
    if(int(a[-1]) in(2,4,6,8,0)):
        two=1
        return True
    else:
        return False
def isDivisible3(n):
     """
    Check the divisibility of 'n' by 
    3
    py:function::
    
    Args:
      n(str):the number to check
    Returns:
      bool:'True' if 'n'is divisible by
      3
      """
    if (n in (3, 6, 9)):
        three=1
        return True
    if(len(str(n))==1):
        return False
    else:
        n1=str(n)
        n2=int(n1[-1])+int(n1[0:len(n1)-1])
        return(isDivisible3(n2))

def isDivisible4(n):
    """
    Check the divisibility of 'n' by 
    3
    py:function::
    
    Args:
      n(str):the number to check
    Returns:
      bool:'True' if 'n'is divisible by
      3
      """

    n1 = str(n)
    n2 = n1[-2:-1]+n1[-1]

    if(int(n2) in(0,4,8,12,16,20,24,28,32,36,40,44,48,52,56,60,64,68,72,76,80,84,88,92,96)):

        return True
    else:
        return False



    # d=0
    # e=0
    # for i in n1:
    #     i=str(i)
    #     if(i==" 2" or i=="5" or i=="8"):
    #         d=d+1
    #     if(i=="1" or i=="4" or i=="7"):
    #         e=e+1
    # if(int(d-e) in(0,3,6,9,12,15)):
    #    return 3
    # n = str(n)
    # sum=0
    # for i in n:
    #     k = int(i)
    #     sum = sum + k
    #
    # if ((int)(sum) in (3, 6, 9, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126, 135, 144, 153, 162, 171, 180)):
    #     return 9


# def isDivisible4(n):
#      n1=str(n)
#      k1 = int(n[-2:-1])
#      k15=int(n[-1])
#      if((k1==2) or (k1==4) or(k1==6) or (k1==8) or(k1==0)):
#           if(k15==0) or(k15==4) or (k16==8):
#               return 4
#
#
#
#      if ((k1 == 1) or (k1 == 3) or (k1 == 5) or (k1 == 7) or(k1==9)):
#
#            if (k15 == 2) or (k15 == 6):
#
#                 return 4
# #
# #     k24 = (int)(n[-1])
# #
# #     h14 = 2 * k14 + k24
# #
# #     st4 = "" + str(h14)
# #
# #     f4 = int(st4)
# #
# #     # while(len(st4)!=1):
# #     #     h14= int(st4[0]) +int(st4[1])
# #     #     st4 = str(h14)
# #
# #
# #     if ((f4) in [0, 4, 8, 12, 16, 20, 24, 28]):
# #
# #         return 4
# #
# #
# #     a=str(n)
# #     if(int(a[-1]) in(2,4,6,8,0)):
# #         return 4
def isDivisible5(n):
    '''
    Checking Divsibility by 5

    :param n:
    :return:
    '''
    a=str(n)
    if(int(a[-1]) in(5,0)):
        return True
    else:
        return False

def isDivisible6(n,two,three):
    """
    Check the divisibility of 'n' by 
    3
    py:function::
    
    Args:
      n(str):the number to check
    Returns:
      bool:'True' if 'n'is divisible by
      3
      """
    if((two==1)and(three==1)):
        return True
    else:
        return False

    a=str(n)
    # if(int(a[-1]) in(2,4,6,8)):
    #     return True
    # else:
    #
    #     return False
def isDivisible7(n):
     """
    Check the divisibility of 'n' by 
    3
    py:function::
    
    Args:
      n(str):the number to check
    Returns:
      bool:'True' if 'n'is divisible by
      3
      """
    noo = 0
    flag = 0
    a=str(n)

    while (len(a) > 2):
            noo = int(a[-2:]) + int(a[0:-2]) * 2
            a = str(noo)
    if (int(a) in (0,7,14,21,28,35,42,49,56,63,70,77,84,91,98)):
        return True
    else:
        return False
def isDivisible8(n):
    """
    Check the divisibility of 'n' by 
    3
    py:function::
    
    Args:
      n(str):the number to check
    Returns:
      bool:'True' if 'n'is divisible by
      3
      """
    n=str(n)
    if (len(n) >= 3):

        count8 = n[-3:-2]

        count81 = ""
        count82 = ""
        count8sum = ""
        count8sum1 = 0

        if (int(count8) in [2,4,6,8,0]):


            count81 = str(n[-2:-1])
            count82 = str(n[-1])

            count8sum = count81 + count82
            count8sum1 = int(count8sum)

        elif ((int)(count8) in [1,3,5,7,9]):



            count81 = str(n[-2:-1])
            count82 = str(n[-1])
            count8sum = count81 + count82
            count8sum1 = int(count8sum) + 4

        if ((int)(count8sum1) in [0,8,16,24,32,40,48,56,64,72,80,88,96]):

            return True
        else:
            return False


    elif (len(n) < 3):


        if (int(n) in [0,8,16,24,32,40,48,56,64,72,80,88,96]):
            return True
        else:
            return False


def isDivisible9(n):
    """
    Check the divisibility of 'n' by 
    3
    py:function::
    
    Args:
      n(str):the number to check
    Returns:
      bool:'True' if 'n'is divisible by
      3
      """
    n=str(n)
    sum=0
    for i in n:


        k=int(i)
        sum=sum+k

    if((int)(k) in (9,18,27,36,45,54,63,72,81,90,99,108,117,126,135,144,153,162,171,180)):
        return True

    else:
        return False
def isDivisible9(n):
    if (n in [9]):
        return True
    if(len(str(n))==1):
        return False
    else:
        n1=str(n)
        n2=int(n1[-1])+int(n1[0:len(n1)-1])
        return isDivisible9(n2)


def Numbers_All(n,two,three):

    for x in n:

        x=round(x)
        x=int(x)
        try:
            if(x!=int(x)) or(str(x)[0:1]=="-"):
                x=int(x)
                x=abs(x)
                x=x.split(".")
                print("No. is negative or No. is decimal")
        except Exception as e1:
                print("Generic error: {0}".format(e1))

        L=""
        if(isDivisible2(x)):
            two=1
            L=L+str(2)+","
        if (isDivisible3(x)):
            three=1
            L=L+str(3)+","
        if (isDivisible4(x)):
            L=L+str(4)+","
        if (isDivisible5(x)):
            L=L+str(5)+","
        if (isDivisible6(x,two,three)):
            L=L+str(6)+","
        if (isDivisible7(x)):
            L=L+str(7)+","
        if (isDivisible8(x)):
            L=L+str(8)+","
        if (isDivisible9(x)):
           L=L+str(9)
        # L.append(isDivisible2(x))
        # L.append(isDivisible3(x))
        # #L.append(isDivisible4(x))
        # L.append(isDivisible5(x))
        # L.append(isDivisible6(x))
        # L.append(isDivisible7(x))
        # L.append(isDivisible8(x))
        # L.append(isDivisible9(x))

        if(len(L)!=0):


            if (L[-1] == ","):
                L = L[0:len(L) - 1]
            print("{}: is divisible by {}".format(x, L))
        else:

            print("{}: is not divisible{}".format(x, L))
def main():


    numb=input("Enter the values")
    numb=list(map(float,numb.split(",")))
    two=0
    three=0
    Numbers_All(numb,two,three)
main()
