bg = 0

avocado = 0 
def draw_avocado(x,y,sz):
    push()
    translate(x,y)
    scale(sz)
    image(avocado,0,0)
    pop()
    
class Avocado:
    def __init__(self):
        self.x = random(0,400)
        self.y = -10
        self.sc = random(0.1,0.3)
        self.speed = random(1,3)
    def draw_(self):
        draw_avocado(self.x , self.y , self.sc)
    def move(self):
        self.y += self.speed


avocados = []
def setup ():
    global img ,dy, avocado,Avocado
    avocado = loadImage("fon.png")
    img = loadImage("gl.png")
    size ( 400, 400 ) 
    imageMode(CENTER)
    textSize (30)
    fill(255,0,0)

def draw () :
    global bg,avocados, dy, avokado
    background (149,245,109) 
    
    if (random(0,500) < bg > 9 ):
        avocados.append(Avocado())
    
    for av in avocados:
        av.draw_()
        av.move()
    
    fill (255)
    image(img,200,200,200,200)
    #ellipse (200,200,70,70)
    text (bg, 190,100)    
def keyPressed () :
    global avocados , bg 
    if key == ENTER:
        avocados.append(Avocado())
    else: 
        keyCode == 0
    if  key == ENTER:
         bg += 1
    else: 
        keyCode == 0
        
     

    
    
