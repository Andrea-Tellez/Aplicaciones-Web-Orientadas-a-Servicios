import web
import json
urls = (
    '/edades?', 'Parametros'
)
app = web.application(urls, globals())

class Parametros():
    def resta(self,ano_actualmente,fecha):
        return ano_actualmente - fecha

    def GET(self):
        try:
            parametros = web.input()
            nombre = parametros.nombre
            fecha = int(parametros["fecha_nacimiento"])
            ano_actualmente = 2021
            resultado= self.resta(ano_actualmente,fecha)
            datos = {}
            datos["nombre"] = nombre
            datos["ano_nacimiento"] = fecha
            datos["edad_actualmente"] = resultado           
            resultado = json.dumps(datos)
            archivo=open('almacenamiento.txt','a')
            texto=resultado+"\n"
            archivo.write(texto)
            archivo.close
            return resultado
            
        except:
            error = {}
            error["advertencia"] = "los datos que ingresaste no son correctos"
            return json.dumps(error)
if __name__ == "__main__":
    app.run()