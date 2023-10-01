import re
from typing import List

def simplify_txt(file_path: str, keywords: List[str] = ["ceo", "pay", "ratio", "times", "compensation", "median", "chief executive officer", ]):

    # load file
    with open(file_path, "r") as f:
        data = f.read()
        print(len(data))
    data = data.lower()
    # remove html tags
    data = re.sub('<[^>]*>', '', data)
    # remove new line
    data = data.replace("\n", " ")
    # for each keyword, find every occurences and extract 2000 characters before and after
    chunks = []
    for keyword in keywords:
        keyword_pos = [substr.start() for substr in re.finditer(keyword , data)]
        for pos in keyword_pos:
            chunks.append(data[pos-500:pos+500])
    chunk_string = "\n".join(chunks)
    # write to file
    with open(file_path.replace(".txt", "_simplified.txt"), "w") as f:
        f.write(chunk_string)