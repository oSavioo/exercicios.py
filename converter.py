from pathlib import Path
import csv

pasta = Path(r"C:\Users\arthur.soares\converter")  # ✅ troquei Usuários -> Users

print("Arquivos na pasta:")
for f in pasta.iterdir():
    if f.is_file():
        print("-", f.name)

# ✅ pega o arquivo pelo começo do nome (sem depender da extensão)
entrada = next(pasta.glob("S_MEASUREMENT_DOCU#FreeText_Mandatory*"))
saida = entrada.with_suffix(".csv")

DELIM = ","  # troque se necessário: ",", "\t", "|"

with open(entrada, "r", encoding="latin-1", errors="replace", newline="") as fin, \
     open(saida, "w", encoding="utf-8", newline="") as fout:
    reader = csv.reader(fin, delimiter=DELIM)
    writer = csv.writer(fout)
    for row in reader:
        writer.writerow(row)

print("Convertido!")
print("Entrada:", entrada)
print("Saída:", saida)
