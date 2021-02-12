class MoneyBox:
  def __init__(self, capacity):
    self.num_coins = 0
    self.capacity = capacity
  def can_add(self, coins_to_add):
    return self.num_coins + coins_to_add <= self.capacity
  def add(self, coins_to_add):
    if self.can_add(coins_to_add):
      self.num_coins += coins_to_add

x = MoneyBox(15)
print(x.num_coins)
x.add(5)
print(x.num_coins)
x.add(10)
print(x.num_coins)
x.add(3)
print(x.num_coins)

"""Реализуйте класс MoneyBox, для работы с виртуальной копилкой.

Каждая копилка имеет ограниченную вместимость, которая выражается целым числом – количеством монет, 
которые можно положить в копилку. Класс должен поддерживать информацию о количестве монет в копилке, 
предоставлять возможность добавлять монеты в копилку и узнавать, 
можно ли добавить в копилку ещё какое-то количество монет, не превышая ее вместимость.

Класс должен иметь следующий вид

class MoneyBox:
    def __init__(self, capacity):
        # конструктор с аргументом – вместимость копилки

    def can_add(self, v):
        # True, если можно добавить v монет, False иначе

    def add(self, v):
        # положить v монет в копилку
При создании копилки, число монет в ней равно 0.
Примечание:
Гарантируется, что метод add(self, v) будет вызываться только если can_add(self, v) – True."""