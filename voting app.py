from tkinter import *
import time, socket, csv, sys
window1 = Tk()
window1.title("Voting app")
window1.geometry = ('300*100')
ip = socket.gethostbyname((socket.gethostbyname))
file=open("IP addresses.csv", "w")
file.write(ip)
file.close

if ip in open('IP addresses.csv').read():
    print("You have already voted. You cannot vote again.This message will shut down in 3 seconds.")
    time.sleep(3)
    sys.exit

print("**********Voting app*********")
file=open("Votes.csv", "w")

#def callLabour():
    #print("You voted for the Labour party.")
#def callConservatives():
    #print("You voted for the Conservative party")
#def callLibDems():
    #print("You voted for the Liberal Democart party.")
#def callGreen():
    #print("You voted for the Green party.")
#def callSpoil():
    #print("You have spoiled your ballot. Your vote will not be counted.")
party = Labour or Conservatives or LibDems or Green or Spoil
def callVote(party):
    print(party)

Labour=Button(window1, text="Labour party", bg="red", command=callVote("Labour"))
Labour.pack()

Conservatives=Button(window1, text="Conservative party", bg="blue", fg="white", command=callVote("Conservatives"))
Conservatives.pack()

LibDems=Button(window1, text="Liberal Democrats", bg="yellow", command=callVote("LibDems"))
LibDems.pack()

Green=Button(window1, text="Green", bg="green", command=callVote("Green"))
Green.pack()

Spoil=Button(window1, text="Spoil", bg="white", command=callVote("Spoil"))
Spoil.pack()

file=open("Votes.csv", "w")
file.write(Vote)
file.close

print("Thank you for voting. This window will shut down in 3 seonds.")
time.sleep(3)
sys.exit()
