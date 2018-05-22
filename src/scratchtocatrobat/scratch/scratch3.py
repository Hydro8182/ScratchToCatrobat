from pprint import pprint

class Scratch3Sprite(object):
    def __init__(self):
        self.isStage = False
        self.objName = "__UNSET__"
        self.variables = []
        self.lists = []
        self.scripts = []
        self.sounds = []
        self.costumes = []
        self.currentCostumeIndex = 0
        self.scratchX = 0
        self.scratchY = 0
        self.scale = 1
        self.direction = 90
        self.rotationStyle = "normal"
        self.isDraggable = False
        self.visible = False
        self.spriteInfo = []

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
        pass


class Scratch3Block(object):

    def __init__(self, block, name):
        self.name = name
        self.opcode = block["opcode"]
        self.nextName = block["next"]
        self.parentName = block["parent"]
        self.nextBlock = None
        self.parentBlock = None
        self.inputs = block["inputs"]
        self.fields = block["fields"]
        self.topLevel = block["topLevel"]
        self.shadow = block["shadow"]
        self.x = 0
        self.y = 0
        if self.topLevel:
            self.x = block["x"]
            self.y = block["y"]

    pass
    class type (object):
        FORMULA = 1
    def visitblock(self, block):
        scratch3_to_scratch2_map = {
            "doifnew" : ["doIf", "CONDITION: {0{1}}", "SUBSTACK"],
            "event_broadcast" : ["whenIReceive", ("BROADCAST_INPUT", 1, 2)] #"whenIReceive", "Trees"
        }
        keys = scratch3_to_scratch2_map[block.opcode]

        newname = keys[0]

        for key in keys[1:]:
            if  key in block["inputs"]:
                blockvalue = block["inputs"][key]


"inputs":{
             "BROADCAST_INPUT":[
                 1,
                 [
                     11,
                     "message1",
                     "PtPY47g*YB=o?D!f@U_C"
                 ]
             ]
         },


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

    def __init__(self, file_path):
        import json
        print file_path
        with open(file_path, "r") as file:
            self.raw_dict = json.load(file)

    def parse_sprites(self):
        sprites = self.raw_dict["targets"]
        project = Scratch3Project()

        for sprite in sprites:
            self.parse_sprite(project, sprite)
        return project

    def parse_sprite(self, project, sprite):
        #project.sprites.append(Scratch3Sprite(sprite))
        #pprint(sprite["blocks"])

        script_blocks = []
        temp_block_dict = {}
        for block in sprite["blocks"]:
            temp_block_dict[block] = Scratch3Block(sprite["blocks"][block], block)

        for blockId in temp_block_dict:
            self.build_block_structure(blockId, temp_block_dict)

        for blockId in temp_block_dict:
            if temp_block_dict[blockId].topLevel:
                script_blocks.append(temp_block_dict[blockId])

        #test
        for block in script_blocks:
            print "------------"
            self.printLinkedBlockList(block, temp_block_dict)

    def printLinkedBlockList(self, block, temp_block_dict):
        #TODO: unhardcode this
        print(block.opcode)
        if "CONDITION" in block.inputs:
            print "--condition--"
            self.printLinkedBlockList(temp_block_dict[block.inputs["CONDITION"][1]], temp_block_dict)
        if "SUBSTACK" in block.inputs:
            print "--substack--"
            self.printLinkedBlockList(temp_block_dict[block.inputs["SUBSTACK"][1]], temp_block_dict)
        if "SUBSTACK2" in block.inputs:
            print "--substack2--"
            self.printLinkedBlockList(temp_block_dict[block.inputs["SUBSTACK2"][1]], temp_block_dict)
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

