""" programme à compléter du kPPV"""
import csv

nbExParClasse = 50
nbApprent = 25
nbCaract = 4
nbClasse = 3

def lectureFichierCSV():
    with open("iris.data", 'r')as fic:
        lines = csv.reader(fic)
        dataset = list(lines)
    #print(dataset[0], len(dataset))
    for i in range(len(dataset)):
        for j in range(nbCaract):
            dataset[i][j] = float(dataset[i][j])
    #print(dataset[0])

    convertDataList = list()
    convertDataList.append(list())
    convertDataList.append(list())
    convertDataList.append(list())


    for data in dataset:
        if dataset[4] == "Iris-setosa":
            convertDataList[0].append(data[0:4])
        elif (dataset[4] == "Iris-versicolor"):
            convertDataList[1].append(data[0:4])
        else:
            convertDataList[2].append(data[0:4])

    return(convertDataList)


# def calculEucli(data1,data2):
#     dist = sqrt((data1[0]-xb)^2 + (data1-yb)^2 + (data1-zb)^2)
#     return dist

def calculDistances(data, dataset):
    """ retourne les distances entre data et la partie apprentissage de dataset"""

    distances = []
    #
    # distances_eucli = list()
    # distances_eucli.append(list())
    # #
    # for c in convertDataList:
    #     for exemple in c:


	#-------- A faire... --------

    return(distances)

def calculClasse(distances):
    """ retourne le numéro de la classe déterminé à partir des distances """

	#-------- A faire... --------

    return(classe)

if __name__ == "__main__":
    print("Début programme kPPV")
    dataset = lectureFichierCSV()
    print(dataset)

    # Calcule et affiche la matrice de confusion et le taux de reco

	#-------- A faire... --------

#--------------------------------- Fin kPPV -----------------------------------
