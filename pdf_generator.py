from flask import Flask, send_file
from reportlab.pdfgen import canvas
from io import BytesIO

app = Flask(__name__)

@app.route('/generate_offer_letter')
def generate_offer_letter():
    buffer = BytesIO()
    p = canvas.Canvas(buffer)

    # Sample Data
    name = "Rakshitha"
    domain = "Artificial Intelligence"
    duration = "1 Month"
    issue_date = "June 15, 2025"

    # PDF Content
    p.setFont("Helvetica-Bold", 16)
    p.drawString(100, 800, "Internship Offer Letter")
    p.setFont("Helvetica", 12)
    p.drawString(100, 760, f"Name: {name}")
    p.drawString(100, 740, f"Internship Domain: {domain}")
    p.drawString(100, 720, f"Duration: {duration}")
    p.drawString(100, 700, f"Issue Date: {issue_date}")
    p.showPage()
    p.save()

    buffer.seek(0)

    return send_file(buffer, mimetype='application/pdf', as_attachment=False, download_name="offer_letter.pdf")

if __name__ == '__main__':
    app.run(debug=True)
