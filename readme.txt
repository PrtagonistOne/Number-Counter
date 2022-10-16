cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c		     Number_counter V0.2           		     c
c		     Oleksandr Kopiievyi (C)  	  	     c
cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

This program currently supports following formats of files - .xlsx, .xlsm, .xltx, .xltm.


Conditions to work properly.

1. Run the script from the folder containing the wanted excel file, make sure it is in one pf the formats that are currently supported.
2. Make sure it is the only one excel file.
3. - In excel file Column 3( or C) is reserved for Initial Set number
- Column 4 (or D) is reserved for Target number.
- Column 5 (or E) is reserved for the Results.
- Column 6 (or F) is reserved for the potential new Target number, if from provided intial set, the equation is not possible. (The number would be a closest to, but greater than the original target number).
4. After running the script, just follow the prompts instructions.
5. After every calculation, you need to reopne the excel file to see the updated changes.
6. You can ran the script ones, but the excel file would need to be reopened each time to see te results.
7. Do not forget that after you change the target and/or initial set to save the excel file.



Updates v0.2:
- Reduced memory usage
- Increased the speed of calculation
- Added time tracking 
 
