from tkinter import END, Text

globalSyntax = "None"
globalSyntaxWords = None
def find_all(str, sub):
    start = 0
    matches = []
    while True:
        start = str.find(sub, start)
        if start == -1: return matches
        matches.append(start)
        start += len(sub)

def syntax_configure(widget: Text, syntaxName = None):
    # cat1 cat2 cat3
    global globalSyntax
    if syntaxName != None:
        globalSyntax = syntaxName
    widget.tag_remove("group1", "1.0", END)
    widget.tag_remove("group2", "1.0", END)
    widget.tag_remove("group1", "3.0", END)
    global globalSyntaxWords
    if globalSyntax == "Cpp":
        globalSyntaxWords = [ ("int", "double", "bool", "void"), ("(", ")", "{", "}", "[", "]", ";"), ("new", "delete", "return" )]
        widget.tag_configure("group1", foreground="#0000ff")
        widget.tag_configure("group2", foreground="#ff0000")
        widget.tag_configure("group3", foreground="#000099")
        syntax(widget)

    else:
        globalSyntaxWords = None
def syntax(widget: Text):
    global globalSyntax
    gr = 0
    if globalSyntax != "None":
        content = widget.get("1.0", END)
        for group in globalSyntaxWords:
            gr += 1
            for word in group:
                wordmatches = find_all(content, word)
                if wordmatches:
                    for i in wordmatches:
                        widget.tag_add("group" + str(gr), "1.0 +" + str(i) + " chars", "1.0 +" + str(i + len(word)) + " chars")
    
