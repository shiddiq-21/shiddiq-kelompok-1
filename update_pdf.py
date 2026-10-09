import pymupdf

input_pdf = "Tugas Wahyu Surya Pratama UIUX NIM 0110226058.pdf"
output_pdf = "Tugas Abdullah Muhammad Ash Shiddiq UIUX NIM 0110226105.pdf"

doc = pymupdf.open(input_pdf)

# ----------------- PAGE 0: COVER -----------------
p0 = doc[0]

# Redact Wahyu's name and Kelompok 20
rect_name = pymupdf.Rect(120, 436, 490, 462)
rect_group = pymupdf.Rect(120, 482, 490, 510)

p0.add_redact_annot(rect_name, fill=(1, 1, 1))
p0.add_redact_annot(rect_group, fill=(1, 1, 1))
p0.apply_redactions()

font_bold = "times-bold"
font_size = 11.5

name_text = "Abdullah Muhammad Ash Shiddiq - 0110226105"
group_text = "Kelompok : 1 (Jadwal Kamis, 13.00-15.30)"

page_width = p0.rect.width
name_width = pymupdf.get_text_length(name_text, fontname=font_bold, fontsize=font_size)
group_width = pymupdf.get_text_length(group_text, fontname=font_bold, fontsize=font_size)

p0.insert_text(
    pymupdf.Point((page_width - name_width) / 2, 452),
    name_text,
    fontname=font_bold,
    fontsize=font_size,
    color=(0, 0, 0)
)

p0.insert_text(
    pymupdf.Point((page_width - group_width) / 2, 498),
    group_text,
    fontname=font_bold,
    fontsize=font_size,
    color=(0, 0, 0)
)

# ----------------- PAGE 1: D. LAPORAN PRAKTIKUM -----------------
p1 = doc[1]

# Redact the old screenshot completely
p1.add_redact_annot(pymupdf.Rect(70, 475, 545, 765), fill=(1, 1, 1))
p1.apply_redactions()

# Explicitly re-insert "D. Laporan Praktikum" in bold
p1.insert_text(
    pymupdf.Point(71.8, 490),
    "D. Laporan Praktikum",
    fontname="times-bold",
    fontsize=11.5,
    color=(0, 0, 0)
)

# Insert screenshot 1 below heading
rect_img1 = pymupdf.Rect(72.05, 500.0, 538.47, 760.0)
p1.insert_image(rect_img1, filename="laporan_assets/screenshot_praktikum01.png")

# ----------------- PAGE 2: E. PRAKTIKUM MANDIRI & F. KESIMPULAN -----------------
p2 = doc[2]

# Redact old image
p2.add_redact_annot(pymupdf.Rect(70, 88, 565, 370), fill=(1, 1, 1))

# Redact ENTIRE old section F area including old "F. Kesimpulan" text and old links
p2.add_redact_annot(pymupdf.Rect(65, 395, 565, 520), fill=(1, 1, 1))
p2.apply_redactions()

# Insert new screenshot 2
rect_img2 = pymupdf.Rect(72.0, 91.24, 561.1, 365.39)
p2.insert_image(rect_img2, filename="laporan_assets/screenshot_praktikummandiri01.png")

# Re-insert F. Kesimpulan & Links cleanly without overlap
p2.insert_text(pymupdf.Point(71.8, 412), "F. Kesimpulan", fontname="times-bold", fontsize=11.5, color=(0, 0, 0))

repo_label = "- Link Repository :"
repo_url = "https://github.com/shiddiq-21/shiddiq-kelompok-1"
web_label = "- Link Website GitHub:"
web_url = "https://shiddiq-21.github.io/shiddiq-kelompok-1/praktikummandiri01/kelompok_1_desainuiux_pemweb.html"

# Write repo
p2.insert_text(pymupdf.Point(89.3, 430), repo_label, fontname="times-roman", fontsize=11, color=(0, 0, 0))
repo_rect = pymupdf.Rect(95, 435, 450, 449)
p2.insert_text(pymupdf.Point(95, 445), repo_url, fontname="times-roman", fontsize=10.5, color=(0, 0.2, 0.7))
p2.insert_link({"kind": pymupdf.LINK_URI, "from": repo_rect, "uri": repo_url})

# Write website
p2.insert_text(pymupdf.Point(89.3, 464), web_label, fontname="times-roman", fontsize=11, color=(0, 0, 0))
web_rect = pymupdf.Rect(95, 469, 560, 483)
p2.insert_text(pymupdf.Point(95, 479), web_url, fontname="times-roman", fontsize=9.2, color=(0, 0.2, 0.7))
p2.insert_link({"kind": pymupdf.LINK_URI, "from": web_rect, "uri": web_url})

# Save output
doc.save(output_pdf, deflate=True)
doc.close()

print("Successfully regenerated:", output_pdf)
