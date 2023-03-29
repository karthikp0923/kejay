def setup():
    size(400, 400)

def draw():
    background(255)
    
    # size of each cell
    cell_width = width / 5
    cell_height = height / 5
    
    # loop
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
    stroke(0)
    fill(80)
    rect(50, 50, 300, 200, 20)
    
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
    rect(175, 75, 50, 50, 10)
    rect(125, 125, 50, 50, 10)
    rect(225, 125, 50, 50, 10)
    rect(175, 175, 50, 50, 10)
