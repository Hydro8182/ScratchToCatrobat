from scratchtocatrobat.scratch.scratch3 import visitBlockAlt

def visitTouchingObject(block, blockmap):
    touch = visitBlockAlt(blockmap[block.inputs["TOUCHINGOBJECTMENU"][1]],blockmap)
    print("touching ", touch)
    return ["touching", touch[0]]

def visitTouchingObjectMenu(block, blockmap):
    selection = block.fields["TOUCHINGOBJECTMENU"][0]
    return selection


def visitAskandwait(block, blockmap):
    pass

def visitSetdragmode(block, blockmap):
    pass

def visitResettimer(block, blockmap):
    pass

def visitLoudness(block, blockmap):
    pass

def visitDistanceto(block, blockmap):
    pass

def visitColoristouchingcolor(block, blockmap):
    pass

def visitOf(block, blockmap):
    pass

def visitTouchingobject(block, blockmap):
    pass

def visitCurrent(block, blockmap):
    pass

def visitAnswer(block, blockmap):
    pass

def visitDayssince2000(block, blockmap):
    pass

def visitKeypressed(block, blockmap):
    key = visitBlockAlt(blockmap[block.inputs["KEY_OPTION"][1]], blockmap)
    return ["keyPressed", key]

def visitKey_options(block, blockmap):
    key = block.fields["KEY_OPTION"][0]
    return key

def visitMousex(block, blockmap):
    pass

def visitMousedown(block, blockmap):
    pass

def visitMousey(block, blockmap):
    pass

def visitTimer(block, blockmap):
    pass

def visitTouchingcolor(block, blockmap):
    pass

