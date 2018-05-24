from scratchtocatrobat.scratch.scratch3 import visitBlockAlt

def visitWait(block, blockmap):
    pass

def visitRepeat(block, blockmap):
    pass

def visitIf(block, blockmap):
    condition = visitBlockAlt(blockmap[block.inputs["CONDITION"][1]], blockmap)
    substack1 = visitBlockAlt(blockmap[block.inputs["SUBSTACK"][1]], blockmap)
    return ["doif", condition[0], substack1]

def visitIf_else(block, blockmap):
    pass

def visitWait_until(block, blockmap):
    pass

def visitRepeat_until(block, blockmap):
    pass

def visitCreate_clone_of(block, blockmap):
    pass

def visitStop(block, blockmap):
    pass

def visitStart_as_clone(block, blockmap):
    pass

def visitDelete_this_clone(block, blockmap):
    pass

def visitForever(block, blockmap):
    pass