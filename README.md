# Projeto de IoT - Processo Seletivo PNAAT

**- Nome:** Samuel Jackson Mesquita Lima  
**- E-mail:** samuel.jacksonjml@gmail.com  
**- Data da entrega:** 26/04/2026 

## 📌 Resumo do Projeto
> Trata-se de um sistema de segurança eletrônica que utiliza o conceito de supervisão por contato NF (Normalmente Fechado). O sistema simula o funcionamento de uma central de alarme ao supervisionar as ferramentas de UP e DOWN do simulador e do ESP32 para supervisão;
> Basicamente, o sistema de segurança varia entre três modos: `ARMADO`, `DESARMADO` e `DISPARADO`. Enquanto desarmado, nada acontece. Se o sistema estiver armado, no entanto, supervisiona o estado dos sensores PIR e de gás/fumaça e, caso se abra o contato NF, o sistema vai para o estado de disparo, onde uma sirene é acionada, informando que um dos sensores detectou ameaça. Além disso, quando uma zona temporizada é acionada, o sistema dá início a um tempo de entrada, intervalo onde o usuário pode desarmar o alarme antes que seja gerado um disparo.

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
**- 1.** 1x microcontrolador ESP32: `wokwi-esp32-devkit-v1`  
**- 2.** 1x botão: `wokwi-pushbutton`  
**- 3.** 1x led: `wokwi-led`  
**- 4.** 1x sirene: `wokwi-buzzer`  
**- 5.** 2x sensores de movimento PIR: `wokwi-pir-motion-sensor`  
**- 6.** 1x sensor de fumaça: `wokwi-gas-sensor`  
**- 7.** 1x resistor de 150 Ohms: `wokwi-resistor`  

## ☑️ Resultados Obtidos
- **O botão simula um efeito de arme/desarme perfeitamente**
- **O sensor de movimento imediato gera disparo quando detecta movimento e o sistema está armado**
- **O sensor de movimento temporizado dá início ao tempo de entrada quando detecta movimento e o sistema está armado**
- **O sensor de fumaça gera disparo quando detecta abaixo de 350 ppm e o sistema está armado**
- **A sirene (buzzer) soa ininterruptamente após um disparo até que o sistema seja novamente desarmado**
- **O LED pisca 1 vez para indicar ARME, 2 vezes parra indicar DESARME, pisca lentamente durante tempo de entrada e pisca ininterruptamente enquanto houver DISPARO**

## 💬 Comentários adicionais
- O simulador não atende bem às ligações OLED e outros displays acabam sendo muito pesados/complexos para um projeto de caráter apenas experimental, sendo descartada a ideia de um print visual que indicque a zona disparada, apesar de ter em código variável `zona_disparo`que armazena a informação da última zona disparada;
- As instruções do Actions, do vídeo e/ou do README inicial não ajudam a resolver o problema da Key do simulador Wokwi, que parece ter instruções erradas para acessar o Secrects do repositório;
- Apesar de seguir todos os passos no README inicial, porposto pelo PNAAT, ainda não é possível passar do `timeout` da CI, acredito que por alguma limitação do simulador ou dos parâmetros do Action. Não consegui passar por esse impecilho, verificar na próxima sessão de tira-dúvidas. 

## Considerações
> Utilizando a ferramenta Claude para identificar possíveis causa do erro por "timeout" a IA sugeriu que o teste estivesse em conflito com o loop infinito do modo de disparo. A ferramenta foi utilziada unicamente para tal finalidade, tentnaod cumprir os parâmetros do teste. Apesar deste e outros esforços, não foi possível identificar a causa.

## 🔍 Link para o repositório original do desafio
[Repositório base PNAT](https://github.com/pnaat/processoseletivoIoT)
