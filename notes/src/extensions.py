from markdown.extensions import Extension

from preprocessors import KeywordPreprocessor
from postprocessors import KeywordPostprocessor

from utils import ITEM, PRIORITY

class KeywordExtension(Extension):
    """ MarkDown Extension """

    def extendMarkdown(self, md):
        md.preprocessors.register(KeywordPreprocessor(md), ITEM, PRIORITY) # TODO: Check documentation for ITEM
        md.postprocessors.register(KeywordPostprocessor(md), ITEM, PRIORITY) # TODO: Check documentation for ITEM
