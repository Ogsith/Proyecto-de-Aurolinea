#ifndef CLASES_H
#define CLASES_H

#include <iostream>
#include <string>
#include <vector>       
#include<cstdio>
#include<cstdlib>
#include <termios.h>
#include <unistd.h>
#include <iostream>
#include <sys/ioctl.h>
#include <stropts.h>

using namespace std;

void menu();
void game_over();
void gracias();

class CPersonaje{
    string nombre;
  public:
    CPersonaje();
    CPersonaje(string nombre);
    virtual ~CPersonaje() = default;
    void set_nombre(string value);
    string get_nombre();
    void inicial(string **escenario, int a, int b);
    void movimiento(string **escenario, int a, int b, char d);
};

class Cnivel{
  int op;
  int a = 20;
  int b = 30;
  
  string **escenario = new string*[a];

public:
  Cnivel(){
    for(int i = 0; i < a; i++)
      escenario[i] = new string[b];
    for(int i = 0; i < a; i++){
      for(int j = 0; j < b; j++){
        if(i == 0 or j == 0 or i == a - 1 or j == b - 1)
          escenario[i][j] = "* ";
        //inicio
        else if((i <= 3 and i >= 2) and j == 4)
          escenario[i][j] = "* ";
        else if(i == 3 and (j >= 1 and j <= 4)) 
          escenario[i][j] = "* ";
        //Final
        else if((i <= 17 and i >= 16) and j == 25) 
          escenario[i][j] = "* ";
        else if(i == 16 and (j >= 25 and j <= 29)) 
          escenario[i][j] = "* ";
        //espacios donde se puede pasar
        else
          escenario[i][j] = "  ";
      }
    }
  }
  //Destructor 
  ~Cnivel() = default;
  void iniciar_nivel();
  void construir_nivel(vector<vector<int>> vec);
  void mostrar_nivel();
  string** get_nivel();
};

#endif