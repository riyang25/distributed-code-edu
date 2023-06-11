#include <iostream>
#include <string>
#include <vector>
#include <fstream>

#include "parse_list.hpp"

using namespace std;

const string DOMAIN {"riyang25-ubiquitous-yodel-44vx645r5v6376gj-3000.preview.app.github.dev"}; // Enter domain here.

int main() {
    vector <string> directories {parseList("directories.txt")};
    string markdown {"# Please click on the link with your id.\n"};
    for (string &i : directories) {
        markdown += "- [" + i + "](https://" + DOMAIN + "/?folder=/workspaces/distributed-code-edu/students/" + i + ")\n";
    }
    ofstream fout {"index.md"};
    fout << markdown;
    fout.close();
    return 0;
}
