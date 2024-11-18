def Toh(n,start,aux,end):
    if n == 1 :
        print(f"Disk 1 move from {start} to {end}")
        return
    Toh(n-1,start,aux,end)
    print(f"Move disk {n} from {start} to {end}")
    Toh(n-1,aux,end,start)

Toh(3,"A","B","C")
