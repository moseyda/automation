import os
import subprocess
import urllib.request

def download_and_install(url, installer_name):
    # Download the installer file
    print(f"Downloading {installer_name} from {url}...")
    urllib.request.urlretrieve(url, installer_name)
    print("Download complete.")

    # Run the installer
    print("Running the installer...")
    subprocess.run([installer_name], check=True)
    print("Installation complete.")

    # Clean up the installer file
    print("Cleaning up the installer file...")
    os.remove(installer_name)
    print("Cleanup complete.")

# Define the URLs and installer names
installers = [
    ('https://github.com/coreybutler/nvm-windows/releases/download/1.2.2/nvm-setup.exe', 'nvm-setup.exe'),
    ('https://github.com/git-for-windows/git/releases/download/v2.48.1.windows.1/Git-2.48.1-64-bit.exe', 'Git-2.48.1-64-bit.exe'),
    ('https://central.github.com/deployments/desktop/desktop/latest/win32', 'GitHubDesktopSetup.exe'),
    ('https://code.visualstudio.com/docs/setup/windows#_install-vs-code-on-windows')
]

# Download and install each
for url, installer_name in installers:
    download_and_install(url, installer_name)

print("All installations completed successfully.")
