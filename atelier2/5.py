list=[47,64,69,37,76,83,95,97]
dict={"yassine":47, "imane":69, "mohamed":76, "abir":97}
for e in list:
    if e not in dict:#l'élément n'est pas une valeur de clé dans le dictionnaire
     list.remove(e) #supprimer l'élément en utilisant la méthode remove()
print(list)