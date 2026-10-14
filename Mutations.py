def mutate_string(string, position, character):
    text = list(string)
    text[position] = character
    new_text = ''.join(text)
    return new_text

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)