#readme
Instructions for the code on HW1

I have used the Python package pandas version 0.22.0 for this HW. In case you don't have the package installed please access the link: (https://pandas.pydata.org/pandas-docs/stable/install.html) to install pandas


The code consists of 6 functions and the only input to be provided to this function is the variable 'file' which should direct to the .csv file that you want to access.

Functions:
1) average_median(file)
	This function answers the second question of the HW#1. It uses the DictReader to access the column 'Final Score' and provides the required outputs

2) hardest_assignment(file)
	This function answers the third question of the HW#1. Here the assignments were considerd as Homeworks. Pandas is used to read the csv file. 
	In order to handle the data type error in case of an object e.g. 'EX' in this case if a student has exempted or not submitted the homework the string values are converted to numeric with an exception for the error

3) hardest_lab(file)
	This function answers the fourth question. Here the mean scores for the Lab quizes and Lab exercies are considered. 
	A mean of the Lab Quiz and Lab Exercise is calculated and thus the lab with the lowest mean was considered as the hardest lab.

4) student_grades(file)
	This function provides the numbers of the students who have got each grade. It also uses the pandas package and an if else data structure

5) student_complain_grade(file)
	This function finds out the number of the students which are within 0.5% of the maximum 
 