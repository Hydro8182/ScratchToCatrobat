from scratchtocatrobat.scratch.scratch3 import visitBlockAlt, Scratch3Block, get_block, testglobalmap, visitGeneric

def visitTouchingObject(block):
    touch = visitBlockAlt(blockmap[block.inputs["TOUCHINGOBJECTMENU"][1]],blockmap)
    print("touching ", touch)
    return ["touching:", touch[0]]

def visitTouchingObjectMenu(block):
    selection = block.fields["TOUCHINGOBJECTMENU"][0]
    return selection


def visitAskandwait(block):
    question = visitGeneric(block, "QUESTION")
    if question == []:
        question = block.inputs["QUESTION"][1][1]
    return ["doAsk", question]

def visitSetdragmode(block):
    dragmode = block.fields["DRAG_MODE"][0]
    return ["dragMode", dragmode] #TODO: not implemented in old converter?


def visitResettimer(block):
    return ["timerReset"]

def visitLoudness(block):
    return ["soundLevel"]

def visitDistanceto(block):
    distance = visitGeneric(block, "DISTANCETOMENU")
    return ["distanceTo:", distance]
    #TODO: distanceTO(join("asdf", "asdfdsf")) hat zwei refernezen in inputs:
        # 1: zum join block, 2: zu distance_menu{mouse} ?????

def visitColoristouchingcolor(block):
    color = visitGeneric(block, "COLOR")
    if color == []:
        color = block.inputs["COLOR"][1][1]

    color2 = visitGeneric(block, "COLOR2")
    if color2 == []:
        color2 = block.inputs["COLOR2"][1][1]
    return ["touchingColor:", color, color2]

def visitOf(block):
    property = block.fields['PROPERTY'][0]
    object = visitGeneric(block, 'OBJECT')
    return ["getAttribute:of:", property, object]


def visitTouchingobject(block):
    object = visitGeneric(block, 'TOUCHINGOBJECTMENU')
    return ["touching:", object]

def visitCurrent(block):
    return ["timeAndDate", block.fields['CURRENTMENU'][0]]

def visitAnswer(block):
    return ["answer"]

def visitDayssince2000(block):
    return ["timestamp"]

def visitKeypressed(block):
    # key = visitBlockAlt(blockmap[block.inputs["KEY_OPTION"][1]], blockmap)
    key = visitGeneric(block, "KEY_OPTION")
    return ["keyPressed:", key] #TODO: is this always key[0]?

def visitKey_options(block):
    key = block.fields["KEY_OPTION"][0]
    return key

def visitMousex(block):
    return ["mouseX"]

def visitMousedown(block):
    return ["mousePressed"]


def visitMousey(block):
    return ["mouseY"]


def visitTimer(block):
    return ["timer"]

def visitTouchingcolor(block):
    color = visitGeneric(block, "COLOR")
    if color == []:
        color = block.inputs["COLOR"][1]
    return ["touchingColor:", color]

def visitUsername(block):
    return ["getUserName"]


def visitOf_object_menu(block):
    return block.fields['OBJECT'][0]

def visitTouchingobjectmenu(block):
    return block.fields['TOUCHINGOBJECTMENU'][0]

