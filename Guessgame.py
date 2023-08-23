import random
count=0
def trys(a,b):
   if(a==b):
     return True
   elif(a>b):
      if(a-b<=20 and a-b>10):
         print("\n")
         
         print("Please choose lower number")
         print("\n")

         return False
      elif(a-b<=10):
         print("\n")
         
         print("Almost there please select lower number")
         print("\n")

         return False

      else:
         print("\n")
         
         print("Too Far please select lower number")
         print("\n")

         return False
   elif(b>a):
      if(b-a<=20 and b-a>10):
         print("\n")
         
         print("Please choose Higher number")
         return False
      elif(b-a<=10):
         print("\n")
         
         print("Almost there please select Higher number")
         print("\n")
         return False
      else:
         print("\n")
         
         print("Too Far please select Higher number")
         print("\n")

         return False
     
print("Guess the number ")
you=int(input("Your chance to guess which number is the answer"))
comp=random.randint(1,100)
result=trys(you,comp)
while(result==False):
      count+=1
      print("\n")
      print(f"Your guessed number {you} which is wrong")
      print("\n")

      print("Try again")
      print("\n")

      you=int(input("Your chance to guess which number is the answer"))
      result=trys(you,comp)
      
else:
   print("\n")
   
   print(f"Your guessed number {you} and correct answer {comp} and you took {count} attempts")
   print("\n")

   print("You won!Congratulations")
   l=open("Highscore.txt")
   s=l.read()
   l.close()
   k=open("Highscore.txt",'w')
   k.write(s+(f" \n New Score is {you} in {count} attempts"))
   k.close()
   