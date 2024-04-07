import random
import time

characters = ["Aatrox", "Ahri", "Akali", "Alistar", "Amumu", "Anivia", "Annie", "Aphelios", "Ashe", "Aurelion Sol",
    "Azir", "Bard", "Blitzcrank", "Brand", "Braum", "Caitlyn", "Camille", "Cassiopeia", "Cho'Gath", "Corki",
    "Darius", "Diana", "Dr. Mundo", "Draven", "Ekko", "Elise", "Evelynn", "Ezreal", "Fiddlesticks", "Fiora",
    "Fizz", "Galio", "Gangplank", "Garen", "Gnar", "Gragas", "Graves", "Hecarim", "Heimerdinger", "Illaoi",
    "Irelia", "Ivern", "Janna", "Jarvan IV", "Jax", "Jayce", "Jhin", "Jinx", "Kai'Sa", "Kalista",
    "Karma", "Karthus", "Kassadin", "Katarina", "Kayle", "Kayn", "Kennen", "Kha'Zix", "Kindred", "Kled",
    "Kog'Maw", "LeBlanc", "Lee Sin", "Leona", "Lillia", "Lissandra", "Lucian", "Lulu", "Lux", "Malphite",
    "Malzahar", "Maokai", "Master Yi", "Miss Fortune", "Mordekaiser", "Morgana", "Nami", "Nasus", "Nautilus",
    "Neeko", "Nidalee", "Nocturne", "Nunu & Willump", "Olaf", "Orianna", "Ornn", "Pantheon", "Poppy",
    "Pyke", "Qiyana", "Quinn", "Rakan", "Rammus", "Rek'Sai", "Rell", "Renekton", "Rengar", "Riven",
    "Rumble", "Ryze", "Samira", "Sejuani", "Senna", "Seraphine", "Sett", "Shaco", "Shen", "Shyvana",
    "Singed", "Sion", "Sivir", "Skarner", "Sona", "Soraka", "Swain", "Sylas", "Syndra", "Tahm Kench",
    "Taliyah", "Talon", "Taric", "Teemo", "Thresh", "Tristana", "Trundle", "Tryndamere", "Twisted Fate",
    "Twitch", "Udyr", "Urgot", "Varus", "Vayne", "Veigar", "Vel'Koz", "Vi", "Viktor", "Vladimir",
    "Volibear", "Warwick", "Wukong", "Xayah", "Xerath", "Xin Zhao", "Yasuo", "Yone", "Yorick", "Yuumi",
    "Zac", "Zed", "Ziggs", "Zilean", "Zoe", "Zyra", "Gwen", "Viego", "Akshan", "Vex", "Zeri", "Renata Glasc", 
    "Bel'Veth", "Nillah", "K'Sante", "Milio", "Naafiri", "Briar", "Hwei", "Smolder"]


def game():
    print('Who is the character?')


    def random_word(characters):
        random_index = random.randint(0, len(characters) - 1)
        random_character = characters[random_index]
        word_length = len(random_character)
        return random_character, word_length
    
        

    random_character, word_length = random_word(characters)
    guess(random_character, word_length)



def guess(random_character, word_length):
    current_progress = "_" * word_length
    print(current_progress)

    while True:
        
        letter_guess = input("Enter a letter or word: ")
        letters_in_word = random_character.count(letter_guess)
        
        if len(letter_guess) > 1:
            if letter_guess == random_character:
                current_progress = letter_guess
            else:
                print("Incorrect word.")
        else:
            if letters_in_word == 1:
                position = (random_character.find(letter_guess))
                if position != -1:
                    current_progress = current_progress[:position] + letter_guess + current_progress[position + 1:]
                else:
                    print("Letter not found. Try again.")
            else:
                for i in range(word_length):
                    if random_character[i] == letter_guess:
                        current_progress = current_progress[:i] + letter_guess + current_progress[i + 1:]

        print(current_progress)


        if "_" not in current_progress:
            print("Congratulations! You guessed the character!")
            time.sleep(1)
            play_again()
            break
        
        

def play_again():
    again = input("Do you want to play again? Y/N: ").upper
    if again() == "Y":
        game()
    elif again() == "N":
        print("See you later...")
        time.sleep(2)
    else:
        play_again()



game()