def visitIf(block, blockmap):

    blockname = "doIf"
    condition = block.visitAlt(block.blocks[block.inputs["CONDITION"][1][1]])


    return ["doif", ["cond"], ["sub1", "sub2"]]