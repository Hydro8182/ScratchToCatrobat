from scratchtocatrobat.scratch.scratch3 import visitBlockAlt
from scratchtocatrobat.scratch.scratch3 import get_block
from scratchtocatrobat.scratch.scratch3 import testglobalmap
from scratchtocatrobat.scratch.scratch3 import Scratch3Block, visitGeneric


def visitWait(block, blockmap):
    duration = visitGeneric(block, 'DURATION')
    if duration == []:
        duration = block.inputs['DURATION'][1][1]
    return ["wait:elapsed:from:", duration]

def visitRepeat(block, blockmap):
    times = visitGeneric(block, "TIMES")
    if times == []:
        times = block.inputs["TIMES"][1][1]
    substack = visitSubStack(block, "SUBSTACK")
    return ["doRepeat", times, substack]

def visitIf(block, blockmap):
    condition = visitCondition(block)
    substack1 = visitSubStack(block, "SUBSTACK")
    return ["doIf", condition, substack1]

def visitIf_else(block, blockmap):
    condition = visitCondition(block)
    substack1 = visitSubStack(block, "SUBSTACK")
    substack2 = visitSubStack(block, "SUBSTACK2")
    return ["doIfElse", condition, substack1, substack2]

def visitWait_until(block, blockmap):
    condition = visitCondition(block)
    return ["doWaitUntil", condition]

def visitRepeat_until(block, blockmap):
    condition = visitCondition(block)
    substack1 = visitSubStack(block, "SUBSTACK")
    return ["doUntil", condition, substack1]

def visitCreate_clone_of(block, blockmap):
    clone = visitGeneric(block, 'CLONE_OPTION')
    return ["createCloneOf", clone]

def visitStop(block, blockmap):
    return ["stopScripts"]

def visitStart_as_clone(block, blockmap):
    return ["whenCloned"]

def visitDelete_this_clone(block, blockmap):
    return ["deleteClone"]

def visitForever(block, blockmap):
    substack1 = visitSubStack(block, "SUBSTACK")
    return ["doForever", substack1]



def visitCondition(block):
    if "CONDITION" in block.inputs:
        conditionblock = get_block(block.inputs["CONDITION"][1])
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
    return []