#include <Adafruit_NeoPixel.h>
#include <Arduino.h>
#define PIN 2
#define MAX_LED 14
Adafruit_NeoPixel strip0 = Adafruit_NeoPixel(14, 2, NEO_GRB + NEO_KHZ800);
Adafruit_NeoPixel strip1 = Adafruit_NeoPixel(14, 3, NEO_GRB + NEO_KHZ800);
Adafruit_NeoPixel strip2 = Adafruit_NeoPixel(14, 4, NEO_GRB + NEO_KHZ800);
Adafruit_NeoPixel strip3 = Adafruit_NeoPixel(14, 5, NEO_GRB + NEO_KHZ800);

const byte p0 = A1;       // buzzer player 1
const byte p1 = A2;       // buzzer player 2
const byte p2 = A3;       // buzzer player 3
const byte p3 = A4;       // buzzer player 4
const byte l0 = 10;       // led player 1 on control unit
const byte l1 = 11;       // led player 2 on control unit
const byte l2 = 12;       // led player 3 on control unit
const byte l3 = 13;       // led player 4 on control unit
const byte clearPin = A5; // clear button

int last_led = MAX_LED - 1; // last led
int counter = 0;            // counter for the led strip
int counter_strip0 = 0;     // counter for the led strip
int counter_strip1 = 0;     // counter for the led strip
int counter_strip2 = 0;     // counter for the led strip
int counter_strip3 = 0;     // counter for the led strip
int buzzer_1_active = 1;
int buzzer_2_active = 1;
int buzzer_3_active = 1;
int buzzer_4_active = 1;

int clearPinState = 4; // inactive buzzer (0 = all active)
int clearPinValue = HIGH;

int buzzer_1_idlecolor_r = 0; // idle color (slow blinking)
int buzzer_1_idlecolor_g = 160;
int buzzer_1_idlecolor_b = 0;
int buzzer_2_idlecolor_r = 0;
int buzzer_2_idlecolor_g = 160;
int buzzer_2_idlecolor_b = 0;
int buzzer_3_idlecolor_r = 0;
int buzzer_3_idlecolor_g = 160;
int buzzer_3_idlecolor_b = 0;
int buzzer_4_idlecolor_r = 0;
int buzzer_4_idlecolor_g = 160;
int buzzer_4_idlecolor_b = 0;

int leuchten = 0;
char stripname;

int idlecolor_r = 0;
int idlecolor_g = 255;
int idlecolor_b = 0;

int activate_color_r = 100; // color for "BUZZED"
int activate_color_g = 0;
int activate_color_b = 0;

int blinkcolor_r = 0; // color for "blink"
int blinkcolor_g = 0;
int blinkcolor_b = 255;

struct Player { // per player
  byte buzzer;  // ... pin for buzzer
  byte led;     // ... pin for led
};

Player const player[]{{p0, l0}, // pin for buzzer, pin for led
                      {p1, l1},
                      {p2, l2},
                      {p3, l3}};


// enumeration for states
enum class State {
  IDLE, // wait for first button press (get blocked buzzer number from python)
  BUZZED, // send buzzed buzzer to python and light up
  WAIT_FOR_CLEAR // wait and blink, get reset button from python
} state;         // store state in this variable

int8_t pressed = -1;                // which button was pressed
uint32_t previousMillis = 0;        // timestamp (blink without delay)
uint32_t previousMillis_strip0 = 0; // timestamp (blink without delay)
uint32_t previousMillis_strip1 = 0; // timestamp (blink without delay)
uint32_t previousMillis_strip2 = 0; // timestamp (blink without delay)
uint32_t previousMillis_strip3 = 0; // timestamp (blink without delay)
uint32_t previousMillis_clearPin = 0;
uint32_t previousMillis_peep = 0;
String buzzer_blocked = "4";

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(1);
  // Serial.println(F("\nBuzzer"));
  // Serial.println(F("press a buzzer..."));
  strip0.begin();
  strip0.show();
  strip1.begin();
  strip1.show();
  strip2.begin();
  strip2.show();
  strip3.begin();
  strip3.show();
  pinMode(clearPin, INPUT_PULLUP);
  // buzzer 1-4
  for (auto &i : player) {
    pinMode(i.buzzer, INPUT_PULLUP); // all against ground
    pinMode(i.led, OUTPUT);          // LEDs are outputs
  }
}

