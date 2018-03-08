import json
import drawStat
import txtStat
import os
import time

globalData = {}


def getDay(timestamp):
    timeArray = time.localtime(timestamp)
    otherStyleTime = time.strftime("%Y-%m-%d", timeArray)
    return otherStyleTime


def processLine(line):
    whole = json.loads(line)
    messagejson = whole['message']
    if messagejson.strip() == '':
        return
    message = json.loads(messagejson)
    # if (getDay(message['AppBoxInfo']['firstInstallTime'] / 1000) != getDay(int(float(whole['timestamp'])))):
    #    globalData[message['AppBoxInfo']['deviceId']] = message
    if int(float(whole['timestamp'])) - (message['AppBoxInfo']['firstInstallTime'] / 1000) > 518400:
        globalData[message['AppBoxInfo']['deviceId']] = message


for f in os.listdir('log/'):
    ff = open('log/' + f)
    for line in ff:
        processLine(line)
    ff.close()

for (k,v) in globalData.items():
    print(v)

# print('3月5日,6日,7日,非当天安装上报的用户,总样本数', len(globalData))
print('上报日期大于等于安装日期7天的上报的用户,总样本数', len(globalData))
print(txtStat.phoneUsedPercentage(globalData))
print(txtStat.phoneTotalSize(globalData))
print(txtStat.appboxTotalPercentage(globalData))
print(txtStat.appboxTotalSize(globalData))
print(txtStat.appboxPluginNum(globalData))
# print(txtStat.appboxPluginPackageSize(globalData,'com.tencent.mm'))
#print(txtStat.appboxPluginPackageSizeList(globalData))

# drawStat.drawTotalPercentage(globalData)
# drawStat.drawTotalSize(globalData)
# drawStat.drawSelfPercentage(globalData)
# drawStat.drawSelfSize(globalData)
