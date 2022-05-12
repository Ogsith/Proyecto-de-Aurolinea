#include <iostream>
#include <vector>
using namespace std;

vector<vector<char>> buildBoard(int N) {

    vector<vector<char>> board;

   // Inicializa el tablero para que tenga el tamaño N X N

    for(int i = 0; i < N; i++) {
        board.push_back(vector<char>());
    }

    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            board[i].push_back('*');
        }
    }

    return board;
} // Construye el tablero y nos da un puntero

void printBoard(vector<vector<char>> *board, int N) {

    cout << "  ";
    for(int i = 0; i <N; i++) {
        cout << i << " ";
    }
    cout << endl;

    for(int i = 0; i < N; i++) {
        cout << i << " ";
        for(int j = 0; j < N; j++) {
            cout << (*board)[i][j] << " ";
        }
        cout << endl;
    }
} // Imprime el tablero actualizado

int condicion_victoria(int cambio_de_jugador, vector<vector<char>> *board, int N) {

    // Verificar horizontalmente
    if(cambio_de_jugador == 1) {
        for(int i = 0; i < N; i++) {
            int conteo_para_ganar = 0;
            for(int j = 0; j < N; j++) {
                if((*board)[i][j] == 'X') {
                    conteo_para_ganar++;
                }
            }
            if(conteo_para_ganar == N) {
                cout << "¡EL JUGADOR 1 HA GANADO!" << endl;
                printBoard(board,N);
                exit(0);
            }
        }
    } else {
        for(int i = 0; i < N; i++) {
            int conteo_para_ganar = 0;
            for(int j = 0; j < N; j++) {
                if((*board)[i][j] == 'O') {
                    conteo_para_ganar++;
                }
            }
            if(conteo_para_ganar == N) {
                cout << "¡EL JUGADOR 2 HA GANADO!" << endl;
                printBoard(board,N);
                exit(0);
            }
        }
    }

    // Verificar verticalmente
    if(cambio_de_jugador == 1) {
        for(int i = 0; i < N; i++) {
            int conteo_para_ganar = 0;
            for(int j = 0; j < N; j++) {
                if((*board)[j][i] == 'X') {
                    conteo_para_ganar++;
                }
            }
            if(conteo_para_ganar == N) {
                cout << "¡EL JUGADOR 1 HA GANADO!" << endl;
                printBoard(board, N);
                exit(0);
            }
        }
    } else {
        for(int i = 0; i < N; i++) {
            int conteo_para_ganar = 0;
            for(int j = 0; j < N; j++) {
                if((*board)[j][i] == 'O') {
                    conteo_para_ganar++;
                }
            }
            if(conteo_para_ganar == N) {
                cout << "¡EL JUGADOR 2 HA GANADO!" << endl;
                printBoard(board, N);
                exit(0);
            }
        }
    }

    // Comprobar diagonal izquierda

    if(cambio_de_jugador == 1) {
        int conteo_para_ganar = 0;
        for(int i = 0,j = 0; i < N, j < N; i++, j++) {
                if((*board)[i][j] == 'X') {
                   conteo_para_ganar++;
            }
        }
        if(conteo_para_ganar == N) {
            cout << "¡EL JUGADOR 1 HA GANADO!" << endl;
            printBoard(board, N);
            exit(0);
        }
    } else {
        int conteo_para_ganar = 0;
        for(int i = 0,j = 0; i < N, j < N; i++, j++) {
            if((*board)[i][j] == 'O') {
                conteo_para_ganar++;
            }
        }
        if(conteo_para_ganar == N) {
            cout << "¡EL JUGADOR 2 HA GANADO!" << endl;
            printBoard(board, N);
            exit(0);
        }
    }

    // Comprobar diagonal derecha

    if(cambio_de_jugador == 1) {
        int conteo_para_ganar = 0;
        for(int i = N - 1, j = N - 1; i >= 0, j >= 0; i--, j--) {
            if((*board)[i][j] == 'X') {
                conteo_para_ganar++;
            }
        }
        if(conteo_para_ganar == N) {
            cout << "¡EL JUGADOR 1 HA GANADO!" << endl;
            printBoard(board, N);
            exit(0);
        }
    } else {
        int conteo_para_ganar = 0;
        for(int i = N - 1, j = N - 1; i >= 0, j >= 0; i--, j--) {
            if((*board)[i][j] == 'O') {
                conteo_para_ganar++;
            }
        }
        if(conteo_para_ganar == N) {
            cout << "¡EL JUGADOR 2 HA GANADO!" << endl;
            printBoard(board, N);
            exit(0);
        }
    }

    // Comprueba si no hay ganador

    int countAllGone = 0;
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            if((*board)[i][j] != '*') {
                countAllGone++;
            }
        }
    }
    if(countAllGone == N * N) {
        cout << "NO HAY GANADOR!" << endl;
        exit(0);
    }

    return 0;
}

int turn(int cambio_de_jugador, vector<vector<char>> *board, int N){

    string entrada;
    bool validInput = false;
    int xInput = 0;
    int yInput = 0;

    if(cambio_de_jugador == 1) {
        cout << "Turno de jugador 1" << endl;
        // Verifique para asegurarse de que el jugador no está insertando en un lugar ya ocupado

        while(!validInput) {
            cout << "Escribir las coordenadas (x,y) para colocar una X en esa posicion." << endl;
            cin >> entrada;

            xInput = (int)entrada[1] - 48;
            yInput = (int)entrada[3] - 48;

            if((*board)[xInput][yInput] == 'O' ||(*board)[xInput][yInput] == 'X' || xInput > N - 1 || yInput > N - 1 || xInput < 0 || yInput < 0) {
                cout << "Entrada no válida ¡El lugar ya está ocupado!" << endl;
            } else {
                validInput = true;
            }
        }

        (*board)[xInput][yInput] = 'X';
        condicion_victoria(cambio_de_jugador,board,N);

        cambio_de_jugador = 0;
        return cambio_de_jugador;
    } else {
        cout << "Turno de jugador 2" << endl;

        while(!validInput) {
            cout << "Escribir las coordenadas (x,y) para colocar una O en esa posicion" << endl;
            cin >> entrada;

            xInput = (int)entrada[1] - 48;
            yInput = (int)entrada[3] - 48;

            if((*board)[xInput][yInput] == 'O' || (*board)[xInput][yInput] == 'X' || xInput > N - 1 || yInput > N - 1 || xInput < 0 || yInput < 0) {
                cout << "Entrada no válida ¡Elige de nuevo!" << endl;
            } else {
                validInput = true;
            }

        }

        (*board)[xInput][yInput] = 'O';
        condicion_victoria(cambio_de_jugador,board,N);

        cambio_de_jugador = 1;
        return cambio_de_jugador;
    }
}

int main() {

    int N = 0;
    vector<vector<char>> board;
    int continuar_juego = 0;
    int cambio_de_jugador = 1;
    
    cout << "          -TIC_TAC_TOC-        "<< endl;
    cout << "-------------------------------"<< endl;
    cout << " Ingrese el tamaño del tablero "<< endl;
    cout << "-------------------------------"<< endl;
    cout << "---> "; cin >> N;

    board = buildBoard(N);
    while(continuar_juego == 0) {
        printBoard(&board,N);
        cambio_de_jugador = turn(cambio_de_jugador, &board, N);
        continuar_juego = condicion_victoria(cambio_de_jugador,&board, N);
    }
}
