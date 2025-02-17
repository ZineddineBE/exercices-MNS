#include <PlayNote.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>

PlayNote::PlayNote()
{
	
}
void PlayNote::setPrint(bool _isPrint)
{
	isPrint = _isPrint;
}
void PlayNote::setBuzzerPin(int pin)
{
	buzzerPin = pin;
	pinMode(buzzerPin, INPUT);
}

char* PlayNote::toUppercase(char *x, int len)
{
    char *ans = (char*)malloc(len);
    for(int i = 0; i < len; i++)
    {
        if ('a' <= x[i] && x[i] <= 'z')
        {
            ans[i] = (x[i] - 'a') + 'A';
        }
        else
        {
            ans[i] = x[i];
        }
    }
    return ans;
}

int PlayNote::diff(const char *x)
{
  /*
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
  */
    char name[10];
    char name2[10];
    int num;
    int name_num;
    char dot[5];
    if(sscanf (x, " %d[1-7]", &name_num) == 1) // 5', 5 tab kalimba
    {
      if(name_num == 1)
      {
        name[0] = 'C';
        name[1] = '\0';
      }
      else if(name_num == 2)
      {
        name[0] = 'D';
        name[1] = '\0';
      }
      else if(name_num == 3)
      {
        name[0] = 'E';
        name[1] = '\0';
      }
      else if(name_num == 4)
      {
        name[0] = 'F';
        name[1] = '\0';
      }
      else if(name_num == 5)
      {
        name[0] = 'G';
        name[1] = '\0';
      }
      else if(name_num == 6)
      {
        name[0] = 'A';
        name[1] = '\0';
      }
      else if(name_num == 7)
      {
        name[0] = 'B';
        name[1] = '\0';
      }
      int cnt = 0;
      for (int i = 0; i < strlen(x); i++)
      {
        if(x[i] == '\'' || x[i] == '*' || x[i] == '`') cnt++;
      }
      num = 4 + cnt;
    }
    else if(sscanf (x, " %5[.] %d[1-7]", dot, &name_num) == 2) // .5, .6 tab kalimba
    {
      if(name_num == 1)
      {
        name[0] = 'C';
        name[1] = '\0';
      }
      else if(name_num == 2)
      {
        name[0] = 'D';
        name[1] = '\0';
      }
      else if(name_num == 3)
      {
        name[0] = 'E';
        name[1] = '\0';
      }
      else if(name_num == 4)
      {
        name[0] = 'F';
        name[1] = '\0';
      }
      else if(name_num == 5)
      {
        name[0] = 'G';
        name[1] = '\0';
      }
      else if(name_num == 6)
      {
        name[0] = 'A';
        name[1] = '\0';
      }
      else if(name_num == 7)
      {
        name[0] = 'B';
        name[1] = '\0';
      }
      num = 4 - strlen(dot);
    }
    else if (sscanf (x, " %10[^0-9] %2d[0-9]", name, &num) != 2) 
    {
      if(sscanf (x, " %10[^0-9]", name2) == 1) // C# .C
      {
        int i2 = strlen(name2) - 1;
        while(name2[i2] == ' ')
        {
          i2--;
        }
        name2[i2+1] = '\0';
        char last = name2[strlen(name2) - 1];
        if (name2[0] == '.')
        {
            int cnt = 0;
            int i = 0;
            while(name2[i] == '.')
            {
              cnt++; i++;
            }
            num = 4 - cnt; // .A = A3
            strncpy(name, name2 + i, strlen(name2));
        }
        else if( last == '\'' || last == '*' || last == '`')
        {
          int cnt = 0;
          int i = strlen(name2) - 1;
          while(name2[i] == '\'' || name2[i] == '*' || name2[i] == '`')
          {
            cnt++; i--;
          }
          num = 4 + cnt; // A'' = A6
          i++;
          name[i] = '\0';
        }
        else
        {
          num = 4; // C -> C4
          strcpy(name, name2);
        }
      }
      else
      {
        fputs ("error: invalid input format.\n", stderr);
        return -400; // khi do am thanh phat ra gan nhu không nghe du?c v?i ~0hz
      }
    }
    char *nameUp = toUppercase(name, sizeof(name)/sizeof(char));

    const char *ABC_notes[] = {"C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"};
    const char *ABC_notes2[] = {"C", "DB", "D", "EB", "E", "F", "GB", "G", "AB", "A", "BB", "B"};
    const char *DoReMi_notes[] = {"DO", "DO#", "RE", "RE#", "MI", "FA", "FA#", "SOL", "SOL#", "LA", "LA#", "SI"};
    const char *DoReMi_notes2[] = {"DO", "REB", "RE", "MIB", "MI", "FA", "SOLB", "SOL", "LAB", "LA", "SIB", "SI"};
    const char *DoReMi_notes3[] = {"Do", "Do#", "Re", "Re#", "Mi", "Fa", "Fa#", "Sol", "Sol#", "La", "La#", "Si"};

    boolean isValid = false;
    int diffName = 0;
    for(int i = 0; i < 12; i++)
    {
        if(strcmp(nameUp, ABC_notes[i]) == 0 || strcmp(nameUp, ABC_notes2[i]) == 0 || strcmp(nameUp, DoReMi_notes[i]) == 0 || strcmp(nameUp, DoReMi_notes2[i]) == 0)
        {
        	if(isPrint)
            	Serial.printf("Note: %s, Octave: %d, ", DoReMi_notes3[i], num);
            diffName = i - 9; // 9 = A
            isValid = true;
            break;
        }
    }
    if(!isValid)
    {
      fputs ("error: invalid input format.\n", stderr);
      return -400;// khi do am thanh phat ra gan nhu khong nghe duoc voi ~0hz
    }
    int diffNum = num - 4;
    return diffName + diffNum*12;
}


