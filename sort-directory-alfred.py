'''
Author: Alex Fails
Date: 30112022 ddmmyyyy
Purpose: This program will automate file organization of the specified folder
'''

# required modules
import os
import shutil

# The below class defines different file extensions for various categories of files.
class autoSortDir:
    # file extentions for all cadigories
    image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif",
                        ".psd", ".raw", ".arw", ".cr2", ".nrw",
                        ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf",
                        ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]
    video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                        ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]
    document_extensions = [".doc", ".docx", ".odt",
                           ".pdf", ".xls", ".xlsx", ".ppt", ".pptx", ".pptm", ".txt"]
    software_extensions = ['.exe', '.dmg', '.pkg', '.bat']
    zip_extentions = ['.zip', '.stix', '.7z', '.7zip', '.gzip', '.arj', '.deb', '.pkg', '.rar', '.rpm', '.tar.gz', '.z']

    #default permisions for creating a directory
    mode = 0o666

    #class var for specified directory locations
    def __init__(self, root_dir):
        """
        The function initializes directories for sorting different types of files in a given root directory.
        
        :param root_dir: The `root_dir` parameter is the root directory where all the files will be sorted
        into different subdirectories
        """
        self.root_dir = root_dir
        self.documents_dir = root_dir + "/01_auto_sorted_documents"
        self.images_dir = root_dir + "/02_auto_sorted_images"
        self.video_dir = root_dir + "/03_auto_sorted_video"
        self.software_dir = root_dir + "/04_auto_sorted_software"
        self.zip_dir = root_dir + "/05_auto_sorted_zip"
        self.other_dir = root_dir + "/06_auto_sorted_other"

    # checks for sorting directories
    def checkSortingDir(self):
        """
        The function checks if specific directories exist and creates them if they don't.
        """
        if os.path.exists(self.documents_dir) != True:
            os.mkdir(self.documents_dir, self.mode)
        if os.path.exists(self.images_dir) != True:
            os.mkdir(self.images_dir, self.mode)
        if os.path.exists(self.video_dir) != True:
            os.mkdir(self.video_dir, self.mode)
        if os.path.exists(self.software_dir) != True:
            os.mkdir(self.software_dir, self.mode)
        if os.path.exists(self.zip_dir) != True:
            os.mkdir(self.zip_dir, self.mode)
        if os.path.exists(self.other_dir) != True:
            os.mkdir(self.other_dir, self.mode)

    # make duplicate files have a unique name
    def make_unique(self, dest, name):
        """
        The `make_unique` function takes a destination directory and a filename as input, and returns a
        unique filename by appending a number to the end if the file already exists in the destination
        directory.
        
        :param dest: The `dest` parameter is the destination directory where the file will be saved
        :param name: The `name` parameter is the original name of the file
        :return: the updated name of the file, which is made unique by adding a number to the end if a file
        with the same name already exists in the destination directory.
        """
        filename, extension = os.path.splitext(name)
        counter = 1
        # * IF FILE EXISTS, ADDS NUMBER TO THE END OF THE FILENAME
        while os.path.exists(f"{dest}/{name}"):
            name = f"{filename}({str(counter)}){extension}"
            counter += 1

        return name

    #moves files once they are checked for duplicate names
    def move_file(self, dest, entry, name):
        """
        The function moves a file to a specified destination, and if a file with the same name already
        exists in the destination, it renames the file to make it unique before moving it.
        
        :param dest: The destination directory where the file will be moved to
        :param entry: The `entry` parameter represents the source file or directory that you want to move.
        It can be a file path or a directory path
        :param name: The `name` parameter represents the name of the file that needs to be moved
        """
        if os.path.exists(f"{dest}/{name}"):
            unique_name = self.make_unique(dest, name)
            oldName = os.path.join(dest, name)
            newName = os.path.join(dest, unique_name)
            os.rename(oldName, newName)
        shutil.move(entry, dest)

    #sorts all files in root directory once checkSortingDir creates sorting directories
    def sortFiles(self):
        """
        The `sortFiles` function sorts files into different directories based on their file extensions.
        """

        self.checkSortingDir()

        with os.scandir(self.root_dir) as files:
            for file in files:
                name = file.name
                split = os.path.splitext(file)
                if os.path.isfile(file) and split[1] in self.document_extensions and not os.path.isdir(file) and not split[0].startswith('.'):
                    self.move_file(self.documents_dir, file, name)
                elif os.path.isfile(file) and split[1] in self.image_extensions and not os.path.isdir(file) and not split[0].startswith('.'):
                    self.move_file(self.images_dir, file, name)
                elif os.path.isfile(file) and split[1] in self.video_extensions and not os.path.isdir(file) and not split[0].startswith('.'):
                    self.move_file(self.video_dir, file, name)
                elif os.path.isfile(file) and split[1] in self.software_extensions and not os.path.isdir(file) and not split[0].startswith('.'):
                    self.move_file(self.software_dir, file, name)
                elif os.path.isfile(file) and split[1] in self.zip_extentions and not os.path.isdir(file) and not split[0].startswith('.'):
                    self.move_file(self.zip_dir, file, name)
                elif not os.path.isdir(file) and not split[0].startswith('.'):
                    self.move_file(self.other_dir, file, name)

def inputSanitization(dir):
    """
    The function checks if a directory exists and returns True if it does, and False otherwise.
    
    :param dir: The `dir` parameter is a string that represents a directory location
    :return: a boolean value. If the directory location does not exist, it returns False. Otherwise, it
    returns True.
    """
    if os.path.exists(dir) == False:
        print("\nInvalid Directory Location")
        return False
    else:
        return True

######################### MAIN #########################
def main():
    """
    The main function sets the root directory for file sorting and calls the necessary functions to
    sanitize the input and sort the files.
    """

    # CHANGE TO THE DESIRED DIRECTORY PATH TO SORT
    root_dir = "C:\\Users\Downloads"

    if inputSanitization(root_dir) == True:
        sorter = autoSortDir(root_dir)
        sorter.sortFiles()


if __name__ == "__main__":
    main()
