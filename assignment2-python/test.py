from assignment2_new import split_and_sort # import the split and sort function
nums = [0] #Sample list
result = split_and_sort(nums) # call the function and store the return value
if type(result) == str: # if the return value is a string, which might be an error
    print(result) #print the return value
else: #else, which means the return value is not a string
    pass 


