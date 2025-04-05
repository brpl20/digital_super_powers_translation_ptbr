import os
import re

def replace_in_htmls(folder_path, old_term, new_term):
    # Verifica se o caminho da pasta existe
    if not os.path.isdir(folder_path):
        print(f"O caminho '{folder_path}' não é uma pasta válida.")
        return
    
    # Conta as substituições
    total_files = 0
    modified_files = 0
    total_replacements = 0
    
    # Percorre todos os arquivos na pasta
    for filename in os.listdir(folder_path):
        # Verifica se é um arquivo HTML
        if filename.lower().endswith('.html'):
            file_path = os.path.join(folder_path, filename)
            
            # Lê o conteúdo do arquivo
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Realiza a substituição
            new_content, count = re.subn(re.escape(old_term), new_term, content)
            
            # Se houve substituições, escreve o arquivo atualizado
            if count > 0:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                
                modified_files += 1
                total_replacements += count
                print(f"Arquivo '{filename}': {count} substituições realizadas.")
            
            total_files += 1
    
    # Exibe o resultado final
    print(f"\nProcessamento concluído:")
    print(f"Total de arquivos HTML: {total_files}")
    print(f"Arquivos modificados: {modified_files}")
    print(f"Total de substituições: {total_replacements}")

# Exemplo de uso
if __name__ == "__main__":
    pasta = input("Digite o caminho da pasta: ")
    termo_antigo = input("Digite o termo a ser substituído: ")
    termo_novo = input("Digite o novo termo: ")
    
    replace_in_htmls(pasta, termo_antigo, termo_novo)
