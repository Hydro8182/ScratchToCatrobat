from scratchtocatrobat.scratch.scratch3 import visitBlockAlt, Scratch3Block, get_block, testglobalmap, visitGeneric

def visitTouchingObject(block, blockmap):
    touch = visitBlockAlt(blockmap[block.inputs["TOUCHINGOBJECTMENU"][1]],blockmap)
    print("touching ", touch)
    return ["touching:", touch[0]]

def visitTouchingObjectMenu(block, blockmap):
    selection = block.fields["TOUCHINGOBJECTMENU"][0]
    return selection


def visitAskandwait(block, blockmap):
    question = visitGeneric(block, "QUESTION")
    if question == []:
        question = block.inputs["QUESTION"][1][1]
    return ["doAsk", question]

def visitSetdragmode(block, blockmap):
    dragmode = block.fields["DRAG_MODE"][0]
    return ["dragMode", dragmode] #TODO: not implemented in old converter?


def visitResettimer(block, blockmap):
    return ["timerReset"]

def visitLoudness(block, blockmap):
    return ["soundLevel"]

def visitDistanceto(block, blockmap):
    pass
    #TODO: distanceTO(join("asdf", "asdfdsf")) hat zwei refernezen in inputs:
        # 1: zum join block, 2: zu distance_menu{mouse} ?????

def visitColoristouchingcolor(block, blockmap):
    color = visitGeneric(block, "COLOR")
    if color == []:
        color = block.inputs["COLOR"][1][1]

    color2 = visitGeneric(block, "COLOR2")
    if color2 == []:
        color2 = block.inputs["COLOR2"][1][1]
    return ["touchingColor:", color, color2]

def visitOf(block, blockmap):
    property = block.fields['PROPERTY'][0]
    object = visitGeneric(block, 'OBJECT')
    return ["getAttribute:of:", property, object]


def visitTouchingobject(block, blockmap):
    object = visitGeneric(block, 'TOUCHINGOBJECTMENU')
    return ["touching:", object]

def visitCurrent(block, blockmap):
    return ["timeAndDate", block.fields['CURRENTMENU'][0]]

def visitAnswer(block, blockmap):
    return ["answer"]

def visitDayssince2000(block, blockmap):
    return ["timestamp"]

def visitKeypressed(block, blockmap):
    key = visitBlockAlt(blockmap[block.inputs["KEY_OPTION"][1]], blockmap)
    return ["keyPressed", key]

def visitKey_options(block, blockmap):
    key = block.fields["KEY_OPTION"][0]
    return key

def visitMousex(block, blockmap):
    return ["mouseX"]

def visitMousedown(block, blockmap):
    return ["mousePressed"]


def visitMousey(block, blockmap):
    return ["mouseY"]


def visitTimer(block, blockmap):
    return ["timer"]

def visitTouchingcolor(block, blockmap):
    color = visitGeneric(block, "COLOR")
    if color == []:
        color = block.inputs["COLOR"][1]
    return ["touchingColor:", color]

def visitUsername(block, blockmap):
    return ["getUserName"]


def visitOf_object_menu(block, blockmap):
    return block.fields['OBJECT'][0]

def visitTouchingobjectmenu(block, blockmap):
    return block.fields['TOUCHINGOBJECTMENU'][0]

