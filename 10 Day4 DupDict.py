nums=[1,2,3,4,1]
nums_dic = {}

# Same as counter in Collections 
# {1:2 , 2: 1 , 3:1 , 4:1}
# assign nums_dic[1]=nums_dic.get(key,val)
# 				= nums_dic.get(1,0) 
# 		=>   value (optional) - Value to be returned if the key is not found. The default value is None.
# op:
# {1: 1}
# {1: 1, 2: 1}
# {1: 1, 2: 1, 3: 1}
# {1: 1, 2: 1, 3: 1, 4: 1}
# {1: 2, 2: 1, 3: 1, 4: 1}
# since 1 is dup, it is inc to 2 so prints true 
# False
for val in nums:
    nums_dic[val] = nums_dic.get(val,0) +1
    print(nums_dic[val])
    # print(nums_dic.get(val) + 1)
    if nums_dic[val] == 2:
        print("True")
        quit()
        
print("False")
