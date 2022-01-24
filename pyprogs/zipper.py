from zipfile import ZipFile
import os
import functions as func


with ZipFile('./IMG/Output.zip', 'w') as zipObj:
    os.chdir("./SVG/")
    zipObj.write('Canvas.svg')
    os.chdir("./../")
    os.chdir("./PNG/")
    zipObj.write('output_.png')
    os.chdir("./../") 
    for folderName, subfolders, filenames in os.walk("./unplaced"):
        for filename in filenames:
            filePath = os.path.join(folderName, filename)
            zipObj.write(filePath)
    func.pushNotification("Zip File Created")
    