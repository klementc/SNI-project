// --- SNI 2019
//     Builds a trajectory of the M/M/1 queue, from 0 to T.
//     Input:	mean time between arrivals (mtba),
//					mean service time (mst),
//					total simulation time (T)
//					and seed for the pseudo-random numbers (seed)

/* This is file "MM1.c"; compile for instance with
   gcc -o MM1 ps.o MM1.c -lm
*/

#include  <stdio.h>
#include  <stdlib.h>
#include  "./ps.h"

#define  arr  1		/* event-class: arrivals */
#define  dep  2		/* event-class: departures */

#define initGen(s) srand48((double)s)
#define expo(mean) (-mean*log(drand48()))

double drand48();
void srand48(long);
double log(double);

int main(int nbOfPars, char **pars)
{
   double mtba;				/* mean time between arrivals */
   double mst;				/* mean service time */
   double T;					/* total simulation time */
   long seed;					/* seed for the pseudo-r.n.s */
   
   double mcn;				/* mean customer number */
   
   long nbUnits;				/* current nb of units */
   double s;					/* current integral of fonction nbUnits */
   
   double time;				/* current sim time */
   int class;					/* current event class */
   
   double t;					/* aux */
   double t_old;				/* last epoch */
   double t_next_arr;		/* next arrival time */
   
   EVENT *ev;

   /* reading the command line */
   nbOfPars--;	/* here, nbOfPars = effective # of parameters */
   if (nbOfPars != 4 ||
      sscanf(pars[1],"%lf",&mtba) != 1 ||
      sscanf(pars[2],"%lf",&mst) != 1 ||
      sscanf(pars[3],"%lf",&T) != 1 ||
      sscanf(pars[4],"%ld",&seed) != 1)
   {
      fprintf(stderr,"\nUsage: %s mtba mst T seed\n\n",pars[0]);
      exit(-1);
   }

   initGen(seed);
   
   /* initialize the event list */
   s = 0.0;
   nbUnits = 0;
   InitEvList(T);
   
   /* first arrival */
   t = expo(mtba);
   CREATE_EV(ev,arr,t);
   InsertEv(ev);
   
   /* first departure */
   t += expo(mst);
   CREATE_EV(ev,dep,t);
   InsertEv(ev);
   t_old = 0.0;

   do
   {
      FirstEv(&class, &time);
      switch(class)
      {
         case arr:  s += nbUnits*(time - t_old);
                    nbUnits++;
                    t = time + expo(mtba);
                    CREATE_EV(ev,arr,t)
                    InsertEv(ev);
                    t_next_arr = t;
                    break;

         case dep:  s += nbUnits*(time - t_old);
                    nbUnits--;
                    if (nbUnits > 0) t = time + expo(mst);
                    else t = t_next_arr + expo(mst);
                    CREATE_EV(ev,dep,t);
                    InsertEv(ev);
                    break;

         case END_SIM: s += nbUnits*(T - t_old);
                       mcn = s/T;

      };
      t_old = time;
   } while(class != END_SIM);
   printf("\n --- mcn = %lf.\n\n",mcn);
}

