---
name: docx
description: "Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers include: any mention of 'Word doc', 'word document', '.docx', or requests to produce professional documents with formatting like tables of contents, headings, page numbers, or letterheads. Also use when extracting or reorganizing content from .docx files, inserting or replacing images in documents, performing find-and-replace in Word files, working with tracked changes or comments, or converting content into a polished Word document. If the user asks for a 'report', 'memo', 'letter', 'template', or similar deliverable as a Word or .docx file, use this skill. Do NOT use for PDFs, spreadsheets, Google Docs, or general coding tasks unrelated to document generation."
license: Proprietary. LICENSE.txt has complete terms
---

# DOCX creation, editing, and analysis

## Overview

A .docx file is a ZIP archive containing XML files.

## Quick Reference

| Task | Approach |
|------|----------|
| **EcoBin Default** | **MANDATORY**: Prefix all python commands with `conda run -n train_mx150 python` |
| **Script Location** | **GLOBAL**: Scripts are located in the Antigravity global directory: `C:\Users\Syahril\.gemini\antigravity\skills\docx\scripts` |
| Read/analyze content | `unpack` for raw XML (Pandoc is [OPTIONAL]) |
| Create new document | Use `docx-js` - see Creating New Documents below |
| Edit existing document | Unpack → edit XML → repack - see Editing Existing Documents below |

### Converting .doc to .docx [OPTIONAL - REQUIRES LIBREOFFICE]

Legacy `.doc` files must be converted before editing (requires LibreOffice):

```bash
conda run -n train_mx150 python scripts/office/soffice.py --headless --convert-to docx document.doc
```

### Reading Content

```bash
# [OPTIONAL - REQUIRES PANDOC] Text extraction with tracked changes
# pandoc --track-changes=all document.docx -o output.md

# Raw XML access (Standard EcoBin Approach)
conda run -n train_mx150 python scripts/office/unpack.py document.docx unpacked/
```

### Converting to Images [OPTIONAL - REQUIRES LIBREOFFICE/POPPLER]

```bash
conda run -n train_mx150 python scripts/office/soffice.py --headless --convert-to pdf document.docx
pdftoppm -jpeg -r 150 document.pdf page
```

### Accepting Tracked Changes [OPTIONAL - REQUIRES LIBREOFFICE]

To produce a clean document with all tracked changes accepted (requires LibreOffice):

```bash
conda run -n train_mx150 python scripts/accept_changes.py input.docx output.docx
```

---

## Re-Engineering Strategy (The Audit-First Approach)

To produce a document that is 100% identical to the reference (High-Fidelity), follow the **Audit-Draft-Build-Verify** phase:

### Phase 1: Mandatory Audit Checklist
Before writing any code, disassemble the reference file (`unpack`) and identify the following elements:

> [!TIP]
> **Automated Code Extraction**: If the reference document has code blocks, **DO NOT** re-type them manually. Use the `extract_code.py` script in the global `scripts/` folder to extract text character-by-character from the original XML to avoid typographical errors.

| Element | XML Tag | What to Look For | Unit |
|---------|---------|------------------|------|
| **Page Size** | `<w:pgSz>` | Width & Height | DXA |
| **Margins** | `<w:pgMar>` | Top, Bottom, Left, Right | DXA |
| **Font Family** | `<w:rFonts>` | `ascii` or `hAnsi` (The TRUE font name) | String |
| **Font Size** | `<w:sz>` | Value / 2 = pt size (e.g., 24 = 12pt) | Half-pt |
| **Spacing** | `<w:spacing>` | `line` (line height), `before`, `after` | DXA |
| **Alignment** | `<w:jc>` | `both` (justified), `center`, `start` | Enum |
| **Indentation** | `<w:ind>` | `left`, `hanging`, `firstLine` | DXA |
| **Numbering** | `<w:numPr>` | `numId` and `ilvl` for list consistency | ID |

