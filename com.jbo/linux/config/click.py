# -*- coding: utf-8 -*-

import click

@click.command()
#prompt 当我们没有直接指定name 这个参数时， Click 会提示我们在交互模式下输入
@click.option("--count", default=1, help="Number of greetings")
@click.option("--name", prompt="Your name", help="The persion to greet")
#confirmation_prompt 为True ，就可以进行密码的两次验证
@click.option("--password", prompt=True, hide_input=True, confirmation_prompt=True)
@click.option("--hash-type", type=click.Choice(["md5", "sha1"]))
def hello(count, name, password, hash_type):
    for x in range(count):
        print(name)
        print(password)
        print(hash_type)

if __name__ == "__main__":
    hello()
