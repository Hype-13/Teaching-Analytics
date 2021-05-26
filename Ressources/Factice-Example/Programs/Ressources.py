###########################################
# digitource par Cours par Année (Factice) #        
###########################################

#Import the required packages
from math import *
import numpy as np
from numpy.core.numeric import NaN
import pandas as pd
import random
import seaborn as sns
import matplotlib.pyplot as plt
import os 
import time


########
# Time #
########

start_time = time.time()


################
#Find the Path #
################

dir_path = os.path.dirname(__file__) #Find the directory path of the current python «FolderCreation» file.
keywords = ['Ressources', 'Factice-Example'] #Determine the keywords that will take the folder position.
folder_name = 'Data' #Name of the Data folder.

glob_path = '/'.join(dir_path.split('/')[(dir_path.split('/').index(keywords[0])):(dir_path.split('/').index(keywords[1]) + 1)])  #Find the General Path
path_data = glob_path + '/' + folder_name + '/'  #Path of the Data Folder


#####################################################
# Initialize a pseudorandom number generator (seed) #
#####################################################

#Define a seed to preserve the same values randomly obtained after each execution.
random.seed( 2000 ) #The seed does not need to be randomize


######################
# Class and Function #
######################

#A class of functions to implement the «Interval» from a value with range
class Interval(object):
    def __init__(self, middle, deviation):
        self.lower = middle - abs(deviation)
        self.upper = middle + abs(deviation)

    def __contains__(self, item):
        return self.lower <= item <= self.upper

def interval(middle, deviation):
    return Interval(middle, deviation)


def Digit_Ratio(CourseID, lst_CoursesID, Lst_Ratio):
    if CourseID in lst_CoursesID:  #In case the selected ID has been already implemented (for a previous year), we keep the same duration.
        inside = True #Set the variable to «False».
        ins = [courses for courses in range(0, len(lst_CoursesID)) if lst_CoursesID[courses] == CourseID] #Find the index of the identical ID as the current «course» selected ID.    
        #Create a while loop to compute the ratio/percentage of digitalization.
        while (inside == True): 
            if Lst_Ratio[ins[-1]] == 0:
                ratio = round(random.uniform(0.1,0.35),2)
            else:
                ratio = Lst_Ratio[ins[-1]] * round(random.uniform(1,1.25),2) #Compute the new ratio from the previous one.
            
            if ratio <= 1: #We can not have a ratio above 1.
                inside = False #Since the conditions is respe
    else:
        ratio = round(random.uniform(0,0.5),2) #Ratio of digitalization.
    return(ratio)


#Function to modify the type of a columns which required the name of the dataframe, of the specic column(s) and associated type(s).
def type_modif(df, lst_columns, lst_type):
    for col, typ in zip(lst_columns, lst_type):
        df[col] = df[col].astype(typ)
    return df


################
# Factice Data #
################

###################################################
# Build the factice Departments (number and type) #
###################################################

#Define a list of departements.
depts_type = ['Economy', 'History', 'Law', 'Management', 'Art', 'Sociology', 'Mathematics', 'Engineering', 'Philosophy', 'Computer Science', 'Languages']
depts_descrp = []

#Take a random integer representing the number of departments (at least 10 departments).
num_depts = random.randint(10, len(depts_type))

#Append the type of each department.
temp_Depts = []
num = 0
while num < num_depts: #Loop to implement the type of each department.
    ran_num = random.randint(0, len(depts_type)-1) #Randomly select a type of department.
    if depts_type[ran_num] not in temp_Depts: #Verify that the selected department is not already implemented in the list.
        temp_Depts.append(depts_type[ran_num]) #Append the select department into the list.
        num += 1  #Incremente the number of department in the list. 

#Display the number of departments and the type of each of them.
print('\nNumber of Departments:', num_depts)   
print('List of Departments:', temp_Depts, '\n')


#####################################
# Build the factice Year (interval) #
#####################################

#Create a list to represent the year interval (from 2013 to 2020).
temp_Years = [year for year in range(2013, 2021)]

#Display the number of departments and the type of each of them.
print('Number of Years:', len(temp_Years))   
print('Year Interval:', temp_Years, '\n')


#########################################################################
# Build the factice Teaching-research Personnel (number per department) #
#########################################################################

