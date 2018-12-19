#include<iostream>
#include<fstream>

using namespace std;
string line;
int main()
{
    //ifstream ifile("123.py");
    //while(ifile>>line)
    //cout<<line<<endl;
    ofstream ofile("cc.txt");
    ofile<<"hello"<<endl;
    ofile<<"world"<<endl;

}
