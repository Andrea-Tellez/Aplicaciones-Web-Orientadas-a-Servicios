import web
#import json

urls = (
    '/Aries(.*)', 'Aries',
    '/Tauro', 'Tauro',
    '/hola', 'hola',
)
app = web.application(urls, globals())

class Aries():
    def GET(self,aries):
        a=[]
        aries = {}

        aries["aries"]= "Hoy se ve recompensada tu generosidad de corazón y tu sinceridad. Alguien te alaba públicamente y después de algunas tormentas interiores, esto te viene estupendamente para sentirte en paz. No te faltará alegría de corazón en esta jornada."
        aries["numero_suerte"]= "el  6, 18 Y 28"
        aries["elemento"]= "fuego"
        aries["color"]= "rojo"
        
        for row in aries:
          print(aries[row])
        return a
class Tauro():
    def GET(tauro):
        t=[]
        tauro = {}

        tauro["tauro"]= "Tu mente se expande y te llega un soplo de tranquilidad. Vuelves a sentir ganas de divertirte y de pasar un rato agradable. Quizá sea un plan casero, sin ninguna cosa especial, pero también puede ser muy atractivo si lo sabes organizar bien. Lo conseguirás con facilidad y los que lo compartan contigo, disfrutarán."
        tauro["numero_suerte"]= "el 4,6 y 11"
        tauro["elemento"]= "fuego"
        tauro["color"]= "amarillo"
        
        for row in tauro:
          print(tauro[row])
        return t
class Geminis():
    def GET(geminis):
        g=[]
        geminis = {}

        geminis["geminis"]= "Tu mente se expande y te llega un soplo de tranquilidad. Vuelves a sentir ganas de divertirte y de pasar un rato agradable. Quizá sea un plan casero, sin ninguna cosa especial, pero también puede ser muy atractivo si lo sabes organizar bien. Lo conseguirás con facilidad y los que lo compartan contigo, disfrutarán."
        geminis["numero_suerte"]= "el 4,6 y 11"
        geminis["elemento"]= "fuego"
        geminis["color"]= "amarillo"
        
        for row in geminis:
          print(geminis[row])
        return g
if __name__ == "_main_":
    app.run()