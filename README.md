# IdleDot - IDLE Extension

A Python IDLE extension that automatically remaps the numeric keypad comma key to a dot (period). This is particularly useful for users with Spanish, German, French, and other European keyboards where the numeric keypad has a comma instead of a period.

## Problem

On many European keyboards (Spanish, German, French, etc.), the numeric keypad decimal key produces a comma (`,`) instead of a period/dot (`.`). This can be frustrating when programming in Python, as you need to use a dot for decimal numbers and attribute access.

## Solution

This IDLE extension intercepts the numeric keypad comma key press and automatically replaces it with a dot, making it work like an American keyboard layout.

## Features

- Automatic keypad comma to dot conversion
- Works in both IDLE editor and shell windows
- Lightweight and transparent
- No configuration needed
- Easy installation and uninstallation

## Installation

### Method 1: Using the setup script (Recommended)

1. Clone or download this repository
2. Navigate to the project directory
3. Run the installation script:

```bash
python3 setup.py
```

4. Restart IDLE

### Method 2: Manual Installation

1. Locate your IDLE user configuration directory:
   - **Linux/macOS**: `~/.idlerc/`
   - **Windows**: `%USERPROFILE%\.idlerc\`

2. Copy `IdleDot.py` to the IDLE configuration directory

3. Edit or create `config-extensions.cfg` in the same directory and add:

```ini
[IdleDot]
enable = True
enable_editor = True
enable_shell = True
```

4. Restart IDLE

## Usage

Once installed, the extension works automatically:

1. Open IDLE
2. Use your numeric keypad comma key
3. It will automatically insert a dot (`.`) instead of a comma (`,`)

That's it! No additional configuration or activation needed.

## Verification

To verify the extension is loaded:

1. Open IDLE
2. Try typing a decimal number using the numeric keypad comma key
3. It should insert a dot instead of a comma

## Uninstallation

To uninstall the extension:

```bash
python3 setup.py uninstall
```

Then restart IDLE.

Alternatively, you can manually delete:
- `IdleDot.py` from your `.idlerc` directory
- The `[IdleDot]` section from `config-extensions.cfg`

## Compatibility

- Python 3.x
- IDLE (included with Python)
- All platforms: Windows, macOS, Linux

## Technical Details

The extension binds to the following key events:
- `<KP_Decimal>` - Standard keypad decimal key
- `<KP_Separator>` - Alternative keypad separator key

When these keys are pressed, the extension:
1. Intercepts the key event
2. Inserts a dot (`.`) at the cursor position
3. Returns `"break"` to prevent the default comma insertion

## Troubleshooting

### Extension not loading

1. Verify the files are in the correct location:
   ```bash
   # On Linux/macOS
   ls ~/.idlerc/IdleDot.py
   cat ~/.idlerc/config-extensions.cfg
   ```

2. Check that the configuration file has the correct format

3. Ensure you've restarted IDLE after installation

### Still getting commas

Some systems may use different key symbols. If the extension doesn't work:

1. Try pressing the key and see what character appears
2. Check if your keyboard layout is properly configured
3. Verify Python/IDLE version compatibility

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

This project is released into the public domain. Feel free to use, modify, and distribute as needed.

## Author

Created to solve a common pain point for European keyboard users programming in Python.
