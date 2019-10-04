import sys
import os
import queue
import threading
import time

class MyThread(threading.Thread):
    def __init__(self, thread_name, begin, end):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.begin = begin
        self.end = end
        self.solutions = set()

    def run(self):
        print('Starting', self.thread_name)
        self.solutions = check_range(self.begin, self.end)
        print('Exiting', self.thread_name)


def check_range(a, b):
    os.system('python3 p8.py {} {} -w'.format(a, b))
    solutions = set()
    with open('{}-{}.txt'.format(a, b)) as infile:
        for line in infile:
            solutions.add(line)
    os.remove('{}-{}.txt'.format(a, b))
    return solutions

def main(thread_count, begin=0, end=10000000000):
    thread_count = int(thread_count)
    begin = int(begin)
    end = int(end)
    spread = int((end - begin) / thread_count)
    solutions = set()
    threads = []
    for i in range(thread_count):
        thread_name = 'Thread_{}'.format(i)
        thread = MyThread(thread_name, begin + i*spread, begin + (i+1)*spread)
        thread.start()
        threads.append(thread)
    for t in threads:
        t.join()
        solutions |= t.solutions

    print('\n\nSolutions:')
    for element in solutions:
        print(element)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        thread_count = sys.argv[1]
        begin = 0
        end = 10000000000
    if len(sys.argv) == 3:
        end = sys.argv[2]
    elif len(sys.argv) == 4:
        begin = sys.argv[2]
        end = sys.argv[3]
    if len(sys.argv) == 1:
        print('Usage: python3 {} thread_count [[max] || [begin end]]'.format(sys.argv[0]))
        quit()
    main(thread_count, begin, end)
