
import time
now=time.ctime()
qna = {
   "hi":"hey",
   "how are you":"I am fine",
   "what is your name":"My name is priya",
   "how old are you":"I am 20 years old",
   "what is the time now":now
}

while True:
    qs = input()
    
    if(qs== "quit"):
        
        break
    
    
    else:
        print(qna[qs])