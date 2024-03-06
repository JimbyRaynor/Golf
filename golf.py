print("Golf - text version. From the book 101 basic games")
f= 1 # hole number
h=0 # handicap
t=0 # handicap type
s1= 0 # number of shots taken
      # s1=0 means get ready to tee off
s2=0 # hook when s2 =14, also slice
g1=18 # total number of holes on golf course
g2=0 # total score for holes so far
g3=0 # total par for holes so far
a=0 # used to skip club printout
p=0 # par (good average) for hole
c=0 # club number
w=0 # weighting of swing, 1 is max, 0 is no swing
d=0 # distance to hole
L=[0,1,1,1,1,1,1,1] # is the type of terrain

#L[]=1 is fairway, 2 is rough,
#    3 is trees, 4 is adjacent fairway
#    5 is trap, 6 is water
#    7 is out of bounds
#L[0] #is forward X=0
# L[1] # is left
# L[2] is right

groundtype = ['blank', 'fairway', 'rough',\
              'trees', 'adjacent fairway',\
              'trap', 'water', 'out of bounds']

holedata=[361,4,4,2,389,4,3,3,206,3,4,2,500,5,7,2,\
408,4,2,4,359,4,6,4,424,4,4,2,388,4,4,4,\
196,3,7,2,400,4,7,2,560,5,7,2,132,3,2,2,\
357,4,4,4,294,4,2,4,475,5,2,3,375,4,4,2,\
180,3,6,2,550,5,6,6]

holes=[]

i=0
while i < 18*4:
    hole = {}
    hole["Ldata"] = [0,holedata[i+2],holedata[i+3]]
    hole["distance"] = holedata[i]
    hole["par"] = holedata[i+1]
    hole["left"] = groundtype[holedata[i+2]]
    hole["right"] = groundtype[holedata[i+3]]
    holes.append(hole)
    i=i+4

print(holes)
    

def showscore():
  print("Your score on hole ", f, " was ", s1)
  print("Total par for ", f, " holes is ", g3,\
        "  Your total is ", g2)
  if s1 > p+2:
      print("Keep your head down.")
  if s1==p:
      print("A Par. Nice Going.")
  if s1==p-1:
      print("A Birdie. Great!")
  if (s1 == p-2) and (s1 != 1):
      print("A great big Eagle.")
  if s1 == 1:
      print("A hole in one.")

def chooseclub():
  clubchosen = False
  while (not clubchosen):
    c = int(input("What club do you choose: "))
    if (c in range(1,5)) or (c in range(12,30)):
        if L[0] <= 5:
            clubchosen = True
        else:
            if c==14 or c==23:
                 clubchosen = True
    else:
        print("That club is not in the bag")
  return c
      
holefinished = False
       
while (f <= g1) : # f is hole number
  L[0] = 0  # f loop
  j=0
  q=0
  s2 = s2 + 1 # hook when s2=14, also slice
  k=0
  if f != 1: showscore()
  if a != 1:
      print("Selection of clubs")
      print("Distance            Suggested club")
      print("200 to 280 yards    1 to 4")
      print("100 to 200 yards    19 to 13")
      print("  0 to 100 yards    29 to 23")
      print("Not all clubs are available")
  s1 = 0
  print('Hole',f)
  L = holes[f-1]["Ldata"]
  d = holes[f-1]["distance"]
  p = holes[f-1]["par"]
  g3=g3+p
  print(L)
  print("You are at the tee off for Hole",f,\
        ", Distance",d,"yards, par",p)
  print("On your right is")
  print(holes[f-1]["right"])
  print("On your left is")
  print(holes[f-1]["left"])
  while not holefinished: #s1 loop, number of shots    
      a = 1
      c = chooseclub()
      s1 = s1 + 1
      w = 1
      if c > 13: # putter or just short distance
        print("Now gauge your distance by a percentage (1 to 100)")  
        print("of a full swing")
        w = int(input("percentage = "))
        print()
      print("shot", s1)
  f = f + 1
