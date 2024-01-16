  ## Description
    The Rekordbox Toolbox is a Python script that creates a playlist tree structure based on a Rekordbox XML file. It allows you to generate an Excel file with the playlist structure or create the playlist structure in a target directory.

    ## Features
    - Parse XML file
    - Get playlist list from XML
    - Map tracks to playlists
    - Get tracks from XML
    - Merge tracks and playlists
    - Copy tracks to the target directory

    ## Requirements
    - Python 3.x
    - lxml library
    - pandas library
    - argparse library
    - colorama library

    ## Usage
    1. Install the required libraries by running the following command:
         ```
         pip install lxml pandas argparse colorama
         ```

    2. Run the script with the following command:
         ```
         python rpe_tool.py xml_source target mode
         ```
         - `xml_source`: Path to the Rekordbox XML file.
         - `target`: Target directory where the playlist structure will be created.
         - `mode`: Execution mode. Use "excel" to generate an Excel file or "exec" to create the playlist structure in the target directory.

    3. The script will generate the playlist structure based on the provided XML file and save it either as an Excel file or in the target directory.

    ## Examples
    - Generate an Excel file with the playlist structure:
        ```
        python rpe_tool.py /path/to/xml_file.xml /path/to/target_directory excel
        ```

    - Create the playlist structure in the target directory:
        ```
        python rpe_tool.py /path/to/xml_file.xml /path/to/target_directory exec
        ```

    ## A juste titre.
    ## __XNIHILO__
