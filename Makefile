CC=gcc
OBJS = qwind/integration/p_zz.so
CFLAGS =  -Wall -fPIC -g -shared
INCLUDE = qwind/integration/*.c
LIBS = -lm -lgsl -lgslcblas

make:
	${CC} ${CFLAGS} ${INCLUDE} -o ${OBJS} ${LIBS}

clean:
	-rm -f *.so
