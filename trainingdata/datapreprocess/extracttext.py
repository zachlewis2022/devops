from unstructured.partition.auto import partition

with open('extracteddata.txt', 'w',encoding="utf-8") as f:
  f.write("---------------------------------------------------------------------\n")
  f.write("***********************  EMAIL EML DOCUMENT INGEST **********************\n")
  f.write("---------------------------------------------------------------------\n")

  elements = partition(filename="emaildemo.eml")
  for el in elements:
    new_string = ' '.join(str(el).split(' '))
    f.write(new_string)

  f.write("---------------------------------------------------------------------\n")
  f.write("***********************  HTML Web DOCUMENT INGEST **********************\n")
  f.write("---------------------------------------------------------------------\n")

  elements = partition(filename="news.html")
  for el in elements:
    new_string = ' '.join(str(el).split(' '))
    f.write(new_string)
    f.flush()

  f.write("---------------------------------------------------------------------\n")
  f.write("***********************  PDF DOCUMENT INGEST **********************\n")
  f.write("---------------------------------------------------------------------\n")

  elements = partition(filename="pdfdemo.pdf")
  for el in elements:
    new_string = ' '.join(str(el).split(' '))
    f.write(new_string)

  f.write("---------------------------------------------------------------------\n")
  f.write("***********************  WORD DOCUMENT INGEST **********************\n")
  f.write("---------------------------------------------------------------------\n")

  elements = partition(filename="worddemo.docx")
  for el in elements:
    new_string = ' '.join(str(el).split(' '))
    f.write(new_string)


  f.write("---------------------------------------------------------------------\n")
  f.write("***********************  DONE **********************\n")
  f.write("---------------------------------------------------------------------\n")