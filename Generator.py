from fpdf import FPDF

#saves DPDF class to variable
pdf = FPDF()

#adds blank page
pdf.add_page()

pdf.set_font("Arial", size = 15)

pdf.cell(200, 10, txt = "Shrek",
    ln = 1, align = 'C')

pdf.cell(200, 10, txt = "ccording to all known laws of aviation, there is no way a bee should be able to fly. It's wings are too small to get its fat little body off the ground. The bee, of course, flies anyway, because bees don't care what humans think is impossible.",
    ln = 2, align = 'C')

pdf.output("Shrek.pdf")