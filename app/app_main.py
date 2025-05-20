# app_main.py
import os
from flask import Flask, request, render_template, redirect, url_for, flash
from werkzeug.utils import secure_filename
from PIL import Image # Pillow para manipulação básica de imagens
from datetime import datetime # <<< ADICIONADO: Importa datetime

# Importará o módulo de predição.
# Certifique-se que app_predictor.py está na mesma pasta que este arquivo (app_main.py)
# Se app_main.py está em 'app/', então app_predictor.py também deve estar em 'app/'
from app_predictor import classify_image_dummy # Usando um dummy por enquanto

# Configurações
UPLOAD_FOLDER = 'uploads' # Relativo à pasta 'app' ou onde app_main.py está.
                          # Para ser mais robusto, pode ser 'app/uploads' se app_main.py estiver na raiz do projeto
                          # ou apenas 'uploads' se app_main.py estiver dentro de 'app/' e 'uploads' também.
                          # Vamos assumir que 'uploads' é uma subpasta de 'app'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

app = Flask(__name__)
# Define o caminho absoluto para UPLOAD_FOLDER e para a pasta de display estática
# Isso torna os caminhos mais explícitos e menos propensos a erros dependendo de onde você executa o script.
APP_ROOT = os.path.dirname(os.path.abspath(__file__)) # Raiz da pasta 'app'
UPLOAD_FOLDER_PATH = os.path.join(APP_ROOT, 'uploads')
DISPLAY_FOLDER_PATH = os.path.join(APP_ROOT, 'static', 'uploads_display')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER_PATH
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE
app.secret_key = 'supersecretkey' # Mude isso para uma chave secreta real em produção

# Cria os diretórios necessários se não existirem
if not os.path.exists(UPLOAD_FOLDER_PATH):
    os.makedirs(UPLOAD_FOLDER_PATH)
if not os.path.exists(DISPLAY_FOLDER_PATH):
    os.makedirs(DISPLAY_FOLDER_PATH)

def allowed_file(filename):
    """Verifica se a extensão do arquivo é permitida."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    """Rota principal para upload de imagem e exibição de resultados."""
    current_year = datetime.now().year # <<< ADICIONADO: Obtém o ano atual

    if request.method == 'POST':
        if 'file' not in request.files:
            flash('Nenhum arquivo selecionado', 'error')
            # Passa current_year mesmo em redirect para o caso de erro antes do POST completo
            return render_template('index.html', current_year=current_year)
        file = request.files['file']
        if file.filename == '':
            flash('Nenhum arquivo selecionado', 'error')
            return render_template('index.html', current_year=current_year)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            try:
                file.save(filepath)
                if os.path.getsize(filepath) > MAX_FILE_SIZE:
                    os.remove(filepath)
                    flash('Arquivo excede o tamanho máximo de 5MB', 'error')
                    return render_template('index.html', current_year=current_year)

                prediction, confidence = classify_image_dummy(filepath)
                
                image_url = None # Inicializa image_url
                try:
                    img = Image.open(filepath)
                    max_width = 400
                    if img.width > max_width:
                        ratio = max_width / float(img.width)
                        height = int(float(img.height) * float(ratio))
                        img = img.resize((max_width, height), Image.Resampling.LANCZOS)
                    
                    safe_display_filename = secure_filename(f"display_{filename}")
                    # Salva na pasta static/uploads_display
                    display_filepath = os.path.join(DISPLAY_FOLDER_PATH, safe_display_filename)
                    img.save(display_filepath)
                    # Gera a URL para o template HTML
                    image_url = url_for('static', filename=f'uploads_display/{safe_display_filename}')

                except Exception as e:
                    flash(f'Erro ao processar a imagem para exibição: {e}', 'error')
                
                # Remove o arquivo original da pasta 'uploads' após processamento e cópia para 'static/uploads_display'
                # Você pode querer manter o original dependendo da sua lógica, mas para este exemplo, vamos remover.
                if os.path.exists(filepath):
                    try:
                        os.remove(filepath)
                    except Exception as e:
                        print(f"Aviso: Não foi possível remover o arquivo temporário {filepath}: {e}")


                return render_template('index.html',
                                       filename=filename,
                                       prediction=prediction,
                                       confidence=confidence,
                                       image_url=image_url,
                                       current_year=current_year) # <<< ADICIONADO: Passa o ano

            except Exception as e:
                if os.path.exists(filepath):
                    os.remove(filepath)
                flash(f'Erro ao processar o arquivo: {e}', 'error')
                # Passa current_year em caso de erro
                return render_template('index.html', current_year=current_year)
        else:
            flash('Tipo de arquivo não permitido. Use png, jpg, jpeg, gif.', 'error')
            # Passa current_year em caso de tipo de arquivo não permitido
            return render_template('index.html', current_year=current_year)

    # Para requisições GET (quando a página é carregada pela primeira vez)
    return render_template('index.html', current_year=current_year) # <<< ADICIONADO: Passa o ano

if __name__ == '__main__':
    # A criação dos diretórios já foi movida para o início do script
    app.run(debug=True)
