from f_my_function.__main__ import main


# noinspection PyUnusedLocal
def lambda_handler(event, context):
    return main(event)


if __name__ == '__main__':
    lambda_handler({}, {})
