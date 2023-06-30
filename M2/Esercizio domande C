#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main () {

	int punteggio = 0;
	char nomeutente[20];
	char risposta[2];
	int contr = 1; //variabile di controllo dei cicli per le risposte non standard
	int cnome = 1; //variabile di controllo per la lunghezza del nome
	int game = 1; //variabile di controllo per ricominciare il gioco
	char a[2]="a";
	char b[2]="b";       //array di controllo delle risposte standard
	char c[2]="c";




printf("\n");
printf("*********************************\n");
printf("Benvenuto al quiz delle capitali!\n");
printf("*********************************\n");
printf("\n");

printf("Effettua una selezione:\n");
printf("\n");
printf("A) Nuova partita  ");
printf("B) Esci dal gioco\n");

contr=1;
while (contr==1){
scanf("%s", &risposta);
printf("\n");

	if (strcasecmp(risposta,b)==0){
	printf("alla prossima!");
	contr=0;
	exit(0);
}
	else if (strcasecmp(risposta,a)==0){
	printf("inserisci il tuo nome:\n");
while (cnome==1){	
	scanf("%s", &nomeutente);
	printf("\n");
	long i = strlen(nomeutente);
	if (i>10){
	printf("il nome è troppo lungo, riprova\n");
	cnome=1;}
	else{
	printf("benvenuto %s!\n", nomeutente);
	printf("\n");
	contr=0;
	cnome=0;}
}
}
	else if (strcasecmp(risposta,a)!=0){
	printf("devi inserire A o B\n");
	contr=1;
}
}

while (game==1){

printf("iniziamo con la prima domanda!: qual è la capitale dell'Italia?\n");
printf("\n");
printf("A) Roma  B)Lisbona  C)Londra\n");

contr=1;
while (contr==1){

scanf("%s",&risposta);
printf("\n");

	if (strcasecmp(risposta,b)==0){

	printf("Risposta sbagliata! la risposta giusta era Roma\n");
	contr=0;
}
	else if (strcasecmp(risposta,c)==0){

	printf("Risposta sbagliata! la risposta giusta era Roma\n");
	contr=0;
}
	else if (strcasecmp(risposta,a)==0){

	printf("Risposta giusta!\n");
	punteggio++;
	contr=0;
}
	else if (strcasecmp(risposta,a)!=0) {
	printf("inserisci A B o C\n");
	contr=1;
}
}
printf("\n");
printf("Bene, andiamo con la prossima: qual è la capitale della Spagna?\n");
printf("\n");
printf("A) Barcellona  B) Madrid  C)Granada\n");

contr=1;
while (contr==1){
scanf("%s", &risposta);
printf("\n");

  	if (strcasecmp(risposta,a)==0){

        printf("Risposta sbagliata! la risposta giusta era Madrid\n");
	contr=0;
}
        else if (strcasecmp(risposta,c)==0){
        printf("Risposta sbagliata! la risposta giusta era Madrid\n");
	contr=0;
}
        else if (strcasecmp(risposta,b)==0){

        printf("Complimenti,risposta giusta!\n");
        contr=0;
	punteggio++;
}
	else if (strcasecmp(risposta,a)!=0) {
        printf("inserisci A B o C\n");
        contr=1;

}
}
printf("\n");
printf("Ok andiamo con l'ultima domanda: qual è la capitale del Brasile?\n");
printf("\n");
printf("A) Rio de Janeiro  B)Bogotà  C)Brasilia\n");

contr=1;
while (contr==1){
scanf("%s", &risposta);
printf("\n");

	if (strcasecmp(risposta,a)==0){

        printf("Risposta sbagliata! la risposta giusta era Brasilia\n");
	contr=0;
}
        else if (strcasecmp(risposta,b)==0){

        printf("Risposta sbagliata! la risposta giusta era Brasilia\n");
	contr=0;
}
        else if (strcasecmp(risposta,c)==0){

        printf("Complimenti,risposta giusta!\n");
        contr=0;
	punteggio++;
}
	else if (strcasecmp(risposta,a)!=0) {
        printf("inserisci A B o C\n");
        contr=1;
}
}
printf("\n");
printf("***********fine gioco************");
printf("\n");
printf("Hai totalizzato %i punti!\n", punteggio);
printf("\n");

	if (punteggio == 3)
	printf("complimenti sei il re delle capitali!\n");
	else if (punteggio >=1)
	printf("dai te la sei cavata!\n");
	else
	printf("mi sa che devi ripassare un po'!\n");

printf("\n");
printf("**********************************************\n");
printf("\n");
printf("che ne dici %s, vuoi riprovarci?\n", nomeutente);
printf("\n");
printf("A) Nuova partita ");
printf("B) Esci dal gioco\n");


contr=1;
while (contr==1){
scanf("%s",&risposta);
printf("\n");

	if (strcasecmp(risposta,b)==0){
	printf("Alla prossima allora!\n");
	game==0;
	exit(0);
}
	if (strcasecmp(risposta,a)!=0){
	printf("devi inserire A o B\n");
	contr=1;
}
	if (strcasecmp(risposta,a)==0){
	printf("giochiamo di nuovo allora!\n");
	game=1;
	contr=0;
	printf("\n");
}
}
}

return 0;
}
