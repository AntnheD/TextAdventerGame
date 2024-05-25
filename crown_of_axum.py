class CrownOfAksum:
    def start(self, game):
        print("You have embarked on a journey to find the Crown of Aksum.")
        game.start_monk_quiz()
        if game.game_state["monk_quiz_passed"]:
            print("After facing numerous challenges, you find the Crown of Aksum.")
            game.update_score(100)
        else:
            print("You failed the monk's quiz and couldn't proceed.")
            game.game_over()
