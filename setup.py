#!/usr/bin/env python3
"""
Setup script for IdleDot IDLE extension.
Installs the extension to the IDLE user configuration directory.
"""

import os
import sys
import shutil
import site
from pathlib import Path


def get_idle_user_dir():
    """Get the IDLE user configuration directory path.

    Returns:
        Path: The IDLE user configuration directory
    """
    if sys.platform == 'win32':
        # Windows
        base = os.environ.get('USERPROFILE', os.path.expanduser('~'))
        idle_dir = Path(base) / '.idlerc'
    else:
        # macOS and Linux
        idle_dir = Path.home() / '.idlerc'

    return idle_dir


def get_user_site_packages():
    """Get the user site-packages directory.

    Returns:
        Path: The user site-packages directory
    """
    # Get user site-packages directory
    user_site = site.getusersitepackages()
    return Path(user_site)


def install_extension():
    """Install the IdleDot extension to IDLE."""
    print("Installing IdleDot IDLE extension...")

    # Get the IDLE user directory
    idle_dir = get_idle_user_dir()

    # Create the directory if it doesn't exist
    idle_dir.mkdir(exist_ok=True)
    print(f"IDLE configuration directory: {idle_dir}")

    # Copy the extension file
    extension_src = Path(__file__).parent / 'IdleDot.py'
    extension_dst = idle_dir / 'IdleDot.py'

    if not extension_src.exists():
        print(f"Error: Extension file not found: {extension_src}")
        return False

    shutil.copy2(extension_src, extension_dst)
    print(f"✓ Copied {extension_src.name} to {extension_dst}")

    # Handle the config file
    config_src = Path(__file__).parent / 'config-extension.def'
    config_dst = idle_dir / 'config-extensions.cfg'

    if config_src.exists():
        # Read the new config
        with open(config_src, 'r') as f:
            new_config = f.read()

        # If config file already exists, append instead of overwriting
        if config_dst.exists():
            with open(config_dst, 'r') as f:
                existing_config = f.read()

            # Check if our extension is already configured
            if '[IdleDot]' not in existing_config:
                with open(config_dst, 'a') as f:
                    f.write('\n\n' + new_config)
                print(f"✓ Added IdleDot configuration to existing {config_dst.name}")
            else:
                print(f"✓ IdleDot configuration already exists in {config_dst.name}")
        else:
            shutil.copy2(config_src, config_dst)
            print(f"✓ Copied {config_src.name} to {config_dst}")

    # Add ~/.idlerc to Python path via .pth file
    # This ensures the extension can be imported from any directory
    try:
        user_site_packages = get_user_site_packages()
        user_site_packages.mkdir(parents=True, exist_ok=True)

        pth_file = user_site_packages / 'idledot.pth'
        pth_content = str(idle_dir)

        with open(pth_file, 'w') as f:
            f.write(pth_content + '\n')

        print(f"✓ Created {pth_file} to add {idle_dir} to Python path")
    except Exception as e:
        print(f"Warning: Could not create .pth file: {e}")
        print("The extension may only work when IDLE is run from ~/.idlerc directory")

    print("\n" + "="*60)
    print("Installation complete!")
    print("="*60)
    print("\nThe IdleDot extension has been installed.")
    print("Please restart IDLE for the changes to take effect.")
    print("\nThe extension will automatically remap the numeric keypad comma")
    print("to a dot in both the editor and shell windows.")

    return True


def uninstall_extension():
    """Uninstall the IdleDot extension from IDLE."""
    print("Uninstalling IdleDot IDLE extension...")

    idle_dir = get_idle_user_dir()

    # Remove the extension file
    extension_file = idle_dir / 'IdleDot.py'
    if extension_file.exists():
        extension_file.unlink()
        print(f"✓ Removed {extension_file}")

    # Remove from config file
    config_file = idle_dir / 'config-extensions.cfg'
    if config_file.exists():
        with open(config_file, 'r') as f:
            lines = f.readlines()

        # Filter out IdleDot configuration
        new_lines = []
        skip = False
        for line in lines:
            if line.strip().startswith('[IdleDot]'):
                skip = True
                continue
            if skip and line.strip().startswith('['):
                skip = False
            if not skip:
                new_lines.append(line)

        with open(config_file, 'w') as f:
            f.writelines(new_lines)
        print(f"✓ Removed IdleDot configuration from {config_file}")

    # Remove the .pth file
    try:
        user_site_packages = get_user_site_packages()
        pth_file = user_site_packages / 'idledot.pth'
        if pth_file.exists():
            pth_file.unlink()
            print(f"✓ Removed {pth_file}")
    except Exception as e:
        print(f"Warning: Could not remove .pth file: {e}")

    print("\nUninstallation complete!")
    print("Please restart IDLE for the changes to take effect.")


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'uninstall':
        uninstall_extension()
    else:
        install_extension()
