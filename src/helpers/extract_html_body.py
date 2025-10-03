from bs4 import BeautifulSoup


def extract_body_content(html):
    soup = BeautifulSoup(html, "html.parser")
    body_content = soup.body

    if body_content:
        return str(body_content)

    return ""
