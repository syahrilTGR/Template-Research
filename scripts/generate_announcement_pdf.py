# Copyright 2026 Google LLC
# Licensed under the Apache License, Version 2.0 (the "License");

import os
import sys

try:
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib import colors
except ImportError:
    print("Reportlab not found. Installing and running via uv...")
    sys.exit(1)

def build_pdf():
    pdf_filename = "supportFiles/announcement_v1.0.7.pdf"
    
    # Ensure supportFiles directory exists
    os.makedirs(os.path.dirname(pdf_filename), exist_ok=True)
    
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=letter,
        rightMargin=54,
        leftMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor('#1A365D'),  # Deep dark blue
        spaceAfter=6,
        alignment=1  # Center
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-BoldOblique',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#4A5568'),  # Slate grey
        spaceAfter=15,
        alignment=1
    )

    h1_style = ParagraphStyle(
        'Heading1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=17,
        textColor=colors.HexColor('#2B6CB0'),  # Royal blue
        spaceBefore=14,
        spaceAfter=8,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'Heading2',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=colors.HexColor('#2D3748'),  # Dark grey
        spaceBefore=10,
        spaceAfter=6,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor('#2D3748'),
        spaceAfter=8
    )

    bullet_style = ParagraphStyle(
        'Bullet',
        parent=body_style,
        leftIndent=15,
        firstLineIndent=-10,
        spaceAfter=6
    )

    note_title_style = ParagraphStyle(
        'NoteTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor('#2B6CB0'),
        spaceAfter=4
    )

    note_body_style = ParagraphStyle(
        'NoteBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#2C5282'),
    )

    code_style = ParagraphStyle(
        'Code',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#C53030'),
        spaceAfter=8,
        leftIndent=20
    )

    story = []

    # Title & Subtitle
    story.append(Paragraph("PENGUMUMAN RILIS: Template Research v1.0.7", title_style))
    story.append(Paragraph("Tanggal Rilis: 25 Mei 2026 | Fokus: Academic Search, Sterile Support Guides, & Venv Alignment", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#E2E8F0'), spaceBefore=0, spaceAfter=15))

    # Intro
    intro_text = (
        "Halo Rekan Peneliti! Kami dengan bangga mengumumkan rilis versi <b>v1.0.7</b> "
        "untuk repositori <b>Template Research</b>. Pembaruan kali ini membawa peningkatan fitur luar biasa "
        "yang akan mengubah cara Anda berkolaborasi dengan AI Agent dalam menyusun naskah ilmiah (skripsi/TA) "
        "dan mengekstrak referensi penelitian secara masal."
    )
    story.append(Paragraph(intro_text, body_style))
    story.append(Spacer(1, 10))

    # Section 1: Apa yang Baru
    story.append(Paragraph("Apa yang Baru di v1.0.7?", h1_style))
    
    story.append(Paragraph("1. Integrasi Pencarian Literatur Ilmiah Global (<i>Academic Search</i>)", h2_style))
    search_desc = (
        "Kini AI Agent Anda dibekali dengan modul riset pustaka langsung ke database jurnal global. "
        "Tiga modul <i>skills</i> baru telah disematkan secara lokal ke dalam repositori:"
    )
    story.append(Paragraph(search_desc, body_style))
    story.append(Paragraph("&bull; <b><font color='#2B6CB0'>literature-search-arxiv</font></b>: Memungkinkan AI mencari <i>preprints</i>, mengekstrak metadata, hingga mengunduh dokumen ilmiah langsung dari server <b>arXiv</b>.", bullet_style))
    story.append(Paragraph("&bull; <b><font color='#2B6CB0'>literature-search-openalex</font></b>: Akses query terstruktur ke pangkalan data ilmiah <b>OpenAlex</b> untuk menyaring makalah akademis, DOIs, dan agregasi data sitasi.", bullet_style))
    story.append(Paragraph("&bull; <b><font color='#2B6CB0'>science_skills_common</font></b>: Pustaka penanganan request HTTP otomatis untuk menjamin kepatuhan terhadap <i>rate-limit</i> server jurnal (anti-blokir).", bullet_style))
    
    story.append(Paragraph("2. Integrasi 5 Berkas Pendukung Riset Tingkat Tinggi (<i>Support Guides</i>)", h2_style))
    guides_desc = (
        "Lima dokumen referensi generik berstandar tinggi telah ditambahkan ke folder <code>supportFiles/</code> "
        "untuk menjadi 'Otak Luar' AI Anda:"
    )
    story.append(Paragraph(guides_desc, body_style))
    story.append(Paragraph("&bull; <b><font color='#2D3748'>thesis_writing_guide.md</font></b>: Panduan gaya penulisan skripsi akademik yang bersih dari gaya tulisan AI (<i>AI-isms</i>), dilengkapi aturan ketat tanda baca teknis (Zero Semicolon/Colon in Prose).", bullet_style))
    story.append(Paragraph("&bull; <b><font color='#2D3748'>UNIVERSAL_THESIS_AI_GUIDE.md</font></b>: Panduan pola kolaborasi AI-Manusia yang terbukti efektif untuk menyusun tesis lintas disiplin ilmu.", bullet_style))
    story.append(Paragraph("&bull; <b><font color='#2D3748'>GRAPHRAG_GUIDE.md</font></b>: Panduan operasional sinkronisasi <i>Knowledge Graph</i> dan <i>Graphify</i> untuk pemetaan semantik otomatis antara kode Python dan draf Obsidian.", bullet_style))
    story.append(Paragraph("&bull; <b><font color='#2D3748'>DOCX_SYNC_GUIDE.md</font></b>: Panduan teknis otomatisasi sinkronisasi draf naskah Markdown ke dalam berkas Microsoft Word (.docx).", bullet_style))
    story.append(Paragraph("&bull; <b><font color='#2D3748'>FILE_INDEX.md</font></b>: Pusat pendaftaran berkas repositori (<i>Central File Registry</i>) untuk menjaga keteraturan ekosistem berkas.", bullet_style))

    story.append(Spacer(1, 10))

    # Section 2: Perbaikan
    story.append(Paragraph("Perbaikan & Penyelarasan Penting", h1_style))
    story.append(Paragraph("&bull; <b>Penyelarasan Venv-First (Powershell PATH)</b>: Semua instruksi pada dokumen panduan sinkronisasi dan GraphRAG kini merujuk ke jalur <i>virtual environment</i> terpusat <code>$HOME\\thesis_venv\\</code> (sesuai alur kerja asli dari <code>setup_env.ps1</code>) untuk menjaga kebersihan direktori repositori.", bullet_style))
    story.append(Paragraph("&bull; <b>Anonimisasi Total (Sterilized 100%)</b>: Seluruh informasi pribadi (Nama, NIM, Kelas) dan topik riset khusus terdahulu telah dibersihkan secara total menggunakan skrip Python otomatis untuk memastikan repositori template ini benar-benar steril dan aman didistribusikan secara publik.", bullet_style))

    story.append(Spacer(1, 10))

    # Section 3: Cara Update
    story.append(Paragraph("Cara Memperbarui untuk Pengguna Lama", h1_style))
    story.append(Paragraph("Untuk pengguna yang sudah men-clone repositori ini sebelumnya, Anda cukup memanggil asisten AI Anda di kolom chat dan mengetik:", body_style))
    story.append(Paragraph("<b>/update-infra</b>", code_style))
    
    # Alert Box
    alert_content = [
        [Paragraph("INFO PEMBARUAN MANDIRI", note_title_style)],
        [Paragraph("Sistem <i>Self-Healing</i> AI akan melakukan <i>backup</i> otomatis, menyajikan <i>Audit Dashboard</i> pembanding, dan menyuntikkan seluruh modul baru ini tanpa merusak naskah draf yang sedang Anda kerjakan!", note_body_style)]
    ]
    alert_table = Table(alert_content, colWidths=[doc.width])
    alert_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#EBF8FF')), # Very light blue
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#BEE3F8')),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
    ]))
    story.append(alert_table)
    
    story.append(Spacer(1, 15))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#E2E8F0'), spaceBefore=5, spaceAfter=10))
    
    # Footer statement
    story.append(Paragraph("<i>Developed with ❤️ as a Universal Research Template.</i>", ParagraphStyle('Foot', parent=body_style, alignment=1)))

    doc.build(story)
    print(f"PDF successfully built at {pdf_filename}")

if __name__ == "__main__":
    build_pdf()
