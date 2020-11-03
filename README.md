# LibraryThingTagScraper

This is a small Python script created to extract all tags for a given list of ISBN numbers to an Excel sheet.

## Getting Started
```
pip3 install -r /requirements.txt
python ./run.py --source=./example.txt
```
### Parameters

| parameter     | default value                                            | explanation                                                                                                                                                |
|---------------|----------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| --source      | input.txt                                                | File with workIDs that need to be processed. each workID is on a separate line                                                                             |
| --destination | output.xlsx                                              | Name of the resulting Excel file.                                                                                                                          |
| --numberOfTags| 6                                                        | The number of tags that need to be put in the resulting file. The n most popular tags will be chosen                                                       |

### Prerequisites

Python 3 is needs to be installed in order to be able to run this script.