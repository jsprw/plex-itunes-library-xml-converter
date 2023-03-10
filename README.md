# `iTunes Library.xml` special character converter for Plex on Windows

In Plex you can import your playlist, plays and rating from `iTunes Library.xml`. However, Plex has a bug where it reads special characters incorrectly. After investigating, it seems that Plex reads UTF-8 url-encoded characters as Windows-1252. This script will convert all UTF-8 url-encoded paths to Windows-1252 url-encoded paths. 

> Windows-1252's charset is not as big as the UTF-8 charset so it may happen that some characters won't be encoded. These characters will be shown as a warning. A solution for this is renaming the files so they don't contain these characters.

## Installation

This script requires Python 3.

1. Clone this github repo.
2. [Install `lxml`.](https://lxml.de/installation.html)

## Usage

This script is non-destructive: it will generate a new file after each succesful run. This means that everytime the original `iTunes Library.xml` changes, this script must be run to reflect the changes in the converted file. 

Furthermore, in Plex, the setting `iTunes library XML path` (under `Settings` > `Plugins`) must be pointed to the converted file.

```python
# python3 converter.py "iTunes Library.xml" "iTunes Library converted.xml"

python3 converter.py <input path> <output path>
```

