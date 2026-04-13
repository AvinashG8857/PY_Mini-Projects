from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf(receipt_id,name,item,amount,date):
    filename= f"reciept_{receipt_id}.pdf"

    c= canvas.Canvas(filename,pagesize=letter)

    #add bold title

    c.setFont("Helvetica-Bold", 20)
    c.drawString(200,750,"OFFICIAL RECEIPT")


    #add Transaction details
    c.setFont("Helvetica", 12)
    c.drawString(50,700,f"Receipt Id: {receipt_id}")
    c.drawString(50,680,f"Date:{date}")
    c.drawString(50,650,f"Customer:{name}")

    #add linbe
    c.line(50,640,550,640)

    #items
    c.drawString(50,610,f"Description:{item}")

    #total price
    c.setFont("Helvetica-Bold",14)

    c.drawString(50,580,f"Total Amount Paid: ${amount:.2f}")

    c.showPage()
    c.save()

    return filename

