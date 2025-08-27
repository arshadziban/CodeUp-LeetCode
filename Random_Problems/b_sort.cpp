#include <iostream>   // include input output stream library
using namespace std;  // use standard namespace

// function to perform bubble sort
void bubbleSort(int arr[], int n) {
    // outer loop runs n-1 times
    for (int i = 0; i < n - 1; i++) {
        bool swapped = false;  // track if any swap happens in this pass
        // inner loop compares adjacent elements
        for (int j = 0; j < n - i - 1; j++) {
            // swap if the element is greater than the next element
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];      // temporary variable for swap
                arr[j] = arr[j + 1];    // swap values
                arr[j + 1] = temp;
                swapped = true;         // mark swap happened
            }
        }
        // if no swap in this pass, array is already sorted
        if (!swapped) break;
    }
}

int main() {
    int n;  
    cout << "Enter number of elements: ";  // ask user for size of array
    cin >> n;  // input number of elements

    int arr[n];  // declare array of size n
    cout << "Enter " << n << " elements: ";  // prompt user for elements
    for (int i = 0; i < n; i++) {
        cin >> arr[i];  // input each element
    }

    bubbleSort(arr, n);  // call bubble sort function

    cout << "Sorted array: ";  // display sorted array
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";  // print each element
    }
    cout << endl;  // move to next line

    return 0;  // end of program
}