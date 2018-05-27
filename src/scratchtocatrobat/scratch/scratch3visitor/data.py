from scratchtocatrobat.scratch.scratch3 import visitGeneric

def visitSetvariableto(block, blockmap):
    variable = block.fields["VARIABLE"][0]
    value = visitGeneric(block, "VALUE")
    return ["setVar:to:", variable, value]

def visitChangevariableby(block, blockmap):
    variable = block.fields["VARIABLE"][0]
    value = visitGeneric(block, "VALUE")
    return ["changeVar:by:", variable, value]

def visitShowvariable(block, blockmap):
    variable = block.fields["VARIABLE"][0]
    return ["showVariable", variable]

def visitHidevariable(block, blockmap):
    variable = block.fields["VARIABLE"][0]
    return ["hideVariable", variable]

def visitRead_variable(block, blockmap):
    pass
    #TODO: a viariable block just shows up as "my_variable",
        # not as an actual block with a reference


def visitAddtolist(block, blockmap):
    list = block.fields["LIST"][0]
    item = visitGeneric(block, "ITEM")
    return ["append:toList:", list, item]

def visitDeleteoflist(block, blockmap):
    list = block.fields["LIST"][0]
    index = visitGeneric(block, "INDEX")
    return ["deleteLine:ofList:", list, index]

def visitInsertatlist(block, blockmap):
    list = block.fields["LIST"][0]
    item = visitGeneric(block, "ITEM")
    index = visitGeneric(block, "INDEX")
    return ["insert:at:ofList:", list, item, index]

def visitReplaceitemoflist(block, blockmap):
    list = block.fields["LIST"][0]
    item = visitGeneric(block, "ITEM")
    index = visitGeneric(block, "INDEX")
    return ["setLine:ofList:to:", list, item, index]

def visitItemoflist(block, blockmap):
    list = block.fields["LIST"][0]
    index = visitGeneric(block, "INDEX")
    return ["getLine:ofList:", index, list]

def visitItemnumoflist(block, blockmap):
    list = block.fields["LIST"][0]
    item = visitGeneric(block, "ITEM")
    return ["placeholder_itemnumoflist", list, item] #TODO: not in scratch2

def visitLengthoflist(block, blockmap):
    list = block.fields["LIST"][0]
    return ["lineCountOfList:", list]

def visitListcontainsitem(block, blockmap):
    list = block.fields["LIST"][0]
    item = visitGeneric(block, "ITEM")
    return ["list:contains:", list, item]

def visitShowlist(block, blockmap):
    list = block.fields["LIST"][0]
    return ["showList:", list]

def visitHidelist(block, blockmap):
    list = block.fields["LIST"][0]
    return ["hideList:", list]

def visitContentsoflist(block, blockmap):
    pass
    #TODO: same as with variable value, we only get the id of list
    