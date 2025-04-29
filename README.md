# 🔍 Port Scanner

A powerful multithreaded TCP port scanner written in Python. Supports customizable port ranges, thread count, host availability check, service identification, banner grabbing, and more!

## 🚀 Usage

```bash
python scanner.py --target <TARGET> --ports <START-END> [options]


Example
python scanner.py --target scanme.nmap.org --ports 1-100 --threads 50 --output results.txt --verbose

⚙️ Options

| Option               | Description                                      |
|----------------------|--------------------------------------------------|
| `--target`           | Target domain or IP address                      |
| `--ports`            | Port range (e.g., `1-1024`)                      |
| `--threads`          | Number of concurrent threads (default: 100)     |
| `--output`           | Save results to a file                           |
| `--verbose`          | Enable detailed output                           |


✨ Features
✅ Multithreaded scanning

✅ Custom port range and thread count

✅ Host availability check (ping)

✅ Service detection (basic)

✅ Banner grabbing

✅ Output results to a file

✅ Verbose mode for detailed output

✅ Color-coded results (open = green, closed = red)

✅ Progress bar during scan