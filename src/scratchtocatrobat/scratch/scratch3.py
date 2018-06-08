from pprint import pprint

def get_block(blockid, spriteblocks):
    if blockid in spriteblocks.keys():
        return spriteblocks[blockid]
    return blockid

def visitBlock(block):
    from scratch3visitor.blockmapping import visitormap

    if not isinstance(block, BlockContext):
        return block
    blocklist = []
    while block.block != None:
        subblock = visitormap.get(block.block.opcode, visitDefault)(block)
        blocklist.append(subblock)
        block = BlockContext(block.block.nextBlock, block.spriteblocks)
    if isinstance(blocklist[0], list) and len(blocklist) == 1:
        blocklist = blocklist[0]
    return blocklist

def visitScriptBlock(block):
    from scratch3visitor.blockmapping import visitormap

    if not isinstance(block, BlockContext):
        return block

    scriptblock = visitormap.get(block.block.opcode, visitDefault)(block)
    block = BlockContext(block.block.nextBlock, block.spriteblocks)
    blocklist = []
    blocklist.append(scriptblock)
    while block.block != None:
        subblock = visitormap.get(block.block.opcode, visitDefault)(block)
        blocklist.append(subblock)
        block = BlockContext(block.block.nextBlock, block.spriteblocks)
    pprint(blocklist)
    return blocklist

def visitBlockList(blockcontext):
    from scratch3visitor.blockmapping import visitormap

    if not isinstance(blockcontext, BlockContext):
        return blockcontext
    blocklist = []

    while blockcontext.block != None:
        subblock = visitormap.get(blockcontext.block.opcode, visitDefault)(blockcontext)
        blocklist.append(subblock)
        blockcontext = BlockContext(blockcontext.block.nextBlock, blockcontext.spriteblocks)
    return blocklist

def visitLiteral(literal):
    if literal[0] == 12:
        return ["readVariable", literal[1]]
    elif literal[0] == 13:
        return ["contentsOfList:", literal[1]]
    elif literal[0] == 5 or literal[0] == 6 or literal[0] == 7:
        if literal[1] == None:
            return 0
        try:
            return int(literal[1])
        except:
            return str(literal[1])
    elif literal[0] == 4 or literal[0] == 8:
        if literal[1] == '':
            return 0.0
        return float(literal[1])
    elif literal[0] == 9:
        return literal[1]
    else:
        return literal[1]


def visitGeneric(blockcontext, attributename):
    block = blockcontext.block
    if attributename in block.inputs:
        substackstartblock = get_block(block.inputs[attributename][1], blockcontext.spriteblocks)
        if isinstance(substackstartblock, Scratch3Block):
            blocklist = visitBlock(BlockContext(substackstartblock, blockcontext.spriteblocks))
            if block.inputs[attributename][0] == 1:
                return blocklist[0]
            return blocklist
        return visitLiteral(block.inputs[attributename][1])
    return [False]

def visitDefault(blockcontext):
    print("########### block not yet implemented: ", blockcontext.block.opcode, "#########")
    return ["say:", "ERROR: BLOCK NOT FOUND: " + blockcontext.block.opcode]

class Scratch3Script(object):
    def __init__(self):
        self.isStage = False
    def getNextBlock(self, currentblock):
        return self.blocks[currentblock.next]

    def getNextBlockScratch2(self, currentblock):
        return currentblock.child

class Scratch3Costume(object):
    def __init__(self):
        self.assetId = "cd21514d0531fdffb22204e0ec5ed84a"
        self.name = "backdrop1"
        self.md5ext = "cd21514d0531fdffb22204e0ec5ed84a.svg"
        self.dataFormat = "svg"
        self.rotationCenterX = 0
        self.rotationCenterY = 0

    pass


class Scratch3Sound(object):
    def __init__(self):
        self.assetId = "83a9787d4cb6f3b7632b4ddfebf74367"
        self.name = "pop"
        self.dataFormat = "wav"
        self.format = ""
        self.rate = 48000
        self.sampleCount = 1123
        self.md5ext = "83a9787d4cb6f3b7632b4ddfebf74367.wav"


