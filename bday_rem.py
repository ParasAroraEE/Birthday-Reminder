import time
import os

birthdayFile = 'bday.txt'


def checkTodaysBirthday():
    fileName = open(birthdayFile, 'r')
    today = time.strftime('%m%d')
    flag = 0
    for line in fileName:
        if today in line:
            line = line.split(' ')
            flag = 1
            print(f'Happy Birthday {line[1]} {line[2]}')
            print(today)
            # os.system('notify-send "Birthday Today: ' + line[1] + ' ' + line[2] + '"')
    if flag == 0:
        # os.system('notify-send "No Birthdays Today!"')
        print('No Birthdays Today!')


if __name__ == '__main__':
    checkTodaysBirthday()
