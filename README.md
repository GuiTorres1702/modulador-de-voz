# 🥭 Efeito Goiaba – Modificador de Voz em Tempo Real com Python

Este projeto aplica um efeito robótico e grave à voz capturada pelo microfone, processando o áudio em tempo real. Ideal para experimentos com manipulação de áudio, modificadores de voz ou apenas para se divertir com efeitos vocais.

## 🎧 Demonstração

> Ao rodar o script, fale no microfone e ouça sua voz com um efeito robótico e grave, batizado de "efeito Goiaba".

---

## 🧪 Requisitos

Instale as dependências com:

```bash
pip install numpy sounddevice scipy
---------------------------------------------------------------------------------
## 🚀 Como Usar
Altere os IDs de entrada e saída de áudio se necessário (veja seção abaixo).

Execute o script Python:

python efeito_goiaba.py
------------------------------------------------------------------------------------
## 🎛️ Parâmetros Configuráveis

FS = 48000         # Taxa de amostragem (Hz)
DURATION = 0.1     # Latência de cada bloco de áudio (segundos)
FREQ_MOD = 70      # Frequência da modulação robótica (Hz)
PITCH_SHIFT = 0.5  # Fator de pitch (<1 = grave, >1 = agudo)

INPUT_ID = 17      # ID do microfone
OUTPUT_ID = 16     # ID dos alto-falantes

import sounddevice as sd
print(sd.query_devices())

-----------------------------------------------------------------------------

## 🔧 Como Funciona
O processamento acontece em tempo real, em blocos de 100 ms:

Modulação Robótica: Multiplica o áudio por uma senoide de 70 Hz.

Alteração de Pitch: Reduz o pitch da voz usando reamostragem.

Distorção Leve: Usa a função tanh para adicionar compressão leve.

Ajuste de Tamanho: Garante que o áudio modificado tenha o mesmo número de amostras.
----------------------------------------------------------------------------------------
📁 Estrutura do Projeto

efeito_goiaba/
├── efeito_goiaba.py   # Script principal com captura e modificação de áudio
├── README.md          # Este arquivo
-------------------------------------------------------------------------------------------
📌 Observações
Funciona melhor com fones de ouvido (para evitar retorno de som).

Pode haver atraso mínimo (100 ms) por conta da latência configurada.

Ideal para testes de efeitos vocais, música experimental ou modificadores de voz.
-------------------------------------------------------------------------------------------

📜 Licença
Este projeto é de uso livre para fins educacionais e experimentais.

✨ Créditos
Desenvolvido por [GuilhermeT], [BrunoK],[KauaM] inspirado em efeitos robóticos de áudio.
