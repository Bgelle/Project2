# # Develop the prototype-->
import os
# query = input("Which drive you have to open ? C , D or E: \n")
#
# # Check the condition for
# # opening the C drive
# if "C" in query or "c" in query:
#     os.startfile("C:")
# elif "D" in query or "d" in query:
#     os.startfile("D:")
# elif "E" in query or "e" in query:
#     os.startfile("E:")
# else:
#     print("Wrong Input")

class FileOperations():
    # 1.Get all the files and directory in the System Drive
    def GetFiles(path):
        print("Python Program to print list the files in a directory.")
        print(f"Files in the directory: {path}")
        files = os.listdir(path)
        # Filtering only the files.
        print(files)
        #files = [f for f in files if (os.path.isfile(path + '/' + f) or os.path.isdir(f))]
        print(*files, sep="\n")

    # 2.Delete the Given Directory/File given by user in given drive
    def DeleteFile(path,filename):
        file=os.path.join(path,filename)
        os.remove(file)
        print(f"{file}File removed")

    # 3.Write the File in to the Given TARGET Directory and content must be taken
    # from user
    def WriteFile(path, filename, content):
        file=os.path.join(path,filename)
        with open(file, "w") as f:
            f.writelines(content)

    # 4.Create the Directory under the given drive
    def Create_Directory(path, filename):
        file=os.path.join(path,filename)
        try:
            os.mkdir(file)
            print("Directory Created")
        except:
            print("Directory aleady exists")

    # 5.Read the user given file from the given directory

    def ReadFile(path, filename):
        file=os.path.join(path,filename)
        with open(file, "r") as f:
            content = f.read()
            print(content)


#FileOperations.GetFiles(path=input("Enter the path))
#FileOperations.DeleteFile(path=input("Enter the path"),filename=input("Enter the filename"))
#FileOperations.WriteFile(path=input("Enter the path"),filename=input("Enter filename),content=input("Enter Content))
#FileOperations.ReadFile(path=input("Enter path"), filename=input("Enter filename"))
#FileOperations.Create_Directory(path=input("Enter path"), filename=input("Enter filename"))




