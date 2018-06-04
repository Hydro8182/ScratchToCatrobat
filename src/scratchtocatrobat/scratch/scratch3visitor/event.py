from scratchtocatrobat.scratch.scratch3 import visitGeneric

def visitWhenflagclicked(blockcontext):
    block = blockcontext.block
    return ["whenGreenFlag"]

def visitBroadcast(blockcontext):
    block = blockcontext.block
    message = visitGeneric(blockcontext, "BROADCAST_INPUT")
    return ["broadcast:", message]

def visitBroadcastandwait(blockcontext):
    block = blockcontext.block
    message = visitGeneric(blockcontext, "BROADCAST_INPUT")
    return ["doBroadcastAndWait", message]

def visitWhenthisspriteclicked(blockcontext):
    block = blockcontext.block
    return ["whenClicked"]

def visitWhenkeypressed(blockcontext):
    block = blockcontext.block
    key = block.fields["KEY_OPTION"][0]
    return ["whenKeyPressed", key]

def visitWhenbackdropswitchesto(blockcontext):
    block = blockcontext.block
    backdrop = block.fields["BACKDROP"][0]
    return ["whenSceneStarts", backdrop]

def visitWhenbroadcastreceived(blockcontext):
    block = blockcontext.block
    message = block.fields["BROADCAST_OPTION"][0]
    return ["whenIReceive", message]


def visitWhengreaterthan(blockcontext):
    block = blockcontext.block
    sensor = block.fields["WHENGREATERTHANMENU"][0].lower()
    value = visitGeneric(blockcontext, "VALUE")
    return ["whenSensorGreaterThan", sensor, value]