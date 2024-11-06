# SlugInfo
Welcome to ***SlugInfo***! This project is a straightforward web application built with Django that gathers and presents information about slugs through web scraping. With this app, you can explore various slugs, read in-depth descriptions of their attacks and behavior, and enjoy a modern, user-friendly interface.

##  Key Features

- **Slug Directory**: Explore a variety of available slugs.
- **Slug Details**: Click on any slug to view its detailed information.
- **Quick Search**: Easily locate your favorite slug with search functionality.
- **Responsive Layout**: Enjoy a sleek design that adapts beautifully to any device.

## Code Overview

### `views.py`
Contains the logic to retrieve a list of slugs through web scraping.
- **get_protoform_image(request)**: Collects images for the listed slugs, stores them in a dictionary, and returns them for display.
- **details(request, slug)**: Retrieves detailed information for a specific slug by its name, presenting a unique description.
- **search_view(request)**: Allows users to search for a specific slug from the list of available slugs.

### `urls.py`
- **pronto/urls.py**: Main URL configuration file that integrates the routes for the Slug app and other core application components.
- **slug/urls.py**: Manages the routes specific to the Slug app, including the list and detail views for individual slugs.

### `slug/templates`
- **base.html**: The homepage template showcasing the list of slugs with integrated search functionality.
- **details.html**: The template for detailed information, displaying a comprehensive view of a specific slug.
- **search.html**: Template for showing search results based on the user’s input, making it easy to find a slug by keyword.

## Questions 😊
### How am I fetching the data about slugs?
- With a little help from our friends *BeautifulSoup* and *requests*, I scrape data straight from the source at [SlugTerra Wiki](https://slugterra.fandom.com/wiki/SlugTerra_Wiki)—no secret potions involved!
- I also employ `quote()` from `urllib` to magically generate URLs dynamically, making it feel like the slugs are just waiting for me to call them out!

### What’s powering the backend?
- Our backend superstar is Django, which neatly stores and displays the data, like a proud parent showing off its slug collection!
- URL mapping is carefully implemented to keep routes clear and straightforward—think of it as GPS for our slugs.
- Functional views handle all the hard work, efficiently processing user’s request. So when you want slug info, Django’s got your back.

### What did I use on the frontend?
- Thanks to Bootstrap 5, we have a fully responsive design that looks great across all devices, with some custom CSS flair to keep things unique!
- The UI is simple yet elegant, making each slug feel like the star it deserves to be on the screen.

##  Contributing

Feel free to fork this repository, create a feature branch, and submit a pull request. All contributions are welcome!

