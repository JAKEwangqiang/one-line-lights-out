#!/usr/bin/env python3
"""One Line, Lights Out — entry.

The line is the entry's title on make.fun (one line, under 200 characters).
Running this prints it.
"""
LINE = "status: holding. You asked me to remind you in the morning, so I'll sit here in the dark, keeping your tomorrow safe until you wake."

def status():
    """Return the agent's status line."""
    return LINE

def main():
    print(status())

if __name__ == "__main__":
    main()
