from scratchtocatrobat.scratch.scratch3 import visitBlockAlt

def visitWait(block):
    pass

def visitRepeat(block):
    pass

def visitIf(block, blockmap):
    condition = visitBlockAlt(blockmap[block.inputs["CONDITION"][1]], blockmap)
    substack1 = visitBlockAlt(blockmap[block.inputs["SUBSTACK"][1]], blockmap)
    return ["doif", condition[0], substack1]

def visitIf_else(block):
    pass

def visitWait_until(block):
    pass

def visitRepeat_until(block):
    pass

def visitCreate_clone_of(block):
    pass

def visitStop(block):
    pass

def visitStart_as_clone(block):
    pass

def visitDelete_this_clone(block):
    pass

def visitForever(block):
    pass