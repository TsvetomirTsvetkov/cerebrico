from markdown.extensions import Extension

from preprocessors import TODOPreprocessor
from postprocessors import TODOPostprocessor

from utils import TODO_ITEM, TODO_PRIORITY

class TODOExtension(Extension):
    """ TODO Extension """

    def extendMarkdown(self, md):
        md.preprocessors.register(TODOPreprocessor(md), TODO_ITEM, TODO_PRIORITY)
        md.postprocessors.register(TODOPostprocessor(md), TODO_ITEM, TODO_PRIORITY)
