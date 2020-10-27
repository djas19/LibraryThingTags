# LibraryThingTagScraper

This is a small Python script created to unzip all zip files in a specified directory and merge the content into a newly created ZIP file.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

To run the script simply execute the run.py file without any parameters. This will look for a folder `./testData` unzip all zip folders in this folder and copy them to a temporary folder called `./tempUnzipped`. This folder will be deleted at the end of the script.
After unzipping everything a reZip wil happen where the content of `./tempUnzipped` will be zipped to a newly created ZIP file.
this zip file will by default be created according to the following specs/pattern:

File nomenclature:
CODAZOOM-XXX-YYYYMMDD-HHMMSS.ZIP
- Where :
  - XXX : trigram identifying the flow (DDE, DIE, DOE or DUE)
  - YYYYMMDD : date
  - HHMMSS : 
- timeExamples :
  - CODAZOOM-DDE-20180227-134059.ZIP
  - CODAZOOM-DUE-20180227-031507.ZIP

After zipping all processed files will be moved to an archive folder `./archive`
### Parameters

| parameter     | default value                                            | explanation                                                                                                                                                |
|---------------|----------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| --source      | ./testData                                               | Location of the folder containing all zip files to be processed.                                                                                           |
| --destination | CODAZOOM-DDE-{datetime.datetime.now():%Y%m%d-%H%M%S}.ZIP | Name of the resulting ZIP file.                                                                                                                            |
| --archive     | ./archive                                                | Location of the folder where all processed ZIP files will be moved to.                                                                                     |
| --dry_run     | false                                                    | When this parameter is present the content of the source folder will be parsed and a ZIP file will be generated but the source folder will not be emptied. |

### Prerequisites

Python 3 is needs to be installed to be able to run this script.

## Running tests

To do a test run the following command can be used:
`run.py --dry_run`