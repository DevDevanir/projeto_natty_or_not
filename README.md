\# Detector "Natty or Not" de Imagens Corporais

\#\# 📒 Descrição  
Este projeto visa criar um sistema de classificação de imagens capaz de distinguir entre imagens corporais "natty" (naturais, sem edição significativa por IA) e "not natty" (geradas ou significativamente alteradas por Inteligência Artificial). Inspirado no desafio da DIO "Natty or Not", este projeto explora o uso de IAs Generativas para criação de datasets sintéticos e modelos de Visão Computacional para a classificação.

O usuário poderá fazer o upload de uma imagem corporal, e o sistema fornecerá uma probabilidade de a imagem ser genuína ou gerada/alterada por IA.

\#\# 🤖 Tecnologias Utilizadas  
\* \*\*Python\*\*: Linguagem de programação principal.  
\* \*\*Flask\*\*: Microframework web para criar a interface do usuário.  
\* \*\*Stable Diffusion (Conceitual)\*\*: Para a geração de um dataset sintético de imagens "not natty". A implementação real requer a instalação do Stable Diffusion Web UI (Automatic1111) ou bibliotecas como \`diffusers\`.  
\* \*\*Detectron2 (Conceitual)\*\*: Framework da Facebook AI Research para detecção e segmentação de objetos, utilizado aqui para treinar o modelo de classificação de imagens. A implementação real requer instalação e configuração do Detectron2.  
\* \*\*HTML/CSS/JavaScript\*\*: Para a interface web.  
\* \*\*Git & GitHub\*\*: Para controle de versão e hospedagem do projeto.

\#\# 🧐 Processo de Criação

1\.  \*\*Configuração do Ambiente (Windows 11)\*\*:  
    \* Instalar Python (versão 3.9+ recomendada).  
    \* Criar um ambiente virtual: \`python \-m venv venv\`  
    \* Ativar o ambiente virtual: \`venv\\Scripts\\activate\`  
    \* Instalar as dependências: \`pip install \-r requirements.txt\`

2\.  \*\*Geração do Dataset (Usando Stable Diffusion \- Conceitual)\*\*:  
    \* \*\*Objetivo\*\*: Criar dois conjuntos de imagens:  
        \* \`dataset/real/\`: Imagens corporais autênticas, não alteradas por IA.  
        \* \`dataset/ai/\`: Imagens corporais geradas ou significativamente alteradas por IA, utilizando Stable Diffusion.  
    \* \*\*Ferramenta\*\*: Stable Diffusion Web UI (Automatic1111) é recomendado para gerar imagens com prompts específicos.  
        \* Exemplo de prompt para "natty": "photorealistic body, no retouch, natural lighting, gym photo"  
        \* Exemplo de prompt para "not natty" (IA): "sculpted muscles, HDR lighting, perfect physique, airbrushed skin, enhanced body"  
    \* Consulte \`scripts/generate\_dataset.py\` para uma visão geral do processo. \*Nota: Este script é um guia e não executa diretamente a geração de imagens com Stable Diffusion.\*

3\.  \*\*Treinamento do Modelo (Usando Detectron2 \- Conceitual)\*\*:  
    \* \*\*Objetivo\*\*: Treinar um modelo de classificação de imagens (ex: usando um backbone ResNet com Detectron2) para distinguir entre as classes "real" e "ai".  
    \* \*\*Preparação\*\*:  
        \* Instalar Detectron2 e suas dependências (incluindo PyTorch com suporte a CUDA, se tiver uma GPU NVIDIA). Siga as instruções oficiais do Detectron2 para Windows.  
        \* Organizar o dataset conforme esperado pelo Detectron2.  
    \* \*\*Treinamento\*\*:  
        \* Adaptar um script de treinamento de classificação de imagens do Detectron2.  
        \* Configurar os parâmetros do modelo, dataset, otimizador e número de épocas.  
        \* Salvar o modelo treinado (ex: em \`models/natty\_detector\_model.pth\`).  
    \* Consulte \`scripts/train\_model.py\` para uma visão geral do processo. \*Nota: Este script é um guia e não executa diretamente o treinamento com Detectron2.\*

4\.  \*\*Desenvolvimento da Interface Web (Flask)\*\*:  
    \* Criar uma aplicação Flask (\`app/main.py\`) para:  
        \* Servir uma página HTML (\`app/templates/index.html\`) com um formulário de upload de imagem.  
        \* Receber a imagem enviada pelo usuário.  
        \* Chamar uma função de predição (\`app/predictor.py\`) que carrega o modelo treinado e classifica a imagem.  
        \* Exibir o resultado da classificação na página.  
    \* O \`app/predictor.py\` inicialmente conterá uma lógica de simulação. Você precisará integrá-lo com seu modelo Detectron2 treinado.

5\.  \*\*Testes e Iteração\*\*:  
    \* Testar o upload de imagens e a funcionalidade de classificação.  
    \* Refinar o modelo e a interface conforme necessário.

\#\# 🚀 Resultados  
O resultado final será uma aplicação web onde o usuário pode fazer upload de uma imagem e receber uma classificação indicando se a imagem é provavelmente "natty" (real) ou "not natty" (gerada/alterada por IA).

\*\*Exemplo de saída (simulada):\*\*  
\* Imagem: \`minha\_foto.jpg\`  
\* Predição: \`Not Natty (IA)\`  
\* Confiança: \`Real: 15%, IA: 85%\`

\*(Após treinar e integrar seu modelo, você poderá apresentar resultados reais aqui, como capturas de tela da interface e exemplos de classificação.)\*

\#\# 🛠️ Como Executar o Projeto (Interface Web com Preditor Simulado)

1\.  Clone este repositório: \`git clone \<URL\_DO\_SEU\_REPOSITORIO\_NO\_GITHUB\>\`  
2\.  Navegue até o diretório do projeto: \`cd natty-or-not-detector\`  
3\.  Crie e ative um ambiente virtual:  
    \`\`\`bash  
    python \-m venv venv  
    venv\\Scripts\\activate   
    \`\`\`  
4\.  Instale as dependências:  
    \`\`\`bash  
    pip install \-r requirements.txt  
    \`\`\`  
5\.  Execute a aplicação Flask:  
    \`\`\`bash  
    python app/main.py  
    \`\`\`  
6\.  Abra seu navegador e acesse \`http://127.0.0.1:5000/\`.

\#\# 💭 Reflexão (Opcional)  
Este projeto destaca o poder das IAs Generativas não apenas na criação de conteúdo, mas também na geração de dados para treinar outros modelos de IA. O desafio de distinguir entre conteúdo real e gerado por IA ("natty or not") é cada vez mais relevante na era digital. Desenvolver um detector como este proporciona um aprendizado valioso sobre o ciclo de vida de projetos de Machine Learning, desde a coleta e preparação de dados até o treinamento e deployment de modelos.

\---  
\*Este README é um template. Adapte-o com os detalhes específicos do seu desenvolvimento e descobertas.\*  
