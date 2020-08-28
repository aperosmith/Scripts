#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/resource.h>

int main()
{
    for(int i = 1; i <= 10; i++){
        int pid = fork();
        int nice(int inc);

        if (i == 1){
        nice(-19);
        }
        else {
        nice(19);
        }


        if (pid == 0){
           int boucle = 0;
           while(boucle != 2147483647){
               boucle++;
           }
           printf("%d est a 50/100 ! (PID:  %d)\n", i, getpid());
           boucle = 0;
           while(boucle != 2147483647){
               boucle++;
           }
           printf("%d a fini ! (PID: %d) \n", i, getpid());
           exit(0);
        }
    }
    for (int j = 1; j <= 10; j++){
    printf("Position du %d : %d\n", wait(NULL), j);
    }
    return 0;
}
