CC = gcc
CFLAGS = -Wall -Werror -pedantic

mutate: mutate.c
	$(CC) $(CFLAGS) -o mutate mutate.c

clean:
	rm -f mutate