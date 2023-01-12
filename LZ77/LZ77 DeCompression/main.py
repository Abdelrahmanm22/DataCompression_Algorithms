"""
Created by abdelrahman Mohamed Ramadan
Computer Science Department
Faculty of Computers and Artificial Intelligence Cairo University


**DeCompression LZ77**
"""

class Tag:
  def __init__(self, Position, Length,NextSympol):
    self.Position = Position
    self.Length = Length
    self.NextSympol=NextSympol



list = [Tag(0,0,'A'),Tag(0,0,'B'),Tag(2,1,'A'),Tag(3,2,'B'),Tag(5,3,'B'),Tag(2,2,'B'),Tag(5,5,'B'),Tag(1,1,'A')]

res=""
p=0
for tag in list:
    if tag.Position==0:
        res+=tag.NextSympol
    else:
        p=len(res)-tag.Position
        res+=res[p:p+tag.Length]+tag.NextSympol

print(res)