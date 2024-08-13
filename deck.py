import random


class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def __str__(self) -> str:
        """Метод возвращает строковое представление значение и масть"""
        card_suits = {'Diamonds': '\u2665', 'Hearts': '\u2666', 'Spades': '\u2663', 'Clubs': '\u2660'}
        return f'{self.value}{card_suits[self.suit]}'

    def __eq__(self, other_card) -> bool:
        """Проверяет, одинаковые ли масти у карт"""
        return self.suit == other_card.suit

    def __gt__(self, other_card):
        """Метод возвращает True, если карта у которой вызван метод больше,
        чем карта которую передали в качестве параметра."""
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Spades", "Clubs", "Diamonds", "Hearts"]

        value1_index = values.index(self.value)
        value2_index = values.index(other_card.value)

        if value1_index != value2_index:
            return value1_index > value2_index
        else:
            return suits.index(self.suit) > suits.index(other_card.suit)

    def __lt__(self, other_card) -> bool:
        """Метод возвращает False, если карта у которой вызван метод меньше,
        чем карта которую передали в качестве параметра."""
        # values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        # suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
        #
        # return values.index(self.value) < values.index(other_card.value) \
        #     if values.index(self.value) != values.index(other_card.value) \
        #     else suits.index(self.suit) < suits.index(other_card.suit)
        return not self.__gt__(other_card)


class Deck:
    # TODO-0: сюда копируем реализацию класса колоды из предыдущего задания
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = [Card(value, suit) for suit in suits for value in values]

    def __str__(self) -> str:
        # TODO-2: Принцип работы данного метода прописан в 00_task_deck.md
        return f"deck[{len(self.cards)}] {', '.join([str(str(card)) for card in self.cards])}"

    def draw(self, x) -> list:
        """метод .draw(x) - возвращает x первых карт из колоды
        в виде списка, эти карты убираются из колоды. Уточнение:
         первую карту в списке считаем верхней картой колоды"""
        result = self.cards[0:x]
        self.cards = self.cards[x:]
        return result

    def shuffle(self):
        """метод .shuffle() - перемешивает колоду, располагая карты в случайном порядке."""
        random.shuffle(self.cards)


# Создаем колоду
deck = Deck()
# Тусуем колоду
deck.shuffle()
print(deck)
# Берем две карты из колоды
card1, card2 = deck.draw(2)
print(card1)
print(card1, card2)
print(deck)

# Тестируем методы .less() и .more()
if card1 > card2:
    print(f"{card1} больше {card2}")
if card1 < card2:
    print(f"{card1} меньше {card2}")
