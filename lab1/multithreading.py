"""
  Multithreading is the ability of a Central Processing Unit (CPU) to break a single process into multiple threads of execution and run them concurrently.

  Just like multiprocessing, multithreading is a way of achieving multitasking. In multithreading, the concept of threads is used. Let us first understand the concept of thread in computer architecture.

  What is a Process in Python?
  In computing, a process is an instance of a computer program that is being executed. Any process has 3 basic components:

  An executable program.
  The associated data needed by the program (variables, workspace, buffers, etc.)
  The execution context of the program (State of the process)

  
  A thread is an entity within a process that can be scheduled for execution. Also, it is the smallest unit of processing that can be performed in an OS (Operating System). In simple words, a thread is a sequence of such instructions within a program that can be executed independently of other code. For simplicity, you can assume that a thread is simply a subset of a process! A thread contains all this information in a Thread Control Block (TCB):

  Thread Identifier: Unique id (TID) is assigned to every new thread
  Stack pointer: Points to the thread’s stack in the process. The stack contains the local variables under the thread’s scope.
  Program counter: a register that stores the address of the instruction currently being executed by a thread.
  Thread state: can be running, ready, waiting, starting, or done.
  Thread’s register set: registers assigned to thread for computations.
  Parent process Pointer: A pointer to the Process control block (PCB) of the process that the thread lives on.
 
 
  Watch: https://www.youtube.com/watch?v=exbKr6fnoUw
"""


import threading
import time

def thread_job():
    print("This is an added Thread, number is %s" % threading.current_thread())
    print("T1 start\n")
    for i in range(10):
        time.sleep(0.1)
    print("T1 finish\n")
    
def T2_job():
    print("T2 start\n")
    print("T2 finish\n")
    
#provide comments
def main():
    added_thread = threading.Thread(target=thread_job, name='T1')
    thread2 = threading.Thread(target=T2_job, name='T2')
    added_thread.start()
    thread2.start()
    thread2.join()
    added_thread.join()
    print("all done\n") 
    
if __name__ == '__main__':
    main()
    
    