def get_block_attribute(block, key):
    if key in block.keys():
        return block[key]
    return None


class Scratch3Block(object):

    def __init__(self, block, name):
        print block
        self.name = name
        self.opcode = get_block_attribute(block, "opcode")
        self.nextName = get_block_attribute(block, "next")
        self.parentName = get_block_attribute(block, "parent")
        self.nextBlock = None
        self.parentBlock = None
        self.inputs = get_block_attribute(block, "inputs")
        self.fields = get_block_attribute(block, "fields")
        self.topLevel = get_block_attribute(block, "topLevel")
        self.shadow = get_block_attribute(block, "shadow")
        self.mutation = get_block_attribute(block, "mutation")
        self.x = 0
        self.y = 0
        if self.topLevel:
            self.x = block["x"]
            self.y = block["y"]

class Scratch3Project(object):
    def __init__(self):
        self.targets = []
        self.meta = { "semver":"3.0.0",
                      "vm":"0.1.0-prerelease.1526320682",
                      "agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}
        self.name = "Untitled"
        self.sprites = []
class Scratch3Parser(object):
    scratch2dict = {}

    def __init__(self, file_path, scratch_project_dir):
        import json
        print file_path
        with open(file_path, "r+") as file1:
            import glob
            import os
            from scratchtocatrobat.tools import common
            file_content = file1.read()
            for file in glob.glob(scratch_project_dir + "/*.*"):
                if not file.endswith(".json"):

                    file_hash = common.md5_hash(file)
                    newname = scratch_project_dir+"/"+ file_hash +"." +file.split(".")[-1]
                    os.rename(file, newname)
                    oldfile = "".join(file.split('/')[-1].split('.')[0:-1])
                    print oldfile
                    print file_hash
                    file_content = file_content.replace(oldfile ,file_hash)
            file1.flush()
            file1.write(file_content)
            self.raw_dict = json.loads(file_content)

    def parse_sprites(self):
        sprites = self.raw_dict["targets"]
        scratch2Data = {}
        scratch2Data['sprites'] = []
        stageSprite = {}

        for sprite in sprites:
            spriteContent = self.parse_sprite(sprite)
            if sprite["isStage"]:
                stageSprite = spriteContent
            else:
                scratch2Data['sprites'].append(spriteContent)

        stageSprite["children"] = []
        for sprite in scratch2Data['sprites']:
            stageSprite["children"].append(sprite)
        stageSprite["info"] = self.raw_dict["meta"]
        stageSprite["penLayerMD5"] = "Scratch3Doesn'tHaveThis"
        stageSprite["penLayerID"] = 0 #TODO: this doesn't exist in scratch3 what is this!?
        stageSprite["tempoBPM"] = 60
        stageSprite["videoAlpha"] = 0.5
        return stageSprite

    def parse_sprite(self, sprite):
        script_blocks = []
        temp_block_dict = {}
        for block in sprite["blocks"]:
            temp_block_dict[block] = Scratch3Block(sprite["blocks"][block], block)

        for blockId in temp_block_dict:
            self.build_block_structure(blockId, temp_block_dict)

        for blockId in temp_block_dict:
            if temp_block_dict[blockId].topLevel:
                script_blocks.append(temp_block_dict[blockId])
        scratch2ProjectDict = {}
        scratch2ProjectDict["scripts"] = []

        for block in script_blocks:
            print "------------"
            self.printLinkedBlockList(block, temp_block_dict)
            blockcontext = BlockContext(block, temp_block_dict)
            scratch2ProjectDict["scripts"] += [[1,1, visitScriptBlock(blockcontext)]]
        variables = []
        for var in sprite["variables"].values():
            curvar = {}
            curvar["name"] = var[0]
            curvar["value"] = var[1]
            curvar["isPersistent"] = var[2] if len(var) > 2 else False
            variables.append(curvar)

        lists = []
        for list in sprite["lists"].values():
            curlist = {}
            curlist["listName"] = list[0]
            curlist["contents"] = list[1]
            curlist["isPersistent"] = list[2] if len(list) > 2 else False
            curlist["x"] = 1
            curlist["y"] = 1
            curlist["width"] = 1
            curlist["height"] = 1
            curlist["visible"] = True
            lists.append(curlist)
        scratch2ProjectDict["lists"] = lists

        scratch2ProjectDict["variables"] = variables
        scratch2ProjectDict["costumes"] = []
        for s3Costume in sprite["costumes"]:
            s2Costume = {}
            s2Costume["costumeName"] = s3Costume["name"]
            s2Costume["baseLayerID"] = s3Costume["assetId"]
            s2Costume["baseLayerMD5"] = s3Costume["md5ext"]
            s2Costume["rotationCenterX"]= s3Costume["rotationCenterX"]
            s2Costume["rotationCenterY"]= s3Costume["rotationCenterX"]
            if "bitmapResolution" in s3Costume:
                s2Costume["bitmapResolution"] = s3Costume["bitmapResolution"]
            else:
                s2Costume["bitmapResolution"] =  1
            scratch2ProjectDict["costumes"].append(s2Costume)

        scratch2ProjectDict["sounds"] = []
        i = 0
        for s3Sound in sprite["sounds"]:
            i += 1
            s2Sound = {}
            s2Sound["assetId"] =  s3Sound["assetId"]
            s2Sound["soundName"] =  s3Sound["name"]
            s2Sound["format"] =  s3Sound["format"]
            s2Sound["rate"] =  s3Sound["rate"]
            s2Sound["sampleCount"] =  s3Sound["sampleCount"]
            s2Sound["md5"] =  s3Sound["md5ext"]
            s2Sound["soundID"] = i #TODO this could be wrong
            scratch2ProjectDict["sounds"].append(s2Sound)


        scratch2ProjectDict["objName"] = sprite["name"]
        scratch2ProjectDict["currentCostumeIndex"] = sprite["currentCostume"]
        scratch2ProjectDict["isStage"] = sprite["isStage"]
        if not sprite['isStage']:
            scratch2ProjectDict["scratchX"] = sprite["x"]
            scratch2ProjectDict["scratchY"] = sprite["y"]
            scratch2ProjectDict["scale"] = sprite["size"] / 100.0
            scratch2ProjectDict["direction"] = sprite["direction"]
            scratch2ProjectDict["rotationStyle"] = sprite["rotationStyle"]
            scratch2ProjectDict["isDraggable"] = sprite["draggable"]
            # scratch2ProjectDict["indexInLibrary"] = sprite["indexInLibrary"]
            # scratch2ProjectDict["spriteInfo"] = sprite["spriteInfo"]
            scratch2ProjectDict["visible"] = sprite["visible"]

        return scratch2ProjectDict

    def printLinkedBlockList(self, block, temp_block_dict):
        #TODO: unhardcode this
        # print(block.opcode)
        group = block.opcode.split('_')[0]
        blockcode = "_".join(block.opcode.split('_')[1:])
        blockcode = blockcode[0].upper() + blockcode[1:]
        # print( '"'+block.opcode+"\" : scratch3visitor." + group + ".visit" + blockcode + ",")

        if block.nextBlock is None:
            return
        self.printLinkedBlockList(block.nextBlock, temp_block_dict)

    def build_block_structure(self, blockId, temp_block_dict):
        block = temp_block_dict[blockId]
        if block.nextName is not None:
            block.nextBlock = temp_block_dict[block.nextName]
        if block.parentName is not None:
            block.parentBlock = temp_block_dict[block.parentName]

    def parse_scripts(self):
        pass
    def parse_script(self, script):
        pass

class BlockContext(object):
    def __init__(self, block, spriteblocks):
        self.block = block
        self.spriteblocks = spriteblocks
