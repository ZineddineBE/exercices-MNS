#ifndef PLAYNOTE_H
#define PLAYNOTE_H
#include "Arduino.h"
/*
tempo default = 100
  Xu ly cac dang dau vao nhu sau:
    Tab Kalimba:
      1) "1", "2", "3", "4", "5", "6", "7"
      2) " 1' ", " 2' ", " 3' ", " 4' ", " 5' ", " 6' ", " 7' "
      3) ".1", ".2", ".3", ".4", ".5", ".6", ".7"
      4) " 1'' ", " 2'' ", " 3'' ", " 4'' ", " 5'' ", " 6'' ", " 7'' "
      5) " A' ", " .A ", " A ", " A'' "
    Tab thong thuong
      1) "C", "C#"
      2) "Cb"
      3) "C5", "C#5"

 Quarter note = 25600/tempo 
 l = 256 = Quarter note
 t = do dai not = l * 2^k = length of note (value is cal when l = 128)
 64 = not tron tu = l * 2^5 = 4096 ms = Large (Latin: Maxima) / Octuple whole note
 32 = not tron ba = l * 2^4 = 2048 ms = Long / Quadruple whole note
 16 = not tron doi = l * 2^3 = 1024 ms = Breve / Double whole note
 8 = not tron = l * 2^2 = 512 ms = Semibreve / Whole note
 2 = not trang = l * 2^1 = 256 ms = Minim / Half note
 1 = not den = l * 2^0 = 128 ms = Crotchet / Quarter note = 100
 0.5 = not moc don = l * 2^-1 = 64 ms = Quaver / Eighth note = 50
 0.25 = not moc kep = l * 2^-2 = 32 ms = Semiquaver / Sixteenth note = 25
 0.125 = not moc ba = l * 2^-3 = 16 ms = Demisemiquaver / Thirty-second note
 0.0625 = not moc tu = l * 2^-4 = 8 ms = Hemidemisemiquaver / Sixty-fourth note
 0.03125 = not moc nam = l * 2^-5 = 4 ms = Semihemidemisemiquaver / Quasihemidemisemiquaver / Hundred twenty-eighth note
 0.015625 = not moc sau = l * 2^-6 = 2 ms = Demisemihemidemisemiquaver / Two hundred fifty-sixth note
 
*/
class PlayNote{
	private:
		uint8_t buzzerPin;
		int lengthQuarterNote = 256;
		bool isPrint = true;
	public:
		PlayNote();
		void setPrint(bool);
		void setBuzzerPin(int);
		void setTempo(int);
		char* toUppercase(char *, int);
		int diff(const char *);
		float ffreq(const char *);
		int freq(const char *);
		struct notes {
            const char *name;
            float length;
        };
		void play(int);
		void playTime(struct notes);
		void playSong(struct notes[], int);
		
};
#endif
