AUTHOR = 'Ozan Baran'
SITENAME = 'Ozan Baran'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Europe/Istanbul'

DEFAULT_LANG = 'Turkish'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("Linkedin", "https://www.linkedin.com/in/ozanbrn/"),
    ("GitHub","https://github.com/ozanbrn"),
)

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['images', 'pdf', 'extra']

THEME_STATIC_PATHS = ['static']

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

THEME = 'pelican-themes/my_themes'


# pelicanconf.py dosyasına ekle
STREAMLIT_PROJECTS = [
    {
        'title': 'Türkiye Maden Veri Analizi',
        'description': 'PostgreSQL ve Python kullanarak Türkiye boksit/bor verilerinin analizi.',
        'github': 'https://github.com/ozanbrn',
        'streamlit': 'https://ozanbaran.streamlit.app',
        'tags': ['PostgreSQL', 'Python', 'Streamlit']
    }
]

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
