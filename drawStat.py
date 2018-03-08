from matplotlib import pyplot
import numpy as np

#总占用百分比分布
def drawTotalPercentage(globalData):
    # percents = [0,0,0,0,0,0,0,0,0,0]
    # for (k,v) in globalData.items():
    #     percent = v['StorageInfo']['systemUsed']/v['StorageInfo']['systemTotal']
    #     percentint  = int(percent*10)
    #     percents[percentint] +=1
    percents = []
    for (k, v) in globalData.items():
        percent = v['StorageInfo']['systemUsed'] / v['StorageInfo']['systemTotal']
        percentint = int(percent * 100)
        #print(percentint)
        percents.append(percentint)
    pyplot.hist(percents, 20)
    pyplot.xlabel('sys total storage percent')
    pyplot.ylabel('num')
    pyplot.title('sys total storage percent')
    pyplot.show()

#手机存储空间分布
def drawTotalSize(globalData):
    percents = []
    for (k, v) in globalData.items():
        percent = v['StorageInfo']['systemTotal']
        percentint = int(percent/1073741824)
        print(percentint)
        percents.append(percentint)
    pyplot.hist(percents, 50,[0,256])
    pyplot.hist(percents, 50,[0,256])
    pyplot.xticks(np.arange(0, 256, 10))
    pyplot.xlabel('sys total storage size')
    pyplot.ylabel('num')
    pyplot.title('sys total storage size')
    pyplot.show()

#插件存储空间百分比分布
def drawSelfPercentage(globalData):
    percents = []
    for (k, v) in globalData.items():
        #percent = v['StorageInfo']['systemUsed'] / v['StorageInfo']['systemTotal']
        for info in v['PluginInfo']:
            tot = info['apkSizeByte']+info['dataSizeByte']+info['sdcardSizeByte']+info['dalvikCacheSizeByte']
        percent = tot / v['StorageInfo']['systemTotal']
        percentint = int(percent * 100)
        print(percentint)
        percents.append(percentint)
    pyplot.hist(percents, 25)
    pyplot.xlabel('plugin total storage percent')
    pyplot.ylabel('num')
    pyplot.title('plugin total storage percent')
    pyplot.show()

#插件存储空间大小分布
def drawSelfSize(globalData):
    percents = []
    for (k, v) in globalData.items():
        #percent = v['StorageInfo']['systemUsed'] / v['StorageInfo']['systemTotal']
        for info in v['PluginInfo']:
            tot = info['apkSizeByte']+info['dataSizeByte']+info['sdcardSizeByte']+info['dalvikCacheSizeByte']
        percentint = int(tot / 1048576)
        print(percentint)
        percents.append(percentint)
    pyplot.hist(percents, 25)
    pyplot.xticks(np.arange(0, 8000, 250))
    pyplot.xlabel('sys total storage percent')
    pyplot.ylabel('num')
    pyplot.title('plugin total storage percent')
    pyplot.show()