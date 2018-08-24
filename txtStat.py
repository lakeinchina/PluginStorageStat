import numpy as np


# 手机已用存储百分比分布


def phoneUsedPercentage(globalData):
    percents = []
    for (k, v) in globalData.items():
        percent = v['StorageInfo']['systemUsed'] / v['StorageInfo']['systemTotal']
        percentint = int(percent * 100)
        # print(percentint)
        percents.append(percentint)

    result = np.histogram(percents, 20, [0, 100], density=True)
    # print(result)
    r = result[0] * 5
    result_string = "手机已用存储百分比分布\n"
    i = 0
    for p in r:
        # resultString += str(resultString) + result[1][i] + "%-" + result[1][i + 1] + " " + p
        result_string += str.format('{}-{} {:.4f}\n', int(result[1][i]), int(result[1][i + 1]), p)
        i += 1

    return result_string


# 手机总存储空间大小分布
def phoneTotalSize(globalData):
    percents = []
    for (k, v) in globalData.items():
        percent = v['StorageInfo']['systemTotal']
        percentint = int(percent / 1073741824)
        # if(percentint>100):
        #     print(percentint," ",k," ",v)
        percents.append(percentint)

    result = np.histogram(percents, 26, [0, 130], density=True)
    # print(result)
    r = result[0] * 5
    resultString = "手机总存储空间大小分布，单位GB\n"
    i = 0
    for p in r:
        # resultString += str(resultString) + result[1][i] + "%-" + result[1][i + 1] + " " + p
        resultString += str.format('{}-{} {:.4f}\n', int(result[1][i]), int(result[1][i + 1]), p)
        i += 1

    return resultString


# 闪电盒子占用存储空间百分比分布
def appboxTotalPercentage(globalData):
    percents = []
    for (k, v) in globalData.items():
        # percent = v['StorageInfo']['systemUsed'] / v['StorageInfo']['systemTotal']
        tot = 0
        for info in v['PluginInfo']:
            tot += info['apkSizeByte'] + info['dataSizeByte'] + info['sdcardSizeByte'] + info['dalvikCacheSizeByte']
        tot += v['StorageInfo']['selfUsed']
        percent = tot / v['StorageInfo']['systemTotal']
        percentint = int(percent * 100)
        # print(percentint)
        percents.append(percentint)

    result = np.histogram(percents, 20, [0, 100], density=True)
    # print(result)
    r = result[0] * 5
    resultString = "闪电盒子占用存储空间百分比分布\n"
    i = 0
    for p in r:
        # resultString += str(resultString) + result[1][i] + "%-" + result[1][i + 1] + " " + p
        resultString += str.format('{}-{} {:.4f}\n', int(result[1][i]), int(result[1][i + 1]), p)
        i += 1

    return resultString


# 闪电盒子占用存储空间大小分布
def appboxTotalSize(globalData):
    percents = []
    for (k, v) in globalData.items():
        tot = 0
        for info in v['PluginInfo']:
            tot += info['apkSizeByte'] + info['dataSizeByte'] + info['sdcardSizeByte'] + info['dalvikCacheSizeByte']
        tot += v['StorageInfo']['selfUsed']
        percentint = int(tot / 1048576)
        # print(percentint)
        percents.append(percentint)

    result = np.histogram(percents, 40, [0, 10000], density=True)
    # print(result)
    r = result[0] * 250
    resultString = "闪电盒子占用存储空间大小分布，单位MB,样本数量" + str(len(percents)) + "\n"
    i = 0
    for p in r:
        # resultString += str(resultString) + result[1][i] + "%-" + result[1][i + 1] + " " + p
        resultString += str.format('{}-{} {:.4f}\n', int(result[1][i]), int(result[1][i + 1]), p)
        i += 1

    return resultString


# 闪电盒子插件安装数量分布
def appboxPluginNum(globalData):
    percents = []
    for (k, v) in globalData.items():
        tot = 0
        for info in v['PluginInfo']:
            if (info['installState'] == 'none'):
                tot += 1
        percents.append(tot)

    result = np.histogram(percents, 25, [0, 50], density=True)
    # print(result)
    r = result[0] * 2
    resultString = "闪电盒子安装插件数量，单位个\n"
    i = 0
    for p in r:
        # resultString += str(resultString) + result[1][i] + "%-" + result[1][i + 1] + " " + p
        resultString += str.format('{}-{} {:.4f}\n', int(result[1][i]), int(result[1][i + 1]), p)
        i += 1

    return resultString


# 闪电盒子插件安装数量分布
def appboxPluginPackageSize(globalData, packageName):
    percents = []
    for (k, v) in globalData.items():
        tot = -1
        for info in v['PluginInfo']:
            if info['packageName'] == packageName:
                tot = info['apkSizeByte'] + info['dataSizeByte'] + info['sdcardSizeByte'] + info['dalvikCacheSizeByte']
                break
        if tot != -1:
            percentint = int(tot / 1048576)
            # print(percentint)
            percents.append(percentint)

    result = np.histogram(percents, 40, [0, 10000], density=True)
    # print(result)
    r = result[0] * 250
    resultString = packageName + "占用存储空间大小分布，单位MB,数量=" + str(len(percents)) + "\n"
    i = 0
    for p in r:
        # resultString += str(resultString) + result[1][i] + "%-" + result[1][i + 1] + " " + p
        resultString += str.format('{}-{} {:.4f}\n', int(result[1][i]), int(result[1][i + 1]), p)
        i += 1

    return resultString


def appboxPluginPackageSizeList(globalData):
    percents = {}
    for (k, v) in globalData.items():
        tot = -1
        for info in v['PluginInfo']:
            tot = info['apkSizeByte'] + info['dataSizeByte'] + info['sdcardSizeByte'] + info['dalvikCacheSizeByte']
            if info['packageName'] in percents:
                percents[info['packageName']] += tot

            else:
                percents[info['packageName']] = tot
            percentint = int(tot / 1073741824)
            # print(percentint)

    result = sorted(percents.items(), key=lambda d: d[1], reverse=True)
    resultString = "插件所有用户占用存储空间之和 大小分布，单位MB,数量=" + str(len(percents)) + "\n"
    for (k, v) in result:
        resultString += k + " " + str(int(v / 1048576)) + "\n"
    return resultString


# 闪电盒子type占用存储空间大小分布
def appboxTotalTypeSize(globalData, type):
    percents = []
    for (k, v) in globalData.items():
        tot = 0
        if type == 'self':
            tot = v['StorageInfo']['selfUsed']
        else:
            for info in v['PluginInfo']:
                if info['installState'] == type:
                    tot += info['apkSizeByte'] + info['dataSizeByte'] + info['sdcardSizeByte'] + info['dalvikCacheSizeByte']
        percentint = int(tot / 1048576)
        # print(percentint)
        percents.append(percentint)

    result = np.histogram(percents, 40, [0, 10000], density=True)
    # print(result)
    r = result[0] * 250
    resultString = "闪电盒子type=" + type + "占用存储空间大小分布，单位MB,样本数量" + str(len(percents)) + "\n"
    i = 0
    for p in r:
        # resultString += str(resultString) + result[1][i] + "%-" + result[1][i + 1] + " " + p
        resultString += str.format('{}-{} {:.4f}\n', int(result[1][i]), int(result[1][i + 1]), p)
        i += 1

    return resultString
