from scratchtocatrobat.scratch.scratch3 import visitGeneric

def visitMovesteps(block):
    steps = visitGeneric(block, "STEPS")
    return ["forward:", steps]

def visitTurnright(block):
    degrees = visitGeneric(block, "DEGREES")
    return ["turnRight:", degrees]

def visitTurnleft(block):
    degrees = visitGeneric(block, "DEGREES")
    return ["turnLeft:", degrees]

def visitGoto(block):
    to = visitGeneric(block, "TO")
    return ["gotoSpriteOrMouse:", to]

def visitGotoxy(block):
    x = visitGeneric(block, "X")
    y = visitGeneric(block, "Y")
    return ["gotoX:y:", x, y]

def visitGlideto(block):
    secs = visitGeneric(block, "SECS")
    to = visitGeneric(block, "TO")
    return ["glideTo:", secs, to] #TODO: not in scratch2?

def visitGlidesecstoxy(block):
    secs = visitGeneric(block, "SECS")
    #TODO: properly parse
   # if isinstance(secs[0], list) and len(secs) == 1:
    #    secs = secs[0]
    x = visitGeneric(block, "X")
    y = visitGeneric(block, "Y")
    return ["glideSecs:toX:y:elapsed:from:", secs, x, y]

def visitPointindirection(block):
    direction = visitGeneric(block, "DIRECTION")
    return ["heading:", direction]

def visitPointtowards(block):
    towards = visitGeneric(block, "TOWARDS")
    return ["pointTowards:", towards]

def visitChangexby(block):
    x = visitGeneric(block, "DX")
    return ["changeXposBy:", x]

def visitSetx(block):
    x = visitGeneric(block, "X")
    return ["xpos:", x]

def visitChangeyby(block):
    y = visitGeneric(block, "DY")
    return ["changeYposBy:", y]

def visitSety(block):
    y = visitGeneric(block, "Y")
    return ["ypos:", y]

def visitIfonedgebounce(block):
    return ["bounceOffEdge"]

def visitSetrotationstyle(block):
    rotation_style = block.fields["STYLE"][0]
    return ["setRotationStyle", rotation_style]

def visitDirection(block):
    return ["heading"]

def visitYposition(block):
    return ["ypos"]

def visitXposition(block):
    return ["xpos"]

def visitGoto_menu(block):
    return block.fields["TO"][0]

def visitGlideto_menu(block):
    return block.fields["TO"][0]

def visitPointtowards_menu(block):
    return block.fields["TOWARDS"][0]