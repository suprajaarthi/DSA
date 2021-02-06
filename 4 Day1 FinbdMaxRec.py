  # Algorithm to find max in a list 
          # Function find_max( list ) 
 
          #   possible_max_1 = first value in list 
          #   possible_max_2 = find_max ( rest of the list ); 
             
          #   if ( possible_max_1 > possible_max_2 ) 
          #     answer is possible_max_1 
          #   else 
          #     answer is possible_max_2 
          #   end 
 
          # end 


max num can either be the 1st num in the list or biggest of rest of the numbers
def maximum(L):
    if len(L) == 1:
        return L[0]
    else:
        return max(L[0],maximum(L[1:]))
        
    # l[0],l[1],l[2:],[2],l[3:],l[3]
  

L= [2,4,6,90,23,1,46]
print(maximum(L))