CC=gcc
CFLAGS=-lGLEW -lglfw -lGL -lX11 -lpthread -lXrandr -lXi -Wall

test:	test_opengl.c
	$(CC) -o test.o test_opengl.c $(CFLAGS)

clean:
	@rm *.o
	@echo Clean done
