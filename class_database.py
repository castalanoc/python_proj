#PA2
#Programmer name: Chris Castalano

#Purpose: This programs purpose is to help faculty find avaliable classrooms based on their individul inputs. After inputting their specific information, they'll be able to see whether or not the room fits their needs.
#My submission of this program indicates that I have neither received nor given unauthorized assistance in writing this program. All coding is my own work.

#user input statements

#classroom data collection statements

room_num = str(input("What is the classroom room number? (ex: ZSH2332): "))

max_cap = int(input("What is the maximum number of students accomodatable?: "))

class_day = str(input("What days is the classroom available? (ex. TTH for tuesday/thursday): ")).upper()

s_time = str(input("What is the start time for the classroom? (Military time / ex. 9:00): "))

e_time = str(input("What is the end time for the classroom? (Military time / ex. 15:00): "))

#course data collection statements

prof_name = str(input("What is the name of the profesor?: "))

cour_name = str(input("What is the name of the course? (ex.COB291): "))

sec_num = int(input("What is the course section number?: "))

cred_hrs = int(input("What is the number of credit hours?: "))

c_enroll = int(input("What is the number of students enrolled in the course?: "))

#data validation statements

if max_cap <= 0:
    print("Capacity must be a positive number, try again.")
    max_cap = int(input("What is the maximum number of students accomodatable?: "))

if sec_num <= 0:
    print("Section number must be a positive number, try again.")
    sec_num = int(input("What is the course section number?: "))

if c_enroll < 0:
    print("Course enrollment must be a positive number, try again.")
    cour_enrol = int(input("What is the number of students enrolled in the course?: "))

if cred_hrs <= 0:
    print("Credit hours must be a positive number greater than 0, try again.")
    cred_hrs = int(input("What is the number of credit hours?: "))
    
if class_day != 'MW' and class_day != 'MWF' and class_day != 'TTH':
    print("Class days must be entered as MW, MWF, or TTH, try again.")
    class_day = str(input("What days is the classroom available? (TTH for tuesday/thursday): "))

#splitting statements for start/end time
    
split_start = int(s_time.split(':')[0])

split_end = int(e_time.split(':')[0])

split_start2 = int(s_time.split(':')[1])

split_end2 = int(e_time.split(':')[1])

#data validation for time / hour intervals

if split_start < 8:
    print("Earliest possible start time is 8:00, try again.")
    s_time = str(input("What is the start time for the classroom? (Military time / ex. 9:00): "))
elif split_start > 18:
    print("18:00 is the latest possible start time, try again")
    s_time = str(input("What is the start time for the classroom? (Military time / ex. 9:00): "))

if split_end < 9:
    print('Earliest possible end time is 9:00, try again.')
    e_time = str(input("What is the end time for the classroom? (Military time / ex. 15:00): "))
elif split_end > 19:
    print('19:00 is the latest possible end time, try again')
    e_time = str(input("What is the end time for the classroom? (Military time / ex. 15:00): "))

#data validation for time / minute intervals
    
if split_start2 > 59:
    print('59 is the highest minute interval, try again')
    s_time = str(input("What is the start time for the classroom? (Military time / ex. 9:00): "))
    
if split_end2 > 59:
    print('59 is the highest minute interval, try again')
    e_time = str(input("What is the end time for the classroom? (Military time / ex. 15:00): "))
    
    
#room matching statements

#suitibilty displays how well the room matches to the inputs entered by the user

# 1 : the room cannot fit the anount of students enrolled / No Match
suitibility = 1

# 2 : the room is larger then needed but can fit the amount enrolled / Match
suitibility = 2

# 3 : the room is a good fit for the amount enrolled / Match
suitibility = 3

if c_enroll > max_cap:
    suitability = 1
elif c_enroll < max_cap:
    suitability = 2
elif c_enroll == max_cap:
    suitability = 3
    
#course information output
print()
print('--------------------------')
print()

#course information headers

print('COURSE #', end = '\t')
print('SEC', end = '\t')
print('HRS', end = '\t')
print('Room', end = '\t')
print('DAYS', end = '\t')
print('START', end = '\t')
print('END', end = '\t')
print('INSTRUCTOR', end = '\t')
print('ENRL',end = '\t')
print('SUITABILITY')

#user input information 

print((f'{cour_name}'), end = '\t         ')
print((f'{sec_num}'), end = '\t ')
print((f'{cred_hrs}'), end = '\t')
print((f'{room_num}'), end = '\t')
print((f'{class_day}'), end = '\t')
print((f'{s_time}'), end = '\t')
print((f'{e_time}'), end = '\t')
print((f'{prof_name}'), end = '\t')
print((f'{c_enroll}'), end = '\t')

#suitability output statements

if suitability == 1:
    print('No Match, the room cannot fit the amount of students enrolled.')
elif suitability == 2:
    print('Match, however the room is larger then required.')
elif suitability == 3:
    print('Match, the room perfectly fits the amount enrolled.')

#end
    
    