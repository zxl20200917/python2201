"""
    拷贝目录
        使用进程池拷贝一个目录及目录中所有内容
        1. 目录中的内容均为普通文件
        2. 进程池中执行的每个进程事件拷贝一个文件
        3. 实时显示拷贝的百分比
"""
from multiprocessing import Pool, Queue
import os

# 创建消息队列
q = Queue()


# 复制文件
def copy_file(file, old_folder, new_folder):
    fr = open(old_folder + '\\' + file, 'rb')
    fw = open(new_folder + '\\' + file, 'wb')
    # 开始拷贝
    while True:
        data = fr.read(1024 * 1024)
        if not data:
            break
        # n 为返回写入的字节数
        n = fw.write(data)
        # 把返回写入的字节放入队列
        q.put(n)
    fr.close()
    fw.close()


def main():
    # 拷贝基准目录下的目录
    base_path = "E:\\develop\\"
    dir = input("输入你要拷贝的目录:")
    # 待拷贝的目录
    old_folder = base_path + dir

    # 目标目录
    new_folder = old_folder + '备份'
    if not new_folder:
        os.mkdir(new_folder)

    # 获取文件列表
    all_file = os.listdir(old_folder)

    # 计算目录大小
    total_size = 0
    for file in all_file:
        total_size += os.path.getsize(old_folder + '\\' + file)

    # 创建进程池
    # 把每个拷贝的文件调用加入到一个进程中
    pool = Pool()
    for file in all_file:
        # 每个copy_file复制一个文件
        pool.apply_async(copy_file, args=(file, old_folder, new_folder))
    # 关闭进程池
    pool.close()

    # 打印出目录总大小
    print("目录总大小:%.2fM" % (total_size / 1024 / 1024))

    # 定义拷贝初始大小变量为0
    copy_size = 0
    while True:
        copy_size += q.get()
        print("拷贝了%.2f%%" % (copy_size / total_size * 100))
        if copy_size >= total_size:
            break

    pool.join()


if __name__ == '__main__':
    main()
