def common_words(filename):
    """Write a program that reads the ﬁles you found at Project Gutenberg and determines
    how many times the word 'the' appears in each text."""
    try:
        with open(filename) as f:
            content = f.read()
    except:
        pass
    else:
        words = content.split()
        common_words = words.count('the')
        print(f"the word 'the' appears {common_words}")


common_words('text_files/RomeoAndJuliet.txt')