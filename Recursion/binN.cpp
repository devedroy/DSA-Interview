#include<iostream>

using namespace std;

void bin(int n) {
  if (n == 0) {
    return;
  }
  bin(n / 2);
  cout << n % 2;
}

int main() {
    int n;
    cout<< "Enter N" << endl;
    cin >> n;
    bin(n);
}