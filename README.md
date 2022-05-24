# General Note

This is a tool written by G_MLo7 to make the process of making hed for NNSVS/ENUNU somewhat easier
Please keep in mind that the hed created by this script might need some manual touch up afterward

Dependencies: Python... yeah (I used 3.9.6)

~~You SHOULD NOT move/remove any of these files from the folder: "hedwriteicon.png" "cNp.txt" "HedWriter.exe"
(these 3 files should be in the same folder, if not, the software will throw you an error or not working at all)~~

If you found any other errors or bugs then please report to me via discord (MLo7#3256)

The codes I did for the script is too messy lmao I wasn't planned on putting it anywhere

# HOW TO USE
(The step by step/box by box name is pretty self explanatory but oh well)

1. Run the "HedWriter.exe"
	- Note: don't close the cmd window that is open when you run the exe, it will also exit out of the software

2. Enter your HED name
	- Note: there should be no space in the name, use underscore instead

3. Enter flag name/category
	- Note: this box is optional
	- Note: this box is just the name of the flag, it will not be put in the note for usage

4. Enter phoneme name/category
	- Note: you can put it as anything, preferably the type of phoneme
	- Note: this box is just the name of the phoneme, it will not be put in the note for usage

6. Enter flag syllable(s)
	- Note: this box is optional
	- Note: anything you put in this box will be used for flag in ENUNU/NNSVS usage/training

7. Enter your phoneme syllable(s)
	- Note: anything you put in this box will be used for phoneme in ENUNU/NNSVS usage/training
	- If you want to use the add too list then you most first press "create new list", ONLY change this input section tp "Add to list".
	   1) Press "New list" to eliminate the placeholder text
	   2) Redo the cycle of "create new list" again
	- Press "ADD" if you want to solely add the phoneme as individual


# Buttons

Get in_dim: get the value of in_dim that needs to be set for acoustic, timelag, and duration for training

Make Hed: copy the content in "cNp.txt" to the hed that you were making and change the extension from ".txt" to ".hed"


# Things that this program can't do (maybe yet)

- The ability to resume/edit the saved or other hed files
- The ability to remove/redo the phonemes/flags that were already added
- The ability to list what has already been added
- Something else I couldn't think of (?)


BTW you will need to keep pressing confirm each time you change the flag and phoneme name/category
Things will be recorded by the stuff on the right side


