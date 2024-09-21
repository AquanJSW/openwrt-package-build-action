# Build OpenWrt Packages with Custom Patches using GitHub Actions

## Usage

- Fork this repository
- Add your package info to `build_db.yaml`
- Add the OpenWrt version and target in `.github/workflows/build.yml`

Once you push your changes, the GitHub Actions will start building the packages. You can download the packages from the Actions tab.

> [!NOTE]
> You will be prompt to SSH to the Actions runner to `make menuconfig` for the first time: `cd openwrt-sdk* && make menuconfig`. After that, the configuration will be saved as artifact and reused for the next builds.
> You can also manually delete the `config` artifact to reset the configuration.