float PlayNote::ffreq(const char *x)
{
  if(strcmp(x, "0") == 0 || strcmp(x, "") == 0)
    {
        return 0;
    }
    int diff0 = diff(x);
    const float A4 = 440.00;
    float res = A4 * powf(2, (float)diff0/12); 
    return res;
}

int PlayNote::freq(const char *x)
{
    return round((double)ffreq(x));
}

////////////////////////////////////////////////////////////////////

void PlayNote::setTempo(int tempo)
{
	lengthQuarterNote = 256*100/tempo;	
}

void PlayNote::play(int f)
{
  if(isPrint)
  	Serial.printf("Frequency %d\n", f);
  if (f != 0)
  {
    tone(buzzerPin, f, 200);
  }
  else
  {
    noTone(buzzerPin);
  }
  delay(500);
}

void PlayNote::playTime(struct notes n)
{
  int f = freq(n.name);
  // int lengthQuarterNote = 256;//ms; temp = 60/lenQuarterNote // lengthQuarterNote (ms) = Quarter note = l
  long t = round(n.length * lengthQuarterNote); //dat gia tri tuong duong voi not den
  if(isPrint)
  	Serial.printf("Frequency: %d, Len: %d\n", f, t);
  // t = do dai not = l * 2^k = length of note (value is cal when l = 128)
  // 64 = not tron tu = l * 2^5 = 4096 ms = Large (Latin: Maxima) / Octuple whole note
  // 32 = not tron ba = l * 2^4 = 2048 ms = Long / Quadruple whole note
  // 16 = not tron doi = l * 2^3 = 1024 ms = Breve / Double whole note
  // 8 = not tron = l * 2^2 = 512 ms = Semibreve / Whole note
  // 2 = not trang = l * 2^1 = 256 ms = Minim / Half note
  // 1 = not den = l * 2^0 = 128 ms = Crotchet / Quarter note = 100
  // 0.5 = not moc don = l * 2^-1 = 64 ms = Quaver / Eighth note = 50
  // 0.25 = not moc kep = l * 2^-2 = 32 ms = Semiquaver / Sixteenth note = 25
  // 0.125 = not moc ba = l * 2^-3 = 16 ms = Demisemiquaver / Thirty-second note
  // 0.0625 = not moc tu = l * 2^-4 = 8 ms = Hemidemisemiquaver / Sixty-fourth note
  // 0.03125 = not moc nam = l * 2^-5 = 4 ms = Semihemidemisemiquaver / Quasihemidemisemiquaver / Hundred twenty-eighth note
  // 0.015625 = not moc sau = l * 2^-6 = 2 ms = Demisemihemidemisemiquaver / Two hundred fifty-sixth note

  if (f != 0)
  {
    tone(buzzerPin, f, t);
  }
  else
  {
    noTone(buzzerPin);
  }
  //delay(t);
  delay(t + round(t * 0.5));
  //noTone(buzzerPin);	
}

void PlayNote::playSong(struct notes songFromUser[], int len)
{
	for (int i = 0; i < len; i++)
	{
		playTime(songFromUser[i]);
	}
	Serial.printf("The end!\n");
}
