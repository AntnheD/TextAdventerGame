class BookOfEnoch:
    def start(self, game):
        print("You have embarked on a journey to discover the Book of Enoch.")
        game.start_monk_quiz()
        if game.game_state["monk_quiz_passed"]:
            print("After solving ancient puzzles, you discover the Book of Enoch.")
            game.update_score(150)
        else:
            print("You failed the monk's quiz and couldn't proceed.")
            game.game_over()
