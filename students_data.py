import matplotlib.pyplot as plt


x_year = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
y_students_s = [446, 414, 405, 399, 398, 381, 381, 403, 366, 347, 295, 326]
y_students_a = [598, 590, 573, 572, 562, 531, 470, 459, 362, 380, 327, 366]


plt.style.use('Solarize_Light2')
plt.rcParams.update({'font.size': 18})
sum_students = [j + i for j, i in zip(y_students_s, y_students_a)]
plt.plot(x_year, sum_students, 'o-')
for x, y in zip(x_year, sum_students):
    label = "{:.1f}".format(int(y))
    plt.annotate(label, (x, y), textcoords="offset points",
                 xytext=(0, 10), ha='center')
plt.plot(x_year, y_students_s, 'o-')
for x, y in zip(x_year, y_students_s):
    label = "{:.1f}".format(int(y))
    plt.annotate(label, (x, y), textcoords="offset points",
                 xytext=(0, -20), ha='center')
plt.plot(x_year, y_students_a, 'o-')
for x, y in zip(x_year, y_students_a):
    label = "{:.1f}".format(int(y))
    plt.annotate(label, (x, y), textcoords="offset points",
                 xytext=(0, 10), ha='center')

plt.legend(['םידימלת ךס', 'תרש', 'ןולא'],
           title='ארקמ',
           loc='upper right',
           ncol=1,
           fancybox=True,
           shadow=True
           )

plt.xlabel('םינש', fontsize=22)
plt.ylabel('םידימלת', fontsize=22)
plt.title("(2008-2019) ךוניח דרשמ ינותנ יפל ,לילגה ףונ ןוכיתב םידימלת ", fontsize=22)
# plt.savefig("students_data.png")
plt.show()
