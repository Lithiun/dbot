def command_list():
    with open("commands.md", "r", encoding="utf-8") as f:
        txt = f.read()
    return txt
