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


def visitProcedures_call(blockcontext):
    proc_name = visitMutation(blockcontext)
    parameters = visitParams(blockcontext)
    return ["call", proc_name] + parameters

def visitProcedures_definition(blockcontext):
    proto = visitGeneric(blockcontext, "custom_block")
    # block = get_block(blockcontext.block.inputs["custom_block"][1], blockcontext.spriteblocks)
    # proto = visitProcedures_prototype(BlockContext(block, blockcontext.spriteblocks))

    return proto #TODO: if there are no subblocks we currently remove one nesting and the userscript no longer counts as valid script(see scratch.py:106)

def visitProcedures_prototype(blockcontext):
    proc_name = visitMutation(blockcontext)
    if proc_name == "%s":
        pass
    arguments = sanitizeListArgument(blockcontext.block.mutation["argumentnames"])
    if len(arguments) == 0:
        default_values = []
    else:
        default_values = sanitizeListDefault(blockcontext.block.mutation["argumentdefaults"])
        # default_values = sanitizeListDefault(blockcontext)

    # default_values = visitParams(blockcontext)
    return [["procDef", proc_name, arguments, default_values, False]] #TODO: what is the last parameter


def visitArgument(blockcontext):
    return ["getParam", blockcontext.block.fields["VALUE"][0], "r"] #TODO what is "r"

def visitCondition(blockcontext):
    block = blockcontext.block
    if "CONDITION" in block.inputs:
        conditionblock = get_block(block.inputs["CONDITION"][1], blockcontext.spriteblocks)
        if isinstance(conditionblock, Scratch3Block):
            condition = visitGeneric(blockcontext, "CONDITION")
            return condition
    return False

def visitSubstack(blockcontext, substackkey):
    if substackkey in blockcontext.block.inputs:
        substackstartblock = get_block(blockcontext.block.inputs[substackkey][1], blockcontext.spriteblocks)
        if isinstance(substackstartblock, Scratch3Block):
            substack = visitBlockList(BlockContext(substackstartblock, blockcontext.spriteblocks))
            return substack
    return None

def visitMutation(blockcontext):
    if blockcontext.block.mutation["proccode"] == "%s":
        pass
    return blockcontext.block.mutation["proccode"]

def visitParams(blockcontext):
    paramids = blockcontext.block.mutation["argumentids"].strip("[]").split(",")
    sanitized = []
    for paramid in paramids:
        sanitized.append(paramid.strip("\""))
        if sanitized =="Comment":
            pass
    arguments = []

    for paramid in sanitized:
        if paramid == "":
            continue #TODO: remove this once we figured out how this works
        arg = visitGeneric(blockcontext, paramid)
        #arg = blockcontext.block.inputs[paramid]
        arguments.append(arg)
    return arguments

def sanitizeListArgument(listString):
    paramids = listString.strip("[]").split(",")
    sanitized = []
    for paramid in paramids:
        paramid = paramid.strip("\"")
        if paramid == '':
            continue
        if sanitized =="Comment":
            pass
        sanitized.append(paramid)
    return sanitized

def sanitizeListDefault(listString):
    paramids = listString.strip("[]").split(",")
    sanitized = []
    for paramid in paramids:
        paramid = paramid.strip("\"")
        sanitized.append(paramid)
    return sanitized

def sanitizeBoth(blockcontext):
    block = blockcontext.block

