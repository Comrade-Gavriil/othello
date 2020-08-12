from multiprocessing import Process, Queue

def add(a,b, q):
    q.put([a+b])


if __name__ == '__main__':
    q = Queue()

    p1 = Process(target=add, args=(1,2,q,))

    p1.start()
    

    p1.join()
    res = q.get()
    print(res)