#include <PlayNote.h>

PlayNote playnote;

struct PlayNote::notes song[] = {
  // Dao dau                                 |                                                                      |                                         |
    {"sol4", 1.5}, {"la4", 1.5}, {"re4", 1}, {"la4", 2.5}, {"si4", 1.5}, {"re5", 0.25}, {"do5", 0.25}, {"si4", 0.5}, {"sol4", 1.5}, {"la4", 1.5}, {"re4", 1}, {"re4", 1.5}, {"0", 1}, {"re4", 0.25}, {"re4", 0.25}, {"mi4", 0.25}, {"sol4", 0.5}, {"sol4", 0.25},
  //             We're          no          stran       -gers         to          love            ...         ...
    {"0", 1}, {"e4", 0.5}, {"f#4", 0.5}, {"g4", 0.5}, {"g4", 0.5}, {"a4", 0.5}, {"f#4", 0.75}, {"mi4", 0.25}, {"re4", 2.5}, {"0", 1}, 
  //              You           know          the           rule        ...         and           so                        do          i
    {"0", 0.5}, {"e4", 0.5}, {"e4", 0.5}, {"f#4", 0.5}, {"g4", 0.5}, {"mi4", 1}, {"d4", 0.5}, {"d5", 0.5}, {"0", 0.5}, {"d5", 0.5}, {"a4", 1.5}, {"0", 1}, 
  //    A           full          com         -mit          -ment's       what        I'm                     think       -ing            of
    {"e4", 0.5}, {"e4", 0.5}, {"f4", 0.5}, {"g4", 0.5}, {"g4", 0.5}, {"g4", 0.5}, {"a4", 0.5}, {"0", 1}, {"f#4", 0.5}, {"e4", 0.5}, {"d4", 1.5}, {"0", 1}, 
  //                You         would         -n't          get         this          from        An          -y          oth           -er           guy
    {"0", 0.5}, {"e4", 0.5}, {"e4", 0.5}, {"f#4", 0.5}, {"g4", 0.5}, {"e4", 0.5}, {"d4", 1}, {"a4", 0.5}, {"a4", 0.5}, {"a4", 0.5}, {"b4", 0.5}, {"a4", 0.5}, {"0", 1}, 
  //      I         just        wan           -na           tell        you           how         I'm           fell          -ing
    {"g4", 2.5}, {"a4", 0.5}, {"b4", 0.5}, {"g4", 0.5}, {"a4", 0.5}, {"a4", 0.5}, {"a4", 0.5}, {"b4", 0.5}, {"a4", 0.5}, {"d4", 0.5}, {"0", 2}, 
  //    Got         -ta           make          you                     un          -der         -stand
    {"e4", 0.5}, {"f#4", 0.5}, {"g4", 0.5}, {"e4", 0.5}, {"0", 0.5}, {"a4", 0.5}, {"b4", 0.5}, {"a4", 1.5}, 
  //    Nev     - er              gon       -   na            give          you           up      
    {"D4", 0.25}, {"E4", 0.25}, {"G4", 0.25}, {"E4", 0.25}, {"B4", 0.75}, {"B4", 0.75}, {"A4", 1.5},
  //    Nev     - er              gon       -   na            let          you           down        ...            ...
    {"D4", 0.25}, {"E4", 0.25}, {"G4", 0.25}, {"E4", 0.25},{"A4", 0.75}, {"A4", 0.75}, {"G4", 0.75}, {"F4", 0.25}, {"E4", 0.5}, 
  //    Nev     - er              gon       -   na           run          a           ...           ...           round         and         de        -   sert      you
    {"D4", 0.25}, {"E4", 0.25}, {"G4", 0.25}, {"E4", 0.25}, {"G4", 1}, {"A4", 0.5}, {"F#4", 0.75}, {"E4", 0.25}, {"D4", 0.5}, {"D4", 0.5}, {"D4", 0.5}, {"A4", 1}, {"G4", 2},
  //    Nev     - er              gon       -   na            make          you           cry      
    {"D4", 0.25}, {"E4", 0.25}, {"G4", 0.25}, {"E4", 0.25}, {"B4", 0.75}, {"B4", 0.75}, {"A4", 1.5},
  //    Nev     - er              gon       -   na           say          good           bye      
    {"D4", 0.25}, {"E4", 0.25}, {"G4", 0.25}, {"E4", 0.25}, {"D5", 1}, {"F#4", 0.5}, {"G4", 0.75}, {"F#4", 0.25}, {"E4", 0.5},  
  //    Nev     - er              gon       -   na           tell          a             lie           ...         ...         and          hurt      you
    {"D4", 0.25}, {"E4", 0.25}, {"G4", 0.25}, {"E4", 0.25}, {"G4", 1}, {"A4", 0.5}, {"F#4", 0.75}, {"E4", 0.25}, {"D4", 1}, {"D4", 0.5}, {"A4", 1}, {"G4", 2}, {"0", 1}
};
int len = sizeof(song)/sizeof(PlayNote::notes);

void setup() {
  Serial.begin(115200);
  playnote.setTempo(150);
  playnote.setBuzzerPin(13);
  // playnote.setPrint(false);
  playnote.play(784); // play a exactly Hz
  playnote.play(880);
  playnote.play(988);
  playnote.play(1047);
  delay(2000);
}

void loop() {
  playnote.playSong(song, len);
  playnote.playTime({"0", 1}); //For silent in 1
  playnote.playTime({"1'", 1});//Kalimba tab
  playnote.playTime({"Sol", 1.25});// Sol = Sol4
  playnote.playTime({"E4", 1.5});// ABC tab
  playnote.playTime({"Do4", 1.75});// Do re mi tab
  delay(5000);
}