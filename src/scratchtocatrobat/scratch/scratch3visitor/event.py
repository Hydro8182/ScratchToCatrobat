from scratchtocatrobat.scratch.scratch3 import visitGeneric

def visitWhenflagclicked(block):
    return ["whenGreenFlag"]

def visitBroadcast(block):
    message = visitGeneric(block, "BROADCAST_INPUT")
    return ["broadcast:", message]

def visitBroadcastandwait(block):
    message = visitGeneric(block, "BROADCAST_INPUT")
    return ["doBroadcastAndWait", message]

def visitWhenthisspriteclicked(block):
    return ["whenClicked"]

def visitWhenkeypressed(block):
    key = block.fields["KEY_OPTION"][0]
    return ["whenKeyPressed", key]

def visitWhenbackdropswitchesto(block):
    backdrop = block.fields["BACKDROP"][0]
    return ["whenSceneStarts", backdrop]

def visitWhenbroadcastreceived(block):
    message = block.fields["BROADCAST_OPTION"][0]
    return ["whenIReceive", message]


def visitWhengreaterthan(block):
    sensor = block.fields["WHENGREATERTHANMENU"][0].lower()
    value = visitGeneric(block, "VALUE")
    return ["whenSensorGreaterThan", sensor, value]