from markdown.postprocessors import Postprocessor

from utils import TODO_BOX_TEMPLATE


class TODOPostprocessor(Postprocessor):
    """ Convert a TODO line into a html tag """

    # Potenitally create the html objects here?
    def run(self, lines):
        cnt = self.md.htmlStash.html_counter
        # TODO: Create a parser of the TODOs (for now, just use 1 word)
        for el in self.md.htmlStash.rawHtmlBlocks[::-1]:
            split_string = el.split()
            lines = TODO_BOX_TEMPLATE.format(str(cnt), str(cnt), str(cnt), " ".join(split_string[1:])) + '\n' + lines
            cnt -= 1
        # Check docs for a way to cleanup the htmlStash more efficiently
        self.md.htmlStash.reset()

        return lines