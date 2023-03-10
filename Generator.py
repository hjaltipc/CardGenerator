from fpdf import FPDF
import json


def generateCardBacks(CardType,skipping):
    row = 0
    column = 4
    #Adds new page for back of sector cards
    pdf.add_page()
    for (index,item) in enumerate(data[CardType][:-skipping]):
        column -= 1
        if column == -1:
            row += 1
            column = 3
        pdf.set_y((col_body+col_title)*row)
        pdf.set_x(50 * column)
        pdf.cell(col_width, col_title+col_body, txt = CardType, border = 1, align = 'C')

#opens and returns file content as dictionary
f = open('StartupSuperfight.json')
data = json.load(f)

#saves DPDF class to variable
pdf = FPDF()

#adds blank page
pdf.add_page()

pdf.set_font("Arial", size = 15)

col_width = 50
col_title = 20
col_body = 50

row = 0
column = 0

#places and generate cards
for (index,item) in enumerate(data["Sectors"][:-2]):
    if (column+1)%5 == 0:
        row += 1
        column = 0
    print(index, item)
    pdf.set_y((col_body+col_title)*row)
    pdf.set_x(50 * column)
    pdf.cell(col_width, col_title, txt = item, border = "LRT", ln = 2, align = 'C')
    pdf.cell(col_width, col_body, txt = "Shrek", border = "LRB", align = 'C')
    column += 1
generateCardBacks("Sectors", 2)

pdf.add_page()
row = 0
column = 0
for (index,item) in enumerate(data["Weaknesses"][:-2]):
    if (column+1)%5 == 0:
        row += 1
        column = 0
    print(index, item)
    pdf.set_y((col_body+col_title)*row)
    pdf.set_x(50 * column)
    pdf.cell(col_width, col_title, txt = item, border = "LRT", ln = 2, align = 'C')
    pdf.cell(col_width, col_body, txt = "Shrek", border = "LRB", align = 'C')
    column += 1
generateCardBacks("Weaknesses",2)


#Adds new page for App cards
pdf.add_page()


pdf.output("Shrek.pdf")
f.close()