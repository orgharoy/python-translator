import json
import googletrans
from googletrans import *
from fpdf import FPDF

#getting the strings from the json file
translationFile = open('json.json', 'r')
translateData = translationFile.read()
translateObject = json.loads(translateData)

#initializing the two string variables in this .py document. 
text = (str(translateObject['text']))
languages = translateObject['languages']

#setting up google translate for the translations
translator = Translator()

#setting up the pdf file (only issue that i am currently facing is that the font does not support all the languages of the world.)
#if the program is run with only languages which uses latin alphabets, the program will run.
pdf = FPDF('P', 'mm', 'A4')
pdf.add_page()
pdf.add_font('helvetica_world','','HelveticaWorld-Regular.ttf', True);
pdf.set_font('helvetica_world', '', 16)

#getting the languages from the json file. and then looping through them one by one and translating them as per requirement. 
for lan in languages:
    destLan = str(lan)
    translatedText = translator.translate(text, dest=destLan).text
    
    pdf.multi_cell(0, 5, destLan + '\n\n\n'  + translatedText + '\n\n\n')


pdf.output('output.pdf')