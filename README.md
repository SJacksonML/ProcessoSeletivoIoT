# Projeto de IoT - Processo Seletivo PNAAT

**- Nome:** Samuel Jackson Mesquita Lima  
**- E-mail:** samuel.jacksonjml@gmail.com  
**- Data da entrega:** 26/04/2026 

## 📌 Resumo do Projeto
> Trata-se de um sistema de segurança eletrônica que utiliza o conceito de supervisão por contato NF (Normalmente Fechado). O sistema simula o funcionamento de uma central de alarme ao supervisionar as ferramentas de UP e DOWN do simulador e do ESP32 para supervisão;
> Basicamente, o sistema de segurança varia entre três modos: `ARMADO`, `DESARMADO` e `DISPARADO`. Enquanto desarmado, nada acontece. Se o sistema estiver armado, no entanto, supervisiona o estado dos sensores PIR e de gás/fumaça e, caso se abra o contato NF, o sistema vai para o estado de disparo, onde uma sirene é acionada, informando que um dos sensores detectou ameaça.

## 📲 Como executar
**1.** Instale as dependências: `pip install -r requirements.txt`  
**2.** Acesse o simulador Wokwi  
**3.** Execute o simulador  
**4.** Arme o sistema através do botão ARME/DESARME e observe seu comportamento ao interagir com os sensores  

## 📂 Arquivos
```
ProcessoSeletivoIA/  
 ├── src/
 │   └── main.py        # Código principal do projeto
 ├── wokwi.toml         # Configuração da simulação
 ├── diagram.json       # Circuito no Wokwi
 └── README.md          # Explicação do seu projeto
```

## 🧩 Composição do Sistema de Segurança dentro do simulador
**- 1.** Um microcontrolador ESP32: `wokwi-esp32-devkit-v1`  
**- 2.** Um botão: `wokwi-pushbutton`  
**- 3.** Um led: `wokwi-led`  
**- 4.** Uma sirene: `wokwi-buzzer`  
**- 5.** Um sensor de movimento: `wokwi-pir-motion-sensor`  
**- 6.** Um sensor de fumaça: `wokwi-gas-sensor`  
**- 7.** Um resistor de 150 Ohms: `wokwi-resistor`  

## ☑️ Resultados Obtidos
- **O botão simula um efeito de arme/desarme perfeitamente**
- **O sensor de movimento gera disparo quando detecta movimento e o sistema está armado**
- **O sensor de fumaça gera disparo quando detecta abaixo de 350 ppm e o sistema está armado**
- **A sirene (buzzer) soa ininterruptamente após um disparo até que o sistema seja novamente desarmado**
- **O LED pisca 1 vez para indicar ARME, 2 vezes parra indicar DESARME e pisca ininterruptamente enquanto houver DISPARO**

## 💬 Comentários adicionais
- O simulador não atende bem às ligações OLED e outros displays acabam sendo muito pesados/complexos para um projeto de caráter apenas experimental, sendo descartada a ideia de um print visual que indicque a zona disparada, apesar de ter em código variável `zona_disparo`que armazena a informação da última zona disparada;
- As instruções do Actions, do vídeo e/ou do README inicial não ajudam a resolver o problema da Key do simulador Wokwi, que parece ter instruções erradas para acessar o Secrects do repositório.

## 🔍 Link para o repositório original do desafio
[Repositório base PNAT](https://github.com/pnaat/processoseletivoIoT).
