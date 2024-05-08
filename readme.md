# Resgate de pessoas em alagamentos no sul

# Visão Geral

O **Flood Rescue Assistant** é um projeto de código aberto desenvolvido para auxiliar equipes de resgate durante enchentes e alagamentos severos, especialmente no sul do Brasil. Utilizando a tecnologia de visão computacional com a rede neural YOLOv8, o sistema identifica pessoas ilhadas nos telhados das casas e emite alertas automáticos para facilitar operações de resgate. Salvando a localização do ocorrido com coordenadas. 

## Como Funciona

O sistema utiliza a rede YOLOv8 para detectar simultaneamente as classes "pessoa" e "telhado" em imagens aéreas capturadas por drones ou outras câmeras. Quando ambas as classes são identificadas na mesma região da imagem, um alerta é gerado na interface do software, indicando a localização precisa das pessoas necessitadas de resgate.

## Instalação

### Pré-requisitos

- Python 3.11 ou superior
- Bibliotecas Python: `opencv-python`, `numpy`, `torch`
- Acesso a uma GPU compatível com CUDA para processamento de imagens em tempo real

### Passos para instalação

Clone o repositório:

```bash
git clone https://github.com/seuusuario/flood-rescue-assistant.git
cd flood-rescue-assistant
```
