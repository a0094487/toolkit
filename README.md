# toolkit
Assembling multi-tool scripts for modular use in work.

Aiming for flexibility and ease of use enough for similarly positioned business/accountancy professionals with only basic knowledge of programming.

## Current works

### General purpose:

mcb.py: Saves, loads and deletes pieces of text to the clipboard.
from lotspaih

multireader.py: reads pdf, docx, xlsx and any other files, outputs successful reads into datastructure in the form of a dictionary, unsuccessful reads in a seperate list.

writemodules.py: writing modules multitool, writes datastructure into txt, csv or into excel, also allows file-directory organization.

inputsql.py: Interfaces via SQLite, handles querries, writes SELECT querries into datastructure.

### Specific purpose:

us2eudatesrename.py: renames filename titles with us to eu date format.
from Al Sweigart

regexcontentsearch.py: searches within files in directories that matches a regular expression. Saves into .txt file.

pdfmerge.py: Merges all pdf in a specified folder. Option to choose which pages.

backtoZip.py: Input an entire subdirectory to backup, names backup by datetime.

## Recommendations:

[lotspaih/automateBoringstuffPython](https://github.com/lotspaih/automateBoringstuffPython) for good specific purpose type examples.

[vinta/awesome-python](https://github.com/vinta/awesome-python) for excellent list of Python frameworks, libraries and resources.

## To do:

-add picture file DPI decrease option into copy-move function in writemodules.

-Pandas, NumPy, matplotlib, scikit-learn, NLTK, and NetworkX, implement current scripts to better interface with data analysis libraries.

-get started on Gui Automation.

-implement SQL drivers into inputsql.py.

-HTML reader with Request, JSON and HTML writer.