### Phase 2: Implementation Blueprint
Gunakan hasil audit di atas sebagai konstanta dalam skrip JavaScript. Jangan menebak nilai.

---

## Creating New Documents

Generate .docx files with JavaScript, then validate. Install: `npm install -g docx`

### Setup
```javascript
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, ImageRun,
        Header, Footer, AlignmentType, PageOrientation, LevelFormat, ExternalHyperlink,
        InternalHyperlink, Bookmark, FootnoteReferenceRun, PositionalTab,
        PositionalTabAlignment, PositionalTabRelativeTo, PositionalTabLeader,
        TabStopType, TabStopPosition, Column, SectionType,
        TableOfContents, HeadingLevel, BorderStyle, WidthType, ShadingType,
        VerticalAlign, PageNumber, PageBreak } = require('docx');

const doc = new Document({ sections: [{ children: [/* content */] }] });
Packer.toBuffer(doc).then(buffer => fs.writeFileSync("doc.docx", buffer));
```

### Validation
After creating the file, validate it. If validation fails, unpack, fix the XML, and repack.
```bash
python scripts/office/validate.py doc.docx
```

### Page Size

```javascript
// CRITICAL: docx-js defaults to A4, not US Letter
// Always set page size explicitly for consistent results
sections: [{
  properties: {
    page: {
      size: {
        width: 12240,   // 8.5 inches in DXA
        height: 15840   // 11 inches in DXA
      },
      margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 } // 1 inch margins
    }
  },
  children: [/* content */]
}]
```

**Common page sizes (DXA units, 1440 DXA = 1 inch):**

