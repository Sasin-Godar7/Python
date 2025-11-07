#student performance analytics

#concept : analysis exam scores for multiple subjects using numpy arrays.
#example tasks

#generate the random marks for 20 students in 5 subjects.

#find each student's total and average scores

#identify top 3 students.

#calculate the subjects-wise highest , lowest , and average marks.

#normalize marks to scale(like converting to percentage or z-score).

import numpy as np
marks = np.random.randint(50,100,(20,5))
print("marks\n",marks) 


total_marks = np.sum(marks,axis=1)
print("total marks of each students is",total_marks)

average_marks = np.mean(marks,axis=1)
print("average marks of a student is ",average_marks)

top3_idx = np.argsort(total_marks)[-3:][::-1]

print("Top 3 students (by total marks):")
for rank, idx in enumerate(top3_idx, start=1):
    print(f"Rank {rank}: Student{idx+1} -> Total Marks: {total_marks[idx]}")

sub_highest = np.max(marks,axis=0)
sub_lowest = np.min(marks,axis=0)
sub_average = np.mean(marks,axis=0)
print("\subject wise highest marks:",sub_highest)    
print("\nsubject wise lowest marks:",sub_lowest)
print("subject wise average marks:",sub_average.round(2))

percentage = (marks/100)*100
print("\n percantage marks (normalize 0-100):\n",percentage.round(2))



