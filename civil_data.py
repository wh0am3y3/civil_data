import matplotlib.pyplot as plt


x_year = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
y_total = [41406, 40898, 40893, 40528, 40829, 40460, 40312, 40198, 40244, 40596, 41169, 41735, 41937, 42659, 44184]
y_arabs = [5900, 6300, 6800, 7200, 7800, 8300, 8700, 9300, 9900, 10500, 11100, 11979, 12729, 13584, 14276]
y_jews = [30400, 29500, 28900, 28000, 27500, 26700, 26000, 25200, 24600, 24100, 23848, 23296, 22740, 22590, 22814]
y_jews_and_others = [35500, 34500, 34100, 33400, 33000, 32200, 31600, 30900, 30400, 30100, 30069, 29756, 29208, 29075, 29909]

plt.style.use('Solarize_Light2')
plt.rcParams.update({'font.size': 16})
plt.plot(x_year, y_total, 'o-')
for x, y in zip(x_year, y_total):
    label = "{:.1f}".format(y / 1000)
    plt.annotate(label, (x, y), textcoords="offset points",
                 xytext=(0, 10), ha='center')
# plt.plot(x_year, y_jews_and_others, 'o-')
# for x, y in zip(x_year, y_jews_and_others):
#     label = "{:.1f}".format(y / 1000)
#     plt.annotate(label, (x, y), textcoords="offset points",
#                  xytext=(0, 10), ha='center')
y_others = [j - i for j, i in zip(y_jews_and_others, y_jews)]
y_arabs_and_others = [j + i for j, i in zip(y_arabs, y_others)]
plt.plot(x_year, y_jews, 'o-')
for x, y in zip(x_year, y_jews):
    label = "{:.1f}".format(y / 1000)
    plt.annotate(label, (x, y), textcoords="offset points",
                 xytext=(0, 10), ha='center')
plt.plot(x_year, y_arabs_and_others, 'o-')
for x, y in zip(x_year, y_arabs_and_others):
    label = "{:.1f}".format(y / 1000)
    plt.annotate(label, (x, y), textcoords="offset points",
                 xytext=(0, 10), ha='center')
plt.legend(['םיבשות ךס',
            # 'םירחאו םידוהי',
            'םידוהי',
            'םירחאו םיברע'],
           title='ארקמ',
           loc='center left',
           ncol=3,
           fancybox=True,
           shadow=True
           )
# plt.axvline(x=2016, linewidth=1, color='black')
plt.xlabel('םינש', fontsize=18)
plt.ylabel('םיבשות', fontsize=18)
plt.title("(2008-2021) ס\"מלה ינותנ יפל ,לילגה ףונב םיבשות", fontsize=22)
# plt.savefig("civil_data.png")
plt.show()
