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

picresize.py: resizes image files in a directory filewalk, specific folder or specific file to (500, x), roughly keeping aspect ratio.

pdfresizer.py: resizes pdf files in a directory filewalk, specific folder or specific file to (500, x), roughly keeping aspect ratio.


## Recommendations:

[lotspaih/automateBoringstuffPython](https://github.com/lotspaih/automateBoringstuffPython) for good specific purpose type examples.

[vinta/awesome-python](https://github.com/vinta/awesome-python) for excellent list of Python frameworks, libraries and resources.

## To do:

-Continue picking up Pandas, NumPy, matplotlib, scikit-learn, NLTK, and NetworkX, implement current scripts to better interface with data analysis libraries. 

--for pandas, tweak multiread to yield, dictionary of ordered lists, keys as imported column name for pandas dataframe, value as list with all the values for the column, in accordance to the index. Alternatively, List of lists, each inner list a row, with values within ordered in accordance to columns. Note common format for tweaking the other more general purpose programming scripts.

-get started on Gui Automation.

-implement SQL drivers into inputsql.py.

-HTML reader with Request, JSON and HTML writer (if non-data analytics task...)
