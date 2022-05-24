import sys
import os
import glob
import traceback
import fnmatch
import re
from tkinter import *

    #window screen overall
window = Tk()
window.title("HED writer version 0.1")

photo = PhotoImage(file = "hedwriteicon.png")
window.iconphoto(False, photo)

Label (window, text="Name your HED (there should be no space in the name, use underscore instead)", font="none 12 bold") .grid(row=1, column=0, sticky=W)
hedname = Entry(window, width=40, bg="green", font="none 12")
hedname.grid(row=2, column=0, sticky=W)
Label (window, text="Example: your_mom", font="none 12", fg="gray") .grid(row=1, column=1, sticky=W)

def click1():
    entered_name=hedname.get() #collect the data from name your HED section
    Label (window, text=f"HED name: {entered_name}", font="none 12 bold") .grid(row=3, column=1, sticky=W)
    with open(f"{entered_name}" + ".txt", "w") as f:
        f.write("")

    Label (window, text="Enter your flag name/category", font="none 12 bold") .grid(row=4, column=0, sticky=W)
    flagname = Entry(window, width=40, bg="green", font="none 12")
    flagname.grid(row=5, column=0, sticky=W)
    def flag_name():
        flag_name=flagname.get()
        Label (window, text=f"Flag name/category: {flag_name}", font="none 12 bold") .grid(row=6, column=1, sticky=W)
    Button(window, text="CONFIRM", width=8, command=flag_name) .grid(row=6, column=0, sticky=W)

    Label (window, text="Enter your phoneme name/category", font="none 12 bold") .grid(row=7, column=0, sticky=W)
    phonename = Entry(window, width=40, bg="green", font="none 12")
    phonename.grid(row=8, column=0, sticky=W)
    def phone_name():
        phone_name=phonename.get()
        Label (window, text=f"Phoneme name/category: {phone_name}", font="none 12 bold") .grid(row=9, column=1, sticky=W)

        def click2():
            entered_phoneme=phoneme.get() #collect the data from your phoneme section
            phone_name1=phonename.get()
            Label (window, text=f"Phone  [ {entered_phoneme} ] added to the list", font="none 12 bold") .grid(row=15, column=1, sticky=W)
            with open(f"{entered_name}.txt", "a+") as file:
                file.write("\n")
                file.write("QS          " + f'"L-phoneme_' + f'{entered_phoneme}"' + "          " + "{" + f"*^{entered_phoneme}-*" + "}\n")
                file.write("QS          " + f'"C-phoneme_' + f'{entered_phoneme}"' + "          " + "{" + f"*-{entered_phoneme}+*" + "}\n")
                file.write("QS          " + f'"R-phoneme_' + f'{entered_phoneme}"' + "          " + "{" + f"*+{entered_phoneme}=*" + "}\n")
        def click4():
            entered_phoneme=phoneme.get() #collect the data from your phoneme section
            phone_name1=phonename.get()
            Label (window, text=f"Phone  [ {entered_phoneme} ] added to the list", font="none 12 bold") .grid(row=15, column=1, sticky=W)
            with open(f"{entered_name}.txt", "a+") as file:
                file.write("\n")
                file.write("QS          " + f'"L-phoneme_' + f'{phone_name1}"' + "          " + "{" + f"*^{entered_phoneme}-*" + "tobereplace}\n")
                file.write("QS          " + f'"C-phoneme_' + f'{phone_name1}"' + "          " + "{" + f"*-{entered_phoneme}+*" + "tobereplace}\n")
                file.write("QS          " + f'"R-phoneme_' + f'{phone_name1}"' + "          " + "{" + f"*+{entered_phoneme}=*" + "tobereplace}\n")
        def click5():
            entered_phoneme=phoneme.get() #collect the data from your phoneme section
            phone_name1=phonename.get()
            replacerL = "-*," + f"*^{entered_phoneme}-*" + "tobereplace}"
            replacerC = "+*," + f"*-{entered_phoneme}+*" + "tobereplace}"
            replacerR = "=*," + f"*+{entered_phoneme}=*" + "tobereplace}"
            with open(f"{entered_name}.txt") as file:
                s = file.read()
            s = s.replace("-*tobereplace}", replacerL )
            s = s.replace("+*tobereplace}", replacerC )
            s = s.replace("=*tobereplace}", replacerR )
            with open(f"{entered_name}.txt", "w") as file:
                file.write(s)
        def click6():
            with open(f"{entered_name}.txt") as file:
                s = file.read()
            s = s.replace("tobereplace", "")
            with open(f"{entered_name}.txt", "w") as file:
                file.write(s)
        Label (window, text="Enter your phoneme syllable(s)", font="none 12 bold") .grid(row=13, column=0, sticky=W)
        Button(window, text="ADD", width=8, command=click2) .grid(row=17, column=0, sticky=W)
        Button(window, text="Create List", width=8, command=click4) .grid(row=15, column=0, sticky=W)
        Button(window, text="Add to List", width=8, command=click5) .grid(row=16, column=0, sticky=W)
        Button(window, text="New List", width=8, command=click6) .grid(row=18, column=0, sticky=W)
        phoneme = Entry(window, width=40, bg="green", font="none 12")
        phoneme.grid(row=14, column=0, sticky=W)

        def click3():
            entered_flag=flag.get() #collect the data from your flag section
            flag_name1=flagname.get()
            Label (window, text=f"Flag  [ {entered_flag} ] added to the list", font="none 12 bold") .grid(row=12, column=1, sticky=W)
            with open(f"{entered_name}.txt", "a+") as file:
                file.write("QS          " + f'"flag_' + f'{flag_name1}"' + "          " + "{" + f"*^{entered_flag}_*" + "}\n")

        Label (window, text="Enter your flag syllable(s)", font="none 12 bold") .grid(row=10, column=0, sticky=W)
        Button(window, text="ADD", width=8, command=click3) .grid(row=12, column=0, sticky=W)
        flag = Entry(window, width=40, bg="green", font="none 12")
        flag.grid(row=11, column=0, sticky=W)


    Button(window, text="CONFIRM", width=8, command=phone_name) .grid(row=9, column=0, sticky=W)
    Label (window, text=" ", font="none 12 bold") .grid(row=19, column=0, sticky=W)
    Label (window, text=" ", font="none 12 bold") .grid(row=20, column=0, sticky=W)
    Label (window, text=" ", font="none 12 bold") .grid(row=21, column=0, sticky=W)
    Label (window, text="click this button AFTER you click [Make HED]", font="none 12 bold", fg="gray") .grid(row=22, column=0, sticky=W)

    def get_indim_value():
        with open(f"{entered_name}.hed", "r") as linecount:
            indim = linecount.read()
            indim_count = sum(1 for match in re.finditer("QS", indim))
            indim_count4acoustic = indim_count + 4
            Label (window, text=f"in_dims:", font="none 12 bold") .grid(row=23, column=0, sticky=W)
            Label (window, text=f"acoustic [ {indim_count4acoustic} ]", font="none 12") .grid(row=24, column=0, sticky=W)
            Label (window, text=f"timelag [ {indim_count} ]", font="none 12") .grid(row=25, column=0, sticky=W)
            Label (window, text=f"duration [ {indim_count} ]", font="none 12") .grid(row=26, column=0, sticky=W)
    Button(window, text="Get in_dim", width=8, command=get_indim_value) .grid(row=23, column=0, sticky=W)

    def touch_cqs():
        with open("cNp.txt", "r") as CQS_content, open(f"{entered_name}.txt", "a") as final_hed:
            for line in CQS_content:
                final_hed.write(line)
        for file in glob.glob(f"{entered_name}" + ".txt"):
            base = os.path.splitext(file)[0]
            os.rename(file, base + ".hed")

        Label (window, text=f"{entered_name}.hed built successfully", font="none 12", fg="green") .grid(row=21, column=1, sticky=W)

    Button(window, text="Make Hed", width=8, command=touch_cqs) .grid(row=23, column=1, sticky=W)




Button(window, text="CONFIRM", width=8, command=click1) .grid(row=3, column=0, sticky=W)








    #main loop
window.mainloop()
