from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import json
import io

app=Flask(__name__)

@app.route('/estadisticos',methods=['GET','POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def index():
    archivoJson=open("../data.json","r")
    datos=json.load(archivoJson)
    conteoMaligno=0
    conteoBenigno=0
    conteoSinDiagnostico=0
    conteoMalignoH=0
    conteoBenignoH=0
    conteoSinDiagnosticoH=0
    if request.method == 'GET':
        for linea in datos:
            if(linea["benign_malignant"]=="malignant"):
                conteoMaligno+=1
            if(linea["benign_malignant"]=="benign"):
                conteoBenigno+=1
            if(linea["benign_malignant"]==""):
                conteoSinDiagnostico+=1
            resultados=[{"maligno":conteoMaligno,"benigno":conteoBenigno,"sinDiagnostico":conteoSinDiagnostico}]
    else:
         entrada = (json.loads(request.data))
         for linea in datos:
            if(entrada["genero"]=="Hombre"):
                if(linea["benign_malignant"]=="malignant" and linea["sex"]=="male\n"):
                    conteoMalignoH+=1
                if(linea["benign_malignant"]=="benign" and linea["sex"]=="male\n"):
                    conteoBenignoH+=1
                if(linea["benign_malignant"]=="" and linea["sex"]=="male\n"):
                    conteoSinDiagnosticoH+=1

            if(entrada["genero"]=="Mujer"):
                if(linea["benign_malignant"]=="malignant" and linea["sex"]=="female\n"):
                    conteoMalignoH+=1
                if(linea["benign_malignant"]=="benign" and linea["sex"]=="female\n"):
                    conteoBenignoH+=1
                if(linea["benign_malignant"]=="" and linea["sex"]=="female\n"):
                    conteoSinDiagnosticoH+=1
            
            resultados=[{"maligno":conteoMalignoH,"benigno":conteoBenignoH,"sinDiagnostico":conteoSinDiagnosticoH}]
    return jsonify(resultados)

if __name__=="__main__":
    app.run(debug=True)