from scratchtocatrobat.scratch.scratch3 import visitBlockAlt
from scratchtocatrobat.scratch.scratch3 import testglobalmap

def visitSayforsecs(block, blockmap):
    message = visitBlockAlt(blockmap[block.inputs["MESSAGE"][1]], blockmap)
    duration = visitBlockAlt(blockmap[block.inputs["SECS"][1]], blockmap)
    return ["sayFor", message, duration]

def visitSay(block, blockmap):
    pass

def visitThinkforsecs(block, blockmap):
    pass

def visitThink(block, blockmap):
    pass

def visitSwitchcostumeto(block, blockmap):
    pass

def visitNextcostume(block, blockmap):
    pass

def visitSwitchbackdropto(block, blockmap):
    pass

def visitNextbackdrop(block, blockmap):
    pass

def visitChangesizeby(block, blockmap):
    pass

def visitSetsizeto(block, blockmap):
    pass

def visitChangeeffectby(block, blockmap):
    pass

def visitSeteffectto(block, blockmap):
    pass

def visitCleargraphiceffects(block, blockmap):
    pass

def visitShow(block, blockmap):
    pass

def visitHide(block, blockmap):
    pass

def visitGotofrontback(block, blockmap):
    pass

def visitGoforwardbackwardlayers(block, blockmap):
    pass

def visitCostumenumbername(block, blockmap):
    pass

def visitBackdropnumbername(block, blockmap):
    pass

def visitSize(block, blockmap):
    pass