import math
filein = open("inout.txt", "r")
fileout = open("output.txt", 'w')

#The float_bin function changes the corresponding floating number to its equivalent binary code will k bits
def float_bin(number, k):
    b = ""
    for x in range(k):
        number = number * 2
        if number > 1:
            b = b + str(1)
            x = int(number)
            number = number - x
        elif number < 1:
            b = b + str(0)
        elif number == 1:
            b = b + str(1)
            break
    return b

# print(float_bin(0.774,10))

"""
The encoder function first creates a list which contains the alphabets along with the lower value and upper value of the particular letter (referred as unity list) forming in a range of 0 to 1.
"""
def Encoder(alpha, prob, N, s):
    arrOfArray = []
    #
    prob_range = 0.0                                                                        #Lower(Symbol)=Lower + Range*Low_range(Ssymbol)
                                                                                            #Upper(Symbol)=Lower + Range*High_range(Ssymbol)
    for i in range(N):
        l = prob_range
        prob_range = prob_range + prob[i]
        u = prob_range
        arrOfArray.append([alpha[i], l, u])
    # print(unity[0])
    for i in range(len(arrOfArray)):
        print(arrOfArray[i][0]," ",arrOfArray[i][1]," ",arrOfArray[i][2])

    """
    Now, for length of sequence – 1 time, a for loop first matches an alphabet from the sequence and the unity list.
    If a match is found, the region is expanded and the lower value of the letter becomes the lower value of the whole range and the upper value of
     the letter becomes the upper value of the whole range and an inner for loop then assigns the new lower and upper values to all the characters and
     the changes these values in the unity list.
    """
    for i in range(len(s) - 1):
        for j in range(len(arrOfArray)):
            if s[i] == arrOfArray[j][0]:
                Low_range = round(arrOfArray[j][1],3)
                High_Range= round(arrOfArray[j][2],3)
                diff = High_Range - Low_range
                for k in range(len(arrOfArray)):
                    arrOfArray[k][1] = Low_range
                    arrOfArray[k][2] = round(Low_range + diff * prob[k],3)
                    Low_range = arrOfArray[k][2]
                break

    """
    We, then calculate the tag for the last letter for the sequence by taking the lower and higher values and tag is given 
    by their arithmetic mean. Now the value of number of bits is calculated by taking the ceil of log on base 2 for (1 / upper – lower) + 1.
    """
    low = 0
    high = 0
    # for i in range(len(arrOfArray)):
    #     print(arrOfArray[i][1]," ",arrOfArray[i][2])
    # print(s[-1])
    for i in range(len(arrOfArray)):
        if arrOfArray[i][0] == s[-1]:
            low = arrOfArray[i][1]
            high = arrOfArray[i][2]
    tag = ((low + high) / 2)
    k = math.ceil(math.log((1 / (high - low)), 2) + 1)
    print(k)
    bin_code = str(float_bin(tag+0.002, k))
    #print("Binary code for the sequence " + s + " is " + bin_code)
    #print("Tag value for sequence is: ", tag+0.001)
    return [bin_code, tag+0.001, N, alpha, prob]


#######################################################Decoder Part#####################################################

"""
Moving on to the decoder function. It first creates a list which contains the alphabets along with the lower value
and upper value of the particular letter (referred as unity list) forming in a range of 0 to 1.
"""
def Decoder(Compression):
    tag = Compression[1]
    N = Compression[2]
    alpha = Compression[3]
    prob = Compression[4]
    arrOfArray = []
    prob_range = 0.0
    seq = ""
    for i in range(N):
        l = prob_range
        prob_range = prob_range + prob[i]
        u = prob_range
        arrOfArray.append([alpha[i], l, u])

    """
    Now, for N + 1 time, a for loop first matches the tag value and checks for which alphabet range it lies from the unity list. If a match is found,
     the region is expanded and the lower value of the letter becomes the lower value of the whole range and the upper 
     value of the letter becomes the upper value of the whole range and an inner
     for loop then assigns the new lower and upper values to all the characters and the changes these values in the unity list.
     We also concatenate the corresponding alphabet to the sequence which is the original sequence.
    """
    for i in range(N + 1):
        for j in range(len(arrOfArray)):
            if tag > arrOfArray[j][1] and tag < arrOfArray[j][2]:
                Low_range = arrOfArray[j][1]
                High_Range = arrOfArray[j][2]
                diff = High_Range - Low_range
                seq = seq + arrOfArray[j][0]
                for k in range(len(arrOfArray)):
                    arrOfArray[k][1] = Low_range
                    arrOfArray[k][2] = prob[k] * diff + Low_range
                    Low_range = arrOfArray[k][2]
                break
    #print("The sequence for Float code " + str(tag) + " is " + seq)
    return seq
#######################################################Decoder Part#####################################################


##The Driver Code

Sequance = filein.readline()
filein.close()
#print(len(Sequance))
frequency = {}
for char in Sequance:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

#f =sorted(frequency)
f = dict(sorted(frequency.items(), key=lambda x: x[0]))
#print(f)
probability = []
alphabet = []
for key in f.keys():
    value = f[key]
    alphabet.append(key)
    N=(len(alphabet))
    probability.append(value/len(Sequance))
filein = open("input.txt", "r")
String = filein.readline()
filein.close()
#print(alphabet)
#print(probability)

#N = int(input("Enter number of letters in file: "))
#for i in range(N):
 #   a = input("Enter the letter: ")
    # p = float(input("Enter probability for " + a + ": "))
  #  alphabet.append(a)
    # probability.append(p)
# sequence = input("Enter the sequence to be encoded: ")

Compression =  Encoder(alphabet, probability,N, String)
decompression = Decoder(Compression)
fileout.writelines(str( Compression)+'\n')
fileout.writelines(str( decompression))
fileout.close()
