from graphics import *

output_list = []#inizilizing a list t0 print the final list and to make the text file

###### --- creating the histogram --- ######
def histogram(box):
    Win = GraphWin("Histogram", 800, 700)

    Total_result = box[0] + box[1] + box[2] + box[3] #getting the sum to show the total outcome in the histogram

    main_topic = Text(Point(110, 80), "Histogram Result")
    main_topic.setSize(17)
    main_topic.draw(Win)

    text_1 = Text(Point(125, 615), "Progress")
    text_1.setSize(14)
    text_1.setFill("dimgray")
    text_1.draw(Win)

    text_2 = Text(Point(305, 615), "Trailer")
    text_2.setSize(14)
    text_2.setFill("dimgray")
    text_2.draw(Win)

    text_3 = Text(Point(485, 615), "Retriever")
    text_3.setSize(14)
    text_3.setFill("dimgray")
    text_3.draw(Win)

    text_4 = Text(Point(665, 615), "Exclude")
    text_4.setSize(14)
    text_4.setFill("dimgray")
    text_4.draw(Win)

    text_5 = Text(Point(110, 670), Total_result)
    text_5.setSize(14)
    text_5.setFill("dimgray")
    text_5.draw(Win)

    text_6 = Text(Point(200, 670), "Outcomes in Total")
    text_6.setSize(14)
    text_6.setFill("dimgray")
    text_6.draw(Win)

    siimple_line = Line(Point(20,600),Point(780,600))# drawing a line 
    siimple_line.setWidth(4)
    siimple_line.draw(Win)

    result1 = Rectangle(Point(190, 600 - box[0] * 10), Point(60, 600))  # drawing first Progress Result
    count_text_1 = Text(Point(125, 585 - box[0] * 8), box[0])
    count_text_1.setSize(14)
    count_text_1.draw(Win)
    result1.setFill("Pale Green")
    result1.draw(Win)

    result2 = Rectangle(Point(370, 600 - box[1] * 10), Point(240, 600))  # drawing first Trailer Result
    count_text_2 = Text(Point(305, 585 - box[1] * 8), box[1])
    count_text_2.setSize(14)
    count_text_2.draw(Win)
    result2.setFill("green")
    result2.draw(Win)

    result3 = Rectangle(Point(550, 600 - box[2] * 10), Point(420, 600))  # drawing first Retriever Result
    count_text_3 = Text(Point(485, 585 - box[2] * 8), box[2])
    count_text_3.setSize(14)
    count_text_3.draw(Win)
    result3.setFill("dark green")
    result3.draw(Win)

    result4 = Rectangle(Point(730, 600 - box[3] * 10), Point(600, 600))  # drawing first Exclude Result
    count_text_4 = Text(Point(665, 585 - box[3] * 8), box[3])
    count_text_4.setSize(14)
    count_text_4.draw(Win)
    result4.setFill("light pink")
    result4.draw(Win)

    try:
        Win.getMouse()
        Win.close()
    except:
        Win.close()

def Correct_input(try_input):  # check the validity of input marks
    correct_number = True
    while correct_number:
        number = input(try_input)
        try:
            number = int(number)  # check the input marks is a integer
            if number not in [0, 20, 40, 60, 80, 100, 120]:  # check the marks are in the range
                print("out of range")
                continue
            return number
        except ValueError:
            print("Integer required")


def Perfect_Output(Pass_marks, Defer_marks, Fail_marks, R1, R2, R3, R4,):  # creating a function to get the student's result
    All_Marks = [Pass_marks, Defer_marks, Fail_marks]  # creating a list to get the input marks

    ######################## creating the condition to get the result #####################40
    if All_Marks == [120, 0, 0]:#cindition for progress
        output_list.append(f"Pogress - {All_Marks}")
        print("progress")
        R1 += 1

    elif All_Marks == [100, 20, 0] or All_Marks == [100, 0, 20]:#condition for progress(module trailer
        output_list.append(f"Progress (module trailer) - {All_Marks}")
        print("Progress(module trailer)")
        R2 += 1

    elif All_Marks == [80, 40, 0] or All_Marks == [80, 20, 20] or All_Marks == [80, 0, 40] \
        or All_Marks == [60, 60, 0] or All_Marks == [60, 40, 20] or All_Marks == [60, 20, 40] \
        or All_Marks == [60, 0, 60] or All_Marks == [40, 80, 0] or All_Marks == [40, 60, 20] \
        or All_Marks == [40, 60, 20] or All_Marks == [40, 40, 40] or All_Marks == [40, 20, 60] \
        or All_Marks == [20, 100, 0] or All_Marks == [20, 80, 20] or All_Marks == [20, 60, 40] or All_Marks == [20, 40,60] \
        or All_Marks == [20, 100, 0] or All_Marks == [20, 80, 20] or All_Marks == [20, 60, 40] or All_Marks == [20, 40,60] or All_Marks == [0,60,60]:
        output_list.append(f"Module retriever - {All_Marks}") #condition for do not progress - module retriever
        print("Do not progress -module retriever")
        R3 += 1

    else:
        All_Marks == [0, 40, 80] or All_Marks == [0, 20, 100] or All_Marks == [0, 0, 120] \
        or All_Marks == [20, 20, 100] or All_Marks == [20, 0, 100] or All_Marks == [40, 0, 80]#condition for Exclude
        output_list.append(f"Exclude - {All_Marks}")
        print("Exclude")
        R4 += 1

    return R1, R2, R3, R4,

