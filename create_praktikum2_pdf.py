import pymupdf

input_pdf = "Praktikum2_UIUX_WahyuSuryaPratamaaaaa.pdf"
output_pdf = "Praktikum2_UIUX_AbdullahMuhammadAshShiddiq.pdf"

doc = pymupdf.open(input_pdf)

# ----------------- PAGE 0: COVER -----------------
p0 = doc[0]

# Redact entire author and group area down to program studi
rect_author = pymupdf.Rect(100, 470, 512, 710)
p0.add_redact_annot(rect_author, fill=(1, 1, 1))
p0.apply_redactions()

page_w = p0.rect.width
font_bold = "times-bold"
font_roman = "times-roman"

t_disusun = "Disusun Oleh:"
t_nama = "Nama: Abdullah Muhammad Ash Shiddiq"
t_nim = "NIM: 0110226105"
t_kelompok = "Kelompok : 1 (Jadwal Kamis, 13.00-15.30)"

p0.insert_text(pymupdf.Point((page_w - pymupdf.get_text_length(t_disusun, fontname=font_roman, fontsize=12)) / 2, 505), t_disusun, fontname=font_roman, fontsize=12, color=(0, 0, 0))
p0.insert_text(pymupdf.Point((page_w - pymupdf.get_text_length(t_nama, fontname=font_roman, fontsize=12)) / 2, 535), t_nama, fontname=font_roman, fontsize=12, color=(0, 0, 0))
p0.insert_text(pymupdf.Point((page_w - pymupdf.get_text_length(t_nim, fontname=font_roman, fontsize=12)) / 2, 560), t_nim, fontname=font_roman, fontsize=12, color=(0, 0, 0))
p0.insert_text(pymupdf.Point((page_w - pymupdf.get_text_length(t_kelompok, fontname=font_roman, fontsize=11.5)) / 2, 675), t_kelompok, fontname=font_roman, fontsize=11.5, color=(0, 0, 0))

# ----------------- PAGE 1: FORM 1 (BURGER KUSTOM) -----------------
p1 = doc[1]

# Redact title "Form Pemesanan Pizza"
p1.add_redact_annot(pymupdf.Rect(70, 380, 300, 405), fill=(1, 1, 1))
# Redact old image area cleanly
p1.add_redact_annot(pymupdf.Rect(80, 406, 535, 638), fill=(1, 1, 1))
# Redact old link
p1.add_redact_annot(pymupdf.Rect(70, 715, 560, 765), fill=(1, 1, 1))
p1.apply_redactions()

# Insert title
p1.insert_text(pymupdf.Point(71.3, 396), "\u2022 Form Pemesanan Burger Kustom", fontname=font_bold, fontsize=11, color=(0, 0, 0))

# Insert new image without overlapping Analisis Kode Script (y=408 to 634)
rect_img1 = pymupdf.Rect(89.25, 408.0, 525.75, 634.0)
p1.insert_image(rect_img1, filename="laporan_assets/preview_burger_form.png")

# Insert link
url_p2_1 = "https://shiddiq-21.github.io/shiddiq-kelompok-1/praktikum02/index.html"
p1.insert_text(pymupdf.Point(71.3, 730), "\u2022 Link GitHub:", fontname=font_roman, fontsize=10.5, color=(0, 0, 0))
p1.insert_text(pymupdf.Point(155, 730), url_p2_1, fontname=font_roman, fontsize=9.5, color=(0, 0.2, 0.7))
p1.insert_link({"kind": pymupdf.LINK_URI, "from": pymupdf.Rect(155, 720, 550, 735), "uri": url_p2_1})

# ----------------- PAGE 2: FORM 2 (HASIL BURGER) -----------------
p2 = doc[2]

# Redact top note and title
p2.add_redact_annot(pymupdf.Rect(70, 65, 560, 150), fill=(1, 1, 1))
# Redact image
rect_img2 = pymupdf.Rect(68.4, 153.86, 515.4, 405.11)
p2.add_redact_annot(pymupdf.Rect(65, 150, 520, 410), fill=(1, 1, 1))
# Redact analysis text & links & bottom note
p2.add_redact_annot(pymupdf.Rect(70, 430, 560, 560), fill=(1, 1, 1))
p2.apply_redactions()

# Insert top text
p2.insert_text(pymupdf.Point(71.3, 80), "\u2022 Informasi pemesanan burger pelanggan terletak di dalam tag <fieldset>, terdapat nama, alamat,", fontname=font_roman, fontsize=10.5, color=(0, 0, 0))
p2.insert_text(pymupdf.Point(82.0, 95), "nomor telepon, email, dan instruksi pengiriman.", fontname=font_roman, fontsize=10.5, color=(0, 0, 0))
p2.insert_text(pymupdf.Point(71.3, 130), "\u2022 Form Hasil Pemesanan Burger Kustom", fontname=font_bold, fontsize=11, color=(0, 0, 0))

