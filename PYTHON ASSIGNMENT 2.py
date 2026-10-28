#list creation
from Dictionary import student

age_list=[10,20,30,40,50,]
print(age_list)
# name
name_list=["ashin","john","abhinav","karthik","rahul"]
print(name_list)
#list operation and modification
name_list.append("Yazhini")
print(name_list)
age_list.insert(2,30)
print(age_list)
name_list.remove("Yazhini")
print(name_list)
age_list.pop()
print(age_list)
age_list.extend([29,30,26])
print(age_list)
age_list.sort()
print(age_list)
# minimum
print(min(age_list))
print(max(age_list)) #age max
print(sum(age_list)) #sum age
#Accessing List Elements:
print(name_list[0])
print(name_list[4])
print(name_list[2:4])
name_list.reverse()
print(name_list)

#Dictionary (Creation, Modification and Access):
student_marks = {
    "ashin":70,
    "john":80,
    "abhinav":90,
    "karthik":60,
    "rahul":70,
}
student_marks["Janani"]=80
student_marks.update({"John": 82})
print(student_marks)
print(student_marks.keys())
print(student_marks.values())
print(student_marks.items())

#Sets (Operations):
my_set={'a','e','i','o','u','a','a','i'}
print(my_set)
#my_set[4]='s'
print(my_set)
#type error :set' object does not support item assignment

set_1 = {1, 3, 5, 7, 9}
set_2 = {2, 3, 5, 8, 10}
print("union:", set_1.union(set_2))
print("intersection:",set_1.intersection(set_2))

#Operators & Conditional Statements :
score=int(input("enter the score(0-100):"))
print("your score is:",score)
if score > 7:
    print("Above Average")
elif score >= 4:
    print("Average")
else:
    print("Below Average")

if score>7:
    print("above average")
    print("good work! keep moving")
elif score>=4:
    print("average")
    print("nice work!keep imporoving")
else:
    print("below average")
    print("neeed to improve ! focuz more on your studies for a better results")





















