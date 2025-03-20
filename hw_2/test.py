import os
from latex_gen.latex_gen import generate_latex_table, generate_latex_image, generate_full_document, compile_pdf

table_data = [
    ["FROM", "TO", "PRICE"],
    ["A", "B", 17],
    ["here", "there", 19],
    ["C", "D", 22]
]

table_code = generate_latex_table(table_data)
image_code = generate_latex_image("example_image.jpg")

full_content = table_code + "\n" + image_code
document = generate_full_document(full_content)

artifacts_dir = "artifacts"
os.makedirs(artifacts_dir, exist_ok=True)

tex_output_path = os.path.join(artifacts_dir, "generated_document.tex")
with open(tex_output_path, "w", encoding="utf-8") as tex_file:
    tex_file.write(document)

pdf_output_path = os.path.join(artifacts_dir, "generated_artifact.pdf")
compile_pdf(document, pdf_output_path)
print(f"PDF с таблицей и картинкой сгенерирован: {pdf_output_path}")
