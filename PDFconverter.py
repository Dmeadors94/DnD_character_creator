import pdfrw
pdfrw.__version__
'0.4'
# Setting Variables for character sheet
playername = "Dillon"
charactername = "Onmius"
# Let's first set some variable to reference our PDF template and output.pdf
pdf_template = "template.pdf"
pdf_output = "output.pdf"

template_pdf = pdfrw.PdfReader(pdf_template)  # create a pdfrw object from our template.pdf
# template_pdf  # uncomment to see all the data captured from this PDF.

ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'

#for page in template_pdf.pages:
    #annotations = page[ANNOT_KEY]
    #for annotation in annotations:
        #if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
            #if annotation[ANNOT_FIELD_KEY]:
                #key = annotation[ANNOT_FIELD_KEY][1:-1]
                #print(key)
data_dict = {
    'ClassLevel': dndclass,
    'PlayerName': playername,
    'CharacterName': charactername,
    'Race ': race,
    'STR': strength,
    'DEX': dexterity,
    'CON': constitution,
    'INT': intelligence,
    'WIS': wisdom,
    'CHA': charisma,
}

def fill_pdf(input_pdf_path, output_pdf_path, data_dict):
    template_pdf = pdfrw.PdfReader(input_pdf_path)
    for page in template_pdf.pages:
        annotations = page[ANNOT_KEY]
        for annotation in annotations:
            if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
                if annotation[ANNOT_FIELD_KEY]:
                    key = annotation[ANNOT_FIELD_KEY][1:-1]
                    if key in data_dict.keys():
                        if type(data_dict[key]) == bool:
                            if data_dict[key] == True:
                                annotation.update(pdfrw.PdfDict(
                                    AS=pdfrw.PdfName('Yes')))
                        else:
                            annotation.update(
                                pdfrw.PdfDict(V='{}'.format(data_dict[key]))
                            )
                            annotation.update(pdfrw.PdfDict(AP=''))
    template_pdf.Root.AcroForm.update(pdfrw.PdfDict(NeedAppearances=pdfrw.PdfObject('true')))  # NEW
    pdfrw.PdfWriter().write(output_pdf_path, template_pdf)
