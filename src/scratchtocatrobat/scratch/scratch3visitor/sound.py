from scratchtocatrobat.scratch.scratch3 import visitGeneric

def visitPlay(block, blockmap):
    sound = visitGeneric(block, 'SOUND_MENU')
    return ['playSound', sound]

def visitPlayuntildone(block, blockmap):
    sound = visitGeneric(block, 'SOUND_MENU')
    return ['playSoundAndWait', sound]

def visitStopallsounds(block, blockmap):
    return ["stopAllSounds"]

def visitChangeeffectby(block, blockmap):
    pass #TODO: doesnt exist in scratch2/catroid

def visitSeteffectto(block, blockmap):
    pass #TODO: doesnt exist in scratch2/catroid

def visitCleareffects(block, blockmap):
    return ["clearSoundEffects"] #TODO: not in scratch2

def visitChangevolumeby(block, blockmap):
    volume = visitGeneric(block, "VOLUME")
    if volume == []:
        volume = block.inputs['VOLUME'][1][1]
    return ["changeVolumeBy", volume]

def visitSetvolumeto(block, blockmap):
    volume = visitGeneric(block, "VOLUME")
    if volume == []:
        volume = block.inputs['VOLUME'][1][1]
    return ["setVolumeTo", volume]

def visitVolume(block, blockmap):
    return ["volume"]


def visitSounds_menu(block, blockname):
    return block.fields["SOUND_MENU"][0]
