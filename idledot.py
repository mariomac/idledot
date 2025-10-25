"""
IDLE Extension: IdleDot
Replaces numeric keypad comma with dot for better compatibility with programming.
Useful for Spanish and other keyboards where the numpad has a comma instead of a period.
"""

import sys
from idlelib.config import idleConf


class IdleDot:
    """IDLE extension that remaps the numeric keypad comma key to a dot."""

    menudefs = []  # No menu entries needed

    def __init__(self, editwin):
        """Initialize the extension.

        Args:
            editwin: The IDLE editor window instance
        """
        self.editwin = editwin
        self.text = editwin.text

        # Bind the keypad comma/decimal key
        # Different systems may use different key symbols
        self._bind_keypad_keys()

    def _bind_keypad_keys(self):
        """Bind keypad comma key events."""
        # KP_Decimal is the keypad decimal key (comma on Spanish keyboards)
        # On Spanish/European keyboards, this produces a comma
        self.text.bind("<KP_Decimal>", self._insert_dot)

        # Some systems might report it differently
        self.text.bind("<KP_Separator>", self._insert_dot)

    def _insert_dot(self, event):
        """Insert a dot instead of the default keypad comma.

        Args:
            event: The key event

        Returns:
            str: "break" to prevent default handling
        """
        # Insert a period at the current cursor position
        self.text.insert("insert", ".")

        # Return "break" to prevent the default key handling
        # This stops IDLE from inserting the comma
        return "break"


# This is required for IDLE to recognize this as an extension
if __name__ == "__main__":
    # This section is for testing purposes
    print("IdleDot IDLE extension loaded")
    print("This extension remaps the numeric keypad comma to a dot.")
