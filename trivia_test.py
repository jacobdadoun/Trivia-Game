
class Run_Doc:
    def __init__(self, file_name):
        self.__infile = open(file_name, 'r')

    def question(self):
        self.__question = self.__infile.readline()
        self.__choice1 = self.__infile.readline()
        self.__choice2 = self.__infile.readline()
        self.__choice3 = self.__infile.readline()
        self.__choice4 = self.__infile.readline()
        self.__answer = self.__infile.readline().rstrip()

    def __str__(self):
        return self.__question + "1. " + self.__choice1 + "2. " + self.__choice2 + "3. " + self.__choice3 + "4. " +\
               self.__choice4

    def check_answer(self, user_selection):
        if user_selection == int(self.__answer):
            print('That is correct')
            return 1
        else:
            print('That is incorrect')
            return 0

def main():
    dq = Run_Doc('triviaquestions.txt')
    player_names = ['Player 1', 'Player 2']
    player_scores = [0, 0]

    for q in range(5):
        for player in player_names:
            print(player)

            dq.question()
            print(dq)

            player_answer = int(input("Your choice: "))
            player_scores[player_names.index(player)] += dq.check_answer(player_answer)

    print()
    print('scores:')
    print("player1:", player_scores[0])
    print("player2:", player_scores[1])

    if player_scores[0] == player_scores[1]:
        print("That's a Tie!")
    elif player_scores[0] > player_scores[1]:
        print("Player 1 is the Winner!")
    else:
        print("Player 2 is the Winner!")

main()