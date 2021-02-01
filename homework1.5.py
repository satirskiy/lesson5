with open("my_file.py", "w", encoding='utf-8') as f:
    while True:
        line = input("введите строку:")
        if not line:
            break
        print(line, file=f)


