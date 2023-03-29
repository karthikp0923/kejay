
def setup():
    size(400, 400)

def draw():
    background(255)
    
    #controller body
    stroke(0)
    fill(80)
    rect(50, 50, 300, 200, 20)
    
    #left stick
    fill(255)
    ellipse(100, 125, 50, 50)
    fill(0)
    ellipse(100, 125, 20, 20)
    
    #right stick
    fill(255)
    ellipse(300, 125, 50, 50)
    fill(0)
    ellipse(300, 125, 20, 20)
    
    #D-pad
    fill(255)
    rect(175, 75, 50, 50, 10)
    rect(125, 125, 50, 50, 10)
    rect(225, 125, 50, 50, 10)
    rect(175, 175, 50, 50, 10)
    
