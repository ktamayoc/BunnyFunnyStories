from tkinter import *
import tkinter as tk

root = tk.Tk()
root.geometry("300x300")
root.title("Mad Libs Generator")
frame = tk.Frame(root, bg = "#a2a8e0")
frame.place(relwidth = 1, relheight = 1)
frame2 = tk.Frame(root, bg = "white")
frame2.place(relwidth = 0.65, relheight = 0.5, x = 195, y = 240)
tk.Label(root, text = "Bunny Funny Stories", font = "Times 12 bold", bg = "#f7deff").pack()
tk.Label(root, text = "Let your imagination run wild. Be creative and have fun! :D" , font = "Times 7", bg = "#ffcce0").pack()
tk.Label(root, text = "Choose a Mad Lib :", font = "Times 10 bold", bg = "#b6fac8").place(x=365, y=70)

def madlib1():
  input1 = input("enter a protagonist name : ")
  input2 = input("enter an animal name : ")
  input3 = input("enter a name of famous monster : ")
  input4 = input("enter a past tense verb : ")
  input5 = input("enter random name : ")
  input6 = input("enter another animal name : ")
  input7 = input("enter same random name : ")
  input8 = input("enter same protagonist name : ")
  input9 = input("enter an adjective : ")
  input10 = input("enter same random name : ")
  input11 = input("enter adjective : ")
  input12 = input("enter an object: ")
  
  i1 = tk.Label(root, wraplength = 600, text = "It was Halloween and " + input1 + " was looking for a costume that was terrifying. They were a " + input2 + " which was difficult to find but they wanted to turn heads when they arrived at the Halloween Bash hosted by " + input3 + " . On the way to the Bash, they " + input4 + " into their arch nemesis, " + input5 + " who was a " + input6 + " ." + input7 + " said, 'Watch where you’re going weirdo! I hope that's not the costume you’re wearing to the Halloween Bash!' They igrnoed them. Before arriving at the Halloween Bash, " + input8 + " looked in the mirror and said, 'Wow, I look " + input9 + '. I will make ' + input10 + ' regret what they said!' " They arrived to the Bash, but it was dark and completely silent. They went to ring the doorbell with a shaky hand. The door opens and a " + input11 + " creature wearing a " + input12 + " looks down. They screamed and ran away, dropping their wig and went straight home.", font = "Times 8", bg = "white")
  i1.place(x = 205, y = 245)

def madlib2():
  input14 = input("enter plural noun : ")
  input15 = input("enter a famous person : ")
  input16 = input("enter a present tense verb : ")
  input17 = input("enter a body part : ")
  input18 = input("enter a random word : ")
  input19 = input("enter the same famous person : ")
  input20 = input("enter a big animal : ")
  input21 = input("enter a body part : ")
  
  i2 = tk.Label(root, wraplength = 600, text = "It was a scorchingly hot day in San Francisco and the scent of sweaty " + input14 + " wafted throughout the streets. " + input15 + " spots you by the ice cream stand and says, 'Yo let’s go " + input16 +  " around the city with my grandma!' We took an Uber to the mall and I couldn’t wait to get my sticky " +  input17 + " in that cold air conditioned building across from " + input18 + " street. After we hung out for a few hours, " + input19 + " had to run back home because their pet " + input20 + " was giving birth to twins. They left you stranded in the mall with nothing but a moist " + input21 + " and $2.", font = "Times 8", bg = "white")
  i2.place(x = 205, y = 245)

# Design features
tk.Button(root, text = "Spooky Halloween Night", font ="Times 8", command = madlib1, bg = "#ffc59c").place(x = 357, y = 120)
tk.Button(root, text = "Hot Day in San Francisco", font = "Times 8", command = madlib2 , bg = "#9ce1ff").place(x = 353, y = 180)
root.mainloop()