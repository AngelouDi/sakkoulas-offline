import requests
import pdfkit
import re
from bs4 import BeautifulSoup


def get_title(url_part, cookie):
    cookies = {
        'JSESSIONID': f'{cookie}',
    }

    html = requests.get(f'https://www.sakkoulas-online.gr{url_part}', cookies=cookies).text
    soup = BeautifulSoup(html, 'html.parser')
    title_container = soup.find("h1", {"class", "noselect"})
    title = title_container.find("a").getText()

    return "".join([c for c in title if c.isalpha() or c.isdigit() or c == ' ']).rstrip() + ".pdf"


def correct_url(url_part, cookie):
    url_part = url_part.replace("editions", "reader")
    cookies = {
        'JSESSIONID': f'{cookie}',
    }

    html = requests.get(f'https://www.sakkoulas-online.gr{url_part}', cookies=cookies).text
    soup = BeautifulSoup(html, 'html.parser')
    enarksi = soup.find_all(string="Έναρξη")
    for button in enarksi:
        if button.parent['href'] != "#":
            return button.parent['href']
    return url_part


def create_body(url_part, cookie):
    cookies = {
        'JSESSIONID': f'{cookie}',
    }

    base_html = requests.get(f'https://www.sakkoulas-online.gr{url_part}', cookies=cookies).text
    soup_base = BeautifulSoup(base_html, 'html.parser')
    body = soup_base.find("body")
    body.clear()
    hc = soup_base.new_tag("div", **{'class': 'home-content'})
    hcc = soup_base.new_tag("div", id="home-column-content")
    rc = soup_base.new_tag("div", id="reader-content", **{'class': 'reader-content'})
    hcc.append(rc)
    hc.append(hcc)
    body.append(hc)
    return soup_base


def add_page(url_part, page_no, cookie, base, config):
    print("Downloading page {}".format(page_no))
    base_url = f'https://www.sakkoulas-online.gr{url_part}'
    cookies = {
        'JSESSIONID': f'{cookie}',
    }
    html_doc = requests.get(base_url, cookies=cookies).text
    soup = BeautifulSoup(html_doc, 'html.parser')
    next_link = (soup.find_all("a", {'class': 'reader-nav-page'}))[1]['href']

    content = soup.find("div", {'class': 'reader-content'})
    con = base.find_all("div", {'class': 'reader-content'})[-1]

    con.insert_after(content)
    line_break = soup.new_tag("hr", "html")
    con.insert_after(line_break)

    page_no += 1
    if next_link != "#":
        return add_page(next_link, page_no, cookie, base, config)
    else:
        print("Creating pdf...")
        pdfkit.from_string(str(base), get_title(url_part, cookie), configuration=config)
        print("Pdf created!")


def make_pdf(url, cookie, config):
    url_part = correct_url(re.split('\.gr', url)[1], cookie)
    print("Downloading {}".format(get_title(url_part, cookie)))
    add_page(url_part, 1, cookie, create_body(url_part, cookie), config)
