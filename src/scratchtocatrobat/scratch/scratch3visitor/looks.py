from scratchtocatrobat.scratch.scratch3 import visitGeneric

def visitSayforsecs(block):
    message = visitGeneric(block, "MESSAGE")
    duration = visitGeneric(block, "SECS")
    return ["say:duration:elapsed:from:", message, duration]

def visitSay(block):
    message = visitGeneric(block, "MESSAGE")
    return ["say:", message]

def visitThinkforsecs(block):
    message = visitGeneric(block, "MESSAGE")
    duration = visitGeneric(block, "SECS")
    return ["think:duration:elapsed:from:", message, duration]

def visitThink(block):
    message = visitGeneric(block, "MESSAGE")
    return ["think:", message]

def visitSwitchcostumeto(block):
    costume = visitGeneric(block, "COSTUME")
    return ["lookLike:", costume]

def visitNextcostume(block):
    return ["nextCostume"]

def visitSwitchbackdropto(block):
    backdrop = visitGeneric(block, "BACKDROP")
    return ["startScene", backdrop]

def visitNextbackdrop(block):
    return ["nextBackdropPlaceholder"] #TODO: not in scratch2

def visitChangesizeby(block):
    size = visitGeneric(block, "CHANGE")
    return ["changeSizeBy:", size]

def visitSetsizeto(block):
    size = visitGeneric(block, "SIZE")
    return ["setSizeTo:", size]

def visitChangeeffectby(block):
    effect = block.fields["EFFECT"][0]
    change = visitGeneric(block, "CHANGE")
    return ["changeGraphicEffect:by:", effect, change]

def visitSeteffectto(block):
    effect = block.fields["EFFECT"][0]
    value = visitGeneric(block, "VALUE")
    return ["setGraphicEffect:to:", effect, value]

def visitCleargraphiceffects(block):
    return ["filterReset"]

def visitShow(block):
    return ["show"]

def visitHide(block):
    return ["hide"]

def visitGotofrontback(block):
    return ["comeToFront"]

def visitGoforwardbackwardlayers(block):
    direction = block.fields["FORWARD_BACKWARD"][0]
    change = visitGeneric(block, "NUM")
    return ["goBackByLayers:", direction, change]

def visitCostumenumbername(block):
    name_number = block.fields["NUMBER_NAME"][0]
    return ["costumeIndexPlaceholder"]#TODO:nur number in scratch2?


def visitBackdropnumbername(block):
    name_number = block.fields["NUMBER_NAME"][0]
    return ["sceneNamePlaceholder"] #TODO: nur name in scratch2

def visitSize(block):
    return ["scale"]

def visitCostume(block):
    return block.fields['COSTUME'][0]

def visitBackdrops(block):
    return block.fields['BACKDROP'][0]