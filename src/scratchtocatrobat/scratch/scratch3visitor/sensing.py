from scratchtocatrobat.scratch.scratch3 import visitBlockAlt, Scratch3Block, get_block, testglobalmap, visitGeneric

def visitTouchingObject(blockcontext):
    block = blockcontext.block
    touch = visitGeneric(blockcontext, "TOUCHINGOBJECTMENU")
    print("touching ", touch)
    return ["touching:", touch[0]]

def visitTouchingObjectMenu(blockcontext):
    block = blockcontext.block
    selection = block.fields["TOUCHINGOBJECTMENU"][0]
    return selection


def visitAskandwait(blockcontext):
    block = blockcontext.block
    question = visitGeneric(blockcontext, "QUESTION")
    if question == []:
        question = block.inputs["QUESTION"][1][1]
    return ["doAsk", question]

def visitSetdragmode(blockcontext):
    block = blockcontext.block
    dragmode = block.fields["DRAG_MODE"][0]
    return ["dragMode", dragmode] #TODO: not implemented in old converter?


def visitResettimer(blockcontext):
    block = blockcontext.block
    return ["timerReset"]

def visitLoudness(blockcontext):
    block = blockcontext.block
    return ["soundLevel"]

def visitDistanceto(blockcontext):
    block = blockcontext.block
    distance = visitGeneric(blockcontext, "DISTANCETOMENU")
    return ["distanceTo:", distance]
    #TODO: distanceTO(join("asdf", "asdfdsf")) hat zwei refernezen in inputs:
        # 1: zum join block, 2: zu distance_menu{mouse} ?????

def visitColoristouchingcolor(blockcontext):
    block = blockcontext.block
    color = visitGeneric(blockcontext, "COLOR")
    if color == []:
        color = block.inputs["COLOR"][1][1]

    color2 = visitGeneric(blockcontext, "COLOR2")
    if color2 == []:
        color2 = block.inputs["COLOR2"][1][1]
    return ["touchingColor:", color, color2]

def visitOf(blockcontext):
    block = blockcontext.block
    property = block.fields['PROPERTY'][0]
    object = visitGeneric(blockcontext, 'OBJECT')
    return ["getAttribute:of:", property, object]


def visitTouchingobject(blockcontext):
    block = blockcontext.block
    object = visitGeneric(blockcontext, 'TOUCHINGOBJECTMENU')
    return ["touching:", object]

def visitCurrent(blockcontext):
    block = blockcontext.block
    return ["timeAndDate", block.fields['CURRENTMENU'][0]]

def visitAnswer(blockcontext):
    block = blockcontext.block
    return ["answer"]

def visitDayssince2000(blockcontext):
    block = blockcontext.block
    return ["timestamp"]

def visitKeypressed(blockcontext):
    block = blockcontext.block
    # key = visitBlockAlt(blockmap[block.inputs["KEY_OPTION"][1]], blockmap)
    key = visitGeneric(blockcontext, "KEY_OPTION")
    return ["keyPressed:", key] #TODO: is this always key[0]?

def visitKey_options(blockcontext):
    block = blockcontext.block
    key = block.fields["KEY_OPTION"][0]
    return key

def visitMousex(blockcontext):
    block = blockcontext.block
    return ["mouseX"]

def visitMousedown(blockcontext):
    block = blockcontext.block
    return ["mousePressed"]


def visitMousey(blockcontext):
    block = blockcontext.block
    return ["mouseY"]


def visitTimer(blockcontext):
    block = blockcontext.block
    return ["timer"]

def visitTouchingcolor(blockcontext):
    block = blockcontext.block
    color = visitGeneric(blockcontext, "COLOR")
    if color == []:
        color = block.inputs["COLOR"][1]
    return ["touchingColor:", color]

def visitUsername(blockcontext):
    block = blockcontext.block
    return ["getUserName"]


def visitOf_object_menu(blockcontext):
    block = blockcontext.block
    return block.fields['OBJECT'][0]

def visitTouchingobjectmenu(blockcontext):
    block = blockcontext.block
    return block.fields['TOUCHINGOBJECTMENU'][0]

