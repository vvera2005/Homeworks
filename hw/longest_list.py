def find_grow(ml):
     temp = []     
     the_longest = []
     for i in range(len(ml)):
         if i+1 < len(ml):
             if ml[i] < ml[i+1]:
                 temp.append(ml[i])    
             elif len(temp) > len(the_longest):
                 the_longest = temp
                 temp = []
             else:
                 temp = []
     return the_longest

ml = [1,2,6,8,9,5,46,8,9,6,7,9,126]
print(find_grow(ml))

