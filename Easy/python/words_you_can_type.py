class WordsYouCanType():
    def can_be_typed(self, text: str, broken_letters: str) -> int:
        letters = set()
        result = 1
        for i in range(len(broken_letters)):
            letters.add(broken_letters[i])
        
        new_word = True
        for j in range(len(text)):
            if text[j] == " ":
                new_word = True
                result += 1
            elif text[j] in letters and new_word == True:
                new_word = False
                result -= 1
        return result

if __name__ == "__main__":
    typed = WordsYouCanType()
    print(typed.can_be_typed("hello world", "ad"))