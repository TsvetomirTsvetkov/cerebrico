# External Imports
from markdown.postprocessors import Postprocessor

# Internal Imports
from notes.src.utils import CB_TYPE, TYPE_DICT


class KeywordPostprocessor(Postprocessor):
    """ Convert a custom line into an html tag """

    def __init__(self, md, profile_settings):
        super().__init__(md)
        self.__profile_settings = profile_settings

    def run(self, lines):
        # Create a dict of profile_settings
        items_dict = {}
        for item in self.__profile_settings:
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

        lines = '<br><h3>Notes</h3><br>' + lines

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
                tasks += ('<br><h3>' + str(key) + ':</h3>')
                for el in items_dict[key]:
                    # TODO: For v1.1 - Handle object type and call relevant func
                    tasks += self.__create_checkbutton_element(el, cnt)
                    cnt -= 1
        return tasks

    def __create_checkbutton_element(self, message, cnt):
        return TYPE_DICT[CB_TYPE].format(
            str(cnt), 
            str(cnt),
            str(cnt), 
            message
        )