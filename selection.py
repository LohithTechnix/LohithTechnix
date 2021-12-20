# def selection_sort(nums):


#     for i in range(5):
#         minipos = i
        

#         for j in range(i,6): 
#             if nums[j] < nums[minipos]:
#                 minipos,j = j,minipos

#         temp = nums[i]
#         nums[i] = nums[minipos]     
#         nums[minipos] = temp


# nums = [5,3,8,6,7,2] 
# nums.sort()

# print(nums)  



numbers = [4,9,3,6,2]

for i in range(len(numbers)):
    min_idx = i
    
    for j in range(i+ 1,len(numbers)):
       
        if numbers[j] < numbers[min_idx]:
            min_idx = j
            
            

            


    numbers[i] , numbers[min_idx]  = numbers[min_idx],numbers[i]       


print(numbers)