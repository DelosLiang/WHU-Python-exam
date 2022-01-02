'''
应用K-means聚类算法，了解1999年各个省份的消费水平在国内的情况。
'''
import numpy as np
from sklearn.cluster import KMeans

def loadData(dataFile):
    f = open(dataFile,'r+')
    lines = f.readlines()
    cityData = []
    cityName = []
    for line in lines:
        items = line.strip().split(",")
        cityName.append(items[0])
        cityData.append([float(items[i]) for i in range(1, len(items))])
    return cityData, cityName

def cityClustering(levelCount=3):
    cityData, cityName = loadData('city.txt')
    km = KMeans(n_clusters=levelCount)
    label = km.fit_predict(cityData)
    # print('label:', label)
    expenses = np.sum(km.cluster_centers_, axis=1)
    # print('expenses:', expenses)

    cityCluster = [[] for i in range(levelCount)]
    for i in range(len(cityName)):
        cityCluster[label[i]].append(cityName[i])
    print('分析结果：')
    for i in range(len(cityCluster)):
        print("{}类省份平均消费额：{:.2f}元".format(i+1, expenses[i]))
        print(cityCluster[i])
        
if __name__ == '__main__':
    cityClustering(5)
