import socket
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
from colorama import init, Fore, Style
import os
import subprocess

init(autoreset=True)

def is_host_up(target):
    try:
        output = subprocess.check_output(["ping", "-n", "1", target], stderr=subprocess.DEVNULL)
        return "TTL=" in output.decode()
    except Exception:
        return False

def grab_banner(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((ip, port))
            return s.recv(1024).decode().strip()
    except:
        return ""

def identify_service(port):
    common_ports = {
        21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
        80: "HTTP", 110: "POP3", 143: "IMAP", 443: "HTTPS", 3306: "MySQL",
        3389: "RDP", 8080: "HTTP-Alt"
    }
    return common_ports.get(port, "Unknown")

def scan_port(ip, port, verbose):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((ip, port))
            if result == 0:
                banner = grab_banner(ip, port)
                service = identify_service(port)
                return f"{Fore.GREEN}[+] Port {port} is OPEN | Service: {service} | Banner: {banner}"
            elif verbose:
                return f"{Fore.YELLOW}[-] Port {port} is CLOSED"
    except Exception as e:
        return f"{Fore.RED}[!] Error on port {port}: {e}"

def main():
    parser = argparse.ArgumentParser(description="Enhanced Multithreaded TCP Port Scanner")
    parser.add_argument("target", help="Target IP or domain")
    parser.add_argument("--ports", help="Port range (e.g., 1-1024)", required=True)
    parser.add_argument("--threads", type=int, default=100, help="Number of threads (default: 100)")
    parser.add_argument("--output", help="Output file to save results")
    parser.add_argument("--verbose", action="store_true", help="Show closed ports and extra details")
    args = parser.parse_args()

    try:
        target_ip = socket.gethostbyname(args.target)
        start_port, end_port = map(int, args.ports.split("-"))
    except Exception:
        print(f"{Fore.RED}[!] Invalid IP or port range format.")
        return

    print(f"{Fore.CYAN}🔍 Scanning {args.target} ({target_ip}) from port {start_port} to {end_port} using {args.threads} threads...
")

    if not is_host_up(args.target):
        print(f"{Fore.RED}[!] Host {args.target} appears to be down.")
        return

    results = []
    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        futures = {executor.submit(scan_port, target_ip, port, args.verbose): port for port in range(start_port, end_port + 1)}
        for future in tqdm(as_completed(futures), total=len(futures), desc="Scanning", ncols=75):
            result = future.result()
            if result:
                print(result)
                results.append(result)

    if args.output:
        try:
            with open(args.output, "w") as f:
                for line in results:
                    f.write(line + "\n")
            print(f"{Fore.BLUE}\n[+] Results saved to {args.output}")
        except Exception as e:
            print(f"{Fore.RED}[!] Could not save to file: {e}")

if __name__ == "__main__":
    main()
