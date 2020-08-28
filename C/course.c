#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <time.h>

int main(){
pid_t pid = getpid();
int i ;

for (i = 1; i <= 10 ; ++i){
    int pid = fork();
    if (pid > 0){
        continue;
    } else if (pid == 0){
        int a ;

        printf("%d est parti !\n", i );
        clock_t begin = clock();
        for (a = 0 ; a <= 1000000000 ; a++){
        }
        clock_t halfway = clock();
        double time_spent = (double)(halfway - begin) / CLOCKS_PER_SEC;
        printf("%d est arrive en %f ! (PID:  %d) \n", i, time_spent, getpid());
        for (a = 0 ; a <= 1000000000 ; a++){
        }
        clock_t end = clock();
        double time_total = (double)(end - begin) / CLOCKS_PER_SEC;
        printf("%d est arrive en %f ! (PID:  %d) \n", i, time_total, getpid());
        break;
    } else {
        printf("fork error\n");
        exit(1);
    }
}

if (pid > 0){
wait(NULL);
}
}
