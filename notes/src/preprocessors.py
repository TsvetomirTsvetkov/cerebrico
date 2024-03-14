import re

from markdown.preprocessors import Preprocessor

from utils import SEPARATOR, TODO_ITEM

class TODOPreprocessor(Preprocessor):
    """ Convert a TODO line into a html tag """

    def run(self, lines):
        new_lines = []
        for line in lines:
            m = re.search(SEPARATOR + TODO_ITEM, line)

            if m:
                self.md.htmlStash.store(line)
            else:
                new_lines.append(line)

        return new_lines