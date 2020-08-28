#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(){

char moi;
moi = "Pere";
int Pid = fork();

if (Pid == 0){
        moi = "Fils";
        printf(moi);
}
else {
        printf(moi);
        wait(NULL);
}
return 0;
}
