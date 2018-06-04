from scratchtocatrobat.scratch.scratch3 import visitGeneric

def visitPlay(block):
    sound = visitGeneric(block, 'SOUND_MENU')
    return ['playSound:', sound[0]]

def visitPlayuntildone(block):
    sound = visitGeneric(block, 'SOUND_MENU')
    return ['playSoundAndWait', sound[0]]

def visitStopallsounds(block):
    return ["stopAllSounds"]

def visitChangeeffectby(block):
    pass #TODO: doesnt exist in scratch2/catroid

def visitSeteffectto(block):
    pass #TODO: doesnt exist in scratch2/catroid

def visitCleareffects(block):
    return ["clearSoundEffects"] #TODO: not in scratch2

def visitChangevolumeby(block):
    volume = visitGeneric(block, "VOLUME")
    if volume == []:
        volume = block.inputs['VOLUME'][1][1]
    return ["changeVolumeBy:", volume]

def visitSetvolumeto(block):
    volume = visitGeneric(block, "VOLUME")
    if volume == []:
        volume = block.inputs['VOLUME'][1][1]
    return ["setVolumeTo:", volume]

def visitVolume(block):
    return ["volume"]


def visitSounds_menu(block):
    return block.fields["SOUND_MENU"][0]
