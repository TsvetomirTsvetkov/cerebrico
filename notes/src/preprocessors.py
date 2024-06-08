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
            m = self.check_for_patterns(line, self.__profile_settings)

            if m:
                self.md.htmlStash.store(line)
            else:
                new_lines.append(line)

        return new_lines
    
    def check_for_patterns(cls, line, profile_settings):
        for item in profile_settings:
            m = re.search(repr(item), line)

            if m:
                return line

        return None
