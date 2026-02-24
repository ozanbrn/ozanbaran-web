AUTHOR = 'Ozan Baran'
SITENAME = 'Ozan Baran | Veri Analisti & Jeoloji Yüksek Mühendisi'
SITESUBTITLE = 'Veri Bilimi ve Mühendislik Projeleri Portfolyosu'
DESCRIPTION = 'Jeoloji Yüksek Mühendisi Ozan Baran\'ın veri analitiği, Python, SQL ve Power BI projelerini paylaştığı profesyonel portfolyo sitesidir.'
SITEURL = 'https://ozanbaran.com.tr'

PLUGIN_PATHS = ['venv/Lib/site-packages'] 

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

STATIC_PATHS = ['images', 'pdf', 'extra/favicon.ico', 'extra/CNAME']

THEME_STATIC_PATHS = ['static']

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'},
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

SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.5,
        "indexes": 0.5,
        "pages": 0.5
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly"
    }
}
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
