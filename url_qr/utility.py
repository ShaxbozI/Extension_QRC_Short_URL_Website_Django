import random
from  .models import Url_QR


def url_random():
    all_url = Url_QR.objects.all()
    bigWords = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    words = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    url_cycle = True
    random_url = ''
    while url_cycle:
        random_word = random.sample(words, 4)
        random_bigWord = random.sample(bigWords, 2)
        # random_num = random.randint(0, 9)
        five_words = ''.join(random_word)
        big_words = ''.join(random_bigWord)
        url = f'{five_words}_{big_words}'
        db_url = all_url.filter(url_short = url)
        if db_url:
            continue
        else:
            random_url = url
            url_cycle = False
    return random_url


