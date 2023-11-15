import os
import json
import io

archivo=io.open("metadata.csv",mode="r",encoding="utf-8")
data=[]
i=0
for linea in archivo:
    if i>0: 
        datos=linea.split(";")
        objeto={"isic_id":datos[0],
                "age_approx":datos[2],
                "anatom_site_general":datos[3],
                "benign_malignant":datos[4],
                "diagnosis":datos[5],
                "diagnosis_confirm_type":datos[6],
                "image_type":datos[7],
                "melanocytic":datos[8],
                "sex":datos[9]
                }
        data.append(objeto)
    i+=1

jsonConversion=json.dumps(data)
json_Archivo=open("../data.json","w")
json_Archivo.write(jsonConversion)
json_Archivo.close()



