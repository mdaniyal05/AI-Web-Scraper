def split_content(content, max_length=7000):
    return [
        content[i: i + max_length] for i in range(0, len(content), max_length)
    ]
