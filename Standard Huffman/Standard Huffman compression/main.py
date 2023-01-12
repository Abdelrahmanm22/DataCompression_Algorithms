"""
-Huffman Coding is generally useful to compress the data in which there are frequently occurring characters.
-Huffman coding first creates a tree using the frequencies of the character and then generates code for each character.
-A code associated with a character should not be present in the prefix of any other code. The tree created above helps in maintaining the property.
                initial string:       B C A A D D D C C A C A C A C
                Frequency of string:   B  D  A  C   (Characters sorted according to the frequency)
                                       1  3  5  6
First Step ==> Sort the characters in increasing order of the frequency. These are stored in a priority queue Q.
Second Step ==> Create an empty node z. Assign the minimum frequency to the left child of z
and assign the second minimum frequency to the right child of z. Set the value of the z as the sum of the above two minimum frequencies.
Third Step ==> Remove these two minimum frequencies from Q and add the sum into the list of frequencies (* denote the internal nodes in the figure above).
Four Step ==> Insert node z into the tree.
Five Step ==> 2 , 3 for all characters
"""


Sympols = "BCAADDDCCACACAC"

# Calculating frequency
frequency = {}
for char in Sympols:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1


# print(frequency)
#First step
# print(frequency)
frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
# print(frequency)

nodes=frequency

#Second Step
class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)

while len(nodes) > 1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))

    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)


#For each non-leaf node, assign 0 to the left edge and 1 to the right edge
def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}

    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))

    return d


huffmanCode = huffman_code_tree(nodes[0][0])

Compression=0
for (char,frequency) in frequency:
    Compression+=frequency*len(huffmanCode[char])
    print(char+" ==> "+huffmanCode[char])










print("Original:",len(Sympols),"*",8,"=",len(Sympols)*8,"bits")
print("Compresses:",Compression,"bits")








"""
The priority queue is an advanced type of the queue data structure. 
Instead of dequeuing the oldest element, a priority queue sorts and dequeues elements based on their priorities.
"""