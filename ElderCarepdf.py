from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pdfrw import PdfReader, PdfWriter, PdfDict, PdfName

def create_fillable_pdf(output_path):
    c = canvas.Canvas("temp.pdf", pagesize=letter)
    width, height = letter

    # Draw title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "AI Companion for Seniors - Survey")

    # Question 1: Age Group (Radio buttons)
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 90, "1. What is your age group?")
    age_options = ["Under 50", "50-64", "65-74", "75+"]
    y = height - 110
    for i, option in enumerate(age_options):
        c.drawString(70, y - i * 20, option)

    # Question 2: Use digital assistant (Checkbox)
    c.drawString(50, y - 100, "2. Do you currently use any digital assistant (e.g., Alexa, Siri)?")

    # Add instructions for fillable fields
    c.drawString(50, y - 130, "Please fill in the form fields with Adobe Acrobat Reader or any PDF reader that supports forms.")

    c.save()

    # Add form fields with pdfrw
    ANNOT_KEY = '/Annots'
    ANNOT_FIELD_KEY = '/T'
    ANNOT_RECT_KEY = '/Rect'
    ANNOT_TYPE_KEY = '/FT'
    ANNOT_SUBTYPE_KEY = '/Subtype'
    WIDGET_SUBTYPE_KEY = '/Widget'
    ANNOT_FLAGS_KEY = '/Ff'

    pdf = PdfReader("temp.pdf")
    page = pdf.pages[0]

    if ANNOT_KEY not in page:
        page[PdfName('Annots')] = []

    def add_textfield(name, rect):
        field = PdfDict(
            FT=PdfName('Tx'),
            Type=PdfName('Annot'),
            Subtype=PdfName('Widget'),
            Rect=rect,
            T=name,
            Ff=1,
            V='',
            DA="/Helv 0 Tf 0 g"
        )
        page[ANNOT_KEY].append(field)

    def add_checkbox(name, rect):
        field = PdfDict(
            FT=PdfName('Btn'),
            Type=PdfName('Annot'),
            Subtype=PdfName('Widget'),
            Rect=rect,
            T=name,
            Ff=1,
            V=PdfName('Off'),
            AS=PdfName('Off'),
            DA="/Helv 0 Tf 0 g"
        )
        page[ANNOT_KEY].append(field)

    def add_radio_group(name, rects, options):
        # Radio buttons are grouped by same field name
        for i, rect in enumerate(rects):
            field = PdfDict(
                FT=PdfName('Btn'),
                Type=PdfName('Annot'),
                Subtype=PdfName('Widget'),
                Rect=rect,
                T=name,
                Ff=32768,  # Radio button flag
                V=PdfName('Off'),
                AS=PdfName('Off'),
                DA="/Helv 0 Tf 0 g",
                # /Opt is not standard, but some readers recognize it
                # We leave values simple for now
            )
            page[ANNOT_KEY].append(field)

    # Example: Add radio buttons for age group next to text
    # Each rect = [xLL, yLL, xUR, yUR]
    # Positions aligned to where the age options were drawn
    age_rects = [
        [50, 700, 65, 715],
        [50, 680, 65, 695],
        [50, 660, 65, 675],
        [50, 640, 65, 655],
    ]
    add_radio_group('age_group', age_rects, ["Under 50", "50-64", "65-74", "75+"])

    # Checkbox example: Yes/No for question 2
    # Place checkboxes next to Yes and No
    add_checkbox('digital_assistant_yes', [50, 580, 65, 595])
    add_checkbox('digital_assistant_no', [100, 580, 115, 595])
    # Add labels manually in PDF if needed

    # Save new PDF
    PdfWriter().write(output_path, pdf)

if __name__ == "__main__":
    create_fillable_pdf("fillable_survey.pdf")
