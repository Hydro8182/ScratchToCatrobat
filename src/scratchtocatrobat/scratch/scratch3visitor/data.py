from scratchtocatrobat.scratch.scratch3 import visitGeneric

def visitSetvariableto(block):
    variable = block.fields["VARIABLE"][0]
    value = visitGeneric(block, "VALUE")
    #TODO: properly parse
    if isinstance(value, list) and len(value) == 1:
        value = value[0]

    return ["setVar:to:", variable, value]

def visitChangevariableby(block):
    variable = block.fields["VARIABLE"][0]
    value = visitGeneric(block, "VALUE")
    #TODO: properly parse
    if isinstance(value, list) and len(value) == 1:
        value = value[0]
    return ["changeVar:by:", variable, value]

def visitShowvariable(block):
    variable = block.fields["VARIABLE"][0]
    #TODO: properly parse
    #if isinstance(value, list) and len(value) > 1:
    #    value = value[0]
    return ["showVariable:", variable]

def visitHidevariable(block):
    variable = block.fields["VARIABLE"][0]
    return ["hideVariable:", variable]

def visitRead_variable(block):
    pass
    #TODO: a viariable block just shows up as "my_variable",
        # not as an actual block with a reference


def visitAddtolist(block):
    list = block.fields["LIST"][0]
    item = visitGeneric(block, "ITEM")
    return ["append:toList:", list, item]

def visitDeleteoflist(block):
    list = block.fields["LIST"][0]
    index = visitGeneric(block, "INDEX")
    return ["deleteLine:ofList:", list, index]

def visitInsertatlist(block):
    list = block.fields["LIST"][0]
    item = visitGeneric(block, "ITEM")
    index = visitGeneric(block, "INDEX")
    return ["insert:at:ofList:", list, item, index]

def visitReplaceitemoflist(block):
    list = block.fields["LIST"][0]
    item = visitGeneric(block, "ITEM")
    index = visitGeneric(block, "INDEX")
    return ["setLine:ofList:to:", list, item, index]

def visitItemoflist(block):
    list = block.fields["LIST"][0]
    index = visitGeneric(block, "INDEX")
    return ["getLine:ofList:", index, list]

def visitItemnumoflist(block):
    list = block.fields["LIST"][0]
    item = visitGeneric(block, "ITEM")
    return ["placeholder_itemnumoflist", list, item] #TODO: not in scratch2

def visitLengthoflist(block):
    list = block.fields["LIST"][0]
    return ["lineCountOfList:", list]

def visitListcontainsitem(block):
    list = block.fields["LIST"][0]
    item = visitGeneric(block, "ITEM")
    return ["list:contains:", list, item]

def visitShowlist(block):
    list = block.fields["LIST"][0]
    return ["showList:", list]

def visitHidelist(block):
    list = block.fields["LIST"][0]
    return ["hideList:", list]

def visitContentsoflist(block):
    pass
    #TODO: same as with variable value, we only get the id of list
    