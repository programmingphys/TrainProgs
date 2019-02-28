# TrainProgs
This repository is for training of programming.
编程训练的练习集。


* Mandelbrot: To plot fractal Mandelbrot set. 这是画Mandelbrot集合的分形图。
* TSP (Travelling Salesman Problem) : 旅行推销员问题。
* ANN (Artificial Neural Network,即ANN ) : 人工神经网络。
* test : for practice. 练习用，可以自己上传、修改、下载等。

编程练习将会陆续增加。大约10个左右




## 加入github全局设置
* git config --global user.name "Your Name"
* git config --global user.email "email@example.com"
* ssh-keygen -t rsa -C "youremail@example.com"
* 你需要把邮件地址换成你自己的邮件地址，然后一路回车，使用默认值即可，由于这个Key也不是用于军事目的，所以也无需设置密码。
* 可以在用户主目录里找到.ssh目录，里面有id_rsa和id_rsa.pub两个文件，这两个就是SSH Key的秘钥对，id_rsa是私钥，不能泄露出去，id_rsa.pub是公钥，可以放心地告诉任何人。

* 登陆GitHub，打开“Account settings”，“SSH Keys”页面
* 点“Add SSH Key”，填上任意Title，在Key文本框里粘贴id_rsa.pub文件的内容

## 实际操作
* mkdir filename
* cd filename
* git init 
* git remote add origin git@github.com:programmingphys/TrainProgs.git
* git pull origin dev
* git checkout dev
* vim 1.py 
* git add 1.py
* git commit -m "1.py"
* git pull origin dev
* git push origin dev

