import random
Head=Tail=0
print("Who are you?")
a=input()
print("Hello "+a)
print("Tossing a coin 3 round.") 
for i in range(3):
  rand1 = random.randint(0,1)
  if(rand1==1):
    Head += 1
    print("Round"+str(i)+":Head")
  else :
    Tail += 1
    print("Round"+str(i)+":Tail")
print ("Head:"+str(Head)+"Tail:"+str(Tail))
if(Head>2):
  print("you won!")
else: 
  print("you lost")
