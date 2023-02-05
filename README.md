# wzirogue

## DESCRIPTION
This is my attempt to write a rogue clone as I want to see it implemented. The plan is to make is as true to the original as I can make it, not having found the Amulet of Yendor myself, with the the following exceptions:

## DEVIATIONS FROM ORIGINAL ROGUE
** No food shortage **
Since there's nothing the player can do to affect the food supply, I don't think it adds value to the game
** No ice monster bug **
...at least not on purpose
** Labeled potions and scrolls **
There's no reason that a monster fighting adventurer deep down in a cave system would drink unlabeled potions or wield unknown magic. There is of course a risk that some labels got lost or that a scroll misfires...
** In-game documentation **
Not a bestiary, but perhaps a weapon/armor list sorted by damage/protection
** personal touch **
I'll try to keep most things as close to the original as possible, but won't put too much effort into it. It's my version after all

## IMPLEMENTATION DETAILS
* Written in Python3
* Avoid reliable but too old ncurses (and own implementations of it)
* Use alternative to ncurses that can be used for other projects
* No external libraries (except "text graphics", testing etc)
