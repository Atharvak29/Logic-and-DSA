lst =  [43,62,32,5, 5,13,52,2,23,10]

l = sorted(lst)

lenth = len(l)

def med(lenth):
    if lenth %2 != 0:
        return int((lenth+1)/2)
    elif lenth %2 == 0:
        d_2 = []
        d_2.append((lenth+1)//2)
        d_2.append(( (lenth+1)//2 )+1)
        return d_2
    
returned_value = med(lenth)
# print(l)
# print(returned_value)

if isinstance( returned_value,int):
    print(l[(returned_value - 1)]) # this if for elemnts with odd n value
elif isinstance( returned_value, list):
    print( ( l[(returned_value[0]-1)] + l[(returned_value[1]-1)] ) / 2 )

