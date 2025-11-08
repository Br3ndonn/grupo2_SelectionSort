# Makefile para compilar o projeto Selection Sort em C

CC = gcc
CFLAGS = -Wall -O2 -std=c11
TARGET = main
OBJS = main.o lista.o selection_sort.o carrega_csv.o

# Regra padrão
all: $(TARGET)

# Compilar o executável
$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJS) -lm

# Compilar arquivos objeto
main.o: main.c lista.h selection_sort.h carrega_csv.h
	$(CC) $(CFLAGS) -c main.c

lista.o: lista.c lista.h
	$(CC) $(CFLAGS) -c lista.c

selection_sort.o: selection_sort.c selection_sort.h lista.h
	$(CC) $(CFLAGS) -c selection_sort.c

carrega_csv.o: carrega_csv.c carrega_csv.h lista.h
	$(CC) $(CFLAGS) -c carrega_csv.c

# Limpar arquivos compilados
clean:
	del /Q $(OBJS) $(TARGET).exe 2>nul || rm -f $(OBJS) $(TARGET) $(TARGET).exe

# Executar com tamanho 10000
run:
	$(TARGET).exe 10000 || ./$(TARGET) 10000

.PHONY: all clean run
