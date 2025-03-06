#include <iostream>

size_t calcASCII(const std::string& source) {
    int sum = 0;

    for (char c : source) {
        sum += static_cast<int>(c);
    }

    return sum;
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cout << "Usage: " << argv[0] << " <Input String>" << std::endl;
        return 1;
    }

    std::string source = argv[1];

    size_t sum = calcASCII(source);

    std::cout << "Sum of ASCII values of \"" << source << "\" is " << sum << std::endl;

    return 0;
}