#Define the number of teacher per department
temp_NumbTRP = []
num_teachers = 0
for depts in temp_Depts:
    ran_ppl = random.randint(5, 8)  #Random number that represents the number of teachers in the current department.
    num_teachers += ran_ppl
    temp_NumbTRP.append(ran_ppl)

#Display the number of departments and the type of each of them.
print('Total Number of Teachers:', num_teachers)   
print('Number of Teachers per Department', temp_NumbTRP, '\n')


################################################
# Build Ressources DataFrame with related Data #
################################################

#Define the DataFrame columns
Ressources = pd.DataFrame({})
Ressources = Ressources.assign(Department = str(),
                               Teacher_ID = int(),
                               Teacher_Name = str(),
                               Year = int(),                                    
                               Course_ID = int(),
                               Course_Duration = int(),
                               Course_Ressources = int(),
                               Course_Ress_Digit = int(),
                               Course_Ress_inClass = int(),
                               Digitalization_Ressource_Ratio = float(),
                               Digitalization_Ressource_Percent = int())

#Import a CSV file containing the most common names from France (sample of 3.378).
Random_ComName = pd.read_csv(path_data + 'Data-Names/French_Names_Lgh3378.csv').reset_index() #Import the CSV containing some common names

#Initial Teaching-research Personnel Information.
PRAG_Hour = 384 #Average Minimal (Hours of teaching) - PRAG.
PRCE_Hour = 192 #Average Minimal (Hours of teaching) - PRCE.
Prop_PRAG_on_PRCE = (8000)/(8000+6000) #PRAG/(PRAG+PRCE)

#Set temporal list 
lst_Digit_Ratio = [] #List that represents the ratio used to compute the next.
lst_Course_ID = [] #List that represents the ID of the course used to compute the ratio.

#Set temporal variables
dep = 0                     #Variable used to implement Department. 
teacher_ID = 0              #Variable used to implement «Teacher_ID».
course_ID = 1               #Variable used to implement «Course_ID».
index = 0                   #Variable used to implement values in the DataFrame.

