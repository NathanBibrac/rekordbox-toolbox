```markdown
# Rekordbox Playlist Structure Generator

A Python script for creating a Rekordbox Playlist tree structure based on a given XML file.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
- [Functionality](#functionality)
  - [Timestamp Functions](#timestamp-functions)
  - [Argument Parsing](#argument-parsing)
  - [Utility Functions](#utility-functions)
  - [XML Parsing and Playlist Generation](#xml-parsing-and-playlist-generation)
  - [Data Mapping and DataFrame Creation](#data-mapping-and-dataframe-creation)
  - [Playlist Structure Creation](#playlist-structure-creation)
  - [Track Copying](#track-copying)
  - [Main Function](#main-function)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This Python script automates the creation of a Rekordbox Playlist tree structure, streamlining the process of organizing tracks based on a provided XML file. It includes functionalities to parse XML, map tracks to playlists, and copy tracks to specified target directories.

## Features

- XML parsing and playlist extraction
- Mapping tracks to playlists
- Creating a DataFrame structure
- Merging track and playlist information
- Copying tracks to specified target directories
- Excel file generation for playlist structure

## Getting Started

### Prerequisites

- Python 3.x
- [lxml](https://lxml.de/)
- [pandas](https://pandas.pydata.org/)
- [colorama](https://pypi.org/project/colorama/)

You can install the required packages using:

```bash
pip install lxml pandas colorama
```

### Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/rekordbox-playlist-generator.git
```

2. Navigate to the project directory:

```bash
cd rekordbox-playlist-generator
```

### Usage

```bash
python playlist_generator.py <xml_source> <target> <mode>
```

- `xml_source`: Path to the Rekordbox XML file.
- `target`: Target directory for playlist structure or track copying.
- `mode`: Operation mode (excel or exec).

## Functionality

### Timestamp Functions

- `ts_str()`: Returns the current timestamp in a specific format.
- `ts_log()`: Returns the current timestamp in a log-friendly format.

### Argument Parsing

- `get_args()`: Uses argparse to parse command-line arguments.

...

## Contributing

Contributions are welcome! Please check the [Contributing Guidelines](CONTRIBUTING.md) for more details.

## License

This project is licensed under the [MIT License](LICENSE).
```

Replace the placeholders like `<your-username>` with your GitHub username, and make sure to create a `LICENSE` file and a `CONTRIBUTING.md` file if needed. Feel free to add more sections or details based on the specific requirements of your project.# rekordbox-toolbox
