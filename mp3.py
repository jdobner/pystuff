import os, requests, threading


t = os.getpid()
print(f"running 1 {t}")
pid = os.fork()
os.spawnlp
print(f"running 2 {t}")
if pid == 0:
    # I am the child process.
    requests.get('https://www.python.org')
    print(f"got it! {t}")
    os._exit(0)
else:
    # I am the parent process.
    print(f"parent! {t}")
    