#Loop to implemente the above DataFrame.
for teachers in temp_NumbTRP: #Loop that take the number of teachers per departments.
    dep += 1  #Increase the dep corresponding the index of the lists to implement.
    for i in range(0, teachers): #Loop that take all the teachers for the current department.
        teacher_ID += 1 #Increase the teacher_ID
        rand_name = random.randint(0, len(Random_ComName['Last_Name'])-1) #Select randomly a name from the database of most common names.
        rand_num = random.random() #Define a random number to find the type of teacher (PRAG/PRCE).

        if (0 <= rand_num <= Prop_PRAG_on_PRCE):
            temp = 0 #Set the temporary variable to compute the total hours worked by a teacher
            while temp not in interval(middle=PRAG_Hour, deviation=PRAG_Hour*0.05):
                ran_courses = random.random()  #Define a random number to choose the time interval of a course.
                if (0 <= ran_courses < 0.4) : 
                    Course_Duration = random.randint(5, 15)   #Define a random number to have a course between 5H and 15H.
                elif (0.4 <= ran_courses < 0.9) :
                    Course_Duration = random.randint(15, 40)   #Define a random number to have a course between 15H and 40H.
                elif (0.9 <= ran_courses < 1):
                    Course_Duration = random.randint(40, 60)   #Define a random number to have a course between 40H and 60H.
                else:
                    Course_Duration = random.randint(60, 90)   #Define a random number to have a course between 60H and 90H. 
                Course_Ressource = random.randint(ceil(Course_Duration/4), Course_Duration)
                
                if temp + Course_Duration <= PRAG_Hour*1.05: #Verify that the possible number of courses teached is lower than the amount of hours to teach.
                    for year in temp_Years: #Loop to implement all the years.
                        ratio = Digit_Ratio(course_ID,  lst_Course_ID,  lst_Digit_Ratio) #Find the ratio of digitalization
                        Digit_Ressource = ceil(Course_Ressource * ratio)
                        if year != temp_Years[0]:
                            if Ressources['Course_Ress_Digit'].iloc[-1] > Digit_Ressource:
                                Digit_Ressource =  Ressources['Course_Ress_Digit'].iloc[-1]
                        inClass_Ressource = Course_Ressource - Digit_Ressource

                        #Append the lists
                        lst_Digit_Ratio.append(ratio)
                        lst_Course_ID.append(course_ID)

                        Ressources.loc[index, 'Department'] = temp_Depts[dep-1]
                        Ressources.loc[index, 'Teacher_ID'] = teacher_ID
                        Ressources.loc[index, 'Teacher_Name'] = Random_ComName['Last_Name'][rand_name]
                        Ressources.loc[index, 'Year'] = year
                        Ressources.loc[index, 'Course_ID'] = course_ID
                        Ressources.loc[index, 'Course_Duration'] = Course_Duration
                        Ressources.loc[index, 'Course_Ressources'] = Course_Ressource
                        Ressources.loc[index, 'Course_Ress_Digit'] = Digit_Ressource
                        Ressources.loc[index, 'Course_Ress_inClass'] = inClass_Ressource
                        Ressources.loc[index, 'Digitalization_Ressource_Ratio'] = round(Digit_Ressource/Course_Ressource, 2)
                        Ressources.loc[index, 'Digitalization_Ressource_Percent'] = round((Digit_Ressource/Course_Ressource) * 100)

                        #lst_NumbTeachers.append(temp_NumbTRP[dep-1])
    
                        index += 1 
                    course_ID += 1 #Increase the course_ID
                    temp += Course_Duration #Add the Course_Duration to the temporary variable


        if (Prop_PRAG_on_PRCE <= rand_num <= 1) :
            temp = 0 #Set the temporary variable to compute the total hours worked by a teacher
            while temp not in interval(middle=PRCE_Hour, deviation=PRCE_Hour*0.05):
                ran_courses = random.random()  #Define a random number to choose the time interval of a course.
                if (0 <= ran_courses < 0.4) : 
                    Course_Duration = random.randint(5, 15)   #Define a random number to have a course between 5H and 15H.
                elif (0.4 <= ran_courses < 0.9) :
                    Course_Duration = random.randint(15, 40)   #Define a random number to have a course between 15H and 40H.
                elif (0.9 <= ran_courses < 1):
                    Course_Duration = random.randint(40, 60)   #Define a random number to have a course between 40H and 60H.
                elif (ran_courses == 1):
                    Course_Duration = random.randint(60, 90)   #Define a random number to have a course between 60H and 90H.
                Course_Ressource = random.randint(ceil(Course_Duration/4), Course_Duration)

                if temp + Course_Duration <= PRCE_Hour*1.05: #Verify that the possible number of courses teached is lower than the amount of hours to teach.
                    for year in temp_Years: #Loop to implement all the years.
                        ratio = Digit_Ratio(course_ID,  lst_Course_ID,  lst_Digit_Ratio) #Find the ratio of digitalization
                        Digit_Ressource = ceil(Course_Ressource * ratio)
                        if year != temp_Years[0]:
                            if Ressources['Course_Ress_Digit'].iloc[-1] > Digit_Ressource:
                                Digit_Ressource = Ressources['Course_Ress_Digit'].iloc[-1]
                        inClass_Ressource = Course_Ressource - Digit_Ressource

                        #Append the lists
                        lst_Digit_Ratio.append(ratio)
                        lst_Course_ID.append(course_ID)

                        Ressources.loc[index, 'Department'] = temp_Depts[dep-1]
                        Ressources.loc[index, 'Teacher_ID'] = teacher_ID
                        Ressources.loc[index, 'Teacher_Name'] = Random_ComName['Last_Name'][rand_name]
                        Ressources.loc[index, 'Year'] = year
                        Ressources.loc[index, 'Course_ID'] = course_ID
                        Ressources.loc[index, 'Course_Duration'] = Course_Duration
                        Ressources.loc[index, 'Course_Ressources'] = Course_Ressource
                        Ressources.loc[index, 'Course_Ress_Digit'] = Digit_Ressource
                        Ressources.loc[index, 'Course_Ress_inClass'] = inClass_Ressource
                        Ressources.loc[index, 'Digitalization_Ressource_Ratio'] = round(Digit_Ressource/Course_Ressource, 2)
                        Ressources.loc[index, 'Digitalization_Ressource_Percent'] = round((Digit_Ressource/Course_Ressource) * 100)

                        index += 1 
                    course_ID += 1 #Increase the course_ID
                    temp += Course_Duration #Add the Course_Duration to the temporary variable

