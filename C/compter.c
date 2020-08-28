#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>


int main(){
pid_t pid = getpid();
int i ;

printf("PID de base  =  %d \n", getpid());

for (i = 0 ; i <= 5 ; i++){
        char * moi = "Papa";

        pid = fork();

        // Quitter si PID pourri
        if (pid == -1){
        printf("ERREUR PID NON VALIDE");
        exit(2);
        }

        // Fils qui print le chiffre
        else if (pid == 0){
        moi = "Fiston";
        printf("%d  :   %d \n", getpid(), i);
        exit(0);
        }

        // Papa qui attend que ses fils soit terminés
        else{
        wait(NULL);
        }
}
//Le Papa créer un fils, celui ci affiche son Pid
//Puis le papa attends la fin de l'execution du Fils
//avant de creer le fils suivant
//L'ordre est donc controle
return 0;

}
