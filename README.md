# Port Scanner

This is a simple, multithreaded TCP port scanner written in Python.
It scans a target IP address or hostname over a custome port range and identifies which ports are open, along with the common service names.

## Features

- Multithreaded for faster scanning
- Custom IP/hostname and port range input
- Service name detection
- Timeout handling to avoid delays
- Clean output for open ports only

## Technologies Used

- Python 3
- Built-in libraries: `socket`, `threading`

## Example Output

Enter the target IP address or hostname: 127.0.0.1
Enter the starting port number: 20
Enter the ending port number: 100

Scanning 127.0.0.1 from port 20 to 100...

Port 22 is open (ssh)

Port 80 is open (http)

Port scan completed.

## How to Run

1. Make sure you have Python 3 installed.
2. Clone this repository or copy the code to a `.py` file.
3. Run the script:

```bash
python portscanner.py
```

## Legal Notice

This tool is for educational and authorized testing only.
Do not use it to scan networks you don't own or have permission to scan - unauthorized scanning may be illegal.

## Future Improvements

- Scan multiple hosts or subnets
- Export results to a file (e.g., scan_results.txt)
- Command-line argument support with `argparse`
- Add UDP scan support

## Author

Created by Giannis Kinalis. Feel free to modify and contribute!