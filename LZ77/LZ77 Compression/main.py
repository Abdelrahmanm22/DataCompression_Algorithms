"""
Created by abdelrahman Mohamed Ramadan
Computer Science Department
Faculty of Computers and Artificial Intelligence Cairo University

**Compression LZ77**
"""

class Tag:
  def __init__(self, Position, Length,NextSympol):
    self.Position = Position
    self.Length = Length
    self.NextSympol=NextSympol

  def printTag(self):
      print("<",self.Position,",",self.Length,",",self.NextSympol,">")


#EXAMPLE 1
SlidingWindow = "ABAABABAABBBBBBBBBBBBA"

#EXAMPLE 2
# SlidingWindow = "AAAABBABABBAAABBAAAAAAAAA"

#EXAMPLE 3
#SlidingWindow = "XYYXZYXYYYYXYYXYYX"


SearchWindow = ""
x=""
list = []
z=0
for i in SlidingWindow:
    x+=i
    Pos=len(SearchWindow)-SearchWindow.rfind(x)
    # print(Pos,len(x)-1)

    #To Handle case 2 we (Fixed Search Window) checked if pos <=10
    if SearchWindow.rfind(x) > -1 and Pos<=10 and len(x)<=4: #if exist
        z=Pos
    else:
        if(len(x)-1==0):
            list.append(Tag(0, len(x) - 1, i))
        else:
            list.append( Tag(z,len(x)-1,i))

        SearchWindow+=x;
        x=""

# lastChar = SlidingWindow[len(SlidingWindow) -1]
if len((x))!=0:
    list.append(Tag(z, len(x), "Null"))

#For output
for obj in list:
    print(obj.printTag())
