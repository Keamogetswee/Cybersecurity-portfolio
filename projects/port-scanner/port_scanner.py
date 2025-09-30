import socket   # provides low-level network interface (create sockets, connect, etc.)
import sys      # to read command-line arguments and exit the script

def scan_ports(target, ports):
    # Inform the user which host is being scanned
    print(f"Scanning target: {target}")

    # Loop from port 1 up to and including 'ports'
    for port in range(1, ports + 1):
        # Create a new socket for each attempt
        # AF_INET = IPv4, SOCK_STREAM = TCP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Don't wait forever for a response — timeout after 0.5 seconds
        sock.settimeout(0.5)

        # connect_ex returns 0 on success (connected), or an error code on failure
        # We pass a tuple (target, port) — if target is a hostname it will be resolved
        result = sock.connect_ex((target, port))

        # If result is 0, the port is open (we established a TCP connection)
        if result == 0:
            print(f"[+] Port {port} is OPEN")

        # Always close the socket to free resources
        sock.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        # Provide helpful usage instructions and exit with a non-zero code (error)
        print("Usage: python3 port_scanner.py <target> <number_of_ports>")
        sys.exit(1)

    # Grab the target from the first argument
    target = sys.argv[1]

    # Convert the second argument to integer (may raise ValueError if not numeric)
    # Consider adding validation if you expect non-integer input
    ports = int(sys.argv[2])

    scan_ports(target, ports)
