def get_file_content(file_path):
    p = file_path
    content = []
    with open(p, "r") as f:
        for line in f:
            content.append(line.rstrip("."))
        return content
