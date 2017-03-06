#include <stdlib.h>
#include <stdio.h>
#include <string.h>

char *toBinCode (char c) {
    char *res = malloc(8*sizeof(char));
    for (int i = 6; i >= 0; i--) {
        res[i] = '0'+(c%2);
        c/=2;
    }
    res[7] = '\0';
    return res;
}

int main(int argc, char** argv)
{
    char msg[100];
    fgets(&msg,100,stdin);
    char binMsg[700];

    char* iter = msg;
    char* binIter = binMsg;
    char *code; 
    while (*iter != '\n') {
        code = toBinCode(*iter);
        strncpy(binIter, code, 7);
        free(code);
        iter++;
        binIter+=7;
    }
    *binIter = '\0';

    char prev = '2';
    int count = 0;

    for (binIter = binMsg; *binIter != '\0'; binIter++) {
        if (*binIter != prev) {
            for (int j = 0; j < count; j++) 
                printf("0");
            if (count != 0) 
                printf(" ");
            printf((*binIter == '0') ? "00 " : "0 ");
            count = 1;
        } else
            count++;
        prev = *binIter;
    }
    for (int j = 0 ; j < count ; j++) 
        printf("0");     

    return EXIT_SUCCESS;
}