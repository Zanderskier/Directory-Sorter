# File Organizer

Author: Alex Fails
Date: 30th November 2022
Purpose: This Python program automates the organization of files in a specified folder by sorting them into different categories.

## Description

This program is designed to help you keep your files organized by sorting them into different directories based on their file extensions. It can automatically categorize files into the following categories:

- Documents
- Images
- Videos
- Software
- Compressed files (ZIP)

The program checks the extensions of each file in the specified folder and moves them to the corresponding category directory. If a file with the same name already exists in the destination directory, it renames the file to make it unique.

## Prerequisites

Before running the program, make sure you have Python installed on your system.

## Usage

1. Clone this repository to your local machine.

2. Open a terminal and navigate to the directory where you cloned the repository.

3. Edit the `main()` function in the `file_organizer.py` file to specify the root directory you want to organize.

4. Run the program by executing the following command:

```bash
python file_organizer.py

