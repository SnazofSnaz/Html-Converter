#! usr/bin/usr python3

FILENAME = "groceries.html"


def read_words():
    try:
        # if os.path.isfile(FILENAME):
        with open(FILENAME) as f:
            words = f.readlines()
        return words
    except FileNotFoundError:
        print("Could not find " + FILENAME + " file.")
        return ""
    except Exception as e:
        print(type(e), e)
        return ""


def list_to_string(words):

    str1 = " "
    return str1.join(words)
# https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/


def main():
    words = read_words()
    list_to_string(words)
#    print(list_to_string(words))
    print("HTML CONVERTER")
    print()
#   print(words)

#    print("testing here")
    for line in words:
        line = str(line)
        print(line.replace("<h1>", "").replace('\n', "").replace("<ul>", "").replace("<li>", "* ")
              .replace("</li>", "").replace("</ul>", "").replace("</h1>", "").lstrip())


if __name__ == '__main__':
    main()
