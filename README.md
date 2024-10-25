# OpenWrt Package Build Action

可以用 Github Action 来编译自己想要的 OpenWrt 软件包，不能用来编译整个 OpenWrt 固件。

## 使用方法

需要一些准备工作：

- `package-to-build.list` 文件，里面写入你想要编译的软件包名，每行一个。
- `artifact-patterns.list` 文件，里面写入你想要保留的 `bin` 目录下的构建产物，
    每行一个。
    
    例如 `*.ipk` 保留所有 ipk 文件
- `diffconfigs`（可选） 目录下的 diffconfig 文件，用来配置编译选项。

    可以用
    [OpenWrt](https://github.com/openwrt/openwrt) 或
    [OpenWrt SDK](https://downloads.openwrt.org/) 的 `./scripts/diffconfig.sh`
    生成，详见 [OpenWrt 官方文档](https://openwrt.org/docs/guide-developer/toolchain/use-buildsystem#configure_using_config_diff_file)。

    命名方式为 `VERSION-SERIES-ARCH.diffconfig`，可见本仓库下的例子。

    如果没有提供 action 对应的 diffconfig 文件，会提示使用
    [tmate](https://tmate.io/) 进行手动配置。

- `custom-feeds` (可选) 目录下的文件用来添加额外的 feeds，它们会默认添加到
    `feeds.conf.default` 文件的头部以保证覆盖.
    
    命名方式为 `VERSION.conf` (不带 revision) ，可见本仓库下的例子。


准备工作到此为止，接下来就是配置 Github Action, 在 `.github/workflows/build.yaml`
中编辑 strategy.matrix 部分来指定 OpenWrt 版本和目标平台

另外，可以通过手动启动 workflow 在指定是否强制启用 `make menuconfig`

编译全部完成后会输出两种产物：

- `artifact-patterns.list` 中指定的产物
- 编译所用的配置的 diffconfig 文件
