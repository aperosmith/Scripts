#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/resource.h>
#include <pthread.h>
#include <time.h>
#include <sys/syscall.h>


void *attente(void *arg){
  sleep(50);
  printf("Thread : %d\n", pthread_self());
  pthread_exit(NULL);
  return(NULL);
}

int main(void){
  printf("\n");
	pthread_t thread1;
  pthread_t thread2;
  pthread_t thread3;
	pthread_create(&thread1, NULL, *attente, NULL);
  pthread_create(&thread2, NULL, *attente, NULL);
  pthread_create(&thread3, NULL, *attente, NULL);
  pthread_join(thread1, NULL);
  pthread_join(thread2, NULL);
  pthread_join(thread3, NULL);
  sleep(4);
  printf("\n\n");
	return 0;
}
