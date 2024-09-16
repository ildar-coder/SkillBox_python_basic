class Cell:
    def __init__(self, number: int, value=None):
        self.occupancy = 0
        self.number = number
        self.value = value

    def is_busy(self):
        return self.occupancy != 0

class Board:
    def __init__(self):
        self.cells = []
        count = 0
        for i in range(3):
            for j in range(3):
                count += 1
                self.cells.append(Cell(count))

class Player:
    def __init__(self, name):
        player_value = input(f"{name}, введите X или O\n")
        self.name = name
        if player_value.lower() == 'x':
            self.value = 'X'
        elif player_value.lower() == 'o' or player_value == '0':
            self.value = 'O'
        else:
            raise ValueError("Недопустимое значение, используйте 'X' или 'O'.")

    def is_win(self, board: Board):
        val = self.value
        win_combinations = [
            (0, 1, 2),  # первая строка
            (3, 4, 5),  # вторая строка
            (6, 7, 8),  # третья строка
            (0, 3, 6),  # первый столбец
            (1, 4, 7),  # второй столбец
            (2, 5, 8),  # третий столбец
            (0, 4, 8),  # первая диагональ
            (2, 4, 6)   # вторая диагональ
        ]
        for combo in win_combinations:
            if (board.cells[combo[0]].value == val and
                    board.cells[combo[1]].value == val and
                    board.cells[combo[2]].value == val):
                return True
        return False

class Game:
    def __init__(self, player_1: Player, player_2: Player):
        self.player_1 = player_1
        self.player_2 = player_2
        self.board = Board()
        self.is_over = False
        self.player_1_wins = 0
        self.player_2_wins = 0

    def is_draw(self):
        for cell in self.board.cells:
            if not cell.is_busy():
                return False
        return not (self.player_1.is_win(self.board) or self.player_2.is_win(self.board))

    def start_move(self, player: Player):
        while True:
            cell_num = int(input(f"{player.name}, введите номер поля от 1 до 9, на которое будете ходить\n"))
            if 1 <= cell_num <= 9 and not self.board.cells[cell_num - 1].is_busy():
                self.board.cells[cell_num - 1].occupancy = 1
                self.board.cells[cell_num - 1].value = player.value
                break
            else:
                print("Неправильный выбор клетки, попробуйте снова.")

        if player.is_win(self.board):
            print(f"Выиграл игрок {player.name}")
            self.is_over = True
            return True

        if self.is_draw():
            print("Ничья!")
            self.is_over = True
            return True

        return False

    def start_game(self):
        print("Началась новая игра")
        for cell in self.board.cells:
            cell.occupancy = 0
            cell.value = None
        self.is_over = False
        count = 0

        while not self.is_over:
            if count % 2 == 0:
                if self.start_move(self.player_1):
                    self.player_1_wins += 1
                    break
            else:
                if self.start_move(self.player_2):
                    self.player_2_wins += 1
                    break
            count += 1

    def print_score(self):
        print(f"Счет в партии:\n{self.player_1.name} выиграл игр: {self.player_1_wins}\n{self.player_2.name} выиграл игр: {self.player_2_wins}\n")

    def main(self):
        while True:
            self.start_game()
            if self.is_over:
                request_to_continue = input("Хотите продолжить Y/N\n")
                if request_to_continue.lower() == 'n':
                    print("Игра окончена")
                    self.print_score()
                    break
                elif request_to_continue.lower() == 'y':
                    self.print_score()
                    continue
                else:
                    print("Ошибка ввода, до свидания!")
                    break

player_1 = Player("Max")
player_2 = Player("Ramil")
game = Game(player_1, player_2)
game.main()
