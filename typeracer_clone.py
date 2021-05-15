import tkinter
import random
import time
import tkinter.messagebox


data= ["With gene therapy.","hello"]
main= tkinter.Tk()
# w, h = main.winfo_screenwidth(), main.winfo_screenheight()
# main.geometry("%dx%d+0+0" % (w, h))
variable= tkinter.StringVar()
random_text= random.choice(data)
modifiable_text= random_text
text_input =""
index=0
index_savepoint=0
charSuccess_count=0
charFail=0

entry = tkinter.Entry(main,textvariable= variable,width=200)
entry.pack()
entry.focus()

startTime= time.time()

    
def showChar(event):
    print(event.keysym)
    global variable,index,random_text
    print("index: ",index)
    variableStr= variable.get()
    global index_savepoint, modifiable_text
    global charSuccess_count,charFail
    if event.keysym=="BackSpace":
        if index > index_savepoint :
            index =index -1
            if charFail ==0 :
                charSuccess_count = charSuccess_count-1
            else:
                charFail = charFail -1
    else:
        if event.keysym != "Shift_L":
            index= index+1
            if event.keysym == "space":
                if (verifyText(" ",modifiable_text,index-1)):
                    print("char: ",event.char)
                    entry.delete(0,"end")
                    index_savepoint= index
            else:

                verifyText(event.char,modifiable_text,index-1)
                print("char: ",event.char)
    print("success: ",charSuccess_count)
        
    
    print(modifiable_text)
#     if verifyText(variableStr,modifiable_text)==True:
#         if variableStr != "":
#             charSuccess_count= charSuccess_count +1
#     else:
#         pass
    print("charfail:",charSuccess_count,charFail)
    display(charSuccess_count,charFail)
    if charSuccess_count == len(random_text):
        showMessage()
    print("index after: ",index)
    

    
    
def display(charSuccess_count,charFail):
    text.tag_delete("green")
    text.tag_delete("red")
    text.tag_add("green","1.0","1."+str(charSuccess_count))
    text.tag_config("green",foreground="green",background="red")
    text.tag_add("red","1."+str(charSuccess_count),"1."+str(charSuccess_count+charFail))
    text.tag_config("red",foreground="red",background="green")

def verifyText(symbol,modifiable_text,index):
    global charSuccess_count,charFail, random_text
    if symbol !="":
        if symbol == modifiable_text[index]:
            if charFail ==0:
                charSuccess_count = charSuccess_count +1
                return True
        charFail = charFail +1
        return False
    
        
def showMessage():
    global startTime, charFail, charSuccess_count, random_text, index, index_savepoint,modifiable_text
    endTime = time.time()
    
    timeUsed="TIME:"+str(endTime-startTime)
    startTime= endTime
    question=tkinter.messagebox.askyesno(message=timeUsed)
    if question == True:
        """restart()"""
        charFail= 0
        charSuccess_count=0
        random_text= random.choice(data)
        modifiable_text = random_text

        index=0
        index_savepoint=0
        text.configure(state="normal")
        text.delete("1.0","end")
        entry.delete(0,"end")
        text.insert("end", random_text)
        text.configure(state="disabled")



entry.bind_all("<KeyPress>",showChar)

text = tkinter.Text(main,height =10)
text.pack()
text.insert("end",random_text)
text.configure(state="disabled") # you have to insert the text first and then disable the input



main.mainloop()
