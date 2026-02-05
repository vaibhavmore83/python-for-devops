# How to think before writing automation code

## Problem Statement
The application is generating multiple log files, and with Python, trying to figure out the count of how many statements are showing **INFO**, **WARNING** and **ERROR**.

## Input Parameters
The input is the application log file.

## Expected Output
The Python Script will read the application log file and print the count of **INFO**, **WARNING** and **ERROR** at terminal as well as to the jason file.

## Execution Plan
The execution steps includes
  -  Read the application log file using different file management commands.
  -  Browse through the lines from the file and identify **INFO**, **WARNING** and **ERROR** in each line.
  -  Count them using FOR loop and print at terminal.
  -  Write the count to the json file using json library.
