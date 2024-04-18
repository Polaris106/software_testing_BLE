#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <time.h>

#include "mutate.h"

int arrlen = 1;

//Parses string of unknown number of integers separated by commas, storing them in provided array and returns length of array
int parse(char* str, int* arr){
    char *token;
    int len = 0;

    token = strtok(str, ",");
    while (token != NULL) {
        len++;
        arr[len-1] = atoi(token);
        token = strtok(NULL, ",");
    }
    arr[len] = -1;
    return len;
}

//Converts array of integers to string, separated by commas, returning the length of the string
int arrToStr(int* arr, char* str, int arrlen){
    int len = 0;
    int i = 0;
    while(i < arrlen){
        int num = arr[i];
        int digits = 0;
        if(num == 0){
            digits = 1;
        } else {
            while(num > 0){
                num /= 10;
                digits++;
            }
        }
        num = arr[i];
        for(int j = 0; j < digits; j++){
            str[len+digits-j-1] = (num % 10) + '0';
            num /= 10;
        }
        len += digits;
        if(i < arrlen-1){
            str[len] = ',';
            len++;
        }
        i++;
    }
    str[len] = '\0';
    return len;
}

void mutate(int* arr){
    int i;
    int pos;
    int val;
    switch (random() % 5){
        case 0:
            //Add a random integer to the array in a random position
            if (arrlen == MAX_VAL - 1) {
                mutate(arr);
                return;
            };
            arrlen++;
            pos = random() % arrlen;
            val = random() % MAX_VAL;
            for(i = arrlen-1; i > pos; i--){
                arr[i] = arr[i-1];
            }
            arr[pos] = val;
            break;
        case 1:
            //Remove a random integer from the array
            if (arrlen == 1) {
                mutate(arr);
                return;
            };
            pos = random() % arrlen;
            for(i = pos; i < arrlen-1; i++){
                arr[i] = arr[i+1];
            }
            arrlen--;
            break;
        case 2:
            //Increment a random integer in the array
            pos = random() % arrlen;
            if (arr[pos] == MAX_VAL) {
                mutate(arr);
                return;
            };
            arr[pos]++;
            break;
        case 3:
            //Decrement a random integer in the array
            pos = random() % arrlen;
            if (arr[pos] == 0) {
                mutate(arr);
                return;
            };
            arr[pos]--;
            break;
        case 4:
            //Randomise a random integer in the array
            pos = random() % arrlen;
            arr[pos] = random() % MAX_VAL;
            break;
    }
}

int main(int argc, char **argv) {
    int i;
    srandom(time(NULL));

    if(argc < 3){
        printf("Usage: %s <input file> <output file>\n", argv[0]);
        return 1;
    }
    FILE* file = fopen(argv[1], "r");
    if(file == NULL){
        printf("Error opening file\n");
        return 1;
    }
    FILE* outFile = fopen(argv[2], "w");
    if(outFile == NULL){
        printf("Error opening output file\n");
        return 1;
    }

    char* line = (char*)malloc(256*sizeof(char));
    while(fgets(line, 256, file) != NULL){
        int* arr = (int*)malloc(MAX_VAL * sizeof(int));
        arrlen = parse(line, arr);

        for (i = 0; i < FIXED_ENERGY; i++) {
            mutate(arr);
        }
        char* newLine = (char*)malloc(MAX_VAL * 4 *sizeof(char));
        arrToStr(arr, newLine, arrlen);
        fprintf(outFile, "%s\n", newLine);

        free(arr);
        free(newLine);
    }
    free(line);

    fclose(file);
    fclose(outFile);
    return 0;
}