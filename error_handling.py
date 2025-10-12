# Runtime and compile error

# nums = [1, 2, 3, 4]
# print(nums[10]) #runtime error

# print(x) # compile type 


# Try
# except
# else
# finally


# nums = [1, 2, 3, 4]
# try: 
#     print(nums[10]) 
# except:
#     print('An Error Occured')


# nums = range(20)
# try: 
#     x = nums[10]
# except:
#     print('An Error Occured')
# else: # this work if no error occur
#     print(x)
    
# finally:
#     print('I run if there is an error or not')
    
    
    
nums = [1, 2, 3, 4]
try: 
    print(nums[1])
    print(2/0)
except IndexError as i:
    print(f'Error:  {i}')
except NameError as n:
    print(f'Error:  {n}')
except Exception as e:
    print(f'Error: {e}')