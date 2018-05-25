from scratchtocatrobat.scratch.scratch3 import visitBlockAlt
from scratchtocatrobat.scratch.scratch3 import get_block
from scratchtocatrobat.scratch.scratch3 import testglobalmap
from scratchtocatrobat.scratch.scratch3 import Scratch3Block
def visitWait(block, blockmap):
    pass

def visitRepeat(block, blockmap):
    pass

def visitIf(block, blockmap):
    # condition = visitBlockAlt(blockmap[block.inputs["CONDITION"][1]], blockmap)
    condition = visitCondition(block)
    # substack1 = visitBlockAlt(blockmap[block.inputs["SUBSTACK"][1]], blockmap)
    substack1 = visitSubStack(block, "SUBSTACK")
    return ["doIf", condition, substack1]

def visitIf_else(block, blockmap):
    condition = visitBlockAlt(blockmap[block.inputs["CONDITION"][1]], blockmap)
    substack1 = visitBlockAlt(blockmap[block.inputs["SUBSTACK1"][1]], blockmap)
    substack2 = visitBlockAlt(blockmap[block.inputs["SUBSTACK2"][1]], blockmap)
    return ["doIfElse", condition[0], substack1, substack2]

def visitWait_until(block, blockmap):
    pass

def visitRepeat_until(block, blockmap):
    condition = visitBlockAlt(blockmap[block.inputs["CONDITION"][1]], blockmap)
    substack1 = visitBlockAlt(blockmap[block.inputs["SUBSTACK"][1]], blockmap)
    return ["doRepeat", condition[0], substack1]

def visitCreate_clone_of(block, blockmap):
    pass

def visitStop(block, blockmap):
    return["stopScripts"]

def visitStart_as_clone(block, blockmap):
    pass

def visitDelete_this_clone(block, blockmap):
    pass

def visitForever(block, blockmap):
    substack1 = visitBlockAlt(blockmap[block.inputs["SUBSTACK"][1]], blockmap)
    return ["doForever", substack1]



def visitCondition(block):
    if "CONDITION" in block.inputs:
        conditionblock = get_block(block["CONDITION"][1])
        if isinstance(conditionblock, Scratch3Block):
            condition = visitBlockAlt(conditionblock, testglobalmap)
            return condition[0]
    else:
        return []

def visitSubStack(block, substackkey):
    if substackkey in block.inputs:
        substackstartblock = get_block(block.inputs[substackkey][1])
        if isinstance(substackstartblock, Scratch3Block):
            substack = visitBlockAlt(substackstartblock, testglobalmap)
            return substack
        else:
            return []
    else:
        return []