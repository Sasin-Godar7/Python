#student performance analytics

#concept : analysis exam scores for multiple subjects using numpy arrays.
#example tasks

#generate the random marks for 20 students in 5 subjects.

#find each student's total and average scores

#identify top 3 students.

#calculate the subjects-wise highest , lowest , and average marks.

#normalize marks to scale(like converting to percentage or z-score).

import numpy as np
marks = np.random(50,100(20,5))
print("marks\n",marks)


total_marks = np.sum(marks,axis=1)
print("total marks of each students is",total_marks)

average_marks = np.mean(marks,axis=1)
print("average marks of a student is ",average_marks)

top3_std = np.argsort((total_marks)[-3: ][::1])
print("top 3 student (by top marks):")
for rank,idx in enumerate(top3_std,start=1):
    print(f"Rank {rank}: Student{idx+1}-> total marks:{total_marks[idx]}")


