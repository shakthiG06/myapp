from typing import Any
from blog.models import Post
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help='This command insert post data'

    def handle(self, *args:Any, **options:Any):
        titles =[
            'The Lord of the Rings: The Fellowship of the Ring (2001)',
            'The Lord of the Rings: The Two Towers (2002)',
            'The Lord of the Rings: The Return of the King (2003)',
            'The Hobbit: An Unexpected Journey (2012)',
            'The Hobbit: The Desolation of Smaug (2013)',
            'The Hobbit: The Battle of the Five Armies (2014)',
            'Harry Potter and the Sorcerer’s Stone (2001)',
            'Harry Potter and the Prisoner of Azkaban (2004)',
            'Fantastic Beasts and Where to Find Them (2016)',
            'Pan’s Labyrinth (2006)',
            'The Chronicles of Narnia: The Lion, the Witch, and the Wardrobe (2005)',
            'The Golden Compass (2007)',
            'Stardust (2007)',
            'The Princess Bride (1987)',
            'Willow (1988)',
            'The NeverEnding Story (1984)',
            'The Dark Crystal (1982)',
            'Howl’s Moving Castle (2004)',
            'Spirited Away (2001)',
            'Eragon (2006)',
        ]

        content =[
            "Where the epic journey begins, and walking becomes a lifestyle. 🧙‍♂️",
            "Middle-earth’s ultimate group project just got way more intense. 🏰",
            "One does not simply emotionally recover from this finale. 👑",
            "Never trust a wizard who says it’s just a “little adventure.” 🐉",
            "Smaug stole the gold, but the dragon sass stole the show. 🔥",
            "So many armies, so many feels, so much chaos. ⚔️",
            "The magic all started under the stairs. 🧙‍♂️📦",
            "The vibe shift, the time-turner, the werewolf drama—iconic. ⏳🐺",
            "Magical creatures, awkward charm, and peak Newt Scamander energy. ✨🦋",
            "Dark fairy tales that hit you in the heart and haunt your dreams. 🕯️",
            "Where closets lead to kingdoms and Turkish delight is sketchy. 🦁❄️",
            "Talking animals, armored bears, and some deep existential vibes. 🐻🧭",
            "A fallen star, sky pirates, and Michelle Pfeiffer stealing scenes. ⭐💫",
            "True love, sword fights, and endless quotable moments. 💘🗡️",
            "Underdog magic, 80s fantasy charm, and the power of believing. 🧝‍♂️",
            "Childhood wonder wrapped in flying dogs and existential dread. 🐉📖",
            "Creepy puppets, epic world-building, and pure cult classic energy. 👁️",
            "A walking castle, cursed hearts, and dreamy chaos magic. 🏰💫",
            "A bathhouse for pirits and a journey into surreal beauty. 🍃👻",
            "Dragons, destiny, and the movie adaptation we almost deserved. 🐲",
        ]

        img_urls=[
            "https://picsum.photos/id/237/200/300",
            "https://picsum.photos/id/237/200/300",
            "https://picsum.photos/id/237/200/300",
            "https://picsum.photos/id/237/200/300",
            "https://picsum.photos/id/237/200/300",
            "https://picsum.photos/id/237/200/300",
            "https://picsum.photos/id/237/200/300",
            "https://picsum.photos/id/237/200/300",
            "https://picsum.photos/id/237/200/300",
            "https://picsum.photos/id/237/200/300",
            "https://picsum.photos/id/237/200/300",
            "https://picsum.photos/id/237/200/300",
            "https://picsum.photos/id/237/200/300",
            "https://picsum.photos/id/237/200/300",
            "https://picsum.photos/id/237/200/300",
            "https://picsum.photos/id/237/200/300",
            "https://picsum.photos/id/237/200/300",
            "https://picsum.photos/id/237/200/300",
            "https://picsum.photos/id/237/200/300",
            "https://picsum.photos/id/237/200/300",
        ]

        for title,content,img_url in zip(titles, content, img_urls):
            Post.objects.create(title=title,content=content,img_url=img_url)
        self.stdout.write(self.style.SUCCESS("Completed inserting data"))