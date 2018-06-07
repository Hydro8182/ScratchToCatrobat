from scratchtocatrobat.scratch.scratch3 import visitGeneric


def visitClear(blockcontext):
    return ["clearPenTrails"]

def visitStamp(blockcontext):
    return ["stampCostume"]

def visitPenDown(blockcontext):
    return ["putPenDown"]

def visitPenUp(blockcontext):
    return ["putPenUp"]

def visitSetPenColorToColor(blockcontext):
    color = visitGeneric(blockcontext, "COLOR")
    return ["penColor:", color]

def visitChangePenColorParamBy(blockcontext):
    colorparam = visitGeneric(blockcontext, "COLOR_PARAM")
    value = visitGeneric(blockcontext, "VALUE")
    return ["changePenHueBy:", colorparam, value] #TODO: not in scratch2? can choose parameter

def visitPen_menu_colorParam(blockcontext):
    return blockcontext.block.fields["colorParam"][0]

def visitSetPenColorParamTo(blockcontext):
    colorparam = visitGeneric(blockcontext, "COLOR_PARAM")
    value = visitGeneric(blockcontext, "VALUE")
    return ["setPenHueTo:", colorparam, value] #TODO: not in scratch2? can choose parameter

def visitChangePenSizeBy(blockcontext):
    sizechange = visitGeneric(blockcontext, "SIZE")
    return ["chagePenSizeBy:", sizechange]

def visitSetPenSizeTo(blockcontext):
    size = visitGeneric(blockcontext, "SIZE")
    return ["penSize:", size]