#!/usr/bin/env python3
"""
Script to render one frame of the Komatsu invoice scene
"""

import os
from ocr_developer_kit.komatsu import InvoiceScene
import manim

def main():
    # Create the scene with frame number 0
    scene = InvoiceScene()
    scene.frame_number = 0
    
    print(f"Rendering frame {scene.frame_number}...")
    print(f"Current working directory: {os.getcwd()}")
    print(f"Assets directory exists: {os.path.exists('ocr_developer_kit/assets')}")
    print(f"Logo file exists: {os.path.exists('ocr_developer_kit/assets/komatsu_logo.png')}")
    
    # Render the scene
    # This will create a video file in the media/ directory
    scene.render()
    
    print("Frame rendered successfully!")
    print("Check the media/ directory for the output file.")

if __name__ == "__main__":
    main()
