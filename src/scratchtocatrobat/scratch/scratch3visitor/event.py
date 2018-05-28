from scratchtocatrobat.scratch.scratch3 import visitGeneric

def visitWhenflagclicked(block, blockmap):
    return ["whenGreenFlag"]

def visitBroadcast(block, blockmap):
    pass

def visitBroadcastandwait(block, blockmap):
    pass

def visitWhenthisspriteclicked(block, blockmap):
    return ["whenClicked"]

def visitWhenkeypressed(block, blockmap):
    key = block.fields["KEY_OPTION"][0]
    return ["whenKeyPressed", key]

def visitWhenbackdropswitchesto(block, blockmap):
    backdrop = block.fields["BACKDROP"][0]
    return ["whenSceneStarts", backdrop]

def visitWhenbroadcastreceived(block, blockmap):
    message = block.fields["BROADCAST_OPTION"][0]
    return ["whenIReceive", message]


def visitWhengreaterthan(block, blockmap):
    sensor = block.fields["WHENGREATERTHANMENU"][0]
    value = visitGeneric(block, "VALUE")
    return ["whenSensorGreaterThan", sensor, value]