import os,sys,time,random

def TopScoresList():
    with open("winners.txt","r") as x:
        k=x.readlines()
    names=[]
    for i in k:
        i=i.rstrip("\n")
        i=i.split(",")
        names.append([i[1],i[0]])
        scores=[]
        for i in names:
            scores.append(i[0])
        scores=sorted(set(scores),reverse=True)
    if len(k)<=4:
        for i in scores:
            for n in names:
                if i==n[0]:
                    print(n[1],":",n[0])
    else:
        for i in scores[:4]:
            for n in names:
                if i==n[0]:
                    print(n[1],":",n[0])
def SaveToFile(pname,total):
    if os.path.exists("winners.txt") and os.path.isfile("winners.txt"):
        with open("winners.txt","a+") as x:
            rec=pname+","+str(total)+"\n"
            x.write(rec)
            TopScoresList()


def playgame(p11,p12):
    pname=[]
    total=0
    p11_total=0
    p11maxtotal=0
    p12_total=0
    p12maxtotal=0

    i=1
    while i<=5:
        i=i+1

        ans=input("player1,type 'r'to roll two 6 sided dice:")
        if ans=="r":
            x=random.randint(1,6)
            y=random.randint(1,6)
            print("Player-1 score is :",x,y)
            #print("Player-1 dice-1:",y)
            if x==y:
                print("Wow!",p11," congracts, you get one more chanceto roll dice")
                ans=input("player1,type 'r'to roll two 6 sided dice:")
                if ans=="r":
                    z=random.randint(1,6)
                    print("Player-1 dice-1:",z)
                    p11maxtotal=z+p11maxtotal

            p11_total=x+y
            p11maxtotal=p11maxtotal+p11_total
            print("Player",p11,"total score is :",p11_total, "and", p11maxtotal)

        ans=input("player2,type 'r'to roll two 6 sided dice:")
        if ans=="r":
            x=random.randint(1,6)
            y=random.randint(1,6)
            print("Player-2 score is :",x,y)
            #print("Player-2 dice-2:",y)
            
            if x==y:
                print("Wow!",p12," congracts, you get one more chanceto roll dice")
                ans=input("player2,type 'r'to roll two 6 sided dice:")
                if ans=="r":
                    z=random.randint(1,6)
                    print("Player-2 dice-1:",z)
                    p12maxtotal=z+p12maxtotal
                    #p12maxtotal=p12maxtotal+p12_total
                    #print("Player",p12,"total score is :",p12_total, "and", p12maxtotal)

            p12_total=x+y
            p12maxtotal=p12maxtotal+p12_total
            print("Player",p12,"total score is :",p12_total, "and", p12maxtotal)
            
                #p11maxtotal=p11maxtotal+p11_total
                    #print("Player",p11,"total score is :",p11_total, "and", p11maxtotal)
    if p11maxtotal%2==0:
        p11maxtotal+=10
            #print("Player",p11,"final total score is :",p11maxtotal)
    else:
        p11maxtotal-=5
            #print("Player",p11,"final total score is :",p11maxtotal)
    print("Player",p11,"final total score is :",p11maxtotal)

    if p12maxtotal%2==0:
        p12maxtotal+=10
    #print("Player",p12,"final total score is :",p12maxtotal)
    else:
        p12maxtotal-=5
    #print("Player",p12,"final total score is :",p12maxtotal)
    print("Player",p12,"final total score is :",p12maxtotal)

    print("\t\t\t Final winner")
    
    print("."*80)
    print("Player",p11,"total score is :",p11_total, "and", p11maxtotal)
    print("Player",p12,"total score is :",p12_total, "and", p12maxtotal)
    
    if p11maxtotal == p12maxtotal:
        print("Both players scores are same,please roll again")
        ans=input("player1,type'r'to roll two 6 sided dice:")
        if ans=="r":
            x=random.randint(1,6)
            print("Player-1 dice-1:",x)
        ans=input("player2,type'r'to roll two 6 sided dice:")
        if ans=="r":
            y=random.randint(1,6)
            print("Player-2 dice-1:",y)
        if x>y:
            pname=p11
            total=p11maxtotal
            print("player-1",p11,"won",total)
        elif x<y:
            pname=p12
            total=p12maxtotal
            print("player-2",p12,"won",total)
        else:
            total=0
            pname="Game tie"
            print("Game tie")
    elif p11maxtotal>p12maxtotal:
        pname=p11
        total=p11maxtotal
        print("player-1",p11,"won and his total is",total )
    else:
        pname=p12
        total=p12maxtotal
        print("player-2",p12,"won and his total is", total)
    print("."*80)
    SaveToFile(pname,total)
    
def check(p11,p12):
    for i in p12:
        i=i.split(",")
        if i[0]==p11:
            print(p11,"welcome to play the game,..")
            break

    else:
        print("sorry,you are not a valid player",p11)
        p11=input("enter a player name : ")
        check(p11,p12)
      
def signin():
    with open("dice.txt","r") as x:
        k=x.readlines()
    sname1=input("enter username 1 : ")
    check(sname1,k)
    sname2=input("enter a username 2: ")
    check(sname2,k)
    playgame(sname1,sname2)
    
def checkuser(a):
    if os.path.exists("dice.txt") and os.path.isfile("dice.txt"):
        with open("dice.txt","r") as x:
            k=x.readlines()
            users=[]
            for i in k:
                i=i.split(",")
                users.append(i[0])
            if a in users:
                print(a,"user already exist")
                print("plz choose other than this user",users)
                uname=input("enter your name : ")
                a=checkuser(uname)
                return a
            else:
                return a
    else:
        return a

def register():
    uname=input("enter new name : ")
    uname=checkuser(uname)
    upassword=input("enter a password : ")
    ph_no=input("enter a phone number : ")
    email=input("enter a email : ")
    rec=uname+","+upassword+","+ph_no+","+email+"\n"
    with open("dice.txt","a") as x:
        x.write(rec)
    print("registered successfully")
    time.sleep(5)
    main()

def main():
    print("welcome to tecno game station")
    print("main menu")
    print("1.sign in") 
    print("2.sign up")
    print("3.exit")
    ans=int(input("enter option to proceed : "))
    
    if ans==1:
        signin()

    elif ans==2:
        register()

    else:
        print("thank you for your interest")
        sys.exit()

if __name__=="__main__":
    main()


