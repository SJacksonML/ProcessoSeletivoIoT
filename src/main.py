from machine import Pin
import time

print("Teste") # Obrigatório pelos parâmetros do teste

# Primeiro, vamos habilitar os pinos a serem utilizados
botao = Pin(26, Pin.IN, Pin.PULL_UP)
led = Pin(22, Pin.OUT)
buzzer = Pin(23, Pin.OUT)
pir_z1 = Pin(14, Pin.IN)
pir_z3 = Pin(27, Pin.IN)
gas_z2 = Pin(12, Pin.IN)

# Definiremos três estados para nossa Central de Alarme
DESARMADO = 0
ARMADO = 1
DISPARADO = 2

# Variáveis de controle gerais
estado = DESARMADO
zona_disparo = None

# Variáveis de controle para zona temporizada
tempo_z3_inicio = None
delay_z3 = 5000  # 5 segundos
ultimo_blink = 0
estado_led = 0

# Função do LED
def piscar_led(vezes, tempo=0.2):
    for _ in range(vezes):
        led.on()
        time.sleep(tempo)
        led.off()
        time.sleep(tempo)

# Entrando no Loop Principal
while True:

    # Parâmetros de comportamento do botão ARME/DESARME
    if botao.value() == 0:
        time.sleep(0.25)
        if estado == DESARMADO:
            estado = ARMADO
            zona_disparo = None
            piscar_led(1)
        else:
            estado = DESARMADO
            tempo_z3_inicio = None
            zona_disparo = None
            buzzer.off()
            led.off()
            piscar_led(2)
        while botao.value() == 0:
            pass

    if estado == ARMADO:
        # ZONA 1 - imediata
        if pir_z1.value():
            estado = DISPARADO
            zona_disparo = "ZONA 1 - ESTOQUE"

        # ZONA 2 - imediata
        elif gas_z2.value():
            estado = DISPARADO
            zona_disparo = "ZONA 2 - GAS"

        # ZONA 3 - temporizada
        elif pir_z3.value() and tempo_z3_inicio is None:
            tempo_z3_inicio = time.ticks_ms()
            zona_disparo = "ZONA 3 - ENTRADA PRINCIPAL"

    # Temporização da Zona 03
    if tempo_z3_inicio is not None and estado == ARMADO:
        agora = time.ticks_ms()

        # piscar lento (500ms)
        if time.ticks_diff(agora, ultimo_blink) > 500:
            ultimo_blink = agora
            estado_led = not estado_led
            led.value(estado_led)

        # verifica tempo
        if time.ticks_diff(agora, tempo_z3_inicio) >= delay_z3:
            estado = DISPARADO
            tempo_z3_inicio = None

    # Para gerar um disparo
    if estado == DISPARADO:
        buzzer.on()
        led.on()
        time.sleep(0.1)
        led.off()
        time.sleep(0.1)
        continue

    # Redefinição das variávis ao desarmar a zona
    if estado == DESARMADO:
        led.off()
        buzzer.off()
        tempo_z3_inicio = None
    time.sleep(0.05)