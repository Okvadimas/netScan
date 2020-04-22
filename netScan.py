def netscan():
    import os
    import platform
    from datetime import datetime
    import getmac
    import socket

    try:
        address = input("Enter the Network Address: ")
        split_ip = address.split(".")
        titik = "."
        jumlah_host = 0

        konversi_address = split_ip[0] + titik + split_ip[1] + titik + split_ip[2] + titik
        start_range = int(input("Enter the Starting Number: "))
        end_range = int(input("Enter the Last Number: "))

        operating_system = platform.system()

        if (operating_system == "Windows"):
            ping1 = "ping -n 1 "
        elif (operating_system == "Linux"):
            ping1 = "ping -c 1 "
        else:
            ping1 = "ping -c 1 "

        t1 = datetime.now()

        print("Scanning in Progress:")
        print("-" * 50)

        for ip_range in range(start_range, end_range + 1):
            full_address = konversi_address + str(ip_range)
            command = ping1 + full_address
            # print(type(command))
            mac = getmac.get_mac_address(ip=f"{full_address}")

            response = os.popen(command)
            result_command = response.readlines()

            try:
                if "bytes" and "TTL" in result_command[2]:
                    hostname = socket.gethostbyaddr(f"{full_address}")

                    print(
                        f"[+] Host {full_address} is Connected\n    Host Name   : {hostname[0]}\n    Mac Address : {mac}")
                    jumlah_host += 1
                else:
                    print(f"[-] Host {full_address} is Not Connected")
            except IndexError:
                print(f"Ping Request Could not Find Host {full_address}")
            except socket.herror:
                print(f"[-] Host {full_address} is Not Connected")
            #     print("error socket")

        t2 = datetime.now()
        total = t2 - t1
        print("-" * 50)
        print(f"Jumlah Host Connect di Jaringan: {jumlah_host}")
        print("-" * 50)
        print("Scanning completed in: ", total)

    except IndexError:
        print("\nSomething Went Wrong")

    except ValueError:
        print("\nError Value Input")
