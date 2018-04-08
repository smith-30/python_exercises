# -  *  - coding:utf-8 -  *  -

import argparse


def main():
    # パーサーを作る
    parser = argparse.ArgumentParser(
        prog='ex01.py',  # プログラム名
        usage='for ex01',  # プログラムの利用方法
        description='description',  # 引数のヘルプの前に表示
        epilog='end',  # 引数のヘルプの後で表示
        add_help=True,  # -h/–help オプションの追加
    )

    parser.add_argument(
        'target',
        help='print target',
        type=str
    )

    args = parser.parse_args()
    print('args: ' + args.target)


if __name__ == "__main__":
    main()
