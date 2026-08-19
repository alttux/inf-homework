for i in range(9):

    A = i * "1" + 8 * "0"

    A = int(A[:8], 2)


    ip_net = ip_network(f"124.23.32.10/255.255.{A}.0", False)


    for ip_ad in ip_net:

        if f'{ip_ad:b}'[:16].count("1") < f'{ip_ad:b}'[16:].count("1"):

            break

    else:

        print(A)

        break