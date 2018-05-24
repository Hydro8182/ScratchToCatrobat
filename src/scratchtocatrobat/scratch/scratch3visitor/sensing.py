from scratchtocatrobat.scratch.scratch3 import visitBlockAlt

def visitTouchingObject(block, blockmap):
    touch = visitBlockAlt(blockmap[block.inputs["TOUCHINGOBJECTMENU"][1]],blockmap)
    return ["touching", touch[0]]

def visitTouchingObjectMenu(block, blockmap):
    selection = block.fields["TOUCHINGOBJECTMENU"][0]
    return selection


def visitAskandwait(block):
    pass

def visitSetdragmode(block):
    pass

def visitResettimer(block):
    pass

def visitLoudness(block):
    pass

def visitDistanceto(block):
    pass

def visitColoristouchingcolor(block):
    pass

def visitOf(block):
    pass

def visitTouchingobject(block):
    pass

def visitCurrent(block):
    pass

def visitAnswer(block):
    pass

def visitDayssince2000(block):
    pass

def visitKeypressed(block):
    pass

def visitMousex(block):
    pass

def visitMousedown(block):
    pass

def visitMousey(block):
    pass

def visitTimer(block):
    pass

def visitTouchingcolor(block):
    pass

