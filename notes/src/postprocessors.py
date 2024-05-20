from markdown.postprocessors import Postprocessor

from .utils import SEPARATOR, ITEMS_DICT


class KeywordPostprocessor(Postprocessor):
    """ Convert a custom line into an html tag """

    # Potenitally create the html objects here?
    def run(self, lines):
        # TODO: Use the DB for the ids iso. cnt (PK will be sufficient?)
        cnt = self.md.htmlStash.html_counter
        
        # TODO: Cover them based on type (go over list) in order to seperate them into "categories"
        for el in self.md.htmlStash.rawHtmlBlocks[::-1]:
            lines = self.__create_field_element(el, cnt) + '\n' + lines
            cnt -= 1

        # TODO: Check docs for a way to cleanup the htmlStash more efficiently
        self.md.htmlStash.reset()

        return lines
    
    def __create_field_element(self, el, cnt):
        split_string = el.split()

        # Check for type of caught keyword 
        # TODO: Think of a better way to pass *args
        return ITEMS_DICT[split_string[0].strip(SEPARATOR)].format(
            str(cnt), 
            str(cnt), 
            str(cnt), 
            " ".join(split_string[1:])
        )