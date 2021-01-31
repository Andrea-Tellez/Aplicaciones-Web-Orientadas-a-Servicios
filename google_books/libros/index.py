import web
import requests
import json

render = web.template.render('libros/')

class Index:

    def GET(self):
        return render.index()

    def POST(self):
        form = web.input()
        book = form.book
        result = requests.get('https://www.googleapis.com/books/v1/volumes?q='+book)
        
        books = result.json()
        print(type(books))

        items = books["items"]

        coded = json.dumps(items)
        decoded = json.loads(coded)

        print(decoded[0]["volumeInfo"]["infoLink"])
        
        url = decoded[0]["volumeInfo"]["infoLink"]
        titulo = decoded[0]["volumeInfo"]["title"]
        autor = decoded[0]["volumeInfo"]["authors"] 
        imag = decoded[0]["volumeInfo"]["imageLinks"] ["thumbnail"]

        tit =" ".join(titulo)
        au =" ".join(autor)


        titulo = "<a> Titulo: "+tit+"</a>"
        autor = "<a> Autor: "+au+"</a>"
        imag = "<a target= 'blank' href='"+imag+"'>Portada del Libro"+book+"</a>"


        link = "<a target='blank' href='"+url+"'>¡Has click aqui para comprar el libro ahora!"+book+"</br> "+titulo+"</br>"+autor+"</br>"+imag+"</a>"

        return link
