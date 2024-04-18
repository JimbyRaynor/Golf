import random, math

print("Golf - text version. From the book 101 basic games")
f= 1 # hole number
h=0 # handicap
t=0 # handicap type
n=0.8 # n used to see if rnd(1) > n handicap works
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
d2 = 0 #distance to hole
L=[0,1,1,1,1,1,1,1] # is the type of terrain
b=0 # previous distance to cup

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


def RND():  # random real number between 0 and 1
    return random.random()

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
      

       
while (f <= g1) : # f is hole number
  holefinished = False  
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
  #print(L)
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
        w = w / 100
        print()
      if int(f/3) == f/3: #L952
          if s2+q+(10*(f-1)/18) < (f-1)*(72+1/.85)/18:
            q=q+1 #L956
            if s1/2 != int(s1/2):
                if d < 95:
                    print("You dubbed it")
                    d1 = 35   
      if c < 4 and L[0]==2:
         print("You dubbed it")
         d1 = 35
      else:
         if s1 > 7: #L760
             if d < 200: #L867
                d2 = 1 + 3*int(2*RND())
     #L770
      d1 = int(30*2.5+187-(30*.25+15)*c/2)+25*RND()
      d1 = int(d1*w)
      #L830
      # d is original distance to cup
      # d,d1,d2,o described on line 360
      # d1 is shot distance
      # d2 is new distance to cup
      # o is offline distance on side of course, o=0 when in middle of course
      o = RND()/.8*16*abs(math.tan(d1*0.0035))
      d2 = int(math.sqrt(o**2+(d-d1)**2))
      if (d1 > d) and (d2 >= 20):
        print("Too much club. You are past the hole.")  
      print("shot", s1)
      if L[0] == 5:  # trap
         d2 = 1+(3*int(2*RND()))
      print("On green, ",d2, "feet from the pin.")
      i = input("Choose your putt potency (1 to 13): ")
      i = int(i)
      s1 = s1 + 1
      if s1+1 -p > 2:
          print("You holed it")
          f=f+1
          holefinished = True
  f = f + 1
