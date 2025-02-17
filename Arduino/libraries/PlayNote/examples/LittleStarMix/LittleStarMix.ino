#include <PlayNote.h>

PlayNote playnote;

struct PlayNote::notes song[] = {
	{"do4", 1}, {"do4", 1}, {"sol4", 1}, {"sol4", 1}, {"la4", 0.5}, {"si4", 0.5}, {"do5", 0.5}, {"la4", 0.5}, {"sol4", 1}, {"0", 1},
	{"fa4", 1}, {"fa4", 0.5}, {"sol4", 0.5}, {"mi4", 1}, {"mi4", 1}, {"re4", 1}, {"re4", 1}, {"sol4", 1}, {"0", 1},
	{"do4", 1}, {"do4", 1}, {"sol4", 1}, {"sol4", 1}, {"la4", 0.5}, {"si4", 0.5}, {"do5", 0.5}, {"la4", 0.5}, {"sol4", 1}, {"0", 1},
	{"fa4", 1}, {"fa4", 0.5}, {"sol4", 0.5}, {"mi4", 1}, {"mi4", 1}, {"re4", 1}, {"re4", 0.5}, {"mi4", 0.5}, {"do4", 1}, {"0", 1}
};
int len = sizeof(song)/sizeof(PlayNote::notes);

void setup() {
  Serial.begin(115200);
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