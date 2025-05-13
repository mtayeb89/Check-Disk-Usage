# Check-Disk-Usage

A Python utility for monitoring disk space usage across file systems.

## Overview

Check-Disk-Usage is a command-line tool that provides detailed information about storage utilization on your system. It helps identify large files, analyze disk space trends, and set up alerts for low disk space conditions.

## Installation

```bash
pip install check-disk-usage
```

## Basic Usage

```bash
# Check usage for all mounted file systems
check-disk-usage

# Check usage for a specific directory
check-disk-usage --path /home/user

# Set a threshold alert (percentage)
check-disk-usage --threshold 90
```

## Features

- **Real-time disk usage monitoring**: Get up-to-date information on disk space utilization
- **Directory-specific analysis**: Analyze specific directories to identify space consumption
- **Threshold alerts**: Set customizable thresholds for disk usage warnings
- **Exportable reports**: Generate reports in various formats (CSV, JSON, TXT)
- **Historical tracking**: Monitor disk usage trends over time

## Command-Line Options

| Option | Short | Description |
|--------|-------|-------------|
| `--path` | `-p` | Specify directory path to analyze |
| `--threshold` | `-t` | Set alert threshold percentage (0-100) |
| `--format` | `-f` | Output format (human, csv, json) |
| `--sort` | `-s` | Sort results by (size, path, usage) |
| `--exclude` | `-e` | Exclude specific directories |
| `--deep-scan` | `-d` | Perform detailed recursive scan |
| `--no-header` | `-n` | Omit header in output |
| `--output-file` | `-o` | Save results to specified file |
| `--verbose` | `-v` | Show detailed output |
| `--quiet` | `-q` | Show only critical information |
| `--help` | `-h` | Show help message |

## Example Output

```
Filesystem    Size    Used    Avail   Use%    Mounted on
/dev/sda1     458G    229G    206G    53%     /
/dev/sdb1     1.8T    1.2T    548G    69%     /media/data
```

## Advanced Usage

### Find Large Files

```bash
check-disk-usage --path /home --sort size --deep-scan
```

### Schedule Regular Checks

Add to crontab to run daily checks:

```bash
0 9 * * * check-disk-usage --threshold 85 --output-file /var/log/disk-usage.log
```

### Exclude Directories

```bash
check-disk-usage --path /home --exclude /home/user/Downloads,/home/user/.cache
```

## Configuration File

You can create a configuration file at `~/.config/check-disk-usage.conf` to set default options:

```ini
[Defaults]
threshold = 90
format = human
exclude = /tmp,/proc,/dev
verbose = true

[Notifications]
email = admin@example.com
smtp_server = smtp.example.com
```

## Programmatic Usage

You can also use Check-Disk-Usage as a library in your Python scripts:

```python
from check_disk_usage import DiskUsage

# Initialize disk usage analyzer
du = DiskUsage()

# Get usage for a specific path
usage = du.analyze_path("/home/user")
print(f"Usage: {usage.used_percent}%")

# Set up a threshold alert
du.set_threshold(90)
if du.is_threshold_exceeded("/"):
    print("Warning: Disk usage threshold exceeded!")
```

## Troubleshooting

- **Permission errors**: Run with sudo for accessing protected directories
- **Slow performance**: Use `--exclude` to skip large file systems or use `--no-deep-scan`
- **Inaccurate results**: Check for hidden files or use `--include-hidden`

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
