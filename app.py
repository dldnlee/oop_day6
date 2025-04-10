# Quick Sort Algorithm
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

# Example usage
if __name__ == "__main__":
    user_input = input("Enter numbers separated by spaces: ")
    sample_array = list(map(int, user_input.split()))
    print("Original array:", sample_array)
    sorted_array = quick_sort(sample_array)
    print("Sorted array:", sorted_array)

