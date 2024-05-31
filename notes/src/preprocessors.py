import re

from markdown.preprocessors import Preprocessor


class KeywordPreprocessor(Preprocessor):
    """ Store a custom line into the html stash """
    def __init__(self, md, user_settings):
        super().__init__(md)
        self.__user_settings = user_settings

    def run(self, lines):
        new_lines = []

        for line in lines:
            m = self.check_for_patterns(line, self.__user_settings)

            if m:
                self.md.htmlStash.store(line)
            else:
                new_lines.append(line)

        return new_lines
    
    @classmethod
    def check_for_patterns(cls, line, user_settings):
        for item in user_settings:
            if item.is_prefix:
                pattern = item.separator + item.keyword
            else:
                pattern = item.keyword + item.separator
            
            m = re.search(pattern, line)

            if m:
                return line
            else:
                continue

        return None
