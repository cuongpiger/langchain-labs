import mistune
import re
import os

from langchain_core.documents import Document

from typing import List, Dict, Any

def load_markdown(filepath: str) -> str:
    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()
    return content


def extract_text_keep_links(markdown_text):
    """Process markdown while keeping hyperlinks and image links."""

    def md_render(text):
        """Custom renderer to process markdown."""
        # Keep text but remove unwanted markdown elements
        return re.sub(r'\*\*|__|\*|_', '', text)  # Remove bold & italics markers

    class CustomRenderer(mistune.HTMLRenderer):
        def text(self, text):
            return md_render(text)  # Process normal text

        def link(self, link, text=None, title=None):
            return f"[{text}]({link})" if text else f"<{link}>"

        def image(self, src, alt="", title=None):
            return f"![{alt}]({src})"  # Preserve image link

    markdown = mistune.create_markdown(renderer=CustomRenderer())
    return markdown(markdown_text)


def load_all_md_files(directory_path: str) -> List[str]:
    md_files = []

    for root, _, files in os.walk(directory_path + "/"):
        for file in files:
            if file.endswith(".md"):
                md_files.append(os.path.join(root, file))

    return md_files

def convert_to_document(markdown_text: str, metadata: Dict[str, Any]) -> Document:
    """Convert markdown text to document."""
    return Document(
        page_content=markdown_text,
        metadata=metadata,
    )