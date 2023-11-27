import requests
from bs4 import BeautifulSoup

needed_headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}

if __name__ == '__main__':
    def get_first_n_chars(response, n):
        return response.text[0:n]

    def verify_response(response):
        print(response.status_code)
        assert response.status_code == 200

    def verify_page_title(movie_soup):
        title = movie_soup.find('title')
        assert title.text == "The Movie Database (TMDb)"

    def get_beautiful_soup_object(url):
        try:
            response = requests.get(url, headers=needed_headers)
            verify_response(response)
            return BeautifulSoup(response.content, 'html.parser')
        except:
            raise Exception("Error in getting the beautiful soup object")
    
    def get_movie_title(movie_html):
        print("*****************************")
        return movie_html.find("h2").a.text
    
    def get_movie_rating(movie_html):
        return movie_html.find("div", class_="outer_ring").div["data-percent"]
    
    def get_movie_url(movie_html):
        return movie_html.find("h2").a["href"]
    
    def all_movie_titles(results):
        movie_titles = []
        for movie_html in results:
            print(movie_html.prettify())
            print(movie_titles)
            movie_titles.append(get_movie_title(movie_html))
        return movie_titles

# URL generation
base_url = "https://www.themoviedb.org/movie"
# movie_url =  f'{base_url}/movie'

# # Get the page
# movie_response = requests.get((movie_url), headers=needed_headers)

# # Check the first 200 characters
# first_200_chars = movie_response.text[0:200]

# # assert the length of characters in the variable
# assert len(first_200_chars) == 200

# print(movie_response.text[0:200])


# base_url = "http://example.com:-80/"

# Create the object of the beautiful soup
movie_response_soup = get_beautiful_soup_object(base_url)
results = movie_response_soup.find(id="page_1")

# First Movie
first_movie_html = results.find("div", class_="style_1")
print(first_movie_html.prettify())
print("")
print
first_movie_text = get_movie_title(first_movie_html)
print(f'First Movie Title: {first_movie_text}')

rating = get_movie_rating(first_movie_html)
print(f'{rating}')

movie_url = get_movie_url(first_movie_html)
print(movie_url)

removals = results.find_all('div', {'class':'filler'})
print(removals)


# print(results_list)
# all_movie_titles = all_movie_titles(results_list)
# print(all_movie_titles)

# I would like to use the `lxml` parser but as given in assignment to use the html.parser so I am using it
# movie_soup = BeautifulSoup(movie_response.text, 'html.parser')

# title = movie_soup.find('title')
# print(title.text)

# import unittest

# class TestStringMethods(unittest.TestCase):

#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')

#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.isupper())

#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         # check that s.split fails when the separator is not a string
#         with self.assertRaises(TypeError):
#             s.split(2)

# if __name__ == '__main__':
#     unittest.main()
