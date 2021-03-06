#!/usr/bin/python2
import hexchat
import random
__module_name__ = "shakespeare"
__module_version__ = "1.0"
__module_description__ = "Shakespearean Insult Generator"

c1 = ['artless', 'bawdy', 'beslubbering', 'bootless', 'churlish', 'cockered',
'clouted', 'craven', 'currish', 'dankish', 'dissembling', 'droning', 'errant',
'fawning', 'fobbing', 'froward', 'frothy', 'gleeking', 'goatish', 'gorbellied',
'impertinent', 'infectious', 'jarring', 'loggerheaded', 'lumpish', 'mammering',
'mangled', 'mewling', 'paunchy', 'pribbling', 'puking', 'puny', 'qualling', 
'rank', 'reeky', 'rogueish', 'ruttish', 'saucy', 'spleeny', 'spongy', 'surly', 
'tottering', 'unmuzzled', 'vain', 'venomed', 'villainous', 'warped', 'wayward', 
'weedy', 'yeastly'] # first column...

c2 = ['base-court', 'bat-fowling', 'beef-witted', 'beetle-headed', 'boil-brained',
'clapper-clawed', 'clay-brained', 'common-kissing', 'crook-pated', 'dismal-dreaming',
'dizzy-eyed', 'doghearted', 'dread-bolted', 'earth-vexing', 'elf-skinned', 'fat-kidneyed',
'fen-sucked', 'flap-mouthed', 'fly-bitten', 'folly-fallen', 'fool-born', 'full-gorged',
'guts-griping', 'half-faced', 'hasty-witted', 'hedge-born', 'hell-hated', 'idle-headed',
'ill-breeding', 'ill-nurtured', 'knotty-pated', 'milk-livered', 'motley-minded', 'onion-eyed',
'plume-plucked', 'pottle-deep', 'pox-marked', 'reeling-ripe', 'rough-hewn', 'rude-growing',
'rump-fed', 'shard-borne', 'sheep-biting', 'spur-galled', 'swag-bellied', 'tardy-gaited',
'tickle-brained', 'toad-spotted', 'unchin-snouted', 'weather-bitten'] # second column...

c3 = ['apple-john', 'baggage', 'barnacle', 'bladder', 'boar-pig', 'bugbear', 'bum-bailey',
'canker-blossom', 'clack-dish', 'clotpole', 'coxcomb', 'codpiece', 'death-token', 'dewberry',
'flap-dragon', 'flax-wench', 'flirt-gill', 'foot-licker', 'fustilarian', 'giglet', 'gudgeon',
'haggard', 'harpy', 'hedge-pig', 'horn-beast', 'hugger-mugger', 'joithead', 'lewdster', 'lout',
'maggot-pie', 'malt-worm', 'mammet', 'measle', 'minnow', 'miscreant', 'moldwarp', 'mumble-news',
'nut-hook', 'pidgeon-egg', 'pignut', 'puttock', 'pumpion', 'ratsbane', 'scut', 'skainsmate',
'strumpet', 'varlot', 'vassal', 'whey-face', 'wagtail'] # third column

def cmd_insult(word, word_eol, userdata):
    insult = "thou %s %s %s!" %(random.choice(c1), random.choice(c2), random.choice(c3))
    channel = hexchat.get_info("channel")
    if len(word) < 2:
        hexchat.command("MSG %s %s" %(channel, insult))
    else:
        hexchat.command("MSG %s %s %s" %(channel, word[1], insult))


hexchat.hook_command("shakespeare", cmd_insult)
