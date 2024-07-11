# wzirogue
The first and best roguelike that I have yet to write

## What and why
This is my own implementation of rogue. I will try to find as much information as possible about the original rogue and then decide what of that to implement. My version will never let a player starve, but I might very well implement the ice monster bug for nostalgic reasons.

There are a couple of reasons for this project
* I sometimes miss having a suitable rogue clone installed on one of my systems
* I've "always" wanted to write my own roguelike
* I need a larger programming project to practice different techniques/tools on

## How to play and where we are
### Play
Download the game, create a virtual Python environment, pip install blessed and run the game with:
./rogue.py

### Rough plan and current status
Basic plan plus limitations:
- [X] simple room generator
   - the rooms are on the smaller side
   - all nine "fields" contains one room
- [ ] place and move character in room
- [ ] interconnect rooms
- [ ] add exit points and new dungeon creation
- [ ] basic combat system
- [ ] items (weapons and armour, not traps or magic)
- [ ] hidden walls/rooms
- [ ] traps and potions
- [ ] monster intelligence
