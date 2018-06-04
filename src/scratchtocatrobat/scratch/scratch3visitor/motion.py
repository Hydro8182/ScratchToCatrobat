from scratchtocatrobat.scratch.scratch3 import visitGeneric

def visitMovesteps(blockcontext):
    block = blockcontext.block
    steps = visitGeneric(blockcontext, "STEPS")
    return ["forward:", steps]

def visitTurnright(blockcontext):
    block = blockcontext.block
    degrees = visitGeneric(blockcontext, "DEGREES")
    return ["turnRight:", degrees]

def visitTurnleft(blockcontext):
    block = blockcontext.block
    degrees = visitGeneric(blockcontext, "DEGREES")
    return ["turnLeft:", degrees]

def visitGoto(blockcontext):
    block = blockcontext.block
    to = visitGeneric(blockcontext, "TO")
    return ["gotoSpriteOrMouse:", to]

def visitGotoxy(blockcontext):
    block = blockcontext.block
    x = visitGeneric(blockcontext, "X")
    y = visitGeneric(blockcontext, "Y")
    return ["gotoX:y:", x, y]

def visitGlideto(blockcontext):
    block = blockcontext.block
    secs = visitGeneric(blockcontext, "SECS")
    to = visitGeneric(blockcontext, "TO")
    return ["glideTo:", secs, to] #TODO: not in scratch2?

def visitGlidesecstoxy(blockcontext):
    block = blockcontext.block
    secs = visitGeneric(blockcontext, "SECS")
    #TODO: properly parse
   # if isinstance(secs[0], list) and len(secs) == 1:
    #    secs = secs[0]
    x = visitGeneric(blockcontext, "X")
    y = visitGeneric(blockcontext, "Y")
    return ["glideSecs:toX:y:elapsed:from:", secs, x, y]

def visitPointindirection(blockcontext):
    block = blockcontext.block
    direction = visitGeneric(blockcontext, "DIRECTION")
    return ["heading:", direction]

def visitPointtowards(blockcontext):
    block = blockcontext.block
    towards = visitGeneric(blockcontext, "TOWARDS")
    return ["pointTowards:", towards]

def visitChangexby(blockcontext):
    block = blockcontext.block
    x = visitGeneric(blockcontext, "DX")
    return ["changeXposBy:", x]

def visitSetx(blockcontext):
    block = blockcontext.block
    x = visitGeneric(blockcontext, "X")
    return ["xpos:", x]

def visitChangeyby(blockcontext):
    block = blockcontext.block
    y = visitGeneric(blockcontext, "DY")
    return ["changeYposBy:", y]

def visitSety(blockcontext):
    block = blockcontext.block
    y = visitGeneric(blockcontext, "Y")
    return ["ypos:", y]

def visitIfonedgebounce(blockcontext):
    block = blockcontext.block
    return ["bounceOffEdge"]

def visitSetrotationstyle(blockcontext):
    block = blockcontext.block
    rotation_style = block.fields["STYLE"][0]
    return ["setRotationStyle", rotation_style]

def visitDirection(blockcontext):
    block = blockcontext.block
    return ["heading"]

def visitYposition(blockcontext):
    block = blockcontext.block
    return ["ypos"]

def visitXposition(blockcontext):
    block = blockcontext.block
    return ["xpos"]

def visitGoto_menu(blockcontext):
    block = blockcontext.block
    return block.fields["TO"][0]

def visitGlideto_menu(blockcontext):
    block = blockcontext.block
    return block.fields["TO"][0]

def visitPointtowards_menu(blockcontext):
    block = blockcontext.block
    return block.fields["TOWARDS"][0]