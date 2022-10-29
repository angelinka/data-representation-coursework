import requests
import csv
from xml.dom.minidom import parseString


retrieveTags=['TrainStatus',
'TrainLatitude',
'TrainLongitude',
'TrainCode',
'TrainDate',
'PublicMessage',
'Direction'
]

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
doc = parseString(page.content)
#to check if everything works can print it out to the console
# print(doc.toprettyxml())

# To store the xml in a file. You can comment this out later
# with open("trainxml.xml", "w") as xmlfp:
#    doc.writexml(xmlfp)


with open('train.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    for objTrainPosNode in objTrainPositionsNodes:
        #traincodenode = objTrainPosNode.getElementsByTagName("TrainCode").item(0)
        #traincode = traincodenode.firstChild.nodeValue.strip()
        #print(traincode)
        dataList = []
        #dataList.append(traincode)
        #train_writer.writerow(dataList)
        '''
        for retriveTag in retrieveTags:
            datanode = objTrainPosNode.getElementsByTagName(retriveTag).item(0)
            dataList.append(datanode.firstChild.nodeValue.strip())
        train_writer.writerow(dataList)
        '''
        for retriveTag in retrieveTags:
            datanode = objTrainPosNode.getElementsByTagName(retriveTag).item(0)
            traincodenode = objTrainPosNode.getElementsByTagName("TrainCode").item(0)
            traincode = traincodenode.firstChild.nodeValue.strip()
            if any(item.startswith('Y') for item in traincode):
                dataList.append(datanode.firstChild.nodeValue.strip())
            else: 
                dataList = ['Nothing found']
               
        train_writer.writerow(dataList)
'''
        latitudenode = objTrainPosNode.getElementsByTagName("TrainLatitude").item(0)
        trainlatitude = latitudenode.firstChild.nodeValue.strip()
        print(trainlatitude)
'''