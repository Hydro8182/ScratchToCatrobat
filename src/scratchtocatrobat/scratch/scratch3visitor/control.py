from scratchtocatrobat.scratch.scratch3 import visitBlockList
from scratchtocatrobat.scratch.scratch3 import get_block
from scratchtocatrobat.scratch.scratch3 import Scratch3Block, visitGeneric, BlockContext


def visitWait(blockcontext):
    block = blockcontext.block
    duration = visitGeneric(blockcontext, 'DURATION')
    if duration == []:
        duration = block.inputs['DURATION'][1][1]
    return ["wait:elapsed:from:", duration]

def visitRepeat(blockcontext):
    block = blockcontext.block
    times = visitGeneric(blockcontext, "TIMES")
    if times == []:
        times = block.inputs["TIMES"][1][1]
    substack = visitSubstack(blockcontext, "SUBSTACK")
    return ["doRepeat", times, substack]

def visitIf(blockcontext):
    block = blockcontext.block
    condition = visitCondition(blockcontext)
    substack1 = visitSubstack(blockcontext, "SUBSTACK")
    return ["doIf", condition, substack1]

def visitIf_else(blockcontext):
    block = blockcontext.block
    condition = visitCondition(blockcontext)
    substack1 = visitSubstack(blockcontext, "SUBSTACK")
    substack2 = visitSubstack(blockcontext, "SUBSTACK2")
    return ["doIfElse", condition, substack1, substack2]

def visitWait_until(blockcontext):
    block = blockcontext.block
    condition = visitCondition(blockcontext)
    return ["doWaitUntil", condition]

def visitRepeat_until(blockcontext):
    block = blockcontext.block
    condition = visitCondition(blockcontext)
    substack1 = visitSubstack(blockcontext, "SUBSTACK")
    return ["doUntil", condition, substack1]

def visitCreate_clone_of(blockcontext):
    block = blockcontext.block
    clone = visitGeneric(blockcontext, 'CLONE_OPTION')
    return ["createCloneOf", clone]

def visitCreate_clone_of_menu(blockcontext):
    block = blockcontext.block
    return block.fields["CLONE_OPTION"][0]

def visitStop(blockcontext):
    block = blockcontext.block
    return ["stopScripts", block.fields["STOP_OPTION"][0]]

def visitStart_as_clone(blockcontext):
    block = blockcontext.block
    return ["whenCloned"]

def visitDelete_this_clone(blockcontext):
    block = blockcontext.block
    return ["deleteClone"]

def visitForever(blockcontext):
    block = blockcontext.block
    substack1 = visitSubstack(blockcontext, "SUBSTACK")
    return ["doForever", substack1]



def visitCondition(blockcontext):
    block = blockcontext.block
    if "CONDITION" in block.inputs:
        conditionblock = get_block(block.inputs["CONDITION"][1], blockcontext.spriteblocks)
        if isinstance(conditionblock, Scratch3Block):
            condition = visitGeneric(blockcontext, "CONDITION")
            return condition
    return []

def visitSubstack(blockcontext, substackkey):
    if substackkey in blockcontext.block.inputs:
        substackstartblock = get_block(blockcontext.block.inputs[substackkey][1], blockcontext.spriteblocks)
        if isinstance(substackstartblock, Scratch3Block):
            substack = visitBlockList(BlockContext(substackstartblock, blockcontext.spriteblocks))
            return substack
    return []