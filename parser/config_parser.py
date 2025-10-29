
# URLs
BASE_URL_PAGES = "https://risazatvorchestvo.com/releases?page="
BASE_URL_RELEASE = "https://risazatvorchestvo.com"

# CSS
CARDS_DIV_CLASS = "hover:bg-white/[8%] bg-white/5 p-1 lg:p-3 overflow-hidden flex flex-col justify-start relative origin-bottom-left w-full h-full rounded-xl border border-zinc-800 group duration-300"
GRADE_INDICATOR_CLASS = "inline-flex size-7 text-xs items-center font-semibold justify-center bg-[rgba(0,0,0,.4)] dark:bg-[rgba(255,255,255,.1)] rounded-full"
RELISE_NAME_CLASS = "text-sm w-full dark:text-white antialiased break-all leading-4 mt-2 block font-medium text-ellipsis max-w-full whitespace-nowrap overflow-hidden"
ARTIST_NAME_CLASS = "flex flex-wrap leading-3 font-semibold mt-1.5 gap-y-1 text-[13px]"

# Paths
DATA_DIR = "data/"
NEW_DATA_DIR = "new_data/"
ALL_PAGES_DIR = NEW_DATA_DIR + "all_pages/"
SORTED_PAGES_DIR = NEW_DATA_DIR + "sorted_pages/"
PAGE_FILENAME = "page_{}.json"

# Output files
ALL_RELEASES_FILE = NEW_DATA_DIR + "all_relises.json"
ALBUMS_FILE = NEW_DATA_DIR + "albums.json"
TRACKS_FILE = NEW_DATA_DIR + "tracks.json"
