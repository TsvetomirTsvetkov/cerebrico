from markdown import Markdown

from extensions import KeywordExtension

# Singleton
parser = Markdown(
    extensions=[
        KeywordExtension(),
    ]
)