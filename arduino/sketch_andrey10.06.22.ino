// Имитируем речь человека и управляем роботом
void setup() {
pinMode(5,OUTPUT);
pinMode(6,OUTPUT);
pinMode(7,OUTPUT);
pinMode(3,OUTPUT);
pinMode(13,OUTPUT);
pinMode(12,INPUT);
digitalWrite(5,1);
digitalWrite(6,1);
digitalWrite(7,1);
}

int nrep={-1}; //nrep -  номер реплики.
int repR[]={3,3,1,5,4,7,4};
int repH[]={1,3,7,2,5};
word i;


void loop() {
  while(digitalRead(12)!=0){} digitalWrite(13,1); delay(50); while(digitalRead(12)==0){} digitalWrite(13,0); delay(50); //Ждем нажатия и отпускания кнопки.
  digitalWrite(7,0); delay(50); digitalWrite(7,1); //Двигаем через реле звук(In3-D7).
  i=50;
  nrep++;
  if(repH[nrep]<0){ while(true){}}
  
  if(250<=repR[nrep]*1000<1000){
  digitalWrite(5,0); //Открыли рот. Подали сигнал на реле.
    delay(50);
    digitalWrite(5,1);
    delay(abs(repR[nrep]-50)/2);
    
    digitalWrite(6,0);//Закрыть рот.
    delay(50);
    digitalWrite(6,1);  
  }

  digitalWrite(5,0); //Открыли рот. Подали сигнал на реле.
    delay(50);
    digitalWrite(5,1);
    delay(200);
    
  while(abs(i+50)/100<=repR[nrep]){ //Рот открыт.Вычисление ведется в десятках милисекунд.
    digitalWrite(5,0); //Открыли рот. Подали сигнал на реле.
    delay(50);
    digitalWrite(5,1);
    delay(200);
    
    digitalWrite(6,0);//Закрыть рот.
    delay(50);
    digitalWrite(6,1);
    delay(200);
    i=i+50;
                 }
                 
    digitalWrite(5,0); //Открыли рот. Подали сигнал на реле.
    delay(50);
    digitalWrite(5,1);
}
