import requests
from bs4 import BeautifulSoup
import time

# Number of pages you want to scrape
num_pages = 5

for page_num in range(1, num_pages + 1):
    # Define the URL for each page
    url = f'https://archiveofourown.org/tags/Voltron:%20Legendary%20Defender/works?page={page_num}'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'lxml')
        works = soup.find_all('li', class_='work')

        for work in works:
            # Extract title
            title = work.find('h4', class_='heading').text.strip()

            # Extract fandoms (located in <a> tags within a <h5> tag with class "fandoms heading")
            fandom = work.find('h5', class_='fandoms heading')
            fandom_tags = [fandom_tag.text.strip() for fandom_tag in fandom.find_all('a')] if fandom else "Unknown"
            fandom_tags = ', '.join(fandom_tags) if fandom_tags != "Unknown" else "No fandom"

            # Extract author
            author = work.find('a', rel='author').text.strip() if work.find('a', rel='author') else "Unknown"

            # Extract word count
            word_count = work.find('dd', class_='words').text.strip() if work.find('dd', class_='words') else "N/A"
            
            # Extract kudos count
            kudos = work.find('dd', class_='kudos').text.strip() if work.find('dd', class_='kudos') else "0"
            
            # Extract number of comments
            comments = work.find('dd', class_='comments').text.strip() if work.find('dd', class_='comments') else "0"
            
            # Extract date posted (in <p> or <div> with class "datetime")
            date_posted = work.find('p', class_='datetime').text.strip() if work.find('p', class_='datetime') else "Unknown"
            
            # Extract description (located in a <blockquote> tag with class "userstuff")
            description = work.find('blockquote', class_='userstuff').text.strip() if work.find('blockquote', class_='userstuff') else "No description"
            
            # Extract tags (located in a <ul> tag with class "tags")
            tags = [tag.text.strip() for tag in work.find_all('li', class_='tag')]
            tags = ', '.join(tags) if tags else "No tags"
            
            # Extract bookmarks count (located in a <dd> tag with class "bookmarks")
            bookmarks = work.find('dd', class_='bookmarks').text.strip() if work.find('dd', class_='bookmarks') else "0"
            
            # Extract hits count (located in a <dd> tag with class "hits")
            hits = work.find('dd', class_='hits').text.strip() if work.find('dd', class_='hits') else "0"

            # Print the results
            print(f"Title: {title}")
            print(f"Author: {author}")
            print(f"Fandoms: {fandom_tags}")
            print(f"Tags: {tags}")
            print(f"Description: {description}")
            print(f"Word Count: {word_count}")
            print(f"Kudos: {kudos}")
            print(f"Comments: {comments}")
            print(f"Date Posted: {date_posted}")
            print(f"Bookmarks: {bookmarks}")
            print(f"Hits: {hits}")
            print("-" * 50)

        # Add a delay between requests to avoid overloading the server
        time.sleep(2)
    else:
        print(f"Failed to retrieve page {page_num}. Status code: {response.status_code}")