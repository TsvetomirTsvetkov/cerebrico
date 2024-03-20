import re

from markdown.preprocessors import Preprocessor

from utils import SEPARATOR, ITEMS_DICT, IS_PREFIX

class KeywordPreprocessor(Preprocessor):
    """ Store a custom line into the html stash """

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
        for item in ITEMS_DICT.keys():
            if IS_PREFIX:
                pattern = SEPARATOR + item                    
            else:
                pattern = item + SEPARATOR
            
            m = re.search(pattern, line)

            if m:
                return line
            else:
                continue

        return None
