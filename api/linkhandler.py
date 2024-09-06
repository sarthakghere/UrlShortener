import string
import random
from .models import ShortLink

class LinkHandler:
    def shorten_link():
        length = 6
        while True:
            letters_and_digits = string.ascii_letters + string.digits
            random_string = ''.join(random.choice(letters_and_digits) for _ in range(length))
            if ShortLink.objects.filter(short_code = random_string).exists():
                continue
            else:
                return random_string