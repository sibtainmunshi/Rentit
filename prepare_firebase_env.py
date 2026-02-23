#!/usr/bin/env python3
"""
Helper script to convert serviceAccountKey.json to single-line format
for Render environment variable.

Usage: python prepare_firebase_env.py
"""

import json

def prepare_firebase_credentials():
    """Read serviceAccountKey.json and output single-line JSON for Render"""
    try:
        with open('serviceAccountKey.json', 'r') as f:
            creds = json.load(f)
        
        # Convert to single-line JSON (no extra whitespace)
        single_line = json.dumps(creds, separators=(',', ':'))
        
        print("\n" + "="*70)
        print("📋 COPY THIS VALUE FOR RENDER ENVIRONMENT VARIABLE")
        print("="*70)
        print("\nVariable Name: FIREBASE_CREDENTIALS")
        print("\nVariable Value (copy everything below):\n")
        print(single_line)
        print("\n" + "="*70)
        print("\n✅ Copy the above JSON and paste it in Render's")
        print("   Environment Variables section as FIREBASE_CREDENTIALS")
        print("="*70 + "\n")
        
        # Save to file for easy copying
        with open('firebase_env_value.txt', 'w') as f:
            f.write(single_line)
        
        print("💾 Also saved to: firebase_env_value.txt")
        print("   (You can copy from this file too!)\n")
        
    except FileNotFoundError:
        print("❌ Error: serviceAccountKey.json not found!")
        print("   Make sure the file exists in the current directory.")
    except json.JSONDecodeError:
        print("❌ Error: Invalid JSON in serviceAccountKey.json")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    prepare_firebase_credentials()
