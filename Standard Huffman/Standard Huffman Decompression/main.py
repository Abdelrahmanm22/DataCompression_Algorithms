


com = {"C": "0","A": "11","D": "101","B": "100"}
d_swap = {v: k for k, v in com.items()}

# print(d_swap)
result=""
dec="0111011000"
x=""
for char in range(len(dec)):
   x+=dec[char]
   if x in d_swap.keys():
        result+=d_swap[x]
        x=""



print(result)