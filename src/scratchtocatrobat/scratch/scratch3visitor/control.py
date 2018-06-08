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
    condition = visitCondition(blockcontext)
    substack1 = visitSubstack(blockcontext, "SUBSTACK")
    return ["doIf", condition, substack1]

def visitIf_else(blockcontext):
    condition = visitCondition(blockcontext)
    substack1 = visitSubstack(blockcontext, "SUBSTACK")
    substack2 = visitSubstack(blockcontext, "SUBSTACK2")
    return ["doIfElse", condition, substack1, substack2]

def visitWait_until(blockcontext):
    condition = visitCondition(blockcontext)
    return ["doWaitUntil", condition]

def visitRepeat_until(blockcontext):
    condition = visitCondition(blockcontext)
    substack1 = visitSubstack(blockcontext, "SUBSTACK")
    return ["doUntil", condition, substack1]

def visitCreate_clone_of(blockcontext):
    clone = visitGeneric(blockcontext, 'CLONE_OPTION')
    return ["createCloneOf", clone]

def visitCreate_clone_of_menu(blockcontext):
    block = blockcontext.block
    return block.fields["CLONE_OPTION"][0]

def visitStop(blockcontext):
    block = blockcontext.block
    return ["stopScripts", block.fields["STOP_OPTION"][0]]

def visitStart_as_clone(blockcontext):
    return ["whenCloned"]

def visitDelete_this_clone(blockcontext):
    return ["deleteClone"]

def visitForever(blockcontext):
    substack1 = visitSubstack(blockcontext, "SUBSTACK")
    return ["doForever", substack1]


def visitProcedures_call(blockcontext):
    proc_name = visitMutation(blockcontext)
    parameters = visitParams(blockcontext)
    return ["call", proc_name] + parameters

def visitProcedures_definition(blockcontext):
    proto = visitGeneric(blockcontext, "custom_block")
    return proto

def visitProcedures_prototype(blockcontext):
    proc_name = visitMutation(blockcontext)
    arguments = sanitizeListArgument(blockcontext.block.mutation["argumentnames"])
    if len(arguments) == 0:
        default_values = []
    else:
        default_values = sanitizeListDefault(blockcontext.block.mutation["argumentdefaults"])
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
    return blockcontext.block.mutation["proccode"]

def visitParams(blockcontext):
    paramids = blockcontext.block.mutation["argumentids"].strip("[]").split(",")
    sanitized = []
    for paramid in paramids:
        sanitized.append(paramid.strip("\""))
    arguments = []

    for paramid in sanitized:
        if paramid == "":
            continue
        arg = visitGeneric(blockcontext, paramid)
        arguments.append(arg)
    return arguments

def sanitizeListArgument(listString):
    paramids = listString.strip("[]").split(",")
    sanitized = []
    for paramid in paramids:
        paramid = paramid.strip("\"")
        if paramid == '':
            continue
        sanitized.append(paramid)
    return sanitized

def sanitizeListDefault(listString):
    paramids = listString.strip("[]").split(",")
    sanitized = []
    for paramid in paramids:
        paramid = paramid.strip("\"")
        sanitized.append(paramid)
    return sanitized


