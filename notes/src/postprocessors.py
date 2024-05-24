from markdown.postprocessors import Postprocessor

from .utils import TYPE_DICT
from .utils import CB_TYPE


class KeywordPostprocessor(Postprocessor):
    """ Convert a custom line into an html tag """

    def __init__(self, md, user_settings):
        super().__init__(md)
        self.__user_settings = user_settings

    def run(self, lines):
        # Create a dict of user_settings
        items_dict = {}
        for item in self.__user_settings:
            items_dict[item] = []

        # Group based on type in order to seperate them into "categories"
        for el in self.md.htmlStash.rawHtmlBlocks:
            split_string = el.split()
            for key in items_dict.keys():
                try:
                    # Search for index of keyword
                    item_index = split_string.index(repr(key))
                    # Save text for task
                    items_dict[key].append(" ".join(split_string[item_index + 1:]))
                except ValueError:
                    pass
                # Save remainder to file contents - TODO: Possibly update preprocessor if we want this to work

            # lines = self.__create_checkbutton_element(split_string[1:], cnt) + '\n' + lines

        # Handle top of the file
        lines = self.__add_items(items_dict, self.md.htmlStash.html_counter) + lines

        # Reset stash
        self.md.htmlStash.reset()

        return lines

    def __add_items(self, items_dict, cnt):
        tasks = ""

        for key in items_dict.keys():
            if items_dict[key] == []:
                pass
            else:
                tasks += (str(key) + '\n')  # TODO: Possibly make it also some sort of a header tag?
                for el in items_dict[key]:
                    # TODO: Handle type of object that needs creation and call relevant funct (dict with default types)
                    tasks += self.__create_checkbutton_element(el, cnt)
                    cnt -= 1
                tasks += '\n'
        return tasks

    def __create_checkbutton_element(self, message, cnt):
        return TYPE_DICT[CB_TYPE].format(
            str(cnt), 
            str(cnt), 
            str(cnt), 
            message
        )