# External Imports
import re
from markdown.preprocessors import Preprocessor

# Internal Imports


class KeywordPreprocessor(Preprocessor):
    """ Store a custom line into the html stash """
    def __init__(self, md, profile_settings):
        super().__init__(md)
        self.__profile_settings = profile_settings

    def run(self, lines):
        new_lines = []

        for line in lines:
            m = self.__check_for_patterns(line)

            if m:
                self.md.htmlStash.store(line)
            else:
                new_lines.append(line)

        return new_lines
    
    def __check_for_patterns(self, line):
        for item in self.__profile_settings:
            m = re.search(repr(item), line)

            if m:
                return line

        return None
