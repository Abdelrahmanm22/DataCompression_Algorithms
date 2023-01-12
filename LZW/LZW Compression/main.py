symbols="ABAABABBAABAABAAAABABBBBBBBB"

#create dictionary-----------------------

Dictionary = {chr(i): i for i in range(65, 90)}     #Uppercase letters
d= {chr(i): i for i in range(97, 97 + 26)}          #lowercase letters
Dictionary.update(d)                                #All Letters

#create dictionary-----------------------

s1=symbols[0]
s2=""

index = 128
Answer = []
numberOfTags=0
for i in range(0, len(symbols)-1):

    s2 = symbols[i+1]

    #To check the element is found before the end of the map
    if s1+s2 in Dictionary:
        s1 += s2

        #check if last iteration
        if(i+1==len(symbols)-1):
            Answer.append(Dictionary[s1])
            numberOfTags += 1
    else:
        # print(s1)
        numberOfTags += 1
        Answer.append(Dictionary[s1])
        Dictionary[s1+s2] = index
        index += 1
        s1 = s2

    s2 = ""

print("Tags:",Answer)
print("Original:",len(symbols),"*",8,"=",len(symbols)*8,"bits")
print("Compresses:",numberOfTags,"*",8,"=",numberOfTags*8,"bits")