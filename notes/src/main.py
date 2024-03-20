from bs4 import BeautifulSoup as bs

from parser import parser


def main():
    with open('test.txt', 'r', encoding="utf-8") as f:
        text = f.read()

    html = parser.reset().convert(text)
    bs_html = bs(html, 'html.parser')  # Might not be needed in the long run

    # Debugging purposes
    print(bs_html.prettify())
    # Hacky way to update the file
    with open('../templates/notes/notes_debug.html', 'w', encoding="utf-8") as f:
        f.write(bs_html.prettify())


if __name__ == '__main__':
    main()
