class Deck_of_cards():
    """docstring for Deck_of_cards."""

    def __init__(self, has_joker):
        super(Deck_of_cards, self).__init__()
        self.has_joker = has_joker


    def shuffle_deck(self):
        pass

    def deal(self, hands, qty, is_seq):
        pass

    def shuffle_from_discard(self, discard):
        pass


class Card():
    """docstring for Card."""

    def __init__(self, face, value, image):
        super(Card, self).__init__()
        self.face = face
        self.value = value
        self.image = image

    def get_card(self):
        pass