| Paper | Width | Height | Content Width (1" margins) |
|-------|-------|--------|---------------------------|
| US Letter | 12,240 | 15,840 | 9,360 |
| A4 (default) | 11,906 | 16,838 | 9,026 |

**Landscape orientation:** docx-js swaps width/height internally, so pass portrait dimensions and let it handle the swap:
```javascript
size: {
  width: 12240,   // Pass SHORT edge as width
  height: 15840,  // Pass LONG edge as height
  orientation: PageOrientation.LANDSCAPE  // docx-js swaps them in the XML
},
// Content width = 15840 - left margin - right margin (uses the long edge)
```

### Styles (Dynamic Auditing)

**MANDATORY**: Do not use default fonts (Arial/Calibri). Extract the font name from the XML audit results (`styles.xml`). Use a **Modular Helper Functions** pattern for consistency.

```javascript
// Example: Implementation based on XML Audit results
const FONT_NAME = "Times New Roman"; // Derived from <w:rFonts w:ascii="..." />
const LINE_SPACING = 360;           // Derived from <w:spacing w:line="..." />

const body = (text) => new Paragraph({
  alignment: AlignmentType.JUSTIFIED,
  spacing: { line: LINE_SPACING },
  children: [new TextRun({ text, font: FONT_NAME, size: 24 })] // 24 = 12pt
});

const h2 = (text, number) => new Paragraph({
  heading: HeadingLevel.HEADING_2,
  spacing: { before: 240, after: 120 },
  children: [new TextRun({ text: `${number} ${text}`, font: FONT_NAME, size: 28, bold: true })]
});

const doc = new Document({
  styles: {
    default: { document: { run: { font: FONT_NAME, size: 24 } } },
    paragraphStyles: [
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 28, bold: true, font: FONT_NAME },
        paragraph: { spacing: { before: 240, after: 120 }, outlineLevel: 1 } },
    ]
  },
  sections: [{
    children: [
      h2("Theory", "1.2"),
      body("This paragraph uses styles derived directly from the XML audit."),
    ]
  }]
});
```

### Lists (NEVER use unicode bullets)

```javascript
// ❌ WRONG - never manually insert bullet characters
new Paragraph({ children: [new TextRun("• Item")] })  // BAD
new Paragraph({ children: [new TextRun("\u2022 Item")] })  // BAD

// ✅ CORRECT - use numbering config with LevelFormat.BULLET
const doc = new Document({
  numbering: {
    config: [
      { reference: "bullets",
        levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] },
      { reference: "numbers",
        levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] },
    ]
  },
  sections: [{
    children: [
      new Paragraph({ numbering: { reference: "bullets", level: 0 },
        children: [new TextRun("Bullet item")] }),
      new Paragraph({ numbering: { reference: "numbers", level: 0 },
        children: [new TextRun("Numbered item")] }),
    ]
  }]
});

// ⚠️ Each reference creates INDEPENDENT numbering
// Same reference = continues (1,2,3 then 4,5,6)
// Different reference = restarts (1,2,3 then 1,2,3)
```

### Tables

**CRITICAL: Tables need dual widths** - set both `columnWidths` on the table AND `width` on each cell. Without both, tables render incorrectly on some platforms.

```javascript
// CRITICAL: Always set table width for consistent rendering
// CRITICAL: Use ShadingType.CLEAR (not SOLID) to prevent black backgrounds
const border = { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" };
const borders = { top: border, bottom: border, left: border, right: border };

new Table({
  width: { size: 9360, type: WidthType.DXA }, // Always use DXA (percentages break in Google Docs)
  columnWidths: [4680, 4680], // Must sum to table width (DXA: 1440 = 1 inch)
  rows: [
    new TableRow({
      children: [
        new TableCell({
          borders,
          width: { size: 4680, type: WidthType.DXA }, // Also set on each cell
          shading: { fill: "D5E8F0", type: ShadingType.CLEAR }, // CLEAR not SOLID
          margins: { top: 80, bottom: 80, left: 120, right: 120 }, // Cell padding (internal, not added to width)
          children: [new Paragraph({ children: [new TextRun("Cell")] })]
        })
      ]
    })
  ]
})
```

**Table width calculation:**

Always use `WidthType.DXA` — `WidthType.PERCENTAGE` breaks in Google Docs.

```javascript
// Table width = sum of columnWidths = content width
// US Letter with 1" margins: 12240 - 2880 = 9360 DXA
width: { size: 9360, type: WidthType.DXA },
columnWidths: [7000, 2360]  // Must sum to table width
```

**Width rules:**
- **Always use `WidthType.DXA`** — never `WidthType.PERCENTAGE` (incompatible with Google Docs)
- Table width must equal the sum of `columnWidths`
- Cell `width` must match corresponding `columnWidth`
- Cell `margins` are internal padding - they reduce content area, not add to cell width
- For full-width tables: use content width (page width minus left and right margins)

### Images (Preservasi Aspect Ratio)

**MANDATORY**: Photos of manual calculations or screenshots often have non-standard ratios. Specifying dimensions by guessing or hardcoding will cause image distortion ("stretching"). Always use a **Calculated Scaling** approach:

1.  **Audit Dimensi Asli**: Cek properti file (lebar & tinggi asli dalam pixel).
2.  **Pilih Anchor Width**: Tentukan lebar yang diinginkan (misal: sesuai lebar konten halaman ~9360 DXA atau ukuran standar foto ~450px).
3.  **Hitung Tinggi Proporsional**: 
    *   `TargetHeight = TargetWidth * (OriginalHeight / OriginalWidth)`

#### **Best Practice: Image Helper (Node.js)**
Use helper functions in the builder script to ensure the ratio remains consistent:

```javascript
// Helper untuk menghitung dimensi proporsional
const getScaledDims = (originalW, originalH, targetW) => ({
    width: targetW,
    height: targetW * (originalH / originalW)
});

// Implementasi
new ImageRun({
    data: fs.readFileSync("manual_calc.png"),
    transformation: getScaledDims(1200, 1600, 450), // Rasio tetap terjaga
})
```

> [!CAUTION]
> Failure to maintain the aspect ratio in academic documents (especially in graphs/calculations) is considered a professional flaw. Always audit dimensions before building.

### Page Breaks

```javascript
// CRITICAL: PageBreak must be inside a Paragraph
new Paragraph({ children: [new PageBreak()] })

// Or use pageBreakBefore
new Paragraph({ pageBreakBefore: true, children: [new TextRun("New page")] })
```

### Hyperlinks

```javascript
// External link
new Paragraph({
  children: [new ExternalHyperlink({
    children: [new TextRun({ text: "Click here", style: "Hyperlink" })],
    link: "https://example.com",
  })]
})

// Internal link (bookmark + reference)
// 1. Create bookmark at destination
new Paragraph({ heading: HeadingLevel.HEADING_1, children: [
  new Bookmark({ id: "chapter1", children: [new TextRun("Chapter 1")] }),
]})
// 2. Link to it
new Paragraph({ children: [new InternalHyperlink({
  children: [new TextRun({ text: "See Chapter 1", style: "Hyperlink" })],
  anchor: "chapter1",
})]})
```

### Footnotes

```javascript
const doc = new Document({
  footnotes: {
    1: { children: [new Paragraph("Source: Annual Report 2024")] },
    2: { children: [new Paragraph("See appendix for methodology")] },
  },
  sections: [{
    children: [new Paragraph({
      children: [
        new TextRun("Revenue grew 15%"),
        new FootnoteReferenceRun(1),
        new TextRun(" using adjusted metrics"),
        new FootnoteReferenceRun(2),
      ],
    })]
  }]
});
```

### Tab Stops

```javascript
// Right-align text on same line (e.g., date opposite a title)
new Paragraph({
  children: [
    new TextRun("Company Name"),
    new TextRun("\tJanuary 2025"),
  ],
  tabStops: [{ type: TabStopType.RIGHT, position: TabStopPosition.MAX }],
})

// Dot leader (e.g., TOC-style)
new Paragraph({
  children: [
    new TextRun("Introduction"),
    new TextRun({ children: [
      new PositionalTab({
        alignment: PositionalTabAlignment.RIGHT,
        relativeTo: PositionalTabRelativeTo.MARGIN,
        leader: PositionalTabLeader.DOT,
      }),
      "3",
    ]}),
  ],
})
```

### Multi-Column Layouts

```javascript
// Equal-width columns
sections: [{
  properties: {
    column: {
      count: 2,          // number of columns
      space: 720,        // gap between columns in DXA (720 = 0.5 inch)
      equalWidth: true,
      separate: true,    // vertical line between columns
    },
  },
  children: [/* content flows naturally across columns */]
}]

// Custom-width columns (equalWidth must be false)
sections: [{
  properties: {
    column: {
      equalWidth: false,
      children: [
        new Column({ width: 5400, space: 720 }),
        new Column({ width: 3240 }),
      ],
    },
  },
  children: [/* content */]
}]
```

Force a column break with a new section using `type: SectionType.NEXT_COLUMN`.

### Table of Contents

```javascript
// CRITICAL: Headings must use HeadingLevel ONLY - no custom styles
new TableOfContents("Table of Contents", { hyperlink: true, headingStyleRange: "1-3" })
```

### Headers/Footers

```javascript
sections: [{
  properties: {
    page: { margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 } } // 1440 = 1 inch
  },
  headers: {
    default: new Header({ children: [new Paragraph({ children: [new TextRun("Header")] })] })
  },
  footers: {
    default: new Footer({ children: [new Paragraph({
      children: [new TextRun("Page "), new TextRun({ children: [PageNumber.CURRENT] })]
    })] })
  },
  children: [/* content */]
}]
```

### Critical Rules for docx-js

- **Set page size explicitly** - docx-js defaults to A4; use US Letter (12240 x 15840 DXA) for US documents
- **Landscape: pass portrait dimensions** - docx-js swaps width/height internally; pass short edge as `width`, long edge as `height`, and set `orientation: PageOrientation.LANDSCAPE`
- **Never use `\n`** - use separate Paragraph elements
- **Never use unicode bullets** - use `LevelFormat.BULLET` with numbering config
- **PageBreak must be in Paragraph** - standalone creates invalid XML
- **ImageRun requires `type`** - always specify png/jpg/etc
- **Always audit image aspect ratio** - use calculated height based on intrinsic dimensions to prevent "gepeng" (distorted) images
- **Always set table `width` with DXA** - never use `WidthType.PERCENTAGE` (breaks in Google Docs)
- **Tables need dual widths** - `columnWidths` array AND cell `width`, both must match
- **Table width = sum of columnWidths** - for DXA, ensure they add up exactly
- **Always add cell margins** - use `margins: { top: 80, bottom: 80, left: 120, right: 120 }` for readable padding
- **Use `ShadingType.CLEAR`** - never SOLID for table shading
- **Never use tables as dividers/rules** - cells have minimum height and render as empty boxes (including in headers/footers); use `border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: "2E75B6", space: 1 } }` on a Paragraph instead. For two-column footers, use tab stops (see Tab Stops section), not tables
- **TOC requires HeadingLevel only** - no custom styles on heading paragraphs
- **Override built-in styles** - use exact IDs: "Heading1", "Heading2", etc.
- **Include `outlineLevel`** - required for TOC (0 for H1, 1 for H2, etc.)

---

## Editing Existing Documents

**Follow all 3 steps in order.**

### Step 1: Unpack
```bash
python scripts/office/unpack.py document.docx unpacked/
```
Extracts XML, pretty-prints, merges adjacent runs, and converts smart quotes to XML entities (`&#x201C;` etc.) so they survive editing. Use `--merge-runs false` to skip run merging.

### Step 2: Edit XML

Edit files in `unpacked/word/`. See XML Reference below for patterns.

**Use "Claude" as the author** for tracked changes and comments, unless the user explicitly requests use of a different name.

**Use the Edit tool directly for string replacement. Do not write Python scripts.** Scripts introduce unnecessary complexity. The Edit tool shows exactly what is being replaced.

**CRITICAL: Use smart quotes for new content.** When adding text with apostrophes or quotes, use XML entities to produce smart quotes:
```xml
<!-- Use these entities for professional typography -->
<w:t>Here&#x2019;s a quote: &#x201C;Hello&#x201D;</w:t>
```
| Entity | Character |
|--------|-----------|
| `&#x2018;` | ‘ (left single) |
| `&#x2019;` | ’ (right single / apostrophe) |
| `&#x201C;` | “ (left double) |
| `&#x201D;` | ” (right double) |

**Adding comments:** Use `comment.py` to handle boilerplate across multiple XML files (text must be pre-escaped XML):
```bash
python scripts/comment.py unpacked/ 0 "Comment text with &amp; and &#x2019;"
python scripts/comment.py unpacked/ 1 "Reply text" --parent 0  # reply to comment 0
python scripts/comment.py unpacked/ 0 "Text" --author "Custom Author"  # custom author name
```
Then add markers to document.xml (see Comments in XML Reference).

### Step 3: Pack
```bash
python scripts/office/pack.py unpacked/ output.docx --original document.docx
```
Validates with auto-repair, condenses XML, and creates DOCX. Use `--validate false` to skip.

---

## 🛠️ Advanced: Surgical XML Editing (High-Fidelity Manual)

Use this method if automation scripts fail or if working with sensitive IEEE/academic templates that require strict XML structural integrity.

### 1. Surgical Text Replacement
Avoid performing bulk text replacements across the entire XML file. Use `multi_replace_file_content` targeting small, specific blocks (per paragraph or per heading) to minimize the risk of mismatched tags.

### 2. Manual Media Injection
To insert new images manually:
1.  **Copy**: Move the image file to `unpacked/word/media/`.
2.  **Relate**: Open `unpacked/word/_rels/document.xml.rels` and add a new relationship (or overwrite an existing one) with a unique `Id` (e.g., `rId15`).
3.  **Audit Cleanup**: If overwriting an existing relationship (e.g., replacing `.jpeg` with `.png`), ensure the old file is deleted from the `media` folder to prevent "Unreferenced file" errors during packing.
4.  **Inject**: Insert the `<w:drawing>` block into `document.xml` referencing the corresponding `rId`.

### 3. XML Integrity Audit
If packing fails due to validation errors:
- Use a tracking script (e.g., `find_stray.py`) to locate runaway `<w:t>` elements or closing `</w:p>` tags that are not properly nested.
- Word XML rules are strict: Text (`<w:t>`) **MUST** be inside a Run (`<w:r>`), and a Run **MUST** be inside a Paragraph (`<w:p>`).

### 4. Final Packing
Always use the `--original [template.docx]` flag when running `pack.py` to ensure that 100% of the original template's metadata, properties, and styles are preserved.

### 5. Critical Desktop Word Compatibility Standards
Desktop Word (2013+) is significantly stricter than Word Online or Google Docs. Violation of these rules will cause a "Catastrophic Failure" or "Word experienced an error" dialog:

> [!IMPORTANT]
> **Rule 1: ID constraint (`paraId`)**
> All `<w:p>` elements must have a valid `w14:paraId` attribute. This ID value **MUST** be a hexadecimal representing a **positive 32-bit signed integer** (range `00000001` to `7FFFFFFF`). If an ID starts with `8-F`, Word Desktop will treat the document as corrupt.

> [!IMPORTANT]
> **Rule 2: No Nested Tags in `<w:t>`**
> Text tags (`<w:t>`) **MUST** only contain plain text. Never place other tags (such as `<m:oMath>`, `<w:rPr>`, or `<w:br/>`) inside a `<w:t>`. If you need to insert a formula in the middle of a sentence, use the following structure:
> `... <w:t>text before</w:t></w:r><m:oMath>...</m:oMath><w:r><w:t>text after</w:t> ...`

> [!WARNING]
> **Rule 3: Whitespace Preservation**
> Use the `xml:space="preserve"` attribute on `<w:t>` tags if the text contains leading or trailing spaces (e.g., `<w:t xml:space="preserve"> where </w:t>`). Failure to do this will cause words to run together in Word Desktop.

---

### 6. Native Math Equations (OMML) Injection
When dealing with academic or engineering documents, use **Office Math Markup Language (OMML)** instead of plain text formatting. Native equations are clickable, editable, and render with professional typography.

> [!IMPORTANT]
> **OMML vs. Text Formatting**: Do NOT use `<w:vertAlign w:val="superscript"/>` for math. It produces non-standard text runs. Always use the `<m:oMath>` structure.

#### Key OMML Tags
- `<m:oMath>`: The root container for a math expression.
- `<m:r>`: Math Run (similar to `<w:r>`).
- `<m:t>`: Math Text (similar to `<w:t>`).
- `<m:sSup>`: Superscript (Base: `<m:e>`, Power: `<m:sup>`).
- `<m:sSub>`: Subscript (Base: `<m:e>`, Index: `<m:sub>`).
- `<m:sSubSup>`: Combined Subscript and Superscript.
- `<m:f>`: Fraction (Numerator: `<m:num>`, Denominator: `<m:den>`).

#### Implementation Pattern (LaTeX Mapping)
To manually inject an equation into a paragraph (`<w:p>`):

1. **LaTeX**: `$y^3$`
   **XML Mapping**:
   ```xml
   <m:oMath>
     <m:sSup>
       <m:e><m:r><m:t>y</m:t></m:r></m:e>
       <m:sup><m:r><m:t>3</m:t></m:r></m:sup>
     </m:sSup>
   </m:oMath>
   ```

2. **LaTeX**: `$x_0$`
   **XML Mapping**:
   ```xml
   <m:oMath>
     <m:sSub>
       <m:e><m:r><m:t>x</m:t></m:r></m:e>
       <m:sub><m:r><m:t>0</m:t></m:r></m:sub>
     </m:sSub>
   </m:oMath>
   ```

#### Mandatory Font Styling
Equations must use **Cambria Math** to render symbols correctly. Ensure every math run (`<m:r>`) has the following property:
```xml
<w:rPr>
  <w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math"/>
</w:rPr>
```

---

### 7. Interactive Math Workflow (Safety-First)
To prevent document corruption and ensure content accuracy, follow this 2-step interactive workflow when a user requests to "insert LaTeX equations" or similar complex math:

#### Phase A: The Plain-Text Draft
1.  **Draft**: Insert the equations as plain text LaTeX strings (e.g., `$y^3$`, `$E=mc^2$`) inside a standard `<w:r>` or `new TextRun`.
2.  **Verify**: Ask the user to open the draft document and confirm the mathematical notation and context are correct.
3.  **Pre-requisite**: Do NOT perform XML surgery or OMML injection in this phase.

#### Phase B: The Surgical Conversion
1.  **Unpack**: Once the user approves the draft, disassemble the document using `unpack.py`.
2.  **Surgical Replace**: Locate the paragraph (`<w:p>`) containing the placeholder and replace the text run with the corresponding `<m:oMath>` structure (see Section 6 for mapping).
3.  **Apply Math Font**: Every math run (`<m:r>`) **MUST** include the `Cambria Math` font property.
4.  **Pack & Validate**: Re-assemble the document using `pack.py` and run `validate.py` to ensure the file structure remains 100% compliant and is not corrupted.

---

**Auto-repair will fix:**
- `durableId` >= 0x7FFFFFFF (regenerates valid ID)
- Missing `xml:space="preserve"` on `<w:t>` with whitespace

**Auto-repair won't fix:**
- Malformed XML, invalid element nesting, missing relationships, schema violations

### Common Pitfalls

- **Replace entire `<w:r>` elements**: When adding tracked changes, replace the whole `<w:r>...</w:r>` block with `<w:del>...<w:ins>...` as siblings. Don't inject tracked change tags inside a run.
- **Preserve `<w:rPr>` formatting**: Copy the original run's `<w:rPr>` block into your tracked change runs to maintain bold, font size, etc.

---

## XML Reference

### Schema Compliance

- **Element order in `<w:pPr>`**: `<w:pStyle>`, `<w:numPr>`, `<w:spacing>`, `<w:ind>`, `<w:jc>`, `<w:rPr>` last
- **Whitespace**: Add `xml:space="preserve"` to `<w:t>` with leading/trailing spaces
- **RSIDs**: Must be 8-digit hex (e.g., `00AB1234`)

### Tracked Changes

**Insertion:**
```xml
<w:ins w:id="1" w:author="Claude" w:date="2025-01-01T00:00:00Z">
  <w:r><w:t>inserted text</w:t></w:r>
</w:ins>
```

**Deletion:**
```xml
<w:del w:id="2" w:author="Claude" w:date="2025-01-01T00:00:00Z">
  <w:r><w:delText>deleted text</w:delText></w:r>
</w:del>
```

**Inside `<w:del>`**: Use `<w:delText>` instead of `<w:t>`, and `<w:delInstrText>` instead of `<w:instrText>`.

**Minimal edits** - only mark what changes:
```xml
<!-- Change "30 days" to "60 days" -->
<w:r><w:t>The term is </w:t></w:r>
<w:del w:id="1" w:author="Claude" w:date="...">
  <w:r><w:delText>30</w:delText></w:r>
</w:del>
<w:ins w:id="2" w:author="Claude" w:date="...">
  <w:r><w:t>60</w:t></w:r>
</w:ins>
<w:r><w:t> days.</w:t></w:r>
```

**Deleting entire paragraphs/list items** - when removing ALL content from a paragraph, also mark the paragraph mark as deleted so it merges with the next paragraph. Add `<w:del/>` inside `<w:pPr><w:rPr>`:
```xml
<w:p>
  <w:pPr>
    <w:numPr>...</w:numPr>  <!-- list numbering if present -->
    <w:rPr>
      <w:del w:id="1" w:author="Claude" w:date="2025-01-01T00:00:00Z"/>
    </w:rPr>
  </w:pPr>
  <w:del w:id="2" w:author="Claude" w:date="2025-01-01T00:00:00Z">
    <w:r><w:delText>Entire paragraph content being deleted...</w:delText></w:r>
  </w:del>
</w:p>
```
Without the `<w:del/>` in `<w:pPr><w:rPr>`, accepting changes leaves an empty paragraph/list item.

**Rejecting another author's insertion** - nest deletion inside their insertion:
```xml
<w:ins w:author="Jane" w:id="5">
  <w:del w:author="Claude" w:id="10">
    <w:r><w:delText>their inserted text</w:delText></w:r>
  </w:del>
</w:ins>
```

**Restoring another author's deletion** - add insertion after (don't modify their deletion):
```xml
<w:del w:author="Jane" w:id="5">
  <w:r><w:delText>deleted text</w:delText></w:r>
</w:del>
<w:ins w:author="Claude" w:id="10">
  <w:r><w:t>deleted text</w:t></w:r>
</w:ins>
```

