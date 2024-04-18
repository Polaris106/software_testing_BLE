#ifndef _HAVE_SWARM
#define _HAVE_SWARM

#define MAX_VAL 256
#define FIXED_ENERGY 16

int parse(char* str, int* arr);
int arrToStr(int* arr, char* str, int arrlen);
void mutate(int* arr);

#endif