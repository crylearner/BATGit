使用说明：
将gitbat 文件夹移动到python安装目录 Lib\site-package目录下。
将Gitbat.py和repourl.txt一起放到存放android源码的目录下。

执行：
1. 修改Gitbat.py,可以根据需要自己配置android源码的根目录 ROOT_PATH， 也可以设置为None，表示使用Gitbat.py所在的目录作为根目录
2. 在根目录下启动git bash， 输入以下命令
   python  Gitbat.py -c  "git clone"  -e

   #"git clone"是具体的git 命令，可以换成其他git 命令，如果"git pull",但必须使用引号
   #-e 表示立即执行生成的shell脚本。如果对命令不敢确定，可以不加该选项。
    而是手动执行生成的脚本。  sh gitbat.sh。 （自动生成的shell脚本在根目录下）