void loop() {
  read_blocked_buzzer();
  switch (state) {
  case State::IDLE:

    // wait for first button press
    if (millis() - previousMillis_strip0 > 250) { // blinkzeit
      if (clearPinState == 0) {
        buzzer_1_idlecolor_r = 100;
        buzzer_1_idlecolor_g = 0;
      } else {
        buzzer_1_idlecolor_r = 0;
        buzzer_1_idlecolor_g = 100;
      }
      if (counter_strip0 == 0) {
        strip0.setPixelColor(last_led, (strip0.Color(0, 0, 0)));
        strip0.show();
      } else {
        strip0.setPixelColor(counter_strip0 - 1, (strip0.Color(0, 0, 0)));
        strip0.show();
      }
      strip0.setPixelColor(
          counter_strip0,
          (strip0.Color(buzzer_1_idlecolor_r, buzzer_1_idlecolor_g,
                        buzzer_1_idlecolor_b)));
      strip0.show();
      counter_strip0 = counter_strip0 + 1;
      if (counter_strip0 > last_led) {
        counter_strip0 = 0;
      }
      previousMillis_strip0 = millis();
    }

    if (millis() - previousMillis_strip1 > 250) { // blinkzeit
      if (clearPinState == 1) {
        buzzer_2_idlecolor_r = 100;
        buzzer_2_idlecolor_g = 0;
      } else {
        buzzer_2_idlecolor_r = 0;
        buzzer_2_idlecolor_g = 100;
      }
      if (counter_strip1 == 0) {
        strip1.setPixelColor(last_led, (strip1.Color(0, 0, 0)));
        strip1.show();
      } else {
        strip1.setPixelColor(counter_strip1 - 1, (strip1.Color(0, 0, 0)));
        strip1.show();
      }
      strip1.setPixelColor(
          counter_strip1,
          (strip1.Color(buzzer_2_idlecolor_r, buzzer_2_idlecolor_g,
                        buzzer_2_idlecolor_b)));
      strip1.show();
      counter_strip1 = counter_strip1 + 1;
      if (counter_strip1 > last_led) {
        counter_strip1 = 0;
      }
      previousMillis_strip1 = millis();
    }

    if (millis() - previousMillis_strip2 > 250) { // blinkzeit
      if (clearPinState == 2) {
        buzzer_3_idlecolor_r = 100;
        buzzer_3_idlecolor_g = 0;
      } else {
        buzzer_3_idlecolor_r = 0;
        buzzer_3_idlecolor_g = 100;
      }
      if (counter_strip2 == 0) {
        strip2.setPixelColor(last_led, (strip2.Color(0, 0, 0)));
        strip2.show();
      } else {
        strip2.setPixelColor(counter_strip2 - 1, (strip2.Color(0, 0, 0)));
        strip2.show();
      }
      strip2.setPixelColor(
          counter_strip2,
          (strip2.Color(buzzer_3_idlecolor_r, buzzer_3_idlecolor_g,
                        buzzer_3_idlecolor_b)));
      strip2.show();
      counter_strip2 = counter_strip2 + 1;
      if (counter_strip2 > last_led) {
        counter_strip2 = 0;
      }
      previousMillis_strip2 = millis();
    }

    if (millis() - previousMillis_strip3 > 250) { // blinkzeit
      if (clearPinState == 3) {
        buzzer_4_idlecolor_r = 100;
        buzzer_4_idlecolor_g = 0;
      } else {
        buzzer_4_idlecolor_r = 0;
        buzzer_4_idlecolor_g = 100;
      }
      if (counter_strip3 == 0) {
        strip3.setPixelColor(last_led, (strip3.Color(0, 0, 0)));
        strip3.show();
      } else {
        strip3.setPixelColor(counter_strip3 - 1, (strip3.Color(0, 0, 0)));
        strip3.show();
      }
      strip3.setPixelColor(
          counter_strip3,
          (strip3.Color(buzzer_4_idlecolor_r, buzzer_4_idlecolor_g,
                        buzzer_4_idlecolor_b)));
      strip3.show();
      counter_strip3 = counter_strip3 + 1;
      if (counter_strip3 > last_led) {
        counter_strip3 = 0;
      }
      previousMillis_strip3 = millis();
    }

    for (byte i = 0; i < sizeof(player) / sizeof(player[0]); i++) {
      if (digitalRead(player[i].buzzer) == LOW) {
        if (clearPinState != i) {
          clear_leds();
          pressed = i; // remember pressed index
          Serial.println(i);
          state = State::BUZZED; // state machine go on
          previousMillis = millis();
          break; // break at pressed key
        }
      }
    }
    break;
 
  case State::BUZZED: // light up all leds on pressed buzzer red for 500 milliseconds
    if (pressed == 0) {
      for (int i = 0; i < MAX_LED; i++) {
        strip0.setPixelColor(i,
                             (strip0.Color(activate_color_r, activate_color_g,
                                           activate_color_b)));
      }
      strip0.show();
    }
    if (pressed == 1) {
      for (int i = 0; i < MAX_LED; i++) {
        strip1.setPixelColor(i,
                             (strip1.Color(activate_color_r, activate_color_g,
                                           activate_color_b)));
      }
      strip1.show();
    }
    if (pressed == 2) {
      for (int i = 0; i < MAX_LED; i++) {
        strip2.setPixelColor(i,
                             (strip2.Color(activate_color_r, activate_color_g,
                                           activate_color_b)));
      }
      strip2.show();
    }
    if (pressed == 3) {
      for (int i = 0; i < MAX_LED; i++) {
        strip3.setPixelColor(i,
                             (strip3.Color(activate_color_r, activate_color_g,
                                           activate_color_b)));
      }
      strip3.show();
    }
    if (millis() - previousMillis > 750) // Einschaltdauer für den BUZZED
    {
      clear_leds();
      state = State::WAIT_FOR_CLEAR;
      // Serial.println(F("wait for reset"));
      counter = 0;
    }

    break;


  case State::WAIT_FOR_CLEAR: // pressed buzzer blinks until reset button is pressed (python)
  read_blocked_buzzer();
    leuchten = 0;
    if (pressed == 0) {
      if (millis() - previousMillis > 40) { // blinkzeit
        if (counter == 0) {
          strip0.setPixelColor(last_led, (strip0.Color(0, 0, 0)));
          strip0.show();
        } else {
          strip0.setPixelColor(counter - 1, (strip0.Color(0, 0, 0)));
          strip0.show();
        }
        strip0.setPixelColor(
            counter, (strip0.Color(blinkcolor_r, blinkcolor_g, blinkcolor_b)));
        strip0.show();
        counter = counter + 1;
        if (counter > last_led) {
          counter = 0;
        }
        previousMillis = millis();
      }
    }
    if (pressed == 1) {
      if (millis() - previousMillis > 40) {
        if (counter == 0) {
          strip1.setPixelColor(last_led, (strip1.Color(0, 0, 0)));
          strip1.show();
        } else {
          strip1.setPixelColor(counter - 1, (strip1.Color(0, 0, 0)));
          strip1.show();
        }
        strip1.setPixelColor(counter, (strip1.Color(0, 0, 255)));
        strip1.show();
        counter = counter + 1;
        if (counter > last_led) {
          counter = 0;
        }
        previousMillis = millis();
      }
    }
    if (pressed == 2) {
      if (millis() - previousMillis > 40) {
        if (counter == 0) {
          strip2.setPixelColor(last_led, (strip2.Color(0, 0, 0)));
          strip2.show();
        } else {
          strip2.setPixelColor(counter - 1, (strip2.Color(0, 0, 0)));
          strip2.show();
        }
        strip2.setPixelColor(counter, (strip2.Color(0, 0, 255)));
        strip2.show();
        counter = counter + 1;
        if (counter > last_led) {
          counter = 0;
        }
        previousMillis = millis();
      }
    }
    if (pressed == 3) {
      if (millis() - previousMillis > 40) {
        if (counter == 0) {
          strip3.setPixelColor(last_led, (strip3.Color(0, 0, 0)));
          strip3.show();
        } else {
          strip3.setPixelColor(counter - 1, (strip3.Color(0, 0, 0)));
          strip3.show();
        }
        strip3.setPixelColor(counter, (strip3.Color(0, 0, 255)));
        strip3.show();
        counter = counter + 1;
        if (counter > last_led) {
          counter = 0;
        }
        previousMillis = millis();
      }
    }

    if (digitalRead(clearPin) == LOW || clearPinState == 5) // checken ob Neustart gedrückt wird
    {
      clear_leds();
      // Serial.println(F("clear game"));
    //   digitalWrite(player[pressed].led, LOW);
      pressed = -1;
      state = State::IDLE;
      // Serial.println(F("started new game"));
      counter_strip0 = 0;
      counter_strip1 = 0;
      counter_strip2 = 0;
      counter_strip3 = 0;
      clearPinState = 4;
      Serial.println(4);
    }
    break;
  }
}

void clear_leds() {
  for (int i = 0; i < MAX_LED; i++) {
    strip0.setPixelColor(i, (strip0.Color(0, 0, 0)));
    strip1.setPixelColor(i, (strip1.Color(0, 0, 0)));
    strip2.setPixelColor(i, (strip2.Color(0, 0, 0)));
    strip3.setPixelColor(i, (strip3.Color(0, 0, 0)));
  }
  strip0.show();
  strip1.show();
  strip2.show();
  strip3.show();
}

void read_blocked_buzzer() {
  if (Serial.available())
  {
    buzzer_blocked = Serial.readString();
    clearPinState = buzzer_blocked.toInt();
    // Serial.print(F("blocked buzzer: "));
    // Serial.println(clearPinState);
  }
}