def setup():
    size(400, 400)
    
def draw():
    background(255)
    
    # size of each cell
    cell_width = width / 5
    cell_height = height / 5
    
    for row in range(5):
        for col in range(5):
            x = col * cell_width
            y = row * cell_height
            push()
            translate(x, y)
        
            scale(0.20)
            
            drawObject()
            
            pop()

def drawObject():
    # Controller body
    push()
    translate(200, 150)  
    rotate(radians(frameCount)) 
    stroke(0)
    fill(80)
    rect(-150, -100, 300, 200, 20) 
    pop()
    
    # Left stick
    fill(255)
    ellipse(100, 125, 50, 50)
    fill(0)
    ellipse(100, 125, 20, 20)
    
    # Right stick
    fill(255)
    ellipse(300, 125, 50, 50)
    fill(0)
    ellipse(300, 125, 20, 20)
    
    # D-pad
    fill(255)
    rect(175, 75 + sin(frameCount*0.05)*10, 50, 50, 10)
    rect(125 + cos(frameCount*0.05)*10, 125, 50, 50, 10)
    rect(225 + cos(frameCount*0.05)*10, 125, 50, 50, 10)
    rect(175, 175 + sin(frameCount*0.05)*10, 50, 50, 10)
