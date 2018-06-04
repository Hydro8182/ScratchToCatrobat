from scratchtocatrobat.scratch.scratch3 import visitGeneric

def visitSayforsecs(blockcontext):
    block = blockcontext.block
    message = visitGeneric(blockcontext, "MESSAGE")
    duration = visitGeneric(blockcontext, "SECS")
    return ["say:duration:elapsed:from:", message, duration]

def visitSay(blockcontext):
    block = blockcontext.block
    message = visitGeneric(blockcontext, "MESSAGE")
    return ["say:", message]

def visitThinkforsecs(blockcontext):
    block = blockcontext.block
    message = visitGeneric(blockcontext, "MESSAGE")
    duration = visitGeneric(blockcontext, "SECS")
    return ["think:duration:elapsed:from:", message, duration]

def visitThink(blockcontext):
    block = blockcontext.block
    message = visitGeneric(blockcontext, "MESSAGE")
    return ["think:", message]

def visitSwitchcostumeto(blockcontext):
    block = blockcontext.block
    costume = visitGeneric(blockcontext, "COSTUME")
    return ["lookLike:", costume]

def visitNextcostume(blockcontext):
    block = blockcontext.block
    return ["nextCostume"]

def visitSwitchbackdropto(blockcontext):
    block = blockcontext.block
    backdrop = visitGeneric(blockcontext, "BACKDROP")
    return ["startScene", backdrop]

def visitNextbackdrop(blockcontext):
    block = blockcontext.block
    return ["nextBackdropPlaceholder"] #TODO: not in scratch2

def visitChangesizeby(blockcontext):
    block = blockcontext.block
    size = visitGeneric(blockcontext, "CHANGE")
    return ["changeSizeBy:", size]

def visitSetsizeto(blockcontext):
    block = blockcontext.block
    size = visitGeneric(blockcontext, "SIZE")
    return ["setSizeTo:", size]

def visitChangeeffectby(blockcontext):
    block = blockcontext.block
    effect = block.fields["EFFECT"][0]
    change = visitGeneric(blockcontext, "CHANGE")
    return ["changeGraphicEffect:by:", effect, change]

def visitSeteffectto(blockcontext):
    block = blockcontext.block
    effect = block.fields["EFFECT"][0]
    value = visitGeneric(blockcontext, "VALUE")
    return ["setGraphicEffect:to:", effect, value]

def visitCleargraphiceffects(blockcontext):
    block = blockcontext.block
    return ["filterReset"]

def visitShow(blockcontext):
    block = blockcontext.block
    return ["show"]

def visitHide(blockcontext):
    block = blockcontext.block
    return ["hide"]

def visitGotofrontback(blockcontext):
    block = blockcontext.block
    return ["comeToFront"]

def visitGoforwardbackwardlayers(blockcontext):
    block = blockcontext.block
    direction = block.fields["FORWARD_BACKWARD"][0]
    change = visitGeneric(blockcontext, "NUM")
    return ["goBackByLayers:", direction, change]

def visitCostumenumbername(blockcontext):
    block = blockcontext.block
    name_number = block.fields["NUMBER_NAME"][0]
    return ["costumeIndexPlaceholder"]#TODO:nur number in scratch2?


def visitBackdropnumbername(blockcontext):
    block = blockcontext.block
    name_number = block.fields["NUMBER_NAME"][0]
    return ["sceneNamePlaceholder"] #TODO: nur name in scratch2

def visitSize(blockcontext):
    block = blockcontext.block
    return ["scale"]

def visitCostume(blockcontext):
    block = blockcontext.block
    return block.fields['COSTUME'][0]

def visitBackdrops(blockcontext):
    block = blockcontext.block
    return block.fields['BACKDROP'][0]