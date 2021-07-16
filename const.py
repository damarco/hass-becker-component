"""Becker Cover Constants."""

DOMAIN = "becker"
MANUFACTURER = "Becker"

DEVICE = "device"
DEVICE_CLASS = "shutter"

CONF_CHANNEL = "channel"
CONF_COVERS = "covers"
CONF_UNIT = "unit"

CLOSED_POSITION = 0
VENTILATION_POSITION = 25
INTERMEDIATE_POSITION = 75
OPEN_POSITION = 100

DEFAULT_CONF_USB_STICK_PATH = (
    "/dev/serial/by-id/usb-BECKER-ANTRIEBE_GmbH_CDC_RS232_v125_Centronic-if00"
)
DEFAULT_DB_FILENAME = "becker.db"