Ressource_col = ['Teacher_ID', 'Year', 'Course_ID', 'Course_Duration', 'Course_Ressources', 'Course_Ress_Digit', 'Course_Ress_inClass', 'Digitalization_Ressource_Percent']
Ressource_type = [int for ress in Ressource_col]
Ressources = type_modif(Ressources, Ressource_col, Ressource_type)
Ressources = Ressources.sort_values(by = ['Year', 'Course_ID'], ascending = True).reset_index().drop('index', axis = 1)
print(Ressources.head(5))    


###############
# Time Update #
###############

Half_Time = round(time.time() - start_time)
print("Time to build the Ressources DataFrame with related Data: %s seconds" % (Half_Time))


#################################
# Specification Ressources Data #
#################################

Ressources = Ressources.assign(Number_Video = int(),
                               Number_QCM = int(),
                               Number_Test = int(),                                    

                               Number_Lecture = int(),
                               Number_Exercise = int(),
                               Number_Exam = int())
Temporal_ID = []

for i, course_ID, ress_Digit, ress_inClass in zip(Ressources.index, Ressources['Course_ID'],  Ressources['Course_Ress_Digit'], Ressources['Course_Ress_inClass']):
    if course_ID not in Temporal_ID: #Verify that the current selected course has never been in the iteration.
        if ress_Digit == 0: #Verify the case where there is no Digitalization.
            Ressources.loc[i, 'Number_Video'] = 0
            Ressources.loc[i, 'Number_QCM'] = 0
            Ressources.loc[i, 'Number_Test'] = 0
        else:
            Digit = False
            while Digit == False: #Maintain the Loop until we find a correct duration/number of video/qcm/test.
                ress_Video = random.randint(0, ceil(ress_Digit*0.70))
                ress_QCM = random.randint(0, ceil(ress_Digit*0.50))
                ress_Test = random.randint(0, ceil(ress_Digit*0.10))
               
                if ress_Digit != ress_Video + ress_QCM + ress_Test: 
                    continue
                else:
                    if ress_Video < ress_Test:
                        continue
                    elif ress_QCM < ress_Test: #Verify the case where the duration of digitalization is not corresponding.
                        continue
                    else:
                        Digit = True
                        Ressources.loc[i, 'Number_Video'] = ress_Video
                        Ressources.loc[i, 'Number_QCM'] = ress_QCM
                        Ressources.loc[i, 'Number_Test'] = ress_Test

        if ress_inClass == 0: #Verify the case where there is no inClass course.
                    Ressources.loc[i, 'Number_Lecture'] = 0
                    Ressources.loc[i, 'Number_Exercise'] = 0
                    Ressources.loc[i, 'Number_Exam'] = 0
        else:
            Present = False
            while Present == False: #Maintain the Loop until we find a correct duration/number of video/qcm/test.
                ress_Lecture = random.randint(0, ceil(ress_inClass*0.65))
                ress_Exercise = random.randint(0, ceil(ress_inClass*0.30))
                ress_Exam = random.randint(0, ceil(ress_inClass*0.05))
                

                if (ress_inClass != ress_Lecture + ress_Exercise + ress_Exam):
                    continue
                else:
                    if ress_Lecture < ress_Exam:
                        continue
                    elif ress_Exercise < ress_Exam: #Verify the case where the duration of digitalization is not corresponding.
                        continue
                    else:
                        Present = True
                        Ressources.loc[i, 'Number_Lecture'] = ress_Lecture
                        Ressources.loc[i, 'Number_Exercise'] = ress_Exercise
                        Ressources.loc[i, 'Number_Exam'] = ress_Exam    
    else:
        ins = [courses for courses in range(0, len(Temporal_ID)) if Temporal_ID[courses] == course_ID] #Find the index of the identical ID as the current «course» selected ID.    
        Digit_RessDif = ress_Digit - Ressources.loc[ins[-1], 'Course_Ress_Digit']
        if Digit_RessDif == 0: #Verify the case where there is no Digitalization.
            Ressources.loc[i, 'Number_Video']  = Ressources.loc[ins[-1], 'Number_Video']
            Ressources.loc[i, 'Number_QCM']  = Ressources.loc[ins[-1], 'Number_QCM']
            Ressources.loc[i, 'Number_Test']  =  Ressources.loc[ins[-1], 'Number_Test']
            Ressources.loc[i, 'Number_Lecture'] = Ressources.loc[ins[-1], 'Number_Lecture']
            Ressources.loc[i, 'Number_Exercise'] = Ressources.loc[ins[-1], 'Number_Exercise']
            Ressources.loc[i, 'Number_Exam'] = Ressources.loc[ins[-1], 'Number_Exam']
        else:
            Digit_inClass = False
            while Digit_inClass == False: #Maintain the Loop until we find a correct duration/number of video/qcm/test.
                ress_Video = random.randint(0, Ressources.loc[ins[-1], 'Number_Lecture'])
                ress_QCM = random.randint(0, Ressources.loc[ins[-1], 'Number_Exercise'])
                ran = random.random()
                if ran <= 0.10:
                    ress_Test = random.randint(0, Ressources.loc[ins[-1], 'Number_Exam'])
                else:
                    ress_Test = 0
                    
                if Digit_RessDif != ress_Video + ress_QCM + ress_Test: #Verify the case where the duration of digitalization is not corresponding.
                    continue
                else:
                    Digit_inClass = True
                    Ressources.loc[i, 'Number_Video'] = Ressources.loc[ins[-1], 'Number_Video'] + ress_Video
                    Ressources.loc[i, 'Number_QCM'] = Ressources.loc[ins[-1], 'Number_QCM'] + ress_QCM
                    Ressources.loc[i, 'Number_Test'] = Ressources.loc[ins[-1], 'Number_Test'] + ress_Test
                    Ressources.loc[i, 'Number_Lecture'] = Ressources.loc[ins[-1], 'Number_Lecture'] - ress_Video
                    Ressources.loc[i, 'Number_Exercise'] = Ressources.loc[ins[-1], 'Number_Exercise'] - ress_QCM
                    Ressources.loc[i, 'Number_Exam'] = Ressources.loc[ins[-1], 'Number_Exam'] - ress_Test
    #print(course_ID, ress_Digit, ress_Video, ress_QCM, ress_Test, ress_inClass, ress_Lecture, ress_Exercise, ress_Exam)
    Temporal_ID.append(course_ID) #Append the current selected Course in the temporal list to keep a memory of the Course accessed.


