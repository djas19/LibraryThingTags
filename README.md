# LibraryThingTagScraper

This is a small Python script created to extract all tags for a given list of ISBN numbers to an excel sheet.

## Getting Started

### Parameters

| parameter     | default value                                            | explanation                                                                                                                                                |
|---------------|----------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| --source      | ./testData                                               | Location of the folder containing all zip files to be processed.                                                                                           |
| --destination | CODAZOOM-DDE-{datetime.datetime.now():%Y%m%d-%H%M%S}.ZIP | Name of the resulting ZIP file.                                                                                                                            |
| --archive     | ./archive                                                | Location of the folder where all processed ZIP files will be moved to.                                                                                     |
| --dry_run     | false                                                    | When this parameter is present the content of the source folder will be parsed and a ZIP file will be generated but the source folder will not be emptied. |

### Prerequisites

Python 3 is needs to be installed to be able to run this script.