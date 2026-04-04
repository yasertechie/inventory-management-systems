from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def generate_purchase_order(product):
    filename = f"purchase_order_{product.id}.pdf"
    filepath = os.path.join("media", filename)

    # Ensure media folder exists
    os.makedirs("media", exist_ok=True)

    c = canvas.Canvas(filepath, pagesize=letter)

    c.drawString(100, 750, "Purchase Order")
    c.drawString(100, 700, f"Product: {product.name}")
    c.drawString(100, 670, f"Quantity: {product.low_stock_limit * 2}")
    c.drawString(100, 640, f"Vendor Email: {product.vendor_email}")

    c.save()

    return filepath