# Insert image
p2.insert_image(rect_img2, filename="laporan_assets/preview_burger_hasil.png")

# Insert analysis & links
p2.insert_text(pymupdf.Point(71.3, 445), "\u2022 Menggunakan struktur HTML5 (<h1>, <fieldset>, <strong>, <blockquote>) untuk membuat", fontname=font_roman, fontsize=10.5, color=(0, 0, 0))
p2.insert_text(pymupdf.Point(82.0, 460), "format hasil pemesanan burger.", fontname=font_roman, fontsize=10.5, color=(0, 0, 0))

url_p2_2 = "https://shiddiq-21.github.io/shiddiq-kelompok-1/praktikum02/hasil.html"
p2.insert_text(pymupdf.Point(71.3, 485), "\u2022 Link GitHub:", fontname=font_roman, fontsize=10.5, color=(0, 0, 0))
p2.insert_text(pymupdf.Point(155, 485), url_p2_2, fontname=font_roman, fontsize=9.5, color=(0, 0.2, 0.7))
p2.insert_link({"kind": pymupdf.LINK_URI, "from": pymupdf.Rect(155, 475, 550, 490), "uri": url_p2_2})

p2.insert_text(pymupdf.Point(71.3, 520), "\u2022 Informasi data pemesanan burger terletak di dalam tag <fieldset>, terdapat data pemesan,", fontname=font_roman, fontsize=10.5, color=(0, 0, 0))
p2.insert_text(pymupdf.Point(82.0, 535), "pilihan varian burger, topping tambahan, dan jumlah kuantitas pesanan.", fontname=font_roman, fontsize=10.5, color=(0, 0, 0))

# ----------------- PAGE 3: MANDIRI 1 (FORM BARANG SPORTX) -----------------
p3 = doc[3]

# Redact image
rect_img3 = pymupdf.Rect(68.4, 130.62, 497.61, 371.87)
p3.add_redact_annot(pymupdf.Rect(65, 125, 505, 375), fill=(1, 1, 1))
# Redact links
p3.add_redact_annot(pymupdf.Rect(70, 475, 560, 530), fill=(1, 1, 1))
p3.apply_redactions()

# Insert image
p3.insert_image(rect_img3, filename="laporan_assets/preview_sportx_form.png")

# Insert link
url_m2_1 = "https://shiddiq-21.github.io/shiddiq-kelompok-1/praktikummandiri02/pesananbarang.html"
p3.insert_text(pymupdf.Point(71.3, 490), "\u2022 Link GitHub:", fontname=font_roman, fontsize=10.5, color=(0, 0, 0))
p3.insert_text(pymupdf.Point(155, 490), url_m2_1, fontname=font_roman, fontsize=9, color=(0, 0.2, 0.7))
p3.insert_link({"kind": pymupdf.LINK_URI, "from": pymupdf.Rect(155, 480, 560, 495), "uri": url_m2_1})

# ----------------- PAGE 4: MANDIRI 2 (HASIL BARANG SPORTX) & KESIMPULAN -----------------
p4 = doc[4]

# Redact image
rect_img4 = pymupdf.Rect(68.4, 127.69, 493.96, 366.89)
p4.add_redact_annot(pymupdf.Rect(65, 105, 505, 370), fill=(1, 1, 1))
# Redact links
p4.add_redact_annot(pymupdf.Rect(70, 480, 560, 535), fill=(1, 1, 1))
p4.apply_redactions()

# Insert title
p4.insert_text(pymupdf.Point(71.3, 118), "\u2022 Form Hasil Pembelian Barang", fontname=font_bold, fontsize=11, color=(0, 0, 0))

# Insert image
p4.insert_image(rect_img4, filename="laporan_assets/preview_sportx_hasil.png")

# Insert link
url_m2_2 = "https://shiddiq-21.github.io/shiddiq-kelompok-1/praktikummandiri02/hasil_pesananbarang.html"
p4.insert_text(pymupdf.Point(71.3, 495), "\u2022 Link GitHub:", fontname=font_roman, fontsize=10.5, color=(0, 0, 0))
p4.insert_text(pymupdf.Point(155, 495), url_m2_2, fontname=font_roman, fontsize=8.8, color=(0, 0.2, 0.7))
p4.insert_link({"kind": pymupdf.LINK_URI, "from": pymupdf.Rect(155, 485, 560, 500), "uri": url_m2_2})

# Save output
doc.save(output_pdf, deflate=True)
doc.close()

print("Successfully regenerated perfect Praktikum 2 PDF:", output_pdf)
