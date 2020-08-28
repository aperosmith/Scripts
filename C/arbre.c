#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>


int main(){
pid_t pid = getpid();
int i ;
//printf("PID de base  =  %d \n", getpid());

for( i = 0; i < 3; i++){
pid = fork();
char * moi = "Papa" ;

if (pid == -1){
  	   printf("EXIT FAILURE\n");
  	   exit(0);
     }
else if (pid == 0){
      moi = "Fiston";
      printf("%s    %d  :   %d \n", moi, getpid(), i);
     }
else {
      moi = "Papa";
      printf("%s      %d  :   %d \n", moi, getpid(), i);
     }
}
return 0;
}
