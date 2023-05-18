import random
from random import choice

# Создаем список

all = [['The Omen (2006)', 'film', 'horror'], ['The Green Knight', 'film', 'fantasy'], ['Welcome to Marwen', 'film', 'fantasy'], ['Raw', 'film', 'horror'], ['It Follows', 'film',  'horror'],
       ['Incident in a Ghostland', 'film', 'horror'], ['The Witch', 'film', 'horror'], ['In the Tall Grass', 'film', 'horror'], ['Jacobs Ladder', 'film', 'horror'],
       ['Lighthouse', 'film', 'horror'], ['Die Hard', 'film', 'thriller'], ['Us', 'film', 'horror'], ['Being John Malkovich', 'film', 'comedy'], ['Луна 2112', 'film', 'fantasy'], 
       ['Невероятная история Острова роз', 'film', 'comedy'], ['The Lobster', 'film', 'fantasy'], ['The Banshees of Inisherin', 'film', 'comedy'], ['Under the Silver Lake', 'film', 'comedy'],
       ['Contact', 'film', 'fantasy'], ['Megan', 'film', 'horror'], ['аферист с тиндера', 'film', 'documentary'], ['True Detective', 'film', 'thriller'], ['Бесславные ублюдки', 'film', 'thriller'], 

       ['Shameless', 'series', 'comedy'], ['Euphoria', 'series', 'drama'], ['What We Do in the Shadows', 'series', 'comedy'], ['Preacher', 'series', 'fantasy'], ['Brooklyn Nine-Nine', 'series', 'comedy'], 
       ['Community', 'series', 'comedy'], ['Sex Education', 'series', 'drama'],

       ['Кайдзи', 'anime', 'thriller'], ['Хантер', 'anime', 'fantasy'], ['Царь горы', 'anime', 'fantasy'], ['О моем перерождении в слизь', 'anime', 'fantasy'], ['Клинок, рассекающий демонов', 'anime', 'fantasy']]

emoji = ['🐙', '🌞', '🎥', '🌲', '🌮', '🍿', '💊', '👺', '👽', '🤖', '👻']

# Выбор типа
#print('What type do you want? film, anime, series?')
type = input('What type do you want? film, anime, series?: ')
#print('What mood do you want? horror, fantasy, thriller, comedy, drama?')
mood = input('What mood do you want? horror, fantasy, thriller, comedy, drama?: ')

# Автовыбор фильма
for item in all:
    if item[1] == type and item[2] == mood:
       print (choice(emoji) + item[0])
    else:
       print ('Nothing it that category')