######################################################################################################################################
################  Part 1 #############
def main():
    R1 = 0
    R2 = 0
    R3 = 0
    R4 = 0
    total_of_all = 0
    main_loop = True
    #################### user identifing in here ##########
    while True:
        try:
            user = input("Are you a student or a staff Member\n(please enter 'Student'if you are student and 'Staff' if you are a staff member  ) : ")
            if user.lower() not in ["staff","student"]:
                continue
            if user.lower() == "staff":

                while main_loop: # to run  this until user want to exit

                    Pass_marks = Correct_input("Enter your total PASS credits: ")#calling function to see the correct they input and assign it to pass marks
                    Defer_marks = Correct_input("Enter your total DEFER credits: ")#calling function to see the correct they input and assign it to defer marks
                    Fail_marks = Correct_input("Enter your total FAIL credits: ")#calling function to see the correct they input and assign it to fail marks
                    
                    total_of_all = Pass_marks + Defer_marks + Fail_marks #to get the total of all marks

                    if total_of_all != 120: #if total incorrect the it will ask the All marks again
                       print("Total incorrct")
                       continue

                    R1, R2, R3, R4, = Perfect_Output(Pass_marks, Defer_marks, Fail_marks, R1, R2, R3, R4)#calling the Function and assigning to a variable

                    while True:
                        continue_input = str(input("\nWould you like to enter another set of data\nEnter 'y' for yes or 'q' to quit and view results: "))  # while user want to exit still this work
                        if continue_input.lower() == "q":  # only this works when the user gave 'n'
                            break
                        elif continue_input.lower() == "y":  # only this works when the user gave 'y'
                            break
                        else:
                            continue
                    if continue_input.lower() == "q":  # if user gave 'q' it will exit
                        break
                    elif continue_input.lower() == "y":  # if user gave 'y' it will continue
                        continue
            
                Box = [R1, R2, R3, R4] #re-storing the data take in r1,r2,r3,r4 to list called box
                histogram(Box) #calling the function called histogram

########################################

######################  Part 2 #####################
                print("\npart 2")  # print the list
                for x in output_list:
                    print(x)
###################################################

#####################  Part 3 #####################
                fo = open("text.txt", "w+")
                print("\nPart 3")  # creating the file to store this results
                for i in output_list:
                    i = i.replace("[", "").replace("]", "")
                    fo.write(f"{i}\n")
                    print(i)
                fo.close()
                break#for end the loop
###################################################
            
            else:#this is for when user enter as a student
                 while True:#made a loop when the total incorrect 
                    Pass_marks = Correct_input("Enter your total PASS credits: ")#calling function to see the correct they input and assign it to pass marks
                    Defer_marks = Correct_input("Enter your total DEFER credits: ")#calling function to see the correct they input and assign it to defer marks
                    Fail_marks = Correct_input("Enter your total FAIL credits: ")#calling function to see the correct they input and assign it to fail marks
                    
                    total_of_all = Pass_marks + Defer_marks + Fail_marks #to get the total of all marks

                    if total_of_all != 120: #if total incorrect the it will ask the All marks again
                        print("Total incorrct")
                        continue
                    else:
                        Perfect_Output(Pass_marks, Defer_marks, Fail_marks, R1, R2, R3, R4)#only calling to the function/show the outcome
                    break#for end the main loop
                 break# end of this loop
        except ValueError:
          print("Enter user again")
main()
