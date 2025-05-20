## Principais Desafios e Soluções Adotadas

Durante o desenvolvimento deste projeto, enfrentei alguns desafios técnicos e de configuração que foram cruciais para o aprendizado e para a definição da arquitetura final da solução:

1.  **Incompatibilidade de Hardware para Stable Diffusion Local:**
    * **Desafio:** Inicialmente, houve uma tentativa de configurar o Stable Diffusion v1.5 localmente. No entanto, encontrei um impasse devido à ausência de uma placa de vídeo NVIDIA compatível com CUDA no meu hardware.
    * **Solução:** Após constatar a incompatibilidade, a estratégia foi adaptada. Decidiu-se utilizar o Google Colab para executar o Stable Diffusion Web UI, aproveitando as GPUs disponíveis na nuvem para a geração do dataset de imagens "not natty".

2.  **Conflito com Caracteres Especiais em Nomes de Pasta:**
    * **Desafio:** Um problema inicial ocorreu devido ao nome da pasta do projeto, que continha a palavra "portfólio" com acentuação. Alguns scripts não lidaram bem com o caractere especial, resultando em erros de "caminho não encontrado".
    * **Solução:** A pasta foi renomeada para um nome sem acentos (ex: "portfolio_projeto"), o que resolveu o conflito e permitiu que os scripts de configuração do ambiente virtual e execução funcionassem corretamente.

3.  **Erro de Localização de Módulo Python (`ModuleNotFoundError`):**
    * **Desafio:** Durante a configuração da aplicação Flask, ocorreu um `ModuleNotFoundError` para o arquivo `predictor.py`. A causa foi uma renomeação manual do arquivo para `app_predictor.py`, fazendo com que o script `app_main.py` não o encontrasse pela importação `from predictor import ...`.
    * **Solução:** O problema foi resolvido ajustando o nome do arquivo para `app_predictor.py` dentro da pasta `app/`, garantindo que a instrução de importação no `app_main.py` pudesse localizar o módulo corretamente.

4.  **Geração de Imagens de IA com Hardware Limitado:**
    * **Desafio:** Devido à ausência de uma GPU NVIDIA local adequada para rodar o Stable Diffusion de forma eficiente, a geração das imagens "not natty" diretamente no meu computador tornou-se inviável.
    * **Solução:** A estratégia adotada foi gerar as imagens "not natty" utilizando o Stable Diffusion Web UI rodando no Google Colab, que oferece acesso a GPUs. As imagens geradas foram então baixadas e adicionadas manualmente ao diretório `dataset/ai/` do projeto local. Esta abordagem também se aplica ao treinamento do modelo de classificação, que será realizado no Google Colab.

Estes desafios foram importantes para reforçar a necessidade de verificar requisitos de hardware, a atenção aos detalhes na nomeação de arquivos e pastas em ambientes de desenvolvimento, e a flexibilidade em adaptar a estratégia do projeto utilizando ferramentas baseadas na nuvem para superar limitações locais.
