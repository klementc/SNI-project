
all: mminf mm1

mminf: MMinf.o ps.o
	gcc -lm -o MMinf MMinf.o ps.o
MMinf.o: MMinf.c
	gcc -lm -o MMinf.o -c MMinf.c
mm1: MM1.o ps.o
	gcc -lm -o MM1 MM1.o ps.o
ps.o: ps.c
	gcc -lm -o ps.o -c ps.c
MM1.o: MM1.c
	gcc -lm -o MM1.o -c MM1.c

