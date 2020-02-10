
import matplotlib.pyplot as plt

student_attendance = {'day1':33, 'day2':34,'day3':29,'day4':31,'day5':28,'day6':26,'day7':30}
keys = student_attendance.keys()
values = student_attendance.values()

squares = [keys for keys in values]
plt.xlabel("Days", fontsize=10)
plt.ylabel("Students", fontsize=10)
plt.plot(squares)
plt.show()