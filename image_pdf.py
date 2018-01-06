#!/usr/bin/python3
from fpdf import FPDF
from PIL import Image
import os


def get_files(rmScriptName=True, filter=""):
    try:
        os.chdir(os.path.dirname(__file__))
    except:
        os.path.dirname(os.path.abspath(__file__))
    pathAbs = os.getcwd()
    files = os.listdir()
    if rmScriptName:
        scriptName = os.path.basename(__file__)
        files.remove(scriptName)
    if filter:
        filtered = []
        for file in files:
            if filter in file:
                filtered.append(file)
        return filtered
    return files


def make_pdf(fileName, listPages):
    pdf = FPDF(orientation="L")
    for image in listPages:
        pdf.add_page()
        cover = Image.open(image)
        width, height = cover.size
        pdf.image(image, 10, 20, width/4, height/4)
    pdf.output(fileName, "F")


if __name__=="__main__":
    imageList = get_files(True, ".png")
    imageList.sort()
    print(imageList)
    make_pdf("2-6.01.18_temp.pdf", imageList)

