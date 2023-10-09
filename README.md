# File Organizer

Author: Zanderskier
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
```

## Automation (Windows)

If you're using this program on a Windows machine and want to automate its execution, consider following these steps:

1. **Convert to .exe using PyInstaller**: You can convert the Python script `file_organizer.py` into a standalone executable (.exe) file using a tool like [PyInstaller](https://www.pyinstaller.org/). This will make it easier to run the program without needing to open a terminal or command prompt each time.

   To do this, open a command prompt or terminal and navigate to the directory containing `file_organizer.py`. Then, run the following command (make sure you have PyInstaller installed):

   ```bash
   pyinstaller --onefile file_organizer.py
   ```
This command will generate a standalone .exe file in the dist directory within your project folder.

Set Up Task Scheduler: After converting the script to an .exe file, you can use Windows Task Scheduler to automate the program's execution at specified intervals.

Search for "Task Scheduler" in the Windows Start menu and open it.
In the Task Scheduler, create a new task and configure it to run the .exe file you generated in step 1. You can set the task to run daily, weekly, or at any desired interval.
Make sure to configure the task with appropriate permissions and triggers based on your requirements.
By following these steps, you can automate the file organization process on your Windows machine, ensuring that files in your specified directory are sorted into their respective categories automatically.
