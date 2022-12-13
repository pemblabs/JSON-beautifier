# JSON-beautifier
A simple json beautifier that you can run locally on your machine

The reason:

As a cybersecurity analyst I am often exposed with logs written in JSON formats 
Many of the SIEMs and log agregattors as well have the option to write logs in JSON format
Which some that can be hard to read due to lack of indentation(oneliners)

Granted there are many JSON beautifiers online that you can run whithin a browser
From my experience they don't seem to focus on security or is hard to find security documentation
JSON logs can contain secrets that you dont want to run on the internet
So I decided to write this simple code that you can run locally to help you do your job
Whether you are a security analyst or simply someone who has to read lots of JSON to  make decision

How To USE:
1- You will be prompt with a menu option
2- Choose option 1 by typing and press ENTER
3- A file explorer opens
4- Navigate to the file with JSON data format you wish to read
5- Filetypes can be .JSON or .TXT files
6- Select a file and click open you 
7- Once you do that a beautified JSON will be printed in the console

PS: you can still read another file by choosing the same option or type 0 and press enter to quit
