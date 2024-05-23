import colorama
from colorama import Fore, Style

# Initialize colorama
colorama.init(autoreset=True)

class AsciiArt:
    def __init__(self):
        pass

    def print_colored_text(self, text, color):
        print(color + Style.BRIGHT + text + Style.RESET_ALL)

    def game_over(self):
        art = """
   _____                        ____                 
  / ____|                      / __ \                
 | |  __  __ _ _ __ ___   ___ | |  | |_   _____ _ __ 
 | | |_ |/ _` | '_ ` _ \ / _ \| |  | \ \ / / _ \ '__|
 | |__| | (_| | | | | | |  __/| |__| |\ V /  __/ |   
  \_____|\__,_|_| |_| |_|\___| \____/  \_/ \___|_|   
        """
        self.print_colored_text(art, Fore.RED)

    def welcome(self):
        art = """
                        ____________
                     /\  ________ \
                    /  \ \______/\ \
                   / /\ \ \  / /\ \ \
                  / / /\ \ \/ / /\ \ \
                 / / /__\_\/ / /__\_\ \
                / /_/_______/ /________\
                \ \ \______ \ \______  /
                 \ \ \  / /\ \ \  / / /
                  \ \ \/ / /\ \ \/ / /
                   \ \/ / /__\_\/ / /
                    \  / /______\/ /

 __          __  _                          _ 
 \ \        / / | |                        | |
  \ \  /\  / /__| | ___ ___  _ __ ___   ___| |
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ |
    \  /\  /  __/ | (_| (_) | | | | | |  __/_|
     \/  \/ \___|_|\___\___/|_| |_| |_|\___(_)
        """
        self.print_colored_text(art, Fore.GREEN)

    def you_won(self):
        art = """
 __     ______  _    _  __          _______ _   _ 
 \ \   / / __ \| |  | | \ \        / /_   _| \ | |
  \ \_/ / |  | | |  | |  \ \  /\  / /  | | |  \| |
   \   /| |  | | |  | |   \ \/  \/ /   | | | . ` |
    | | | |__| | |__| |    \  /\  /   _| |_| |\  |
    |_|  \____/ \____/      \/  \/   |_____|_| \_|
        """
        self.print_colored_text(art, Fore.YELLOW)

    def goodbye(self):
        art = """
  ____                 _ _                 _ 
 / ___| ___   ___   __| | |__   ___   ___ | |
| |  _ / _ \ / _ \ / _` | '_ \ / _ \ / _ \| |
| |_| | (_) | (_) | (_| | | | | (_) | (_) | |
 \____|\___/ \___/ \__,_|_| |_|\___/ \___/|_|
        """
        self.print_colored_text(art, Fore.CYAN)
        
        
        

    def book_of_enoch(self):
        art = """
         
             __...--~~~~~-._   _.-~~~~~--...__
            //               `V'               \\ 
           //                 |                 \\ 
          //__...--~~~~~~-._  |  _.-~~~~~~--...__\\ 
         //__.....----~~~~._\ | /_.~~~~----.....__\\
        ====================\\|//====================
                dwb `---`
       
        """
        self.print_colored_text(art, Fore.CYAN)
    def crown_of_axum(self):
        art = """
  ____                 _ _                 _ 
                                    o
                                   $""$o
                                  $"  $$
                                   $$$$
                                   o "$o
                                  o"  "$
             oo"$$$"  oo$"$ooo   o$    "$    ooo"$oo  $$$"o
o o o o    oo"  o"      "o    $$o$"     o o$""  o$      "$  "oo   o o o o
"$o   ""$$$"   $$         $      "   o   ""    o"         $   "o$$"    o$$
  ""o       o  $          $"       $$$$$       o          $  ooo     o""
     "o   $$$$o $o       o$        $$$$$"       $o        " $$$$   o"
      ""o $$$$o  oo o  o$"         $$$$$"        "o o o o"  "$$$  $
        "" "$"     @@@@@            "$"             @@@      @@@ "
         "oooooooooooooooooooooooooooooooooooooooooooooooooooooo$
          "$$$$"$$$$" $$$$$$$"$$$$$$ @ @$$$$$"$$$$$$@  $$$@@$$$$
           $$$oo$$$$   $$$$$$o$$$$$$o" $$$$$$$$$$$$$$ o$$$$o$$$"
           $@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@$
           $"                                                 "$
           $"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$
        """
        self.print_colored_text(art, Fore.CYAN)