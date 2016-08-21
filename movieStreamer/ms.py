import os
import sys
import requests
from bs4 import BeautifulSoup

def system_test():
    if (os.system("npm --version")) != 0:
        print("Need to install NPM - Node Package Manager")
        exit()
    if(os.system("peerflix --version")) !=0:
        print("Installing Dependency: peerflix")
        os.system("npm install -g peerflix")


# URL in the form https://yts.ag/movie/money-monster-2016
# Input should be 'Movie Name 720/1080'


##  Declare global variables




def wrap_input():
    ## Get the movie name
    movie_name = ' '.join(sys.argv[1:])
    # replace all the blanks with -
    movie_name = movie_name.replace(' ','-').lower()
    searhURL(movie_name)



# pass movie name
# pull out quality from the last of the string
def searhURL(search_movie):
    url = 'https://yts.ag/movie/' +  search_movie
    get_torrent(url)


def get_torrent(search_url):
    print(search_url)
    torrent_link = ''
    search_requests = requests.get(search_url, verify=False)
    soup = BeautifulSoup(search_requests.text, 'html.parser')
    for link in soup.find_all("a"):
        if link.string == '720p':
            torrent_link = link.get('href')
            break
    print('Streaming Torrent: ' + torrent_link)
    os.system('peerflix ' + torrent_link + ' -a --vlc')


wrap_input()




















