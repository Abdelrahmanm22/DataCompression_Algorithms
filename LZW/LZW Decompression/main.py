Array = [65,66,65,128,128,129,131,134,130,129,66,138,139,138]
result = []

#create dictionary-----------------------

Dictionary = {i: chr(i) for i in range(65, 90)}     #Uppercase letters
d= {i: chr(i) for i in range(97, 97 + 26)}          #lowercase letters
Dictionary.update(d)                                #All Letters


#create dictionary-----------------------

index=128

prev = Array.pop(0)
result.append(Dictionary[prev])

for c in Array:
    if c in Dictionary:
        next = Dictionary[c]
    result.append(next)
    Dictionary[index] = Dictionary[prev] + next[0]
    index += 1
    prev = c


print(''.join(result))


