# 10.12.23

# Class import
import Stream.api.page as Page
from Stream.util.message import msg_start
from Stream.upload.update import main_update
from Stream.util.console import console, msg, console_print
from Stream.api.film import main_dw_film as download_film
from Stream.api.tv import main_dw_tv as download_tv

domain = "cz"
site_version = Page.get_version(domain)

def main():
    msg_start()
    main_update()

    film_search = msg.ask("[blue]Insert film to search: ").strip()
    db_title = Page.search(film_search, domain)

    for i in range(len(db_title)):
        console_print(f"[yellow]{i} [white]-> [green]{db_title[i]['name']} [white]- [cyan]{db_title[i]['type']}")
    index_select = int(msg.ask("[blue]Index to download: "))

    if db_title[index_select]['type'] == "movie":
        console.log(f"[green]Movie select: {db_title[index_select]['name']}")
        download_film(db_title[index_select]['id'], db_title[index_select]['name'].replace(" ", "+"), domain)

    else:
        console.log(f"[green]Tv select: {db_title[index_select]['name']}")
        download_tv(db_title[index_select]['id'], db_title[index_select]['name'].replace(" ", "+"), site_version, domain)

if __name__ == '__main__':
    main()