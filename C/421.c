#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/resource.h>
#include <pthread.h>
#include <time.h>
#include <sys/syscall.h>

int resultat[3];
int tentative = 1;

void* lancer(int nombre){
  int dice = rand()%((6+1)-1)+1;
  resultat[nombre] = dice;
  pthread_exit(EXIT_SUCCESS);
}


int main(){
  int total = 0;
  printf("\t\tTentative n° %d\n", tentative);
  srand(time(NULL));
  pthread_t id[3];
  for (int i = 0; i < 3; i++){
    pthread_create(&id[i], NULL, &lancer, i);
    pthread_join(&id[i], NULL);
  }
  for (int i = 0; i < 3; i++){
//    printf("%i", resultat[i]);
  if(resultat[i] == 1)
  {
      total = total + 1;
      printf ("\n");
      printf ("\t _________  \n");
      printf ("\t|         | \n");
      printf ("\t|    .    | \n");
      printf ("\t|         | \n");
      printf ("\t|_________| \n");
  }
  else if(resultat[i] == 2)
  {
      total = total + 2;
      printf ("\n");
      printf ("\t _________  \n");
      printf ("\t|  .      | \n");
      printf ("\t|         | \n");
      printf ("\t|      .  | \n");
      printf ("\t|_________| \n");
  }
  else if(resultat[i] == 3)
  {
      printf ("\n");
      printf ("\t _________  \n");
      printf ("\t|  .      | \n");
      printf ("\t|    .    | \n");
      printf ("\t|      .  | \n");
      printf ("\t|_________| \n");
  }
  else if(resultat[i] == 4)
  {
      total = total + 4;
      printf ("\n");
      printf ("\t _________  \n");
      printf ("\t| .     . | \n");
      printf ("\t|         | \n");
      printf ("\t| .     . | \n");
      printf ("\t|_________| \n");
  }
  else if(resultat[i] == 5)
  {
      printf ("\n");
      printf ("\t _________  \n");
      printf ("\t| .     . | \n");
      printf ("\t|    .    | \n");
      printf ("\t| .     . | \n");
      printf ("\t|_________| \n");
  }
  else if(resultat[i] == 6)
  {
      printf ("\n");
      printf ("\t _________  \n");
      printf ("\t| .     . | \n");
      printf ("\t| .     . | \n");
      printf ("\t| .     . | \n");
      printf ("\t|_________| \n");
    }
  }
  printf("\n");
  printf ("\t ____________________________________  \n");
  if (total == 7){
    printf("\n\t\t!!! WINNER !!!\n\n");
    exit(0);
  }
  printf ("\t ____________________________________  \n");
  printf("\n");
  tentative = tentative + 1;
  sleep(1);
  main();
  return 0;
}

/*int dice = 0;

void *lancer(void *arg){
  dice = rand()%((6+1)-1)+1;
  printf("%d", dice);
  return(dice);
}

int main(void){

  srand(time(NULL));
  printf("\n");
	pthread_t thread1;
  pthread_t thread2;
  pthread_t thread3;
	pthread_create(&thread1, NULL, *lancer, NULL);
  pthread_create(&thread2, NULL, *lancer, NULL);
  pthread_create(&thread3, NULL, *lancer, NULL);
  pthread_join(thread1, NULL);
  pthread_join(thread2, NULL);
  pthread_join(thread3, NULL);
  sleep(1);
  main();
	return 0;
}
*/
