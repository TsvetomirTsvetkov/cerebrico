# Singleton
from markdown import Markdown

from extensions import TODOExtension

parser = Markdown(
    extensions=[
        TODOExtension(),
    ]
)