##################
# Data Selection #
##################

col_Digit = ['Year', 'Course_ID', 'Course_Duration', 'Course_Ress_Digit', 'Number_Video', 'Number_QCM', 'Number_Test'] #Select the column specific to the Digit data and store it in «col_Digit».
Ressources_Digit = Ressources[col_Digit] #Filter the main DataFrame using the «col_Digit» array and store it in «Ressource_Digit».
Ressources_Digit = Ressources_Digit.sort_values(by = ['Course_ID', 'Year'], ascending = True) #Sort the new DataFrame by «Course_ID» and «Year».

col_inClass = ['Year', 'Course_ID', 'Course_Duration', 'Course_Ress_inClass', 'Number_Lecture', 'Number_Exercise', 'Number_Exam'] #Select the column specific to the Digit data and store it in «col_inClass».
Ressources_inClass = Ressources[col_inClass] #Filter the main DataFrame using the «col_inClass» array and store it in «Ressource_inClass».
Ressources_inClass = Ressources_inClass.sort_values(by = ['Course_ID', 'Year'], ascending = True) #Sort the new DataFrame by «Course_ID» and «Year».

col_Digit_inClass = ['Year', 'Course_ID', 'Course_Duration', 'Course_Ressources', 'Course_Ress_Digit', 'Course_Ress_inClass', 'Number_Video', 'Number_QCM', 'Number_Test', 'Number_Lecture', 'Number_Exercise', 'Number_Exam'] #Select the column specific for both the Digit and inClass data and store it in «col_Digit_inClass».
Ressources_Digit_inClass = Ressources[col_Digit_inClass] #Filter the main DataFrame using the «col_Digit_inClass» array and store it in «Ressources_Digit_inClass».
Ressources_Digit_inClass = Ressources_Digit_inClass.sort_values(by = ['Course_ID', 'Year'], ascending = True) #Sort the new DataFrame by «Course_ID» and «Year».
print(Ressources_Digit_inClass.head(10)) #Display the ten first rows of the «Ressources_Digit_inClass» DataFrame.


#############
# Save Data #
#############

#Save the Ressources into a CSV File.
Ressources.to_csv(path_data + 'Ressources.csv')

#Save the Ressources_Digit_inClass into a CSV File.
Ressources_Digit_inClass.to_csv(path_data + 'Ressources_Digit_inClass.csv')


########################
# Data Ressources DONE #
########################
Total_Time = round(time.time() - start_time)
print("Program Execution Time: %s seconds" % (Total_Time))
