import web
import requests
import json

render = web.template.render('libros/')

class Index:

    def GET(self):
        return render.index()

    def POST(self):
        form = web.input()
        autor = form.autor
        result = requests.get('https://www.etnassoft.com/api/v1/get/?book_author='+autor)
        
        autores = result.json()
      
        coded = json.dumps(autores)
        decoded = json.loads(coded)
        
        
        titulo = decoded[0]["title"]
        autor = decoded[0]["author"]
        contenido = decoded[0]["content"]
           
        Titulo = "<a> Titulo: "+titulo+" </a>"
        Autor = "<a> Autor: "+autor+" </a>"
        Contenido = "<a> Reseña: "+contenido+" </a>"

        A = "<a target='blank'> "+Autor+" </br>" +Titulo+"</br> "+Contenido+"</a>"

        return  A
