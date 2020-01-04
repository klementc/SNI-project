// --- // --- SNI 2019 - PICOSIMULATOR, simplified version v0 - file ps.c

/* Compiling command (example):   gcc  -c  -o  ps.o  ps.c */
/* It needs file "ps.h". We obtain object code in file "ps.o" */

#include  <stdio.h>
#include  <stdlib.h>
#include  "ps.h"

/* --- this will point to the first event in the list */
EVENT * First;

/* --- event insertion */
void 
InsertEv(EVENT * ev)
{
	EVENT	*x, *y;
	double	time;

	time = ev->Time;
	if (time < First->Time) {
		/* --- ev will become the first one */
		ev->Next = First;
		First = ev;
		return;
	}
	/* here, ev goes at least at 2nd position */
	x = First;
	y = x->Next;
	while (y != NULL) {
		if (time < y->Time) {	/* --- ev goes after x end before y */
			ev->Next = y;
			x->Next = ev;
			return;
		}
		x = y;
		y = y->Next;
	}
	/* ev goes after the whole list */
	x->Next = ev;
	ev->Next = NULL;
}

/* accessing the first event */
void 
FirstEv(int *c, double *t)
{
	EVENT	*x;

	x = First;
	First = First->Next;
	*t = x->Time;
	*c = x->Class;
	free(x);
}

/* initializing the event-list */
void 
InitEvList(double t)
{
	EVENT	*ev;

	CREATE_EV(ev, END_SIM, t);
	First = ev;
}
