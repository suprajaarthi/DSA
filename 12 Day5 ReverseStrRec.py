def reverse(s): 
    if len(s) == 0: 
        return s 
    else: 
        return reverse(s[1:]) + s[0] 
  
 # "HELLO"
 # reverse(s[1:]) + s[0]     reverse(ello) + H
 # reverse(s[2:]+s[1]+s[0])  reverse(llo)	+ EH
 # reverse(s[3:]+s[2]+s[1]+s[0]) reverse(lo) LEH
 # 		s[4:]+s[3]+s[2]+s[1]+s[0]	reverse(o) + LLEH


print(reverse("HELLOWORLD"))