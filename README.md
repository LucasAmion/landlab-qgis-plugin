# Landlab Algorithm Provider

A QGIS plugin for integrating [Landlab](https://landlab.csdms.io) models and workflows.

## Features

- Run Landlab models directly in QGIS
- Visualize model outputs on maps
- Easy-to-use interface

## Installation

1. Open QGIS and go to **Plugins** > **Manage and Install Plugins**.
2. Search for "Landlab" in the plugin repository. If the plugin doesn't appear in the search results, you may need to enable experimental plugins by checking **Show also experimental plugins** in the plugin manager settings.
3. Click **Install Plugin** to download and install the plugin.
4. Enable the plugin if it was not automatically activated.

Alternatively, you can install from a downloaded zip file:
1. Download the latest release zip file from the [GitHub repository releases page](https://github.com/LucasAmion/landlab-qgis-plugin/releases).
2. Open QGIS and go to **Plugins** > **Manage and Install Plugins** > **Install from ZIP**, select the newly downloaded zip file and click on **Install Plugin**.
3. Enable the plugin if it was not automatically activated.

- **Important**: During the installation process, a message will appear asking if you want to install the "PackageInstallerQgis" plugin as a dependency. Click **"Ok"** to proceed. This plugin is necessary to install the Landlab library.

## Requirements

- QGIS 3.8 or higher.
- [PackageInstallerQgis](https://plugins.qgis.org/plugins/PackageInstallerQgis/) Plugin.
- Landlab Python library.

## License

MIT License

## Contributing

Pull requests are welcome. For major changes, please open an issue first.
