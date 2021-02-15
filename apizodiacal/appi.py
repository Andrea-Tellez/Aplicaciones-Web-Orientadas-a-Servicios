import web
import json
import random

link = (
    '/(.*)', 'Horoscopo',
)
app = web.application(link, globals())

class Horoscopo():
  
  def GET(self,fecha_nacimiento):
    try:
      mes=int(fecha_nacimiento[3:5])
      dia=int(fecha_nacimiento[0:2])
      r = random.randint(0,11) 
      zodiacos = ["Hoy se ve recompensada tu generosidad de corazon y tu sinceridad. Alguien te alaba publicamente y despues de algunas tormentas interiores, esto te viene estupendamente para sentirte en paz. No te faltara alegria de corazon en esta jornada.",
      "Tu mente se expande y te llega un soplo de tranquilidad. Vuelves a sentir ganas de divertirte y de pasar un rato agradable. Quiza sea un plan casero, sin ninguna cosa especial, pero tambien puede ser muy atractivo si lo sabes organizar bien. Lo conseguiras con facilidad y los que lo compartan contigo, disfrutaran",
      "Nunca esta de mas perdonar y perdonarse. No te vas a preocupar demasiado si alguien te da una negativa en un tema economico porque ya tienes en mente otro plan que puede solucionar mucho mejor eso en lo que estas trabajando. Tu energia hoy estara bastante bien potenciada y estable.",
      "Hoy se abre una esperanza en una preocupacion relacionada con la salud. Si es de algun familiar, ves que todo contribuye a que mejore. Debes estar cerca de el o de ella si puedes para insuflar animos y carino. Seran la mejor medicina en este momento.",
      "Sera una jornada en la que vas a mostrar un espiritu conciliador y muy buen humor y eso es muy importante para los que estan a tu alrededor. Reconoceran tus esfuerzos y te lo agradeceran. Lo relacionado con los deportes o la cultura, te sera muy divertido",
      "Te gustan bastante las sorpresas y hoy te llevaras alguna que te hara sonreir. Deja que las cosas sean ligeras hoy con tu entorno e incluso si no te gusta algo, no hagas una escena ni contestes airadamente. Dejalo pasar, no merecera la pena",
      "Sereno y tranquilo, mantiene siempre el equilibrio entre lo posible y sus suenos, aunque lucha por ellos. Signo de aire, dominado por Venus, su caracter es fuerte y no se precipita en comprometerse con nada ni con nadie si no lo ve claro, lo que le lleva a evitar situaciones desagradables sean las que sean.",
      "Hoy algo te hara sonreir y sentir bien. Olvidaras ciertos temas tristes o melancolicos. La familia puede suponer tu mejor ambito de relaciones hoy, ya que es en ella donde vas a encontrar mas apoyo o reconocimiento a lo que estas haciendo, incluso si estas lejos fisicamente",
      "Andaras hoy con mas calma y aceptando muchas cosas de tu vida que son importantes y que de ahora en adelante vas a llevar mucho mejor. Si se trata de algo relacionado con una perdida, lo asumiras. Piensa que la vida son etapas. Hay cabos sueltos de un tema afectivo que debes de cerrar",
      "Abre tu mente a todo lo que signifique nuevas maneras de enfocarte. Eso te dara aliento de sobra para seguir. No es un dia para andar pensando en lo que haces o no, debes pasar a la accion cuanto antes y no esperar a que nadie venga a decirtelo. Es muy importante que hoy tomes la iniciativa",
      "Vas a tender a estar mas pendiente de tus procesos mentales que de tu situacion fisica, que respondera perfectamente a lo que necesites, probablemente con mucha actividad y ganas de salir de casa. Cuidado con los deseos inconscientes que no controlas",
      "Tienes mucho que hacer y no te podras pararte hoy demasiado en lo que te gustaria, al menos durante la manana. Luego ya, si consigues organizarte bien, te sera mas facil descansar, cosa que te hace falta. Respira hondo y regresaras al bienestar"
    
      ]
      if dia >= 21 and mes == 3 or mes == 4 and dia <= 20:
        aries = {} 
        aries["signo"]="aries"
        aries["numero_suerte"]= "el  6, 18 Y 28"
        aries["elemento"]= "Fuego"
        aries["color"]= "Rojo"
        aries["Horoscopo_de_hoy"] = zodiacos[r]
        a = json.dumps(aries)
        return a
      
      elif  dia >= 21 and mes == 4 or mes == 5 and dia <= 20:
        tauro = {}
        tauro["signo"]="tauro"
        tauro["numero_suerte"]= "el 4,6 y 11"
        tauro["elemento"]= "Tierra"
        tauro["color"]= " Verde"
        tauro["Horoscopo_de_hoy"] = zodiacos[r]
        t = json.dumps(tauro)
        return t
      elif  dia >= 21 and mes == 5 or mes == 6 and dia <= 21:
        geminis = {}
        geminis["signo"]="geminis"
        geminis["numero_suerte"]= "3, 12 y 18"
        geminis["elemento"]= "Aire "
        geminis["color"]= "Amarillo"
        geminis["Horoscopo_de_hoy"] = zodiacos[r]
        g = json.dumps(geminis)
        return g
      elif  dia >= 21 and mes == 6 or mes == 7 and dia <= 22:
        cancer = {}
        cancer["signo"]="cancer"
        cancer["numero_suerte"]= "2, 8 y 12"
        cancer["elemento"]= "Agua  "
        cancer["color"]= "Blanco"
        cancer["Horoscopo_de_hoy"] = zodiacos[r]
        c = json.dumps(cancer)
        return c
      elif  dia >= 23 and mes == 7 or mes == 8 and dia <= 22:
        leo = {}
        leo["signo"]="leo"
        leo["numero_suerte"]= "1, 9 y 10"
        leo["elemento"]= "Fuego"
        leo["color"]= "Amarillo"
        leo["Horoscopo_de_hoy"] = zodiacos[r]
        l = json.dumps(leo)
        return l
      elif  dia >= 23 and mes == 8 or mes == 9 and dia <= 22:
        virgo = {}
        virgo["signo"]="virgo"
        virgo["numero_suerte"]= "10, 15 y 7"
        virgo["elemento"]= "Tierra"
        virgo["color"]= "Marron"
        virgo["Horoscopo_de_hoy"] = zodiacos[r]
        v = json.dumps(virgo)
        return v
      elif  dia >= 23 and mes == 9 or mes == 10 and dia <= 22:
        libra = {}
        libra["numero_suerte"]= "2, 8 y 19"
        libra["elemento"]= "Aire"
        libra["color"]= "Rosa"
        libra["Horoscopo_de_hoy"] = zodiacos[r]
        lib= json.dumps(libra)
        return lib
      elif  dia >= 23 and mes == 10 or mes == 11 and dia <= 22:
        escorpio = {}
        escorpio["signo"]="escorpio"
        escorpio["numero_suerte"]= "4, 13 y 21"
        escorpio["elemento"]= "Agua"
        escorpio["color"]= "Rojo"   
        escorpio["Horoscopo_de_hoy"] = zodiacos[r]
        e = json.dumps(escorpio)
        return e
      elif  dia >= 23 and mes == 11 or mes == 12 and dia <= 21:
        sagitario = {}
        sagitario["signo"]="sagitario"
        sagitario["numero_suerte"]= " 9, 14 y 23"
        sagitario["elemento"]= "Fuego"
        sagitario["color"]= " Violeta"
        sagitario["Horoscopo_de_hoy"] = zodiacos[r]
        s = json.dumps(sagitario)
        return s
      elif  dia >= 22 and mes == 12 or mes == 1 and dia <= 20:
        capricornio = {}
        capricornio["signo"]="capricornio"
        capricornio["numero_suerte"]= "3, 16 y 25"
        capricornio["elemento"]= "Tierra"
        capricornio["color"]= "Gris"
        capricornio["Horoscopo_de_hoy"] = zodiacos[r]
        c = json.dumps(capricornio)
        return c
      elif  dia >= 21 and mes == 1 or mes == 2 and dia <= 18:
        acuario = {}
        acuario["signo"]="acuario"
        acuario["numero_suerte"]= " 7, 14 y 20"
        acuario["elemento"]= "Aire"
        acuario["color"]= "Azul"
        acuario["Horoscopo_de_hoy"] = zodiacos[r]
        acu = json.dumps(acuario)
        return acu  
      elif  dia >= 19 and mes == 2 or mes == 3 and dia <= 20:
        piscis = {}
        piscis["signo"]="piscis"
        piscis["numero_suerte"]= "34, 25 y 20"
        piscis["elemento"]= "Agua"
        piscis["color"]= "Azul"
        piscis["Horoscopo_de_hoy"] = zodiacos[r]
        p = json.dumps(piscis)
        return p
    except:
      error = {}
      error ["Recuerda:"] = "Solo puedes indroducir tu feha de nacimiento empezando por el dia,mes y ano" 
      e = json.dumps(error)
      return e
if __name__ == "__main__":
    app.run()