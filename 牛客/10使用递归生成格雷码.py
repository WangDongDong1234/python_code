class GrayCode {
vector < string > res;
public:
    vector < string > getGray(int


n) {
   // write
code
here
string
s;
getGrayCore(s, n);
return res;
}
void
getGrayCore(string & s, int
n)
{
if (n == 0)
    {
        res.push_back(s);
return;
}
s.push_back('0');
getGrayCore(s, n - 1);
s.pop_back();

s.push_back('1');
getYargCore(s, n - 1);
s.pop_back();
}
void
getYargCore(string & s, int
n)
{
if (n == 0)
{
res.push_back(s);
return;
}
s.push_back('1');
getGrayCore(s, n - 1);
s.pop_back();

s.push_back('0');
getYargCore(s, n - 1);
s.pop_back();
}
};