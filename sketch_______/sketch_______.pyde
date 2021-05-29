bg = 0

avocado = []
 
def draw_fruits(x,y,sz , type):
    push()
    translate(x,y)
    scale(sz)
    image(avocado[type],0,0)
    pop()
    
class Avocado:
    def __init__(self):
        self.x = random(0,1300)
        self.y = -10
        self.sc = random(0.1,0.2)
        self.speed = random(1,2)
        self.type = floor(random(0,len(avocado)))
    def draw_(self):
        draw_fruits(self.x , self.y , self.sc , self.type)
    def move(self):
        self.y += self.speed


avocados = []
def setup ():
    global img ,dy, avocado,Avocado
    
    textFont(loadFont('Impact-48.vlw'))
    textSize(50)
    fill(124,71,44)
    avocado.append(loadImage("fon.png"))
    avocado.append(loadImage("kawai.png"))
    avocado.append(loadImage("gu.png"))
    
    img = loadImage("gl.png")
    size ( 1300, 400 ) 
    imageMode(CENTER)
    #textSize (30)
def draw () :
    global bg,avocados, dy, avokado, kavai
    background (149,245,109) 
    
    if (random(0,500) < bg > 9 ):
        avocados.append(Avocado())
    
    for av in avocados:
        av.draw_()
        av.move()

    image(img,655,200,200,200)
    #ellipse (200,200,70,70)
    text (bg, 640,100)    
def keyPressed () :
    global avocados , bg, kavai 
    if key == ENTER:
        avocados.append(Avocado())
    else: 
        keyCode == 0
    if  key == ENTER:
         bg += 1
    else: 
        keyCode == 0
        
     

    
    
