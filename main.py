import os

def list_html_files(folder):
    html_files = [file for file in os.listdir(folder) if file.endswith(".html")]
    return html_files

def save_to_markdown(html_files, output_file):
    with open(output_file, "w") as f:
        f.write("# Lista de Embed:\n")
        for file in html_files:
            link = f"https://p1x3lr4.github.io/Embed-Tools/{file}"
            f.write(f"### [{file}]({link})\n")
            f.write(f"```\n{link}\n```\n")

if __name__ == "__main__":
    current_directory = os.getcwd()
    html_files = list_html_files(current_directory)

    if not html_files:
        print("Nenhum arquivo HTML encontrado na pasta atual.")
    else:
        markdown_output_file = "README.md"
        save_to_markdown(html_files, markdown_output_file)
        print(f"Lista de arquivos HTML salva em '{markdown_output_file}'.")
