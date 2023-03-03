#include <stdio.h>
#include<string.h>
#include<stdlib.h>
#include<time.h>
#include<stdbool.h>
#define max_line 20480 /*Macro definition of word source for easy to remember password */

int main() {
    printf("\n^^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^\n");
    printf("\n^^    EASY- TO- REMEMBER PASSWORD GENERATOR       ^^\n");
    printf("\n^^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^\n");


/*Variable declaration*/
    char buffer[max_line], WordStore[10][10], *Dictionary[5] =
            {"Dummy.txt", "four.txt", "five.txt", "six.txt", "Seven.txt"};
    int read_line = 0, word = 1, i, No_Of_Words, RandFile, x = 0;
    FILE *fp; /*pointer definition*/

    printf("\nHow many Words would you like your password to contain ? "); /* prompt to ask user for number of words*/
    scanf("%d", &No_Of_Words); /* prompt to read user input*/

    while (No_Of_Words < 3 || No_Of_Words > 4) /*loop to check if user input falls within permissible range*/
    {
        printf("\nInvalid input!"); /* error message associated with incorrect input */
        printf("\nNo of words Must be either 3 or 4"); /* prompt displaying permissible range*/
        printf("\nPlease enter how many words you would like your password to contain: ");
        scanf("%d", &No_Of_Words);
    }

/*Word collector*/

    srand(time(NULL)); /*prompt to seed randomization with system time*/

    printf("\nGenerating password . . .\n"); /* message displayed to user to let them know their password is being generated */
    printf(" \n");

    /*loader*/

    system("cls");
    char a = 177, b = 219;
    printf("\t\t");
    for (int i = 0; i < 20; i++)
        printf("%c", a);
    printf("\t\t");
    for (int i = 0; i < 20; i++)
    {
        printf("%c", b);
        sleep(1);
    }

    for (i = 1; i <= No_Of_Words; i++, word++) /* loop to read words from dictionary until number of words = number of words input by the user*/
    {
        /*Dictionary randomiser*/
        RandFile = (rand() % 4) + 1;/*prompt to randomize file selection*/
        fp = fopen(Dictionary[RandFile], "r");/* prompt to read a random file from the dictionary array */

        printf("\nword %d = ", word);
        read_line = (rand() % 500) + 1; /*prompt to read a random line number within a randomly selected file*/
        printf("%d", read_line);

        if (fp == NULL) /*condition to check if selected text files are null */
        {
            printf("error opening file");/*error message associated with null text file*/
            return 1;
        }

        bool keep_reading = true;/* program keeps reading if file is not an error*/
        int current_line = 1;/*initializing output*/

        /*Word randomiser*/
        while (keep_reading)
        {
            fgets(buffer, max_line, fp);
            buffer[strcspn(buffer, "\n")] = 0;

            if (feof(fp))
            {
                keep_reading = false;
                printf(" file lines %d \n", current_line) - 1;
                printf("coudn't find line %d \n", read_line);
            } else if (current_line == read_line)
            {
                keep_reading = false;
                printf(" line: %s", buffer);
                strcpy(WordStore[x], buffer);
                x++;

            }
            current_line++;

        }
        rewind(fp);
    }
    fclose(fp);

    if (No_Of_Words == 3)
    {
        printf("\n\nYour e-t-r password is: %s-%s-%s", WordStore[0], WordStore[1], WordStore[2]);  /*final password output for length of 3 words*/
    }
    else if (No_Of_Words == 4)
    {
        printf("\n\nYour e-t-r password is: %s-%s-%s-%s", WordStore[0], WordStore[1], WordStore[2], WordStore[3]); /*final password output for length of 4 words*/
    }
    return 0;
}
