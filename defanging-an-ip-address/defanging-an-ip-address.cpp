class Solution {
public:
    string defangIPaddr(string address) {
        string ret = "";
        for (auto &ch : address) {
            if (ch == '.') {
                ret += "[.]";
            } else {
                ret += ch;
            }
        }
        return ret;
    }
};