from markdown.extensions import Extension

from .preprocessors import KeywordPreprocessor
from .postprocessors import KeywordPostprocessor


# TODO: Cleanup / Check how this should be handled
ITEM = "ITEM"
PRIORITY = 1


class KeywordExtension(Extension):
    """ MarkDown Extension """

    def __init__(self, **kwargs):
        self.config = {
            'user_settings' : ['placeholder']
        }
        super(KeywordExtension, self).__init__(**kwargs)

    def extendMarkdown(self, md):
        md.preprocessors.register(KeywordPreprocessor(md, self.config['user_settings'][0]), ITEM, PRIORITY)
        md.postprocessors.register(KeywordPostprocessor(md, self.config['user_settings'][0]), ITEM, PRIORITY)
