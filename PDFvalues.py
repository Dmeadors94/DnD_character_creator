import pdfrw
pdfrw.__version__
'0.4'
# Let's first set some variable to reference our PDF template and output.pdf
pdf_template = "template.pdf"
pdf_output = "output.pdf"

template_pdf = pdfrw.PdfReader(pdf_template)  # create a pdfrw object from our template.pdf
#print(template_pdf)  # uncomment to see all the data captured from this PDF.

ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'

for page in template_pdf.pages:
    annotations = page[ANNOT_KEY]
    for annotation in annotations:
        if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
            if annotation[ANNOT_FIELD_KEY]:
                key = annotation[ANNOT_FIELD_KEY][1:-1]
                print(key)
