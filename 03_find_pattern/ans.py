# -  *  - coding:utf-8 -  *  -

import re

if __name__ == "__main__":
    with open("./README.md", "r", encoding="utf-8") as f:
        for line in f:
            pattern = re.compile("^##.*")
            m = pattern.match(line)
            if m is not None:
                print(m.group())
