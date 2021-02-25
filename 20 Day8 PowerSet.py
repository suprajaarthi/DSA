def powerSet(str1, index, curr): 
    n = len(str1) 
    # string : Stores input string  
    # curr : Stores current subset  
    # index : Index in current subset, curr 
    if (index == n): 
        return
    
    # powerSet(abc,-1,'')
    #     -1 
    #     ''
    #     f 0,3 
    #       a
    #       powerSet(abc,0,a)
    # a.replace(a[0],"")
    # ""
    # ab     
    # powerSet(abc,0,a)
    #     f 1,3 
    #       a+abc[1]=ab 
    #       powerSet(abc,1,ab)
        #   ab.replace(ab[2-1],"")
        #   curr='a'
    # powerSet(abc,1,a)
    #     f 2,3 
    #         ac
    #         powerSet(abc,2,abc)
       
    print(curr) 
  
       # Try appending remaining characters 
    # to current subset 
    for i in range(index + 1, n): 
        curr += str1[i] 
        powerSet(str1, i, curr) 
  
        # Once all subsets beginning with 
        # initial "curr" are printed, remove 
        # last character to consider a different 
        # prefix of subsets. 
        curr = curr.replace(curr[len(curr) - 1], "") 
  

# Driver code 
if __name__ == '__main__': 
    str = "abc"; 
    powerSet(str, -1, "") 

