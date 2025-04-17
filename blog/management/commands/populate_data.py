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
            "https://i.pinimg.com/736x/68/82/7c/68827c6d11f2158f477043160df7a3c5.jpg",
            "https://i.pinimg.com/474x/63/f6/bf/63f6bfe72dc2da023016b4863239819b.jpg",
            "https://i.pinimg.com/474x/7a/ae/b7/7aaeb7d933aaa6a9000f9243c97715e9.jpg",
            "https://i.pinimg.com/474x/d3/e4/37/d3e437ff50dfe3f0cbee916b39c401a2.jpg",
            "https://i.pinimg.com/474x/84/df/f9/84dff9edccca44d98e46aa7bbd7bdc1f.jpg",
            "https://i.pinimg.com/474x/77/96/fb/7796fbccb267b6fa909a92c00502d384.jpg",
            "https://i.pinimg.com/736x/4b/cf/1d/4bcf1dbd1cb2e86c36bed6ff6b1c937b.jpg",
            "https://i.pinimg.com/474x/5d/1e/a1/5d1ea15b7aba2970d61d94bb534a5aec.jpg",
            "https://i.pinimg.com/474x/40/07/f8/4007f8147b6e27824a85ca58772d8fe6.jpg",
            "https://i.pinimg.com/474x/f9/6e/4f/f96e4f0a9744309157ef9393bfdd1bbb.jpg",
            "https://i.pinimg.com/474x/60/91/ea/6091eaf0ee01d555c786e25646d1b30e.jpg",
            "https://i.pinimg.com/474x/e2/6c/11/e26c1115ee70423134248c8db9e29e4e.jpg",
            "https://i.pinimg.com/474x/49/2d/b3/492db37ae5619851e29c24b477470aff.jpg",
            "https://i.pinimg.com/736x/e3/00/48/e3004844a43e279be276d95d833531aa.jpg",
            "https://i.pinimg.com/474x/24/f7/31/24f73190423a5330701776dc48dedfe7.jpg",
            "https://i.pinimg.com/474x/67/a2/48/67a248774b91455779058b7675774660.jpg",
            "https://i.pinimg.com/474x/28/2b/8a/282b8ae746ca7f02541e92fd43b22e2b.jpg",
            "https://i.pinimg.com/736x/02/7c/36/027c367e7e36ef65cefe17a51486dc21.jpg",
            "https://i.pinimg.com/474x/0b/fe/7d/0bfe7dc773bf5b70a89312c83167a8c5.jpg",
            "https://i.pinimg.com/474x/d9/2d/a5/d92da55f12147fc4aba4937f9e54f6dd.jpg",
        ]

        for title,content,img_url in zip(titles, content, img_urls):
            Post.objects.create(title=title,content=content,img_url=img_url)
        self.stdout.write(self.style.SUCCESS("Completed inserting data"))