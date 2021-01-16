import dropbox
import os
class TransferData():
    def __init__(self,aT):
        self.aT = aT
    def uploadFiles(self,fileFrom, fileTo):
        dbx = dropbox.Dropbox(self.aT)
        f = open(fileFrom, 'rb')
        dbx.files_upload(f.read(), fileTo)

def main():
    accessToken = "N3vEZUcLqTIAAAAAAAAAATW9l5Z5y1uPyOwdbCqJPpdX7vsbt1WkwnoKr4XYSdDf"
    file1 = TransferData(accessToken)
    file_from = input("Enter path here: ")
    fileTo = input("Enter the path of the file to which you want to transfer the data: ")
    for root, dirs, files in os.walk(file_from):
        for file in files:
            path = (file_from + "\\" + file)
            print("path",path)
            relPath = os.path.relpath(path,file_from)
            print(relPath)
            dbPath = os.path.join(fileTo,relPath)
            print("dbPath",dbPath)
            file1.uploadFiles(dbPath,fileTo)
main()