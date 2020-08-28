#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/resource.h>
#include <pthread.h>
#include <time.h>

void *etoile(void *arg){
  for (int i = 0; i < 100; i++) {
  printf("*");
  nanosleep((const struct timespec[]){{0, 9000000L}}, NULL);
  }
  return(NULL);
//	pthread_exit(EXIT_SUCCESS);
}

void *planete(void *arg) {
  for (int i = 0; i < 100; i++) {
  printf("o");
  nanosleep((const struct timespec[]){{0, 3000000L}}, NULL);
  }
  return(NULL);

//	pthread_exit(EXIT_SUCCESS);
}

int main(void) {
  printf("\n");
	pthread_t thread1;
  pthread_t thread2;
	pthread_create(&thread1, NULL, *etoile, NULL);
  pthread_create(&thread2, NULL, *planete, NULL);
  pthread_join(thread1, NULL);
  pthread_join(thread2, NULL);
  printf("\n\n");
	return EXIT_SUCCESS;
}