### Comments

After running `comment.py` (see Step 2), add markers to document.xml. For replies, use `--parent` flag and nest markers inside the parent's.

**CRITICAL: `<w:commentRangeStart>` and `<w:commentRangeEnd>` are siblings of `<w:r>`, never inside `<w:r>`.**

```xml
<!-- Comment markers are direct children of w:p, never inside w:r -->
<w:commentRangeStart w:id="0"/>
<w:del w:id="1" w:author="Claude" w:date="2025-01-01T00:00:00Z">
  <w:r><w:delText>deleted</w:delText></w:r>
</w:del>
<w:r><w:t> more text</w:t></w:r>
<w:commentRangeEnd w:id="0"/>
<w:r><w:rPr><w:rStyle w:val="CommentReference"/></w:rPr><w:commentReference w:id="0"/></w:r>

<!-- Comment 0 with reply 1 nested inside -->
<w:commentRangeStart w:id="0"/>
  <w:commentRangeStart w:id="1"/>
  <w:r><w:t>text</w:t></w:r>
  <w:commentRangeEnd w:id="1"/>
<w:commentRangeEnd w:id="0"/>
<w:r><w:rPr><w:rStyle w:val="CommentReference"/></w:rPr><w:commentReference w:id="0"/></w:r>
<w:r><w:rPr><w:rStyle w:val="CommentReference"/></w:rPr><w:commentReference w:id="1"/></w:r>
```

### Images

1. Add image file to `word/media/`
2. Add relationship to `word/_rels/document.xml.rels`:
```xml
<Relationship Id="rId5" Type=".../image" Target="media/image1.png"/>
```
3. Add content type to `[Content_Types].xml`:
```xml
<Default Extension="png" ContentType="image/png"/>
```
4. Reference in document.xml:
```xml
<w:drawing>
  <wp:inline>
    <wp:extent cx="914400" cy="914400"/>  <!-- EMUs: 914400 = 1 inch -->
    <a:graphic>
      <a:graphicData uri=".../picture">
        <pic:pic>
          <pic:blipFill><a:blip r:embed="rId5"/></pic:blipFill>
        </pic:pic>
      </a:graphicData>
    </a:graphic>
  </wp:inline>
</w:drawing>
```

---

## Dependencies

- **pandoc**: Text extraction
- **extract_code.py**: Python script in the global `scripts/` folder for high-precision text extraction of code from XML.
- **docx**: `npm install -g docx` (new documents)
- **LibreOffice**: PDF conversion (auto-configured for sandboxed environments via `scripts/office/soffice.py`)
- **Poppler**: `pdftoppm` for images
