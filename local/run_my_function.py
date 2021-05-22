from common_local.environment import setup_test_environment
from common_local.events import load_sample

FUNCTION_NAME = "my_function"
setup_test_environment(FUNCTION_NAME)


def load_event(event_name):
    return load_sample(FUNCTION_NAME, event_name)

# TESTS

SAMPLE_1 = load_event("event_1")

if __name__ == '__main__':
    # Local test
    from f_my_function.__main__ import main
    main(SAMPLE_1)
