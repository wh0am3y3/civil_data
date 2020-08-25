import matplotlib.pyplot as plt


x_year = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
y_total = [41406, 40898, 40893, 40528, 40829, 40460, 40312, 40198, 40244, 40596, 41169, 41735]
y_arabs = [5900, 6300, 6800, 7200, 7800, 8300, 8700, 9300, 9900, 10500, 11100, 11979]
y_jews = [30400, 29500, 28900, 28000, 27500, 26700, 26000, 25200, 24600, 24100, 23848, 23296]
y_jews_and_others = [35500, 34500, 34100, 33400, 33000, 32200, 31600, 30900, 30400, 30100, 30069, 29756]

plt.style.use('Solarize_Light2')
plt.rcParams.update({'font.size': 22})
plt.plot(x_year, y_total, 'o-')
for x, y in zip(x_year, y_total):
    label = "{:.1f}".format(y / 1000)
    plt.annotate(label, (x, y), textcoords="offset points",
                 xytext=(0, 10), ha='center')
plt.plot(x_year, y_jews_and_others, 'o-')
for x, y in zip(x_year, y_jews_and_others):
    label = "{:.1f}".format(y / 1000)
    plt.annotate(label, (x, y), textcoords="offset points",
                 xytext=(0, 10), ha='center')
plt.plot(x_year, y_jews, 'o-')
for x, y in zip(x_year, y_jews):
    label = "{:.1f}".format(y / 1000)
    plt.annotate(label, (x, y), textcoords="offset points",
                 xytext=(0, 10), ha='center')
plt.plot(x_year, y_arabs, 'o-')
for x, y in zip(x_year, y_arabs):
    label = "{:.1f}".format(y / 1000)
    plt.annotate(label, (x, y), textcoords="offset points",
                 xytext=(0, 10), ha='center')
plt.legend(['םיבשות ךס', 'םירחאו םידוהי', 'םידוהי', 'םיברע'],
           title='ארקמ',
           loc='center left',
           ncol=2,
           fancybox=True,
           shadow=True
           )
# plt.axvline(x=2016, linewidth=1, color='black')
plt.xlabel('םינש')
plt.ylabel('םיבשות')
plt.title("(2008-2019) ס\"מלה ינותנ יפל ,לילגה ףונב םיבשות", fontsize=22)
# plt.savefig("civil_data.png")
plt.show()
