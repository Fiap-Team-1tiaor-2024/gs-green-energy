#include <Ultrasonic.h> // Biblioteca para o sensor ultrassônico

#define LDR_PIN 14           // Pino conectado ao divisor de tensão do LDR
#define TRIG_PIN 5           // Pino TRIG do sensor ultrassônico
#define ECHO_PIN 17          // Pino ECHO do sensor ultrassônico
#define RELAY_PIN 18         // Pino de controle do relé

const int LDR_THRESHOLD = 2000;  // Limiar de luz baixa (ajustar conforme necessário)
const int DISTANCE_THRESHOLD = 96; // Distância máxima para detectar algo (em cm)

Ultrasonic ultrasonic(TRIG_PIN, ECHO_PIN);

void setup() {
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  pinMode(RELAY_PIN, OUTPUT);

  digitalWrite(RELAY_PIN, LOW); // Liga o LED amarelo inicialmente (NC ativo)
  Serial.begin(115200);         // Inicializa o monitor serial
}

void loop() {
  int ldrValue = analogRead(LDR_PIN); // Leitura analógica do LDR
  int distance = ultrasonic.read();  // Calcula a distância pelo sensor ultrassônico

  if (ldrValue < LDR_THRESHOLD || distance < DISTANCE_THRESHOLD) {
    // Se o LDR detectar luz baixa ou o sensor ultrassônico detectar algo próximo:
    Serial.println("Presença detectada! Luz de alarme ligada!");
    Serial.print("A distância em cm detectada é de: ");
    Serial.println(distance);
    Serial.println("--------------------");
    blinkRedLed(); // Pisca o LED vermelho
  } else {
    // Condição normal: Luz amarela ativa
    Serial.println("Nenhuma presença detectada.");
    Serial.println("--------------------");
    digitalWrite(RELAY_PIN, LOW); // Mantém NC ativo (LED amarelo)
  }

  delay(300); // Pequena pausa para estabilidade
}

// Função para piscar o LED vermelho
void blinkRedLed() {
  digitalWrite(RELAY_PIN, HIGH); // Liga o LED vermelho
  delay(100);
  digitalWrite(RELAY_PIN, LOW);  // Desliga o LED vermelho
  delay(100);
}