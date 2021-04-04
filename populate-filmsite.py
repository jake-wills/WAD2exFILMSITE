import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'filmsite.settings')

import django

django.setup()

from film_site.models import Film

def populate():

    Allfilms = [
        {'name': 'Seven',
         'slug':'seven',
         'director':'David Fincher',
         'bio':'Two detectives, a rookie and a veteran, hunt a serial killer who uses the seven deadly sins as his motives.',
         'img':'film_images/seven.jpg',
         'category':1
        },
        {'name': 'Joker',
         'slug': 'joker',
         'director': 'Todd Phillips',
         'bio': 'In Gotham City, mentally troubled comedian Arthur Fleck is disregarded and mistreated by society. He then embarks on a downward spiral of revolution and bloody crime. This path brings him face-to-face with his alter-ego: the Joker.',
         'img': 'film_images/joker.jpg',
         'category': 3
         },
        {'name': 'Bad Trip',
         'slug': 'bad-trip',
         'director': 'Kitao Sakurai',
         'bio': 'This mix of a scripted buddy comedy road movie and a real hidden camera prank show follows the outrageous misadventures of two buds stuck in a rut who embark on a cross-country road trip to NYC. The storyline sets up shocking real pranks.',
         'img': 'film_images/badTrip.jpg',
         'category': 2
         },
        {'name': 'Talladega Nights: The Ballad of Ricky Bobby',
         'slug': 'talladega-nights:the-ballad-of-ricky-bobby',
         'director': 'Adam McKay',
         'bio': 'Number one NASCAR driver Ricky Bobby stays atop the heap thanks to a pact with his best friend and teammate, Cal Naughton, Jr. But when a French Formula One driver, makes his way up the ladder, Ricky Bobbys talent and devotion are put to the test.',
         'img': 'film_images/talladegaNights.jpg',
         'category': 2
         },
        {'name': 'Jojo Rabbit',
         'slug': 'jojo-rabbit',
         'director': 'Taika Waititi',
         'bio': 'A young boy in Hitlers army finds out his mother is hiding a Jewish girl in their home.',
         'img': 'film_images/jojoRabbit.jpg',
         'category': 2
         },
        {'name': 'Psycho',
         'slug': 'psycho',
         'director': 'Alfred Hitchcock',
         'bio': 'A Phoenix secretary embezzles $40,000 from her employers client, goes on the run, and checks into a remote motel run by a young man under the domination of his mother.',
         'img': 'film_images/psycho.jpg',
         'category': 4
         },
        {'name': 'Alien',
         'slug': 'alien',
         'director': 'Ridley Scott',
         'bio': 'After a space merchant vessel receives an unknown transmission as a distress call, one of the crew is attacked by a mysterious life form and they soon realize that its life cycle has merely begun.',
         'img': 'film_images/alien.jpg',
         'category': 5
         },
        {'name': 'The Exorcist',
         'slug': 'the-exorcist',
         'director': 'William Friedkin',
         'bio': 'When a 12-year-old girl is possessed by a mysterious entity, her mother seeks the help of two priests to save her.',
         'img': 'film_images/theExorcist.jpg',
         'category': 4
         },
        {'name': 'Evil Dead II',
         'slug': 'evil-dead-ii',
         'director': 'Sam Raimi',
         'bio': 'The lone survivor of an onslaught of flesh-possessing spirits holes up in a cabin with a group of strangers while the demons continue their attack.',
         'img': 'film_images/evilDeadII.jpg',
         'category': 4
         },
        {'name': 'Halloween',
         'slug': 'halloween',
         'director': 'John Carpenter',
         'bio': 'Fifteen years after murdering his sister on Halloween night 1963, Michael Myers escapes from a mental hospital and returns to the small town of Haddonfield, Illinois to kill again.',
         'img': 'film_images/halloween.jpg',
         'category': 4
         },
        {'name': 'Saw',
         'slug': 'saw',
         'director': 'James Wan',
         'bio': 'Two strangers awaken in a room with no recollection of how they got there, and soon discover theyre pawns in a deadly game perpetrated by a notorious serial killer.',
         'img': 'film_images/saw.jpg',
         'category': 4
         },
        {'name': 'Pulp Fiction',
         'slug': 'pulp-fiction',
         'director': 'Quentin Tarantino',
         'bio': 'The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.',
         'img': 'film_images/pulpfiction.jpg',
         'category': 3
         },
        {'name': 'The Godfather',
         'slug': 'the-godfather',
         'director': 'Francis Ford Coppola',
         'bio': 'An organized crime dynastys aging patriarch transfers control of his clandestine empire to his reluctant son.',
         'img': 'film_images/theGodfather.jpg',
         'category': 3
         },
        {'name': 'Mad Max: Fury Road',
         'slug': 'mad-max-fury-road',
         'director': 'George Miller',
         'bio': 'In a post-apocalyptic wasteland, a woman rebels against a tyrannical ruler in search for her homeland with the aid of a group of female prisoners, a psychotic worshiper, and a drifter named Max.',
         'img': 'film_images/Mad-Max_Fury-Road.jpg',
         'category': 1
         },
        {'name': 'The Internship',
         'slug': 'the-internship',
         'director': 'Shawn Levy',
         'bio': 'Two salesmen whose careers have been torpedoed by the digital age find their way into a coveted internship at Google, where they must compete with a group of young, tech-savvy geniuses for a shot at employment.',
         'img': 'film_images/theInternship.jpg',
         'category': 2
         },
        {'name': 'Spider-Man: Into the Spider-Verse',
         'slug': 'spider-man-into-the-spider-verse',
         'director': 'Bob Persichetti, Peter Ramsey, Rodney Rotham',
         'bio': 'Teen Miles Morales becomes the Spider-Man of his universe, and must join with five spider-powered individuals from other dimensions to stop a threat for all realities.',
         'img': 'film_images/Spider-Man_Into_the_Spider-Verse.png',
         'category': 1
         },
        {'name': 'The Godfather: Part II',
         'slug': 'the-godfather-part-ii',
         'director': 'Francis Ford Coppola',
         'bio': 'The early life and career of Vito Corleone in 1920s New York City is portrayed, while his son, Michael, expands and tightens his grip on the family crime syndicate.',
         'img': 'film_images/theGodfatherpart2.jpg',
         'category': 3
         },
        {'name': 'Black Panther',
         'slug': 'black-panther',
         'director': 'Ryan Coogler',
         'bio': 'TChalla, heir to the hidden but advanced kingdom of Wakanda, must step forward to lead his people into a new future and must confront a challenger from his countrys past',
         'img': 'film_images/blackPanther.jpg',
         'category': 1
         },
        {'name': 'Ex Machina',
         'slug': 'ex-machina',
         'director': 'Alex Garland',
         'bio': 'A young programmer is selected to participate in a ground-breaking experiment in synthetic intelligence by evaluating the human qualities of a highly advanced humanoid A.I.',
         'img': 'film_images/exMachina.jpg',
         'category': 5
         },
        {'name': 'Star Wars: Episode IV - A New Hope',
         'slug': 'star-wars-episode-iv-a-new-hope',
         'director': 'George Lucas',
         'bio': 'Luke Skywalker joins forces with a Jedi Knight, a cocky pilot, a Wookiee and two droids to save the galaxy from the Empires world-destroying battle station, while also attempting to rescue Princess Leia from the mysterious Darth Vader.',
         'img': 'film_images/starwarsepisodeiv.jpg',
         'category': 5
         },
        {'name': 'Interstellar',
         'slug': 'interstellar',
         'director': 'Christopher Nolan',
         'bio': 'A team of explorers travel through a wormhole in space in an attempt to ensure humanitys survival.',
         'img': 'film_images/interstellar.jpg',
         'category': 5
         }
        ]


    for i in Allfilms:
        add_film(i['name'],i['slug'],i['director'],i['bio'],i['img'],i['category'])

def add_film(name, slug, director, bio,img,category):
    f = Film.objects.get_or_create(name=name, slug=slug, director=director,
                                   bio=bio,  img=img, rating=0, reviews=0, views=0,category=category)[0]

    f.save()
    return f

# Start execution here!
if __name__ == '__main__':
    print('Starting filmsite population script...')
    populate()
