CFLAGS=-g -O2

all: cpu mem threads.v1 threads.v0 io
clean:
	rm -f *.o *.exe cpu mem threads.v1 threads.v0 io

cpu: cpu.o common.o

mem: mem.o common.o

threads.v1: threads.v1.o common.o

threads.v0: threads.v0.o common.o

io: io.o common.o
