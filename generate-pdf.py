import pdfkit

# Additional options
# 'page-size': [width,height] #'A4', letter, legal
# 'page-width': '100',
# 'page-height': '100',

options = {
         'dpi': 92,
         'page-size': 'A4',
         'page-width': '210',
         'page-height': '350',
         'margin-top': '0.25in',
         'margin-right': '0.25in',  
         'margin-bottom': '0.25in',
         'margin-left': '0.25in',
         'encoding': "UTF-8",
         'custom-header' : [
            ('Accept-Encoding', 'gzip')
         ],
         "enable-local-file-access": None,
         'no-outline': None        
    }





# Windows
config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
pdfkit.from_file('C:\\Users\\sbssd\\Desktop\\wip\\cv\\index.html', 'CV-sebastian-oviedo.pdf', configuration=config, options=options)

# Linux
#pdfkit.from_file('/home/sov/Documents/Cv/Cv/index.html', 'CV-sebastian-oviedo.pdf', options=options)


# web for generate pdfs
# https://www.sejda.com/html-to-pdf