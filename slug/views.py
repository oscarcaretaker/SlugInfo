from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from urllib.parse import quote

# List of all slugs fo URL generation.
slug_names = [
          "Air_Elemental",
          "Aquabeek",
          "Arachnet",
          "Armashelt",
          "Blastipede",
          "Boon Doc (White)",
          "Bubbaleone",
          "Crystalyd",
          "Diggrix",
          "Dirt Urchin",
          "Earth Elemental",
          "Enigmo",
          "Fandango",
          "Fire Elemental",
          "Flaringo",
          "Flatulorhinkus",
          "Forgesmelter",
          "Frightgeist",
          "Frostcrawler",
          "Gazzer",
          "Geoshard",
          "Grenuke",
          "Hexlet",
          "Hop Rock",
          "Hoverbug",
          "Hypnogrif",
          "Infurnus",
          "Jellyish",
          "Lariat",
          "Lavalynx",
          "MakoBreaker",
          "Negashade",
          "Neotox",
          "Phosphoro",
          "Polero",
          "Rammstone",
          "Sand Angler",
          "Slicksilver",
          "Slyren",
          "Speedstinger",
          "Tazerling",
          "Thresher",
          "Thugglet",
          "Tormato",
          "Vinedrill",
          "Water Elemental",
          "Xmitter"
     ]
def get_protoform_image(request):
     # dictionary to store data as info["SLUG_NAME"] = "IMAGE_URL"
     info = {}

     # loop to get data of each slug
     for i in slug_names:
      # Custom URL generation
      slug_url_name = quote(i)
      """The quote() function replaces special characters with their percent-encoded format. 
         This encoding is essential when passing data in a URL because it ensures that special
          characters do not interfere with the URL format."""
      url = f"https://slugterra.fandom.com/wiki/{slug_url_name}"

      # use of BeautifulSoup
      response = requests.get(url)
      soup = BeautifulSoup(response.text, 'html.parser')

      # targeting the image url
      level1 = soup.find("main", {"class": "page__main"})
      level2 = level1.find("div", {"class": "mw-parser-output"})
      image = level2.find('a', attrs={"class": "image image-thumbnail", 'title': 'Protoform'})
      if image:
          info[i] = image['href']
      else:
          image = level2.find('a', attrs={"class": "image image-thumbnail", "title": "Slug Protoform"})
          info[i] = image['href']

     return render( request, 'slug/base.html', {'info':info})

# - - - - - - - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - -- - - - -- - -

# Slug Detail View
def details(request,slug):

    #data dictionary to store detail info of slug
     data = {}
     slug_url_name = quote(slug)
     url = f"https://slugterra.fandom.com/wiki/{slug_url_name}"
     response = requests.get(url)

     # check if url runs successfully
     if response.status_code == 200:

          # Web Scapped
          soup = BeautifulSoup(response.content, "html.parser")
          level1 = soup.find("main", {"class": "page__main"})
          level2 = level1.find("div", {"class": "mw-parser-output"})


          # Description of slug
          description = level2.find_all("p")[1]
          data["description"] = description.text

          # Analysis of slug
          try:
              # Attempt to access the fourth <p> tag in the result of find_all
              analysis = level2.find_all("p")[3]
              data["analysis"] = analysis.text
          except IndexError:
              # Handle the error if there aren't enough <p> tags in the list
              print("The list does not contain enough <p> elements.")
              analysis = None  # Or set this to some default value if needed


          # Attacks of sLug
          try:
              # Attempt to access the fourth <p> tag in the result of find_all
              span = soup.find("span", id="Attacks")
              h2 = span.find_parent("h2")
              attacks = h2.find_next_sibling("ul")
              data["attacks"] = attacks.text
          except AttributeError:
              # Handle the error if find_all is not a valid method on level2
              span = soup.find("span", id="Attacks/Abilities")
              h2 = span.find_parent("h2")
              attacks = h2.find_next_sibling("ul")
              attacks2 =attacks.find_next_sibling("ul")
              data["attacks"] = attacks.text + attacks2.text



          # Protoform Slug Image
          image = level2.find('a',attrs={"class": "image image-thumbnail", 'title': 'Protoform'})
          if image:
            data['protoform']= image['href']
          else:
              image = level2.find('a', attrs={"class": "image image-thumbnail", "title": "Slug Protoform"})
              data['protoform'] = image['href']


          # Velocimorph of slug
          morph = level2.find('a', attrs={"class": "image image-thumbnail", "title": "Velocimorph"})
          if morph:
            data["morph"]=morph['href']
          else:
              morph = level2.find('a', attrs={"class": "image image-thumbnail", "title": "Slug Velocity"})
              data["morph"]=morph['href']


          # Megamorph of slug
          megamorph = level2.find("div", {"class": "pi-image-collection wds-tabber", "data-source": "megamorphImage"})
          if megamorph:
            megamorph = megamorph.find("a", {"title": "Velocimorph"})
            if megamorph:
             data["megamorph"] = megamorph['href']
            else:
             data["meguno"] = 'NO'
          else:
               data["meguno"] = 'NO'


          # Fusion Shots
          span = soup.find("span", id="Fusion_Shots")
          if span:
             h2 = span.find_parent("h2")
             if h2:
              shots = h2.find_next_sibling("ul")
              data["shots"] = shots.text


          return render(request,'slug/details.html',context={'data':data,"slug":slug})


def search_view(request):
    query = request.GET.get('searched', '')

    if query:
        filtered_names = [name for name in slug_names if query.lower() in name.lower()]
        info = {}
        for i in filtered_names:
            # Custom URL generation
            slug_url_name = quote(i)
            """The quote() function replaces special characters with their percent-encoded format. 
               This encoding is essential when passing data in a URL because it ensures that special
                characters do not interfere with the URL format."""
            url = f"https://slugterra.fandom.com/wiki/{slug_url_name}"

            # use of BeautifulSoup
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')

            # targeting the image url
            level1 = soup.find("main", {"class": "page__main"})
            level2 = level1.find("div", {"class": "mw-parser-output"})
            image = level2.find('a', attrs={"class": "image image-thumbnail", 'title': 'Protoform'})
            if image:
                info[i] = image['href']
            else:
                image = level2.find('a', attrs={"class": "image image-thumbnail", "title": "Slug Protoform"})
                info[i] = image['href']

    else:
        filtered_names = slug_names

    return render(request, 'slug/search.html', {'info': info})

