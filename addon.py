import xbmc
import xbmcgui
import xbmcaddon
import sys
import os
import errno
import shutil

__addon__ = xbmcaddon.Addon()
__addonname__ = __addon__.getAddonInfo('name')

def copyFileOrFolder(src, dest):
    print("(src, dest)",src, dest)
    xbmc.executebuiltin("Notification(\"Started Copying ...\", \"%s\")" % sys.listitem.getLabel())

    try:
        shutil.copytree(src, dest)
    except OSError as e:
        if e.errno == errno.ENOTDIR:
            shutil.copy2(src, dest)
        else:
            xbmc.executebuiltin("Notification(\"Directory not copied\", \"%s\")" % e)


def main():
    srcFilePath = sys.listitem.getPath()

    if srcFilePath[len(srcFilePath)-1] == "/":
        srcFilePath = srcFilePath[:len(srcFilePath)-1]
        print("new srcFilePath",srcFilePath)


    fileName = os.path.basename(srcFilePath)

    try:

        dialog = xbmcgui.Dialog()
        destPathOnly = dialog.browseSingle(3, 'Copy file', 'files', '', True, False, '')

        if(srcFilePath != "" and destPathOnly != ""):
            destFilePath = destPathOnly + fileName

            copyFileOrFolder(srcFilePath, destFilePath)
        
            xbmcgui.Dialog().ok(__addonname__, "Copied Sucessfully", fileName)


        

    except Exception as e:
        xbmcgui.Dialog().ok(__addonname__, fileName, "Failed to copy")

        xbmc.executebuiltin("Notification(\"File Copying Error\", \"%s\")" % e)


if __name__ == '__main__':
    main()
