#include "clases.h"

void menu(){
  cout<<"------------------------------"<<endl;
  cout<<"|           FLAPPY FC         |"<<endl;
  cout<<"------------------------------"<<endl;  
  cout<<"| 1. Play                     |"<<endl;
  cout<<"| 0. Salir                    |"<<endl;
  cout<<"------------------------------"<<endl;
}

void game_over(){
  cout << "perdiste, rocky no volvera a casa" << endl;
  cout << "-----------------------------------------" << endl;
}

void gracias(){
  cout << "¡¡¡¡¡¡¡¡¡¡  GRACIAS POR JUGAR  !!!!!!!!!!" << endl;
  cout << "-----------------------------------------" << endl;
}

void Cnivel::construir_nivel(vector<vector<int>> vec){
  for(size_t i=0; i<vec.size(); i++){
    escenario[vec[i][0]][vec[i][1]] = "* ";
  }
}

string** Cnivel::get_nivel(){ return escenario; }

void Cnivel::mostrar_nivel(){
  for (int i = 0; i < a; i++){
    for (int j = 0; j < b; j++)
      cout << escenario[i][j];
    cout << endl;
  }
}

CPersonaje::CPersonaje(string nombre){
  this->nombre = nombre;}

void CPersonaje::set_nombre(string value){
  nombre = value;}

string CPersonaje::get_nombre(){
  return nombre;}

void CPersonaje::inicial(string **escenario, int a, int b){
  for (int i = 0; i < a; i++){
    for(int j = 0; j < b ; j++){
      if(i == 1 and j == 1)
        escenario[i][j] = "R ";}
  }
}

void CPersonaje::movimiento(string **escenario, int a, int b, char d){
  int pos_i = 0; int pos_j = 0;
  switch(toupper(d)){
      case 'd':
      case 'D':
      for (int i = 0; i < a; i++){
        for(int j = 0; j < b ; j++){
          if(escenario[i][j] == "R "){
            pos_i = i; 
            pos_j = j;
            }
        }
      }
      if(escenario[pos_i][pos_j+1]=="* ")
        escenario[pos_i][pos_j+1] = "* ";
      else{
        escenario[pos_i][pos_j] = "  ";
        escenario[pos_i][pos_j + 1] = "R ";
      }
      break;
    
    case 'A':
    case 'a':
      for (int i = 0; i < a; i++){
        for(int j = 0; j < b; j++){
          if(escenario[i][j] == "R "){
            pos_i = i; 
            pos_j = j;
            }
        }
      }
      if(escenario[pos_i][pos_j-1]=="* ")
        escenario[pos_i][pos_j-1] = "* ";
      else{
        escenario[pos_i][pos_j] = "  ";
        escenario[pos_i][pos_j - 1] = "R ";
      }
      break;
    
    case 'S':
    case 's':
      for (int i = 0; i < a; i++){
        for(int j = 0; j < b; j++){
          if(escenario[i][j] == "R "){
            pos_i = i; 
            pos_j = j;
            }
        }
      }
      if(escenario[pos_i+1][pos_j]=="* ")
        escenario[pos_i+1][pos_j] = "* ";
      else{
        escenario[pos_i][pos_j] = "  ";
        escenario[pos_i + 1][pos_j] = "R ";
      }
      break;
    
    case 'W':
    case 'w':
      for (int i = 0; i < a; i++){
        for(int j = 0; j < b; j++){
          if(escenario[i][j] == "R "){
            pos_i = i; 
            pos_j = j;
            }
        }
      }
      if(escenario[pos_i-1][pos_j]=="* ")
        escenario[pos_i-1][pos_j] = "* ";
      else{
        escenario[pos_i][pos_j] = "  ";
        escenario[pos_i - 1][pos_j] = "R ";
      }
      break;
  }
}
