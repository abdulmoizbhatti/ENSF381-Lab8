# 
# Completed by:
# Moiz Bhatti: 30163705
# Faheem Mazhar: 30140922
#

import requests
from bs4 import BeautifulSoup
import re
from collections import Counter
import matplotlib.pyplot as plt

url = "https://en.wikipedia.org/wiki/University_of_Calgary"

try:
    response = requests.get(url)
    response.raise_for_status() # Ensures the request was successful
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f"Successfully fetched content from {url}")
    print(soup.prettify())
    
    # Step 3
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    print(f"\nNumber of headings: {len(headings)}")
    
    links = soup.find_all('a')
    print(f"Number of links: {len(links)}")
    
    paragraphs = soup.find_all('p')
    print(f"Number of paragraphs: {len(paragraphs)}")
    
    # Step 4
    keyword = input("\nEnter a keyword to search for: ")
    page_text = soup.get_text().lower()
    keyword_count = page_text.count(keyword.lower())
    print(f"The keyword '{keyword}' appears {keyword_count} times in the webpage.")
    
    # Step 5
    print("\nStep 5: Word Frequency Analysis")
    page_text = soup.get_text()
    page_text = page_text.lower()

    # adding this so "calgary" and things like "calgary." wont be considered two different words, thus making frequency accurate:
    page_text = re.sub(r'[^\w\s]', ' ', page_text)

    words = page_text.split()
    word_counts = Counter(words)
    print("Top 5 most frequently occurring words:")
    for word, count in word_counts.most_common(5):
        print(f"'{word}': {count} occurrences")
    
    # Step 6
    print("\nStep 6: Finding the Longest Paragraph")
    longest_paragraph = ""
    longest_word_count = 0
    
    for p in paragraphs:

        paragraph_text = p.get_text().strip()
        words_in_paragraph = len(paragraph_text.split())

        if words_in_paragraph >= 5 and words_in_paragraph > longest_word_count:
            longest_paragraph = paragraph_text
            longest_word_count = words_in_paragraph
    
    print(f"Longest paragraph contains {longest_word_count} words:")
    print(longest_paragraph)
    
    #Step 7
    labels = ['Headings', 'Links', 'Paragraphs']
    values = [len(headings), len(links), len(paragraphs)]

    plt.bar(labels, values)
    plt.title('Group 27')
    plt.ylabel('Count')
    plt.show()

except Exception as e:
    print(f"Error fetching content: {e}")

