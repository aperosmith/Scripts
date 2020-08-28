#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>


int main(){
pid_t pid = getpid();
int i ;

printf("PID de base  =  %d \n", getpid());

sleep(2);
printf("------------------------------------------\n");

for (i = 0 ; i < 4 ; i++){

        char * moi = "Papa" ;
        pid = fork();

        if (pid == -1){
        printf("ERREUR PID NON VALIDE");
        exit(2);
        }

        else if (pid == 0){
        moi = "Fiston";
        printf("%s  :   %d \n", moi, getpid());
        // printf("Mon Papa  :   %d \n", getppid());
        // fflush;
        }

        else{
        printf("%s  :   %d \n", moi, getpid());
        // fflush;
        wait(NULL);
        }
        printf("\n");
}

return 0;

}
