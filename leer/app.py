import web
import json
urls = (
    '/edades?', 'Parametros'
)
app = web.application(urls, globals())

class Parametros():
  json_file={}
  def GET(self):
      parametros = web.input() 
      action = parametros["action"]
      if action == "get":
        return self.read()
      elif action == "put":
        nombre = parametros["nombre"]
        fecha_nacimiento = parametros["fecha_nacimiento"]
        add={}
        add["resultado"]="registro anadido"
        a = json.dumps(add)
        return self.write(nombre, fecha_nacimiento),a
        
 
  def write(self, nombre,fecha_nacimiento):
    try:
      fecha = fecha_nacimiento
      año_nacimiento = int(fecha_nacimiento[6:10])
      año_actualmente = 2021
      edad= año_actualmente - año_nacimiento
      datos = {
      "nombre" : nombre,
      "fecha_nacimiento" : fecha,
      "edad" : edad
      }
      with open("datos.json") as file:
        self.json_file = json.load(file)
        self.json_file["datos"].append(datos)
        with open("datos.json","w") as file:
          json.dump(self.json_file, file)
          return json.dumps(datos)
    except  Exception as error:
      print("Error {}".format(error.args[0])) 

  def read(self):
        with open("datos.json") as file:
            self.json_file = json.load(file)
            return json.dumps(self.json_file)             
if __name__ == "__main__":
    app.run()