﻿import os

ASSETS_PATH = os.path.join(".", "Assets")
CARD_BORDERS_PATH = os.path.join(ASSETS_PATH, "CardBorders")
SYMBOL_PATH = os.path.join(ASSETS_PATH, "Symbols")
SET_SYMBOL_PATH = os.path.join(ASSETS_PATH, "SetSymbols")
SAGA_SYMBOL_PATH = os.path.join(ASSETS_PATH, "SagaSymbols")
FONT_PATHS = {"name":   os.path.join(ASSETS_PATH, "Fonts", "Beleren-Bold.ttf"),
              "token":  os.path.join(ASSETS_PATH, "Fonts", "Beleren-Small-Caps.ttf"),
              "type":   os.path.join(ASSETS_PATH, "Fonts", "Beleren-Bold.ttf"),
              "rules":  os.path.join(ASSETS_PATH, "Fonts", "MPlantin.ttf"),
              "flavor": os.path.join(ASSETS_PATH, "Fonts", "MPlantin-Italic.ttf")}

DECK_PATH = os.path.join("..", "Decks")

COCKATRICE_IMAGE_PATH = os.path.join("/", "Users", "fabiochiappina", "Library", "Application Support", "Cockatrice", "Cockatrice", "pics", "CUSTOM")