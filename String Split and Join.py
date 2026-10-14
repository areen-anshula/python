def split_and_join(line):
    text = line.split()
    new_text = "-".join(text)
    return new_text

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)