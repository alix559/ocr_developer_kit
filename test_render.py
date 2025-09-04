#!/usr/bin/env python3
"""
Test script to render one frame of the Komatsu invoice scene
"""

import os
import sys

# Change to the ocr_developer_kit directory where the assets are located
os.chdir('ocr_developer_kit')

# Add the current directory to Python path so we can import the module
sys.path.insert(0, '.')

from komatsu import InvoiceScene

def main():
    # Create the scene with frame number 0
    scene = InvoiceScene()
    scene.frame_number = 0
    
    print(f"Rendering frame {scene.frame_number}...")
    print(f"Current working directory: {os.getcwd()}")
    print(f"Assets directory exists: {os.path.exists('assets')}")
    print(f"Logo file exists: {os.path.exists('assets/komatsu_logo.png')}")
    
    # Render the scene
    # This will create a video file in the media/ directory
    scene.render()
    
    print("Frame rendered successfully!")
    print("Check the media/ directory for the output file.")

if __name__ == "__main__":
    main()
