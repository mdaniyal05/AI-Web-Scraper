from bs4 import BeautifulSoup


def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for scripts_or_styling in soup(["script", "style"]):
        scripts_or_styling.extract()

    cleaned_body_content = soup.get_text(separator="\n")

    cleaned_body_content = "\n".join(
        line.strip() for line in cleaned_body_content.splitlines() if line.strip())

    return cleaned_body_content
