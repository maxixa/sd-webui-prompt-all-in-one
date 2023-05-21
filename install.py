import launch

packages = {
    "chardet": "chardet",
    "fastapi": "fastapi",
    "hashlib": "hashlib",
}

for package_name in packages:
    package = packages[package_name]
    try:
        if not launch.is_installed(package_name):
            launch.run_pip(f"install {package}", f"sd-webui-prompt-all-in-one: {package_name}")
    except Exception as e:
        print(e)
        print(f'Warning: Failed to install {package}, some preprocessors may not work.')
