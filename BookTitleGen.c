#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

//Functions

void strip(char string[]) {
    if(string[strlen(string)-1] == '\n'){
        string[strlen(string)-1] = '\0';
    }
}

void randomgen(char * words[], int num) {
    srand((unsigned int)time(NULL));
    char* random;
    random = words[rand() % num];
    printf("%s ", random);
}

int main() {

    printf("Type Yes to recieve book reconmendation \n");
    printf("-> ");

    char input[5];
    fgets(input, 5, stdin);
    strip(input);
    if(strcmp("Yes", input) == 0)
    {
        char* words1[3];
        words1[0] = "The";
        words1[1] = "An";
        words1[2] = "I,";

        char* words2[3];
        words2[0] = "Tree";
        words2[1] = "Cat";
        words2[2] = "Chicken";

        char* words3[3];
        words3[0] = "Ate";
        words3[1] = "Ran";
        words3[2] = "Said";

        char* words4[3];
        words4[0] = "Cheese";
        words4[1] = "Apples";
        words4[2] = "Watermelon";

        randomgen(words1, 3);
        randomgen(words2, 3);
        randomgen(words3, 3);
        randomgen(words4, 3);
        printf("\n");

} else {

    printf("Fine:(");

}
}