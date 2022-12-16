print("Howdy Cowboys and cowgirls are you ready for a wild crazy ride on a horse with a mind of its own? ")
print("\nBefore we begin there are just a few questions I need you to answer")
print("After entering your answer please press the enter key ")

input("\nPress the enter key to begin...")

Keepgoing = ("Y")

while Keepgoing.lower() == "y":

    RanchName = input("\nWhat is the name of the ranch:  ")
    while (len(RanchName) == 0):
            RanchName = input("please input a ranch name ")
    Location = input("\nWhat is the name of a small town near you: ")
    while (len(Location) == 0):
            Location = input("Please enter a small town near you ")
    State = input("\nWhat state are you from: ")
    while (len(State) == 0):
            State = input("Please enter the name of your state ")
    Number = input("\nwhat is your favorite number: ")
    while (len(Number) == 0):
            Number = input("Please enter a number I.E. 1,2,3 ")
    YourName = input("\nWhat is your name: ")
    while (len(YourName) == 0):
            YourName = input("Please enter your name ")
    Color = input("\nWhat is your favorite color: ")
    while (len(Color) == 0):
            Color = input("Please enter a color ")
    HorseBreed = input("\nbreed of a horse: ")
    while (len(HorseBreed) == 0):
            HorseBreed = input("Please enter the breed of a horse ")
    HorsesName = input("\nWhat is the horses name: ")
    while (len(HorsesName) == 0):
            HorsesName = input("Please name your horse ")

    print("\nYEHAWWW!! let's ride!!!!!")

    print("\nOur adventurous trail ride begins at, " + RanchName + " in " + Location + "," + State + ".")
    print(RanchName,"is nestled on " + Number +  " acres surounded by picture perfect scenary. ")
    print(YourName, "Recently purchased a beautiful " + Number + " year old " + Color + "," + HorseBreed + " named, "  + HorsesName +  ". ")
    print("It's a beautiful early Saturday morng in, " + Location + ", " + State + ".")
    print(YourName,"decides to take " + HorsesName + ", for a trail ride for the first time. ")
    print("Wanting to be home before sunset, " + YourName + " saddles up, " + HorsesName + ". ")
    print("Excited, " + YourName + " and " + HorsesName + " set on thier first adventure together. ")
    print(YourName, "takes a deep breath of fresh air and can feel the stress of college, work, and every day life just disapear. ")
    
    print("\nSuddenly, " + HorsesName + " starts to trot!!! ")
    print("Although a little confused " + YourName + " doesn't mind the slight increase in speed. ")
    print("After trotting for ten minutes, " + HorsesName + " BEGINS TO CANTER!! ")
    print(YourName, " is having so much fun!! ")
    print("After cantering for five minutes, " + YourName + " starts to think about seeing how fast " + HorsesName + " can gallop. ")

    Gallop = input("\nShould " + YourName + " see how fast " + HorsesName + " can gallop type y or n: ")
    while (len(Gallop) == 0):
            Gallop = input("Please type y or n ")
    
    if Gallop.lower() == "y":
        print(YourName, "\nis loving this ride! ")
        print(YourName,"decides to see just how fast this " + HorseBreed + " can gallop . ")
        print(YourName, "loosens the reins, and " + HorsesName + " begins walking. ")
        print("Although confused, " + YourName + " just decides to go with the flow. ")

    else:
      print(YourName, "doesn't feel comfortable running with " + HorsesName + ", at this time ")
      print("tightening the reins causes, " + HorsesName + " to gallop!!! ")
      print("Puzzeled at " + HorsesName + "'s actions " + YourName + " just decides to go with the flow." )
      print("loosening the reins, causes, " + HorsesName + " to slow to a walk. ")
      print(YourName, "is really confused by " + HorsesName + "'s actions and wonders what is really going on with this crazy " + HorseBreed + "? ")
      
    print("\nAfter riding several miles, " + YourName + " comes to a fork in the trail.")
    print(YourName, "realizes they must have taken a different trail and wonders which trail to take.")

    Direction = input("\nshould " + YourName + " take the trail on the righ? type y or n ")
    
    while (len(Direction) == 0):
            Direction = input(" Must decide if " + UserName + " should go to the right please type y oy n ")
    
    if Direction.lower() == "y":
        print(HorsesName,"starts to kick and buck while neighing loudly, and canters down the trail on the left. ")
        print(YourName,"begins to wonder what is going on with this crazy " + HorseBreed + "?")
        print("After " + HorsesName + ", calms down " + YourName + " settles back in the saddle and enjoys the ride ")
        print("Daydreaming " + YourName + " loses tract of time when suddenly, " + HorsesName + " stops, causing ." + YourName + "to snap back to reality ")
        print(YourName, "realizes the reason, " + HorsesName + " stopped was because the came to a narrow river. ")

        Cross = input("\nDoes " + YourName + " cross the river? please type y or n ")
        
        while (len(Cross) == 0):
            Cross = input("Please choose to cross the river or not please type y or n ")
        
        if Cross.lower() == "y":
            print("\nAttempts to the cross the river but " + HorsesName + " doesn't want to have any of that and rears up and turns to to run in the same direction you just came . ")
            print(YourName, " tries to stop " + HorsesName + " but to no avail, " + HorsesName + " canters all the way back to the fork in the trail and goes down the right trail. ")
            print("After " + HorsesName + " Calms down " + YourName + " Settles back in the saddle and begins to take in the beautiful scenery and the fresh clean air once again ")
            print("After enjoing the relaxing ride and taking in the beautiful scenery for several miles, " +YourName + " comes to an open field and can see " + RanchName + "in the distance ")
            print("remembering tightning the riens caused, " + HorsesName + "to gallop")
            print(YourName, "tightens the riens and, " + HorsesName + " stops. ")
            print(YourName, "chuckles and loosens the reins and kicks " + HorsesName + " gently in the sides, " + HorsesName + " starts to canter back to " + RanchName + ".")
            print(YourName, "and " + HorsesName + " finally make it back to " + RanchName + ".")
            print("\nAs " + YourName + " dismounts the saddle," + HorsesName + " rubs up against " + YourName + " as if looking for approval for an adventurous and exciting trail ride. ")
            print(YourName, "could not resist, and gives " + HorsesName + " a hug. Although not making it back before sunset, it has been an advertrous wild ride. ")

        else:
            print(YourName, "\nDoesn't want to get wet, and tries to turn " + HorsesName + " around. ")
            print(HorsesName, "Bolts across the river. ")
            print("As they get to the other side of the river, " + YourName + " can see " + RanchName + " across an open field. ")
            print(YourName, "lossens the riens, and gently kicks, " + HorsesName + " in the sides, " + HorsesName + " starts to canter towards " + RanchName + "." )
            print("Getting back to " + RanchName + "," + YourName + " dismounts the saddle a little confused but happy ")
            print(HorsesName, "Snuggles up to " + YourName + " looking for approval for such an adveturous fun filled day ")
            print(YourName, " Smiling, just couldn't resist and gives " + HorsesName + " a big hug after all it has been a fun adventure and they were back before sunset ")

    else:
      print(HorsesName,"\nrears up and whinny's loudly, and runs down the trail on the right. ")
      print("After  " + HorsesName + " Calms down " + YourName + " Settles back in the saddle and begins to take in the beautiful scenery and the fresh clean air once again ")
      print(" After enjoing the relaxing ride and taking in the beautiful scenery for several miles, " +YourName + " comes to an open field and can see " + RanchName + "in the distance ")
      print(YourName, "remembers pulling the riens back, " + HorsesName + "ran faster however, this time pulling the riens back caused, " + HorsesName + " to slow down")
      print(YourName, "and " + HorsesName + " finally make it back to " + RanchName + ".")
      print("\nAs " + YourName + " dismounts the saddle, " + HorsesName + " starts to snuggle up to you, as if looking for approval for an adventurous and exciting trail ride. ")
      print(YourName, "could not resist, and gives " + HorsesName + " a hug. After all they were home before sunset. ")
      
    Keepgoing = input("Would you like to play again Please type y or n ")
    while (len(Keepgoing) == 0):
            Keepgoing = input("can not be blank please type y or n")