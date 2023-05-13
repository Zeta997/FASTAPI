import json


class DataJSON():
    
    wheatherCiudades=dict() 
    ciudad=str()
    def ficheroJSON(self,data): 
        
       pass
        # for key in data:
        #     if key=='ciudades':
        #         self.wheatherCiudades[key]=data[key] 
        # try:
        #     fichero="tiempo.json"
        #     with open(fichero,"w") as dato:
        #         dato.write(f'"{self.wheatherCiudades}"')
        #         dato.close()
        # except:           
        #     file = open(fichero, "wt", encoding="UTF-8")
        #     contenido=f'"{self.wheatherCiudades}"'
        #     file.write(contenido)
        #     file.close()     


    def TemperaturaMax(self,valor,data):
        for casilla in range(0,len(data['ciudades'])):
            if data['ciudades'][casilla]['name']==valor:
                temperaturaMax=data['ciudades'][casilla]['temperatures']['max']
                return temperaturaMax

    def TemperaturaMin(self,valor,data):
        for casilla in range(0,len(data['ciudades'])):
            if data['ciudades'][casilla]['name']==valor:
                temperaturaMin=data['ciudades'][casilla]['temperatures']['min']
                return temperaturaMin
            
if __name__=='__main__':
    ejecute = DataJSON()
    ejecute.ficheroJSON()