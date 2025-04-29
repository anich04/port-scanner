# 🔍 Port Scanner

A powerful, multithreaded TCP port scanner built with Python. This tool enables efficient and customizable scanning with support for port range selection, threading, host availability checks, service identification, banner grabbing, output logging, and more.

---

## 🚀 Usage

```bash
python scanner.py --target <TARGET> --ports <START-END> [options]
```

### 📌 Example

```bash
python scanner.py --target scanme.nmap.org --ports 1-100 --threads 50 --output results.txt --verbose
```

---

## ⚙️ Command-Line Options

 Option                   Description                                         

 `--target`              Target domain or IP address
                         
 `--ports`               Port range to scan (e.g., `1-1024`)                 

 `--threads`             Number of concurrent threads (default: 100)        

 `--output`              File path to save the scan results                 
 
 `--verbose`             Enable detailed output for each scanned port       

---

## ✨ Features

- ✅ **Multithreaded scanning** for faster results  
- ✅ **Customizable port range** and thread count  
- ✅ **Host availability check** before scanning  
- ✅ **Basic service detection**  
- ✅ **Banner grabbing** for open ports  
- ✅ **Output results** to a file  
- ✅ **Verbose mode** for detailed scanning feedback  
- ✅ **Color-coded results** (Open = Green, Closed = Red)  
- ✅ **Progress bar** to show scanning status  

---

## 📦 Requirements

- Python 3.x  
- `tqdm` for progress display  
- `colorama` for colored terminal output  

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## 🛡️ Disclaimer

This tool is intended for educational and authorized penetration testing purposes **only**. Unauthorized use is prohibited.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
