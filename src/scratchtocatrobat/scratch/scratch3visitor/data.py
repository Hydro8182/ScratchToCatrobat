from scratchtocatrobat.scratch.scratch3 import visitGeneric

def visitSetvariableto(blockcontext):
    block = blockcontext.block
    variable = block.fields["VARIABLE"][0]
    value = visitGeneric(blockcontext, "VALUE")
    return ["setVar:to:", variable, value]

def visitChangevariableby(blockcontext):
    block = blockcontext.block
    variable = block.fields["VARIABLE"][0]
    value = visitGeneric(blockcontext, "VALUE")
    return ["changeVar:by:", variable, value]

def visitShowvariable(blockcontext):
    block = blockcontext.block
    variable = block.fields["VARIABLE"][0]
    return ["showVariable:", variable]

def visitHidevariable(blockcontext):
    block = blockcontext.block
    variable = block.fields["VARIABLE"][0]
    return ["hideVariable:", variable]

def visitRead_variable(blockcontext):
    block = blockcontext.block
    pass
    #TODO: a variable block just shows up as "my_variable",
        # not as an actual block with a reference


def visitAddtolist(blockcontext):
    block = blockcontext.block
    list = block.fields["LIST"][0]
    item = visitGeneric(blockcontext, "ITEM")
    return ["append:toList:", item, list]

def visitDeleteoflist(blockcontext):
    block = blockcontext.block
    list = block.fields["LIST"][0]
    index = visitGeneric(blockcontext, "INDEX")
    return ["deleteLine:ofList:", index, list]

def visitInsertatlist(blockcontext):
    block = blockcontext.block
    list = block.fields["LIST"][0]
    item = visitGeneric(blockcontext, "ITEM")
    index = visitGeneric(blockcontext, "INDEX")
    return ["insert:at:ofList:", index, list, item]

def visitReplaceitemoflist(blockcontext):
    block = blockcontext.block
    list = block.fields["LIST"][0]
    item = visitGeneric(blockcontext, "ITEM")
    index = visitGeneric(blockcontext, "INDEX")
    return ["setLine:ofList:to:", index, list, item]

def visitItemoflist(blockcontext):
    block = blockcontext.block
    list = block.fields["LIST"][0]
    index = visitGeneric(blockcontext, "INDEX")
    print list
    print index
    return ["getLine:ofList:", index, list]

def visitItemnumoflist(blockcontext):
    block = blockcontext.block
    list = block.fields["LIST"][0]
    item = visitGeneric(blockcontext, "ITEM")
    return ["placeholder_itemnumoflist", list, item] #TODO: not in scratch2

def visitLengthoflist(blockcontext):
    block = blockcontext.block
    list = block.fields["LIST"][0]
    return ["lineCountOfList:", list]

def visitListcontainsitem(blockcontext):
    block = blockcontext.block
    list = block.fields["LIST"][0]
    item = visitGeneric(blockcontext, "ITEM")
    return ["list:contains:", list, item]

def visitShowlist(blockcontext):
    block = blockcontext.block
    list = block.fields["LIST"][0]
    return ["showList:", list]

def visitHidelist(blockcontext):
    block = blockcontext.block
    list = block.fields["LIST"][0]
    return ["hideList:", list]

def visitContentsoflist(blockcontext):
    block = blockcontext.block
    pass
    #TODO: same as with variable value, we only get the id of list
    