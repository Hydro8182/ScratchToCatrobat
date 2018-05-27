from scratchtocatrobat.scratch.scratch3 import visitGeneric

def visitSayforsecs(block, blockmap):
    message = visitGeneric(block, "MESSAGE")
    duration = visitGeneric(block, "SECS")
    return ["say:duration:elapsed:from:", message, duration]

def visitSay(block, blockmap):
    message = visitGeneric(block, "MESSAGE")
    return ["say:", message]

def visitThinkforsecs(block, blockmap):
    message = visitGeneric(block, "MESSAGE")
    duration = visitGeneric(block, "SECS")
    return ["think:duration:elapsed:from:", message, duration]

def visitThink(block, blockmap):
    message = visitGeneric(block, "MESSAGE")
    return ["think:", message]

def visitSwitchcostumeto(block, blockmap):
    costume = visitGeneric(block, "COSTUME")
    return ["lookLike:", costume]

def visitNextcostume(block, blockmap):
    return ["nextCostume"]

def visitSwitchbackdropto(block, blockmap):
    backdrop = visitGeneric(block, "BACKDROP")
    return ["startScene", backdrop]

def visitNextbackdrop(block, blockmap):
    return ["nextBackdropPlaceholder"] #TODO: not in scratch2

def visitChangesizeby(block, blockmap):
    size = visitGeneric(block, "CHANGE")
    return ["changeSizeBy:", size]

def visitSetsizeto(block, blockmap):
    size = visitGeneric(block, "SIZE")
    return ["setSizeTo:", size]

def visitChangeeffectby(block, blockmap):
    effect = block.fields["EFFECT"][0]
    change = visitGeneric(block, "CHANGE")
    return ["changeGraphicEffect:by:", effect, change]

def visitSeteffectto(block, blockmap):
    effect = block.fields["EFFECT"][0]
    value = visitGeneric(block, "VALUE")
    return ["setGraphicEffect:to:", effect, value]

def visitCleargraphiceffects(block, blockmap):
    return ["filterReset"]

def visitShow(block, blockmap):
    return ["show"]

def visitHide(block, blockmap):
    return ["hide"]

def visitGotofrontback(block, blockmap):
    return ["comeToFront"]

def visitGoforwardbackwardlayers(block, blockmap):
    direction = block.fields["FORWARD_BACKWARD"][0]
    change = visitGeneric(block, "NUM")
    return ["goBackByLayers:", direction, change]

def visitCostumenumbername(block, blockmap):
    name_number = block.fields["NUMBER_NAME"][0]
    return ["costumeIndexPlaceholder"]#TODO:nur number in scratch2?


def visitBackdropnumbername(block, blockmap):
    name_number = block.fields["NUMBER_NAME"][0]
    return ["sceneNamePlaceholder"] #TODO: nur name in scratch2

def visitSize(block, blockmap):
    return ["scale"]

def visitCostume(block, blockmap):
    return block.fields['COSTUME'][0]

def visitBackdrops(block, blockmap):
    return block.fields['BACKDROP'][0]