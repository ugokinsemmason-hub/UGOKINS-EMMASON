import base64, re

files = {
    "COMPANY_LOGO_SRC": "logo.png",       # rename to your logo filename
    "SIGNATURE_SRC":    "signature.png",
    "SEAL_SRC":         "company_seal.jpg",
    # Add footer images like:
    # "FOOTER_0": "product1.jpg",
    # "FOOTER_1": "product2.jpg",
}

with open("ets_invoice.html", "r", encoding="utf-8") as f:
    html = f.read()

for const, filename in files.items():
    try:
        ext = filename.split(".")[-1].upper()
        mime = "image/jpeg" if ext in ["JPG","JPEG"] else "image/png"
        with open(filename, "rb") as img:
            b64 = base64.b64encode(img.read()).decode("utf-8")
        data_uri = f"data:{mime};base64,{b64}"
        html = re.sub(
            rf'(const {const}\s*=\s*)"[^"]*"',
            rf'\1"{data_uri}"',
            html
        )
        print(f"✅ Embedded {filename} into {const}")
    except FileNotFoundError:
        print(f"⚠️  Skipped {filename} (file not found)")

with open("ets_invoice.html", "w", encoding="utf-8") as f:
    f.write(html)

print("\n✅ Done! Open ets_invoice.html in Chrome.")