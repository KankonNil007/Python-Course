# Shutil Module in Python

import shutil as sh
import os

sh.copy("087-Shutil-Module/main.md", "087-Shutil-Module/tutorial.md") # Makes a copy of that file in a certain destination

sh.copytree("087-Shutil-Module", "087-Shutil-Module2") # Copies a whole directory with the files and pastes it in a certain location

sh.move("087-Shutil-Module/main.md", "exercise.md") # Moves a file in a certain destination

sh.rmtree("087-Shutil-Module2") # Deletes a whole directory with their files

os.remove("exercise.md") # Deletes a file

os.rename("087-Shutil-Module/tutorial.md", "087-Shutil-Module/main.md") # Renames a file