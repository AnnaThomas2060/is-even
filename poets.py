import random 


def choose_poet_mascot():
    

    MASCOTS = [
    {
        "name": "Blorp the Anxious Alien",
        "art": r"""
    .---.
   /o   o\  *Blorp... Did I forget the rhyme?*
  (  "^"  )
   \ --- /
    `---'
    /|📜|\
   / |_|  \
"""
    },
    {
        "name": "Sprout, The Sentient Sapling",
        "art": r"""
       _.._
     .'    '.
    (________) *I am a mighty poet!*
      (o  o)
      (  V  )
       |__|
      /|📜|\
       _||_
"""
    },
    {
        "name": "Bartholomew the Hovering Blob",
        "art": r"""
     .-----.
    /  ^ ^  \
   |  ( O )  | *Jiggles in iambic pentameter*
    \  ---  /
     '-----'
     /|📜|\
     / / \ \
"""
    },
    {
        "name": "Glimmer the Cloud Spirit",
        "art": r"""
     .  * .
   :  '   '  :
  :   (o o)   : *Whispers a breezy stanza*
   :   \_/   :
    '  : :  '
      /|📜|\
       ^ ^
"""
    },
{
        "name": "Professor Whiskerton III",
        "art": r"""
    /\_/\    
   ( o.o )   *Adjusts monocle*
    > ^ <    
   /  |  \   
  / | 📜 | \ 
"""
    },
]

    chosen_mascot = random.choice(MASCOTS)

    return chosen_mascot


