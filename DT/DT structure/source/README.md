# Reproducing the figures

Run `python source/build_figures.py` from this package with Python and ReportLab installed. The source uses Times New Roman from the Windows Fonts directory; change the font registration paths if using another operating system. Fonts are embedded in PDFs but not redistributed as separate files.

The script generates SVG and PDF files into `figures/`. Render each PDF with Poppler at 300 dpi to generate the accompanying PNG, for example:

```text
pdftoppm -r 300 -png -singlefile figures/figure_1_design_to_use.pdf figures/figure_1_design_to_use
```

The supplied SVG and PDF share the same drawing coordinates. SVG text remains editable and depends on installed serif fonts. Check text layout after changing labels, fonts or publication dimensions.

This source controls the visual layout. It does not infer scientific relationships. Evidence status and mappings are documented separately in the papers folder.
