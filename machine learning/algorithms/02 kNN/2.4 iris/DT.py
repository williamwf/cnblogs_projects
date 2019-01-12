from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import tree
from sklearn import preprocessing
from sklearn.externals.six import StringIO


#读文件
allElectronicsData = open('AllElectronics.csv','r')

reader = csv.reader(allElectronicsData) #reader按行读取
headers = next(reader)

print(headers)

#拆分标签列和特征列并赋值
featureList = []
labelList = []

for row in reader:
    labelList.append(row[len(row)-1])
    rowDict = {}
    for i in range(1, len(row)-1):
        rowDict[headers[i]] = row[i]
    featureList.append(rowDict)

# print(featureList)
# print(labelList)

# 特征化特征
vec = DictVectorizer()
dummyX = vec.fit_transform(featureList) .toarray()

print("dummyX: "+str(dummyX))
print(vec.get_feature_names())

# 特征化标签
lb = preprocessing.LabelBinarizer()
dummyY = lb.fit_transform(labelList)
print("dummyY: "+str(dummyY))


# 构建决策树并分类
clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(dummyX, dummyY)
print("clf: " + str(clf))
