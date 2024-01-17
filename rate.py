import datetime
import requests
import time
import matplotlib.pyplot as plt
usernames = input("ユーザー名をカンマ区切りで入力してください:").split(",")
users = {}
for uname in usernames:
    users[uname] = requests.get("https://atcoder.jp/users/"+uname+"/history/json").json()
    time.sleep(1)
user_rates = {uname : [users[uname][i]["NewRating"] for i in range(len(users[uname]))] for uname in usernames}
user_times = {uname : [datetime.datetime.strptime((users[uname][i]["EndTime"]).split("T")[0], '%Y-%m-%d')  for i in range(len(users[uname]))] for uname in usernames}
plt.figure()
for uname in usernames:
    plt.plot(user_times[uname], user_rates[uname],label=uname)
plt.legend()
plt.gcf().autofmt_xdate() 
plt.yticks([i * 400 for i in range(13) if (i-1)*400 <= max(max(user_rates[uname] for uname in usernames))])
plt.grid(which = "major", axis = "y", color = "green", alpha = 0.8,linestyle = "--", linewidth = 1)
plt.show()