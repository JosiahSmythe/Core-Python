#!/usr/bin/env python3
"""Retreive and print words form a URL.

Usage:
    python3 words.oy <URL>
"""
import sys
from urllib.request import urlopen

def fetch_words(url):
    """Fetch a list of words from a URL.
    
    Args: 
        url: The URL of a UTF-8 text document.

    Returns: 
        A list of string containing the words form the document.
    
    """
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words

def print_items(items):
    """Print items one per line.
    
    Args: 
        An iterable series of printable items.    
    """
    for item in items:
        print(item)

def main(url): 
    """Print each word from a text document from at a URL.
    
    Args: 
        url: The URL of a UTF-8 text document.    
    """
    words = fetch_words(url)
    print_items(words)

if __name__ == '__main__':
    main(sys.argv[1]) # the sys.argv peramater is for the URL