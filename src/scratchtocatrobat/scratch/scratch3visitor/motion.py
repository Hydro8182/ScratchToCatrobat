from scratchtocatrobat.scratch.scratch3 import visitGeneric

def visitMovesteps(block, blockmap):
    steps = visitGeneric(block, "STEPS")
    return ["forward:", steps]

def visitTurnright(block, blockmap):
    degrees = visitGeneric(block, "DEGREES")
    return ["turnRight:", degrees]

def visitTurnleft(block, blockmap):
    degrees = visitGeneric(block, "DEGREES")
    return ["turnLeft:", degrees]

def visitGoto(block, blockmap):
    to = visitGeneric(block, "TO")
    return ["gotoSpriteOrMouse:", to[0]]

def visitGotoxy(block, blockmap):
    x = visitGeneric(block, "X")
    y = visitGeneric(block, "Y")
    return ["gotoX:y:", x, y]

def visitGlideto(block, blockmap):
    secs = visitGeneric(block, "SECS")
    to = visitGeneric(block, "TO")
    return ["glideTo:", secs[0], to[0]] #TODO: not in scratch2?

def visitGlidesecstoxy(block, blockmap):
    secs = visitGeneric(block, "SECS")
    #TODO: properly parse
    if isinstance(secs, list) and len(secs) == 1:
        secs = secs[0]
    x = visitGeneric(block, "X")
    y = visitGeneric(block, "Y")
    return ["glideSecs:toX:y:elapsed:from:", secs, x, y]

def visitPointindirection(block, blockmap):
    direction = visitGeneric(block, "DIRECTION")
    return ["heading:", direction]

def visitPointtowards(block, blockmap):
    towards = visitGeneric(block, "TOWARDS")
    return ["pointTowards:", towards]

def visitChangexby(block, blockmap):
    x = visitGeneric(block, "DX")
    return ["changeXposBy:", x]

def visitSetx(block, blockmap):
    x = visitGeneric(block, "X")
    return ["xpos:", x]

def visitChangeyby(block, blockmap):
    y = visitGeneric(block, "DY")
    return ["changeYposBy:", y]

def visitSety(block, blockmap):
    y = visitGeneric(block, "Y")
    return ["ypos:", y]

def visitIfonedgebounce(block, blockmap):
    return ["bounceOffEdge"]

def visitSetrotationstyle(block, blockmap):
    rotation_style = block.fields["STYLE"][0]
    return ["setRotationStyle", rotation_style]

def visitDirection(block, blockmap):
    return ["heading"]

def visitYposition(block, blockmap):
    return ["ypos"]

def visitXposition(block, blockmap):
    return ["xpos"]

def visitGoto_menu(block, blockmap):
    return block.fields["TO"][0]

def visitGlideto_menu(block, blockmap):
    return block.fields["TO"][0]

def visitPointtowards_menu(block, blockmap):
    return block.fields["TOWARDS"][0]