from collections import OrderedDict
from Ellipse import Ellipse
from Circle import Circle
from Rhombus import Rhombus
from Shape import Shape
circleCount =0
ellipseCount = 0
rhombusCount = 0
shapeCount =0
shapes = [] #store shape objects in list
lineNB =0 # count the lines
errors=0 #count errors

quit = False # check if the user quits the program
print("""Choose the option:
    LOAD <file>
    TOSET
    SAVE <file>
    PRINT
    SUMMARY
    DETAILS
    QUIT""" )
while not quit: 
    user_input = input("Enter your option: ").split() #prompts user to choose the option

    if not user_input: #if no input
        continue

    option = user_input[0].upper() #checks the option

    if option == "LOAD": #option load
        if len(user_input) < 2: #check if user wrote a file
            print("Error: No file chosen")
            continue

        filename = user_input[1] #save users filename
        print("processing file ",filename) #message tells user thats being compiled
        try:
            with open(filename, "r") as file:
                for line in file:
                    lineNB +=1
                    words = line.split()

                    if words[0].lower() == "shape": #shape options
                        shapeCount +=1 #increment shape counter
                        shape = Shape() #create the shape object
                        shapes.append(shape) #adds it to the list
                        continue

                    elif words[0].lower() == "rhombus": #rhombus option
                        if len(words) < 3: # check if it has missing attributes
                            print("Error! missing attributes for rhombus")
                            errors+= 1 #increment errors if missing attributes
                            continue
                        d1 = int(words[1]) #initializes the attributes as floats
                        d2 = int(words[2]) #initializes the attributes as floats
                        if(d1 <=0 or d2<=0): #check if attributes are negative
                            print("Error! invalid Rhombus on line",lineNB,":",words[0],d1,d2)
                            errors+=1 #counts error if invalid attribute
                            continue #doesnt include it in the set
                        shape = Rhombus(d1, d2) #create shape object
                        shapes.append(shape) #adds it to the list
                        shapeCount +=1 #up the count
                        rhombusCount+=1 #up the count
                        continue
                        #same concept for other shapes  below 
                    elif words[0].lower() == "circle": #circle
                        if len(words) < 2: # check if it has missing attributes
                            print("Error! missing attributes for circle")
                            errors+= 1
                            continue
                        radius = int(words[1])
                        if(radius<=0):
                            print("Error! invalid Circle on line",lineNB,":",words[0],radius)
                            errors+=1 #counts error if invalid attribute
                            continue
                        shape = Circle(radius) 
                        shapes.append(shape)
                        shapeCount +=1
                        circleCount+=1
                        continue

                    elif words[0].lower() == "ellipse":
                        if len(words) < 3: # check if it has missing attributes
                            print("Error! missing attributes for ellipse")
                            errors+= 1
                            continue                        
                        a = int(words[1])
                        b = int(words[2])
                        if(a <=0 or b<=0):
                            print("Error! invalid Ellipse on line",lineNB,":",words[0],a,b)
                            errors+=1
                            continue
                        shape = Ellipse(a, b)
                        shapes.append(shape)
                        shapeCount +=1
                        ellipseCount+=1
                        continue 
                    else:
                        print(words[0], "invalid shape detected!") #if theres an invalid shape
                        errors+=1
                        continue


        except FileNotFoundError: #if file is not found
            print("error, file not found!!, make sure you add .txt after the file name")
            continue   

        print("Processed ", lineNB , " row(s),", shapeCount," shapes added,", errors, "error(s)") #prints the count of everything 

    elif option == "TOSET": #TOSET option
        if len(shapes) == 0: #if theres no objects in the list, error message prints
            print("Error! no shapes in multi-list!")
            continue
        shapes = list(OrderedDict.fromkeys(shapes)) # removes duplicates and preserves the order using OrderedDict
        print("multi-set converted! duplicates have been deleted")
        continue

    elif option == "SAVE": #save option
        if len(user_input) < 2: #if its missing the file name
            print("Error: No filename specified")
            continue

        filename = user_input[1]#assigns the file name to a variable
        try:
            with open(filename, "w") as file:
                for shape in shapes:
                    file.write(shape.attributes() + "\n") #writes the shapes to the file
            print("Shapes saved to", filename)
        except OSError:
            print("invalid or non-accessable file name! ") #if file cannot be created
            continue
        
    elif option == "PRINT": #print option
        print("printing shapes...")
        if len(shapes) == 0: #if theres no objects in the list, error message prints
            print("Error, no shapes!")
            continue
        for shape in shapes:
            print(shape.print(),shape) # prints the shapes using the print method and the overidden __str__ method for the additional  attributes
   

    elif option == "SUMMARY": #summary options
        print("generating summary...")
        if len(shapes) == 0: #if theres no objects in the list, error message prints
            print("Error! no shapes")
            continue
        print("Circle(s):",circleCount,"\nEllipse(s):",ellipseCount, "\nRhombus(es):", rhombusCount,"\nShape(s):",shapeCount) # prints count of every shape
        

    elif option == "DETAILS": # details option
        print("generating details...")
        if len(shapes) == 0: #if theres no objects in the list, error message prints
            print("Error! no shapes")
            continue
        for shape in shapes:
            print(shape.attributes()) #prints the nameand the attributes of every shape using the attributes method
        
      
    elif option == "QUIT": #quit option
        print("exiting program....")
        quit = True #exits the program 

    else:
        print("Invalid option!")
        continue
