
# URLs
BASE_URL_PAGES = "https://risazatvorchestvo.com/releases?page="
BASE_URL_AUTORS_PAGES = "https://risazatvorchestvo.com/authors?page="
BASE_URL_RELEASE = "https://risazatvorchestvo.com"
BASE_GENIUS_URL = "https://genius.com/"
BASE_GENIUS_ARTIST_URL = "https://genius.com/artists/"

# CSS risazatvorchestovo.com
CARDS_DIV_CLASS = "hover:bg-white/[8%] bg-white/5 p-1 lg:p-3 overflow-hidden flex flex-col justify-start relative origin-bottom-left w-full h-full rounded-xl border border-zinc-800 group duration-300"
GRADE_INDICATOR_CLASS = "inline-flex size-7 text-xs items-center font-semibold justify-center bg-[rgba(0,0,0,.4)] dark:bg-[rgba(255,255,255,.1)] rounded-full"
RELISE_NAME_CLASS = "text-sm w-full dark:text-white antialiased break-all leading-4 mt-2 block font-medium text-ellipsis max-w-full whitespace-nowrap overflow-hidden"
ARTIST_NAME_CLASS = "flex flex-wrap leading-3 font-semibold mt-1.5 gap-y-1 text-[13px]"
ARTIST_LINK_CLASS = "inline-flex items-center justify-center whitespace-nowrap cursor-pointer text-sm font-medium ring-offset-background transition-colors focus-visible:outline-hidden focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 hover:bg-accent hover:text-accent-foreground h-10 py-2 has-[>svg]:px-3 px-2 pl-1 lg:px-3 lg:py-0 lg:pl-2 rounded-full gap-x-1.5 lg:gap-x-2 flex items-center"

# CSS genius.com
NOT_FOUND_DIV_CLASS = "render_404"

# Paths
PARSER_DIR = "parser/"
DATA_DIR = "data/"
NEW_DATA_DIR = "new_data/"
ALL_PAGES_DIR = NEW_DATA_DIR + "all_pages/"
SORTED_PAGES_DIR = NEW_DATA_DIR + "sorted_pages/"
PAGES_WITH_GRADES = NEW_DATA_DIR + "assessed_pages/"
PAGE_FILENAME = "page_{}.json"

OTHER_PARSER_DIR = PARSER_DIR + "other_jsons/"

# Output files
ALL_RELEASES_FILE = NEW_DATA_DIR + "all_relises.json"
ALBUMS_FILE = NEW_DATA_DIR + "albums.json"
TRACKS_FILE = NEW_DATA_DIR + "tracks.json"
SELECTED_RELEASES_FILE_TEMPLATE = NEW_DATA_DIR + "selection_releases_{}.json"
SELECTED_RELEASES_1000_FILE = SELECTED_RELEASES_FILE_TEMPLATE.format(1000)
SELECTED_RELEASES_FINAL_FILE = "selected_release.json"

ALT_NAME_ARTIST = OTHER_PARSER_DIR + "alt_name.json"
ERR_ALT_NAME_ARTIST = OTHER_PARSER_DIR + "err_alt_name.json"

VALID_GENIUS_SLUGS_FILE = OTHER_PARSER_DIR + "valid_genius_slugs.json"
INVALID_GENIUS_SLUGS_FILE = OTHER_PARSER_DIR + "invalid_genius_slugs.json"

GENIUS_LYRICS_OUTPUT_FILE = NEW_DATA_DIR = "releases_with_lyrics.json"

# Other
GRADES_MARKER = [
    ("Рифмы / образы", 84),
    ("Структура / ритмика", 89), 
    ("Реализация стиля", 86),
    ("Индивидуальность / харизма", 96),
    ("Атмосфера / вайб", 86)
]