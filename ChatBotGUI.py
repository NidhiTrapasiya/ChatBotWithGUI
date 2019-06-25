from tkinter import *                       
from random import choice
import random
 # Define variables 
name = "Nidhi"   
weather = "cloudy"
flag=1
# Define a dictionary containing a list of responses for each message
#str.formate(str) used for substituting 
responses = {
    "hi":[
        "hello",
        "hi, how are you?"
        ],
    "I am fine, how are you?":[
        "I am good."
        ],
    "what is your name?": [
       "my name is {0}".format(name),
       "they call me {0}".format(name),
       "I go by {0}".format(name)
        ],
    "what's today's weather?": [
       "the weather is {0}".format(weather),
       "it's {0} today".format(weather)
        ],
    "what are you studying?":[
       "I am doing MBA",
       "I am in First year of BscIT",
       "I am doing CA"
        ],
    "which place do you go?":[
       "i love to go juhu",
       "i love to go in gardon"
        ],
    "default": ["default message"]  
}
                                                     
root = Tk()                             
user = StringVar()                          
bot  = StringVar()                          
                                    
root.title(" Simple ChatBot ")                  
Label(root, text=" user : ").pack(side=LEFT)                
Entry(root, textvariable=user).pack(side=LEFT)          
Label(root, text=" Bot  : ").pack(side=LEFT)                
Entry(root, textvariable=bot).pack(side=LEFT)               
                            
                                
def main():
    if user.get():
        question = user.get()                        
        if question in responses:                      
             bot.set(random.choice(responses[question]))                    
        else:                                
             bot.set(random.choice(responses["default"]))
    else:
        question = bot.get()
        if question in responses:
             user.set(random.choice(responses[question]))                    
        else:                                
             user.set(random.choice(responses["default"]))

def clear():
    user.set(" ")
    bot.set(" ")
                                
Button(root, text="speak", command=main).pack(side=LEFT)
Button(root, text="clear", command=clear).pack(side=LEFT)
                                    
mainloop()   
