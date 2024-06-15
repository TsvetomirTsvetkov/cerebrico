# External Imports
from markdown.extensions import Extension

# Internal Imports
from notes.src.preprocessors import KeywordPreprocessor
from notes.src.postprocessors import KeywordPostprocessor



class KeywordExtension(Extension):
    """ MarkDown Extension """

    def __init__(self, **kwargs):
        self.config = {
            'profile_settings' : ['placeholder']
        }
        super(KeywordExtension, self).__init__(**kwargs)

    def extendMarkdown(self, md):
        md.preprocessors.register(KeywordPreprocessor(md, self.config['profile_settings'][0]), 'item', 1)
        md.postprocessors.register(KeywordPostprocessor(md, self.config['profile_settings'][0]), 'item', 1)
