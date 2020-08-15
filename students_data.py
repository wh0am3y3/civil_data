import matplotlib.pyplot as plt


x_year = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
y_students_s = [446, 414, 405, 399, 398, 381, 381, 403, 366, 347, 295, 326]
y_students_a = [598, 590, 573, 572, 562, 531, 470, 459, 362, 380, 327, 366]

sum_students = [j + i for j, i in zip(y_students_s, y_students_a)]
plt.plot(x_year, sum_students)

plt.plot(x_year, y_students_s)
plt.plot(x_year, y_students_a)


plt.legend(['Total', 'Sharet', 'Alon'])

plt.xlabel('םינש')
plt.ylabel('םידימלת')

plt.savefig("students_data.png")
