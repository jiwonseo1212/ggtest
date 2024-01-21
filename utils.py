import time
import functools
import tracemalloc

def algorithm_performance_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Start measuring time and memory
        start_time = time.time()
        tracemalloc.start()

        # Call the function
        result = func(*args, **kwargs)

        # Stop measuring time and memory
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        # Calculate elapsed time and used memory
        elapsed_time = end_time - start_time
        used_memory = peak / 1024.0 / 1024.0  # Convert to MB

        print(f"Function '{func.__name__}' executed in {elapsed_time:.4f} seconds.")
        print(f"Peak memory usage was {used_memory:.4f} MB.")

        return result

    return wrapper

# Example usage
@algorithm_performance_decorator
def example_function():
    # Example function logic
    result = [i ** 2 for i in range(10000)]
    return result

