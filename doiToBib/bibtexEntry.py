# Defines a class for containing and outputting a bibtex entry for an article
#
# October 2016 Robert Shaw

class BibEntry:
    """A bibtex entry object for an article"""
    type = "article"
    number = ""
    pages = ""
    month = ""
    note = ""
    key = ""
    
    def __init__(self, author="", title="", journal="", year="", volume=""):
        self.author = author
        self.title = title
        self.journal = journal
        self.year = year
        self.reference = author + year
        self.volume = volume
    
    def ToString(self):
        output = "@Article{" + self.reference + ",\n"
        output += "author = {" + self.author + "},\n"
        output += "title = {" + self.title + "},\n"
        output += "journal = {" + self.journal + "},\n"
        output += "year = " + self.year + ",\n"
        
        if self.number != "":
            output += "number = " + self.number + ",\n"
        
        if self.pages != "":
            output += "pages = {" + self.pages + "},\n"
        
        if self.month != "":
            output += "month = " + self.month + ",\n"
        
        if self.note != "":
            output += "note = {" + self.note + "},\n"
        
        output += "volume = " + self.volume + "\n}"
        return output
