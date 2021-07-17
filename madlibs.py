from random import randint
import copy
word_dict = { 
    'adjective':['lazy','hobbit-ish','wholesome','fuzzy','hungry','crunchy','darling','spicy'],
    'city name':['Hong Kong','Mordor','Dallas','Venice','Key West','Tahoe','St. Petersburg','London'],
    'noun':['cat','ravioli','fireplace','daily planner','hummus','burps','castaway','dumpster fire'],
    'action verb':['canter','sparkle','bargain','quip','rest','tiptoe','binge','replace'],
    'sports noun': ['puck','hustle','hole in one','touchdown','foul','strike','out','cleats'],
    }
story=(
    "One day my {} friend and I decided to go to the {} game in {}. "+
    "We really wanted to see the {} play the {}. So, we {} our {} "+ 
    "down to the {} and bought some {}s. We got into the game and "+
    "it was a lot of fun. We ate some {} {} and drank some {} {}. "+
    "We had a great time! We plan to go again next year!")
def get_word(type, local_dict): 
    words = local_dict[type]
    cnt=len(words)-1
    index=randint(0, cnt)
    return local_dict[type].pop(index)
def create_story():
    local_dict=copy.deepcopy(word_dict)
    return story.format(
        get_word('adjective', local_dict), 
        get_word('sports noun', local_dict),
        get_word('city name', local_dict),
        get_word('noun', local_dict),
        get_word('noun', local_dict),
        get_word('action verb', local_dict),
        get_word('noun', local_dict),
        get_word('noun', local_dict),
        get_word('noun', local_dict),
        get_word('adjective', local_dict),
        get_word('noun', local_dict),
        get_word('adjective', local_dict),
        get_word('noun', local_dict)
    )
story1=create_story()